'''
This is the main model class.

@author: Razvan
'''
import random
import string

from symbol import Symbol
from link import Link 

class Slim:
    """A structure based on the SLiM model.  
    
    Manages symbols, links, mappings and information. 
    """
    
    symbols = {}            
    """Collection of symbols indexed by id"""
    
    links = {}
    """Dictionary of link symbols indexed by id"""
    
    mappings = {}           
    """A dictionary with the active mappings.
       Every symbol that does not exist here is considered to be mapped to itself.
    """
    
    _cnt = 0                
    """Counter used for symbols with anonymous symbols"""
    
    _pref = None
    """The prefix used for anonymous symbols"""
    
    def __init__(self):  
        """Constructor"""
        
        self.symbols = {}  
        self.links = {}
        self.mappings = {}   
        self._cnt = 0    
        
        # generate a random 6 letters prefix
        self._pref = "".join(random.choice(string.letters) for _ in range(6))

    # CREATE
    
    def add(self, id = None, info = None):
        """Adds a new symbol to the model.
        
        If the id is set to `None` then an auto-generated name will be used.
        
        :param id: The name to be used as the identity of the symbol.
        :param info: The information to be attached with the symbol.
        
        :return: The newly created symbol.    
        """
        
        if id == None:
            self._cnt = self._cnt + 1
            id = self._pref + str(self._cnt)
        
        symbol = Symbol(id, info)
        self.symbols[id] = symbol
            
        return symbol.id
    
    def link(self, id, info, symbols):
        """Creates a new link.
        
        For each link, based on the ids of the inner symbols, a *default_id* is computed. 
        If this *default_id* is different than the given *id* then a new symbol with 
        *default_id* as id is created and is mapped to the symbol with the id *id*. This 
        way a link can be both accessed through the given id or the default id.
        If *id* is None only the symbol with the default id is created.
        
             
        :param id: The name to be used as the identity of the symbol. It can be None, in which case only the default name is used.
        :param info: The information to be attached with the symbol.
        :param symbols: The ordered list of symbol ids contained in the link. 
        
        :return: The id of the newly created link.
        
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
        
        :param src: The id of the source symbol.
        :param dest: The id of the destination symbol.  
        """
        
        s_src = self.get(src, follow = False)
        s_dest = self.get(dest, follow = False)
        
        self.mappings[src] = dest
        s_src.mapping = s_dest
        
    def set_info(self, id, info):
        """Sets the information value for a symbol given by id."""
        
        if not id in self.symbols:
            print "id '", id, "' not found" 
            return None
        
        symbol = self.symbols[id]
        symbol.info = info
        
        
    # GET   
 
        
    def get(self, id, follow = True):
        """Search for a symbol. 
        
        :param id: The id of the desired symbol.
        :param follow: If it's set to True than if the symbol for id is mapped to \
        another symbol, and so on, then the function returns the last symbol of the chain.
        
        :returns: A symbol instance for the given id. 
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
        """Search for a link by its symbols. 
        
        If the ids are mapped to other symbols they are automatically followed.
        
        :param ids: The list of ids that form the symbols contained in the link.
        
        :returns: A Link instance for the given list of ids and `None` if none is found. 
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
        """Information associated with a symbol (mappings are automatically followed).  
        
        :returns: `None` if the symbol has no info attached or the id is not found.
        """    
        symbol = self.get(id);
        
        if symbol != None:
            return symbol.info;
        
        return None
         
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
            if not id in self.links:
                print str(self.symbols[id])
        print ""
                
        for link in self.links.itervalues():
            print link
        print ""
        
        for src in self.mappings:
            print self.symbols[src], " : ", self.symbols[self.mappings[src]]
        print ""
        
        print "---------------the end-------------------"
    
class ContextualSlim(Slim):
    """A *ContextualSlim* is a slim that exists in the context of another slim. 
     
    """
    
    def __init__(self, object, context):
        """Initializes the ContextualSlim by setting the context slim.
        
        :param object: The slim for which a context must be attached.
        :param context: The slim that will be used as a context. 
        """
        
        Slim.__init__(self)
        
        self.symbols = object.symbols
        self.links = object.links;
        self.mappings = object.mappings;
        
        self.context = context
    
    def add(self, id = None, info = None):
        """Any new symbol is created into the context slim"""
        
        self.context.add(id, info)
        
    def link(self, id, info, symbols):
        """Any new link is created into the context slim"""
        
        self.context.link(id, info, symbols)
        
    def map(self, src, dest):
        """Any new mapping is created into the context slim"""
        
        self.context.map(src, dest)
    
    def set_info(self, id, info):
        """Any information is set in the context slim"""
        
        self.context.set_info(id, info)
        
    def get(self, id, follow = True):
        """Search for a symbol first in this slim and then in its context. 
        
        :param id: The id of the desired symbol.
        :param follow: If it's set to True than if the symbol for id is mapped to \
        another symbol, and so on, then the function returns the last symbol of the chain.
        
        :returns: A symbol instance for the given id. 
        """    
        if not id in self.symbols:
            return self.context.get(id, follow)
        
        symbol = self.symbols[id]
        
        if follow:
            while symbol.id in self.mappings and \
                  self.mappings[symbol.id] != symbol.id and self.mappings[symbol.id] != None:
                symbol = self.symbols[self.mappings[symbol.id]]
        
            # if the symbol found until now is further mapped in the context we
            # follow those mappings too
            if symbol.id in self.context.mappings:
                symbol = self.context.get(symbol.id)
    
        return symbol
    
    def info(self, id):
        """Information associated with a symbol (mappings are automatically followed).  
        
        :returns: `None` if the symbol has no info attached or the id is not found.
        """    
        symbol = self.get(id);
        
        if symbol != None:
            # if no information is found and the symbol exists also in the context
            # then we use the information from the context
            if symbol.info == None and symbol.id in self.context.symbols:
                return self.context.info(symbol.id)
                
            return symbol.info;
        
        return None

    def dump(self):
        """Dumps the content of the contextual slim, for debugging purposes.
        
        """
        
        print "Symbolic core dump (", len(self.symbols), " symbols, ", len(self.links), " links, ", len(self.mappings), " mappings)"
                               
        for id in self.symbols:
            if not id in self.links:
                print str(self.symbols[id])
                
        for id in self.context.symbols:
            if not id in self.context.links:
                print str(self.context.symbols[id])
        print ""
                
        for link in self.links.itervalues():
            print link
            
        for link in self.context.links.itervalues():
            print link
            
        print ""
        
        for src in self.mappings:
            print self.symbols[src], " : ", self.symbols[self.mappings[src]]
            
        for src in self.context.mappings:
            print self.context.symbols[src], " : ", \
                self.context.symbols[self.context.mappings[src]]
        print ""
        
        print "---------------the end-------------------"
