'''
A flexible core based on the SLiM model.

:author: Razvan
'''

import antlr3
from slim.lang.output.slimLexer import slimLexer
from slim.lang.output.slimParser import slimParser

from slim.symbolic.slim import Slim, ContextualSlim
from slim.matching.FSAMatcherOptimized import FSAMatcher


class SlimCore(object):
    """The middleware based on the SLiM model.
    
    It maintains a "big" slim, the set of registered modules, the patterns and 
    the two automata that perform the matching. 
    """
    
    slim = None
    """The Slim structure"""
    
    modules = {}            
    """The registered modules indexed by id"""

    pattern_names = []
    """A list of pattern names."""
    
    pattern_slims = []
    """A list of slims corresponding to the registered patterns"""
    
    pattern_entry_point = []
    """A list with the entry point to each pattern"""
    
    pattern_strings = []
    """A list of string patterns. Corresponds index by index with pattern_slims"""
    
    pattern_modules = []
    """The id of the module that has registered each pattern"""
    
    capabilities_automaton = None
    """The automaton that matches all the capabilities registered by modules"""
    
    # Constructor.
    def __init__(self):
        
        self.modules = {}
        self.slim = Slim()
        
        # Add default symbols.
        self.slim.add("type")
        self.slim.add("module")
        self.slim.add("capability")
        
        self.capabilities_automaton = FSAMatcher()
        
    # REGISTER  

    def register(self, moduleObj, name):
        """Performs the registration of a module.
        
        When a module is registered a symbol is created with its name. 
        
        :param module: An object that represent the module to be registered.
        :param name: The name under which the module will be registered.
        
        :returns: The id of the symbol created for the module.
        """
              
        s_module = self.slim.add(name, moduleObj)
        
        link1 = self.slim.link(None, None, ["type", name]);
        self.slim.map(link1, "module")
        
        # allow the module to perform initializations and register its capabilities
        moduleObj.on_register(s_module)
        
        self.modules[name] = moduleObj
        
        return s_module
    
    def register_capability(self, module, pattern_name, pattern_slim, pattern_entry_point):
        """Registers a module capability
        
        :param module: The id of the module registering the capability.
        :param pattern_name: The name of the pattern to be registered. Must \
                   be unique per module. 
        :param pattern_slim: The slim describing the capability. 
        :param pattern_entry_point: The entry point for the capability to be registered.
        """
        
        # extract the pattern's string representation
        pattern_string = pattern_slim.symbols[pattern_entry_point].nstr()
        
        self.pattern_names.append(pattern_name)
        self.pattern_slims.append(pattern_slim)
        self.pattern_entry_point.append(pattern_entry_point)
        self.pattern_strings.append(pattern_string)
        self.pattern_modules.append(module)
        
        # register the pattern with the automaton
        self.capabilities_automaton.add_pattern(pattern_string)
        
        #print "Registered the pattern '", pattern_string, "' for module '", \
        #    module, "'" 
     
    # ACTION
    
    def tell(self, slim):
        """Loads a given slim into the core-slim. 
        
        :param slim: The slim which will be loaded.
        """
            
        # check each non-link symbol and if it does not exist create it
        for s in slim.symbols:
            if s in slim.links:
                continue
            
            if not s in self.slim.symbols:
                self.slim.add(s, slim.info(s))
        
        # check every link and create them if they don't exist
        for l in slim.links:
            if not l in self.slim.links:
                ids = []
                for s in slim.get(l, follow = False).symbols:
                    ids.append(s.id)
                    
                self.slim.link(None, slim.info(l), ids)
        
        # perform all the mappings
        for s in slim.mappings:
            self.slim.map(s, slim.mappings[s])
        
    def do(self, slim, entry_points):
        """Performs the actions described by the entry points.
        
        All the entry points are executed in parallel and the order is undetermined.
        
        :param slim: The slim that contains all the actions/information.
        :param entry_points: The symbols/links that will be used as entry points\
                             for actions
        """
        
        # First we create a contextual slim
        do_slim = ContextualSlim(slim, self.slim)
        
        for what in entry_points:
            self.do_entry_point(do_slim, what)
        

    def do_entry_point(self, slim, what):
        """Does something described by a symbol entry point.
        
        :param slim: The slim on which the *do* is invoked.
        :param what: The id of the symbol representing the entry point. 
                
        Returns the id of a symbol or None.
        """
         
        #print "The normal string representation is: "
        string_what = slim.get(what, follow = False).nstr()
        #print string_what
        
        match = self.capabilities_automaton.match(string_what)
        #print "match = ", match
        
        # if no match is found and what is a link we take each symbol at a time
        if match == -1 or match == None:
            s_what = slim.get(what)
            
            if hasattr(s_what, "symbols"):
                for s_sub_what in s_what.symbols:
                    self.do_entry_point(slim, s_sub_what.id)
                    
        else:
            # we must identify the values of parameters if any (symbols mapped
            # to ?)
            params = {}
            
            s_what = slim.get(what)
            entry = self.pattern_slims[match].get(self.pattern_entry_point[match])
            
            # make a DF like procedure in parallel on s_what and entry 
            self._df(entry, s_what, params)
            
            #if len(params) > 0:
            #    print "Found the following params: "
            #    for param in params:
            #        print param, " = ", params[param]
            #else:
            #    print "No parameters found"
                
            # we must notify the corresponding module
            module = self.pattern_modules[match]
            pattern_name = self.pattern_names[match]
            
            self.modules[module].do(slim, pattern_name, params)
            
    def _df(self, pattern, match, params):
        """Performs a DF on pattern and in parallel on match.
        
        Whenever a symbol mapped to ? is found in pattern the corresponding
        value is taken from match. 
        """
        
        if pattern.mapping != None and pattern.mapping.id == "?":
            params[pattern.id] = match
        elif hasattr(pattern, "symbols"):
            for i in range(len(pattern.symbols)):
                self._df(pattern.symbols[i], match.symbols[i], params)  
            
        
            
    def _do_entry_point_old(self, slim, what):
        """Does something described by a symbol entry point.
        
        :param slim: The slim on which the *do* is invoked.
        :param what: The id of the symbol representing the entry point. 
        
        If 'what' is a symbol whose type is 'capability' then the corresponding module
        is invoked with no parameters... to be changed ...
        
        Returns the id of a symbol or None.
        """
        
        s_what = slim.get(what)
        if s_what == None:
            print "Could not find '" + what + "'"
            return None
        
        type = slim.get_type(s_what.id)
        
        # Capability with no parameters
        if type == "capability":
            module = slim.get(slim.id_merge("module", s_what.id)).info
            return module.do(slim, s_what);
        
        # Action with no parameters
        elif type == "action":
            
            # an action body is given by the {a 'action_name'} link
            body = slim.get(slim.id_merge("a", s_what.id))
            
            if body != None:
                return self._do_entry_point(slim, body.id)
            
            return None
            
        else:
            # check if it's a link (by checking if it has a symbols attribute)
            if hasattr(s_what, "symbols"):
                first = s_what.symbols[0]
                type = slim.get_type(first.id)
                
