'''
Created on Dec 4, 2010

@author: Razvan
'''
from symbolic.symbol import Symbol

# A link in our model
class Link(Symbol):
    
    symbols = []             # The symbols contained in this link
    
    # Constructor.
    # @param id: The link's id (URI).
    # @param symbols: The symbols to be linked in this link.
    # @param info: The information corresponding to the link as a symbol.  
    def __init__(self, id, symbols, info = None):
        super(Link, self).__init__(id, info)
        
        self.symbols = symbols