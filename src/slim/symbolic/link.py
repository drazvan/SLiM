'''Created on Dec 4, 2010

:author: Razvan
'''
from symbol import Symbol

class Link(Symbol):
    """A link in the SLiM model.
    
    """
    
    symbols = []             # The symbols contained in this link
    
    def __init__(self, id, symbols, info = None):
        """Constructor.
        
        @param id: The link's id (name or URI).
        @param symbols: The symbols to be linked in this link.
        @param info: The information corresponding to the link as a symbol.  
        """
        
        super(Link, self).__init__(id, info)
        
        self.symbols = symbols
        
    def __str__(self):
        """String representation conforming to the SLiM language.
        
        """
        
        _str = ""
        
        for symbol in self.symbols:
            if _str == "":
                _str = str(symbol)
            else:
                _str = _str + " " + str(symbol)
        
        _str = "{" + _str + "}"
        
        if self.info != None:
            _str = _str + ": " + '"' + self.info + '"'
        
        return _str
    
    def nstr(self):
        """The normal string representation of a link"""
        
        # if the link itself is mapped to something else then we follow it
        if self.mapping != None and self.mapping != self:
            return self.mapping.nstr()
        
        _str = ""
        
        for symbol in self.symbols:
            if _str == "":
                _str = symbol.nstr()
            else:
                _str = _str + " " + symbol.nstr()
        
        _str = "{" + _str + "}"
        
        return _str
