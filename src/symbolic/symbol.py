'''
Created on Dec 4, 2010

@author: Razvan
'''

class Symbol(object):
    """A symbol in the SLiM model with information attached to it.
    
    """
    
    id = None           # The symbol's id
    info = None         # The information contained in the symbol 
    
    links = []          # The links that contain the symbol
    

    def __init__(self, id, info = None):
        """Constructor.
        
        @param identity: The symbol's identity (name or URI).
        @param info: An object to be attached as information.
        """
    
        self.id = id
        self.info = info
        
    def __str__(self):
        """String representation conforming to the SLiM language.
        
        """
        
        if self.info == None:
            return self.id
        else:
            return self.id + ": " + '"' + str(self.info) + '"'
        