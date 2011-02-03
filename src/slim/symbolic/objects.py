'''
Created on Dec 4, 2010

@author: Razvan
'''

# The object associated with a symbol
class Object(object):
    symbol = None
    
    # Constructor
    def __init__(self, symbol):
        self.symbol = symbol
        
    # Custom function that parses attributes from links
    def __getattr__(self, attr_name):
        for link in self.symbol.linksFrom:
            if (attr_name == link[0].name):
                return link[1];
        return None
        
    def __getitem__(self, x):
        return ContextObject(self, x)
        
    
# The object associated with a symbol and a context
class ContextObject(object):
    
    # Constructor
    def __init__(self, obj, context):
        self.obj = obj
        self.context = context
        
    # Custom function that parses attributes from links
    def __getattr__(self, attr_name):
        for link in self.obj.symbol.linksFrom:
        
            if (attr_name == link[0].name and len(link) > 2 and (self.context in link[2:])):
                return link[1];
                
        return None    
        