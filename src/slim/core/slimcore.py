'''
A flexible core based on the SLiM model.

:author: Razvan
'''

from slim.symbolic.slim import Slim, ContextualSlim


class SlimCore(object):
    """The middleware based on the SLiM model.
    
    It maintains a "big" slim, the set of registered modules, the patterns and 
    the two automata that perform the matching. 
    """
    
    modules = {}            
    """The registered modules indexed by id"""
    
    slim = None
    """The Slim structure"""
    
    # Constructor.
    def __init__(self):
        
        self.modules = {}
        self.slim = Slim()
        
        # Add default symbols.
        self.slim.add("type")
        self.slim.add("module")
        self.slim.add("capability")
        
        pass

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
        
        return s_module
    
    def register_capability(self, module, capability):
        """Registers a module capability
        
        :param module: The symbol corresponding to the module registering the capability.
        :param capability: The symbol corresponding to the capability being registered.
        """
        
        link1 = self.slim.link(None, None, ["type", capability]);
        self.slim.map(link1, "capability")
        
        link1 = self.slim.link(None, None, ["module", capability]);
        self.slim.map(link1, module);      
     
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
            self._do_entry_point(do_slim, what)
        
        
    def _do_entry_point(self, slim, what):
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
