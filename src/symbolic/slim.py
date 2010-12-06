'''
This is the main model class.

@author: Razvan
'''

from symbolic.symbol import Symbol
from symbolic.link import Link
from symbolic.mapping import Mapping

class SLiM:
    
    symbols = {}            # Collection of symbols indexed by id
    links = {}              # Dictionary of link symbols indexed by id
    mappings = {}           # A set of mappings indexed by id
    
    noname_counter = 0      # counter used for symbols with unspecified names
    
    
    # Constructor.
    def __init__(self):  
        
        # add default mappings
        
        # The mapping that states the owner module of each symbol (if any)
        self.owner = self.new_mapping("owner");    
        
        pass
    
    # Adds a new symbol to the model.
    # @param id: The name to be used as the identity of the symbol
    # @param info: The information to be attached with the symbol
    def add(self, id, info = None):
        self.symbols[id] = Symbol(id, info)
            
        return self.symbols[id]
        
        
    # Creates a new link
    def link(self, id, info, symbols):
        # new link
        link = Link(id, symbols, info)
        self.symbols[id] = link
        self.links[id] = link
        
        # connect to symbols
        for symbol in symbols:
            symbol.links.append(link)
            
        return link
            
    # Creates a no-name link
    def quick_link(self, info, symbols):
        self.noname_counter = self.noname_counter + 1
        name = "NoName" + str(self.noname_counter)
        
        return self.link(name, info, symbols)  
       
        
    # Creates a new map
    def new_mapping(self, id):
        self.mappings[id] = Mapping(id)
        
        return self.mappings[id]

    # For debugging purposes, shows the content of the model
    def show(self):
        print "----------------------------------------------"
        print "There are ", len(self.symbols), " symbols."
        
        for symbol in self.symbols:
            print symbol, ", " ,
        print ""
        
        
        print "There are ", len(self.links), " links."
        for link in self.links.itervalues():
            print link.id, ": ",
            for symbol in link.symbols:
                print symbol, " ",
            print ""
        
        print "There are ", len(self.mappings), " mappings."
        for mapping in self.mappings:
            print mapping
    



  
    
