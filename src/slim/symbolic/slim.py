'''
This is the main model class.

@author: Razvan
'''

from symbolic.symbol import Symbol
from symbolic.link import Link

class SLiM:
    """An implementation of the SLiM model. 
    
    Manages symbols, links and mappings, handles modules registration, etc. 
    """
    
    symbols = {}            # Collection of symbols indexed by id
    links = {}              # Dictionary of link symbols indexed by id
    
    mappings = {}           # A dictionary with the active mappings.
                            # Every symbol that does not exist here is considered to be mapped to itself.
    
    
    _cnt = 0                # counter used for symbols with unspecified names
    
    def __init__(self):  
        """Constructor"""
        
        # Add default symbols.
        self.add("type")
        self.add("module")
        self.add("capability")
        
        pass
    
    # CREATE
    
    def add(self, id, info = None):
        """Adds a new symbol to the model.
        
        @param id: The name to be used as the identity of the symbol.
        @param info: The information to be attached with the symbol.
        
        Returns then newly created symbol.    
        """
        
        symbol = Symbol(id, info)
        self.symbols[id] = symbol
            
        return symbol.id
    
    def link(self, id, info, symbols):
        """Creates a new link.
        
        For each link, based on the ids of the inner symbols, a 'default_id' is computed. 
        If this 'default_id' is different than the given 'id' then a new symbol with 
        'default_id' as id is created and is mapped to the symbol with the id 'id'. This 
        way a link can be both accessed through the given id or the default id.
        If 'id' is None only the symbol with the default id is created.
        
        @param id: The name to be used as the identity of the symbol. It can be None, in which case only 
                   the default name is used.
        @param info: The information to be attached with the symbol.
        @param symbols: The ordered list of symbol ids contained in the link.
        
        Returns the if of the newly created link.
        """
        
        default_id = self.id_merge(*symbols)
        if id == None:
            id = default_id
        
        # Convert ids to symbols
        s_symbols = []
        for symbol_id in symbols:
            s_symbols.append(self.symbols[symbol_id])
        
        # Create the link and register it
        link = Link(id, s_symbols, info)
        
        self.symbols[id] = link
        self.links[id] = link
        
        for symbol in s_symbols:
            symbol.links.append(link)
            
        # if the id is different than default_id than we create an new symbol
        if id != default_id:
            default_link = self.add(default_id, None)
            self.map(default_link, link)
            
        return link.id
    
    def map(self, src, dest):
        """Maps the 'src' symbol to 'dest'.
        
        @param src: The id of the source symbol.
        @param dest: The id of the destination symbol.  
        """
        
        self.mappings[src] = dest
    
    
    def set_info(self, id, info):
        """Sets the value of info"""
        
        if not id in self.symbols:
            print "id '", id, "' not found" 
            return None
        
        symbol = self.symbols[id]
        symbol.info = info
        
        
    # GET   
 
        
    def get(self, id, follow = True):
        """Returns a Symbol instance for the given id.
        
        @param id: The id of the desired symbol.
        @param follow: If it's set to True than if the symbol for id is mapped to another
        symbol, and so on, then the function returns the last symbol of the chain. 
        """    
        if not id in self.symbols:
            return None
        
        symbol = self.symbols[id]
        
        if follow:
            while symbol.id in self.mappings and \
                  self.mappings[symbol.id] != symbol.id and self.mappings[symbol.id] != None:
                symbol = self.symbols[self.mappings[symbol.id]]
                 
        return symbol
    
    def get_link(self, *ids):
        """Returns a Link instance for the given list of ids.
        
        If the ids are mapped to other symbols they are automatically followed.
        @param ids: The list of ids that form the symbols contained in the link.
        """
        
        # we take each id and follow its mappings
        followed_ids = []
        
        for id in ids:
            symbol = self.get(id)
            
            if symbol == None:
                print "Could not find id '", id, "'"
                return None
            
            followed_ids.append(symbol.id)
            
        link_id = self.id_merge(*followed_ids)
        
        return self.get(link_id)      
    
    def info(self, id):
        """Returns the information associated with a symbol. 
        
        Mappings are automatically followed.
        Returns None if the symbol has no info attached or the id is not found.
        """    
        symbol = self.get(id);
        
        if symbol != None:
            return symbol.info;
        
        return None
     
     
    # REGISTER 
     
     
    def register(self, moduleObj, name):
        """Performs the registration of a module.
        
        When a module is registered a symbol is created with its name. 
        
        @param module: An object that represent the module to be registered.
        @param name: The name under which the module will be registered.
        
        Returns the id of the symbol created for the module.
        """
              
        s_module = self.add(name, moduleObj)
        
        link1 = self.link(None, None, ["type", name]);
        self.map(link1, "module")
        
        # allow the module to perform initializations and register its capabilities
        moduleObj.on_register(s_module)
        
        return s_module
    
    def register_capability(self, module, capability):
        """Registers a module capability
        
        @param module: The symbol corresponding to the module registering the capability.
        @param capability: The symbol corresponding to the capability being registered.
        """
        
        link1 = self.link(None, None, ["type", capability]);
        self.map(link1, "capability")
        
        link1 = self.link(None, None, ["module", capability]);
        self.map(link1, module);      
     
     
    # ACTION
    
        
    def do(self, what):
        """Does something described by a symbol.
        
        If 'what' is a symbol whose type is 'capability' then the corresponding module
        is invoked with no parameters.
        
        Returns the id of a symbol or None.
        """
        
        # We go from mapping to mapping until we find an action or
        # we find a symbol mapped to itself
        if not what in self.symbols:
            return None
        
        symbol = self.symbols[what]
                
        while symbol.id in self.mappings and \
              self.mappings[symbol.id] != symbol.id and self.mappings[symbol.id] != None:
            symbol = self.symbols[self.mappings[symbol.id]]
            
        type = self.get_type(symbol.id)

        # the final symbol which represents what to do
        s_what = symbol
        
        if s_what == None:
            print "Could not find '" + what + "'"
            return None
        
        type = self.get_type(s_what.id)
        
        # Capability with no parameters
        if type == "capability":
            module = self.get(self.id_merge("module", s_what.id)).info
            return module.do(s_what);
        # Action with no parameters
        elif type == "action":
            
            # an action body is given by the {a 'action_name'} link
            body = self.get(self.id_merge("a", s_what.id))
            
            if body != None:
                return self.do(body.id)
            
            return None
            
        else:
            # check if it's a link
            if s_what.id in self.links:
                first = s_what.symbols[0]
                type = self.get_type(first.id)
                