#                symbol = first
#                type = self.get_type(symbol.id)
#                
#                while type != "action" and symbol.id in self.mappings and \
#                      self.mappings[symbol.id] != symbol.id and self.mappings[symbol.id] != None:
#                    symbol = self.symbols[self.mappings[symbol.id]]
#                    type = self.get_type(symbol.id)
        
                # Capability with parameters
                if type == "capability":
                    module = slim.get(slim.id_merge("module", first.id)).info
                    return module.do(slim, first, s_what.symbols[1:]);
                
                elif type == "action":
                    
                    # an action body is given by the {a 'action_name'} link
                    body = slim.get(slim.id_merge("a", first.id))
                                       
                    if body != None:
                        # extract and map parameters
                        body_params = body.symbols[0]

                        # TODO: this should be done with a ContextualSlim too                        
                        for j in range(min(len(body_params.symbols), len(s_what.symbols) - 1)):
                            s_value = slim.get(s_what.symbols[j + 1].id)
                            slim.map(body_params.symbols[j].id, s_value.id)
                        
                        body = body.symbols[1]
                        
                        return self._do_entry_point(slim, body.id)
                    
                    return None
                     
                
                # Otherwise we will do every symbol in the link individually
                result = None
                for inner_what in s_what.symbols:
                    result = self._do_entry_point(slim, inner_what.id)
                
                # and return the last result
                return result 
            else:
                print "Don't know to do '" + what + "'"
                return what

    def load_slim(self, str_slim):
        """Load the slim from a string representation in the SLiM language. 
        
        """
        str_stream = antlr3.ANTLRStringStream(str_slim)
        lexer = slimLexer(str_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = slimParser(tokens)
        parser.slim = Slim()
        parser.entry_points = []
        parser.aslim()
        
        return (parser.slim, parser.entry_points)