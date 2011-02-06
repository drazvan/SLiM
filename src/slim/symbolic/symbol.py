'''Created on Dec 4, 2010

:author: Razvan
'''

class Symbol(object):
    """A symbol in the SLiM model with information attached to it.
    
    """
    
    id = None           
    """An alpha-numeric string representing symbol's identifier."""
    
    info = None         
    """The information contained in the symbol.""" 
    
    links = []          
    """The links that contain the symbol.
    
    TODO: to make a dictionary of links indexed by position
          - links[0] = the list of links whose first symbol is this one
          - links[1] = the list of links whose second symbol is this one
          - etc. 
    """
    
    mapping = None
    """The symbol to which this symbol is mapped. 
    Can be None, itself or any other symbol.
    """

    def __init__(self, id, info = None):
        """Constructor.
        
        @param identity: The symbol's identity (name or URI).
        @param info: An object to be attached as information.
        """
    
        self.id = id
        self.info = info
        self.links = []
        self.mapping = None
        
    def __str__(self):
        """String representation conforming to the SLiM language.
        
        """
        
        if self.info == None:
            return self.id
        else:
            return self.id + ": " + '"' + str(self.info) + '"'
        
    def nstr(self):
        """The normal string representation of a symbol.
        
        If the symbol is mapped to another symbol than we follow the link.
        """
        
        s = self
        while s.mapping != None and s.mapping != s:
            s = s.mapping
        
        return s.id
        