#                symbol = first
#                type = self.get_type(symbol.id)
#                
#                while type != "action" and symbol.id in self.mappings and \
#                      self.mappings[symbol.id] != symbol.id and self.mappings[symbol.id] != None:
#                    symbol = self.symbols[self.mappings[symbol.id]]
#                    type = self.get_type(symbol.id)
        
                # Capability with parameters
                if type == "capability":
                    module = self.get(self.id_merge("module", first.id)).info
                    return module.do(first, s_what.symbols[1:]);
                
                elif type == "action":
                    
                    # an action body is given by the {a 'action_name'} link
                    body = self.get(self.id_merge("a", first.id))
                                       
                    if body != None:
                        # extract and map parameters
                        body_params = body.symbols[0]
                        
                        for j in range(min(len(body_params.symbols), len(s_what.symbols) - 1)):
                            s_value = self.get(s_what.symbols[j + 1].id)
                            self.map(body_params.symbols[j].id, s_value.id)
                        
                        body = body.symbols[1]
                        
                        return self.do(body.id)
                    
                    return None
                     
                
                # Otherwise we will do every symbol in the link individually
                result = None
                for inner_what in s_what.symbols:
                    result = self.do(inner_what.id)
                
                # and return the last result
                return result 
            else:
                print "Don't know to do '" + what + "'"
                return what

    
    # Functions for internal use
    
    def id_merge(self, *ids):
        """ Creates a single symbol id from a list of other ids.
        
        For now the merging mechanism is a simple one: concatenation with "-" as separator.
        """
        
        if (len(ids) == 1):
            return "{" + ids[0] + "}"
        
        return "-".join(ids)

    def get_type(self, id):
        """ Returns the type of a given symbol.
        
        Searches for a link of the form {type id} and returns its mapping.
        """
        
        s_type = self.get(self.id_merge("type", id))
        
        if s_type == None:
            return None
        
        return s_type.id

    
    # Debug
    
    def dump(self):
        """Dumps the content of the core, for debugging purposes.
        
        """
        
        print "Symbolic core dump (", len(self.symbols), " symbols, ", len(self.links), " links, ", len(self.mappings), " mappings)"
                               
        for id in self.symbols:
            print str(self.symbols[id])
        print ""
                
        for link in self.links.itervalues():
            print link
        print ""
        
        for src in self.mappings:
            print self.symbols[src], " > ", self.symbols[self.mappings[src]]
        print ""
    
