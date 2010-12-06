'''
Created on Dec 4, 2010

@author: Razvan
'''

# A symbol in our model
class Symbol(object):
    
    id = None           # The symbol's id
    info = None         # The information contained in the symbol 
    
    links = []          # The links that contain the symbol
    

    # Constructor.
    # @param identity: the symbol's identity (URI)
    def __init__(self, id, info = None):
        self.id = id
        self.info = info
        
    # string representation
    def __str__(self):
        return self.id