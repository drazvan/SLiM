'''
Created on Dec 9, 2010

@author: Razvan
'''
#from modules import Module
from slim.modules import Module

class Lang(Module):
    """A module that provides classical language capabilities such as 'if'.
    
    """
    
    def __init__(self):
        """Constructor.
        
        """
        super(Lang, self).__init__("Lang")

    def on_register(self, module):
        # general stuff        
        self.waa.core.add("True")
        self.waa.core.add("False")
        self.waa.core.add("None")
        self.waa.core.add("in")
        
        self.waa.core.add("a")
        
        self.waa.core.add("if")
        self.waa.core.add("eqi")
        self.waa.core.add("is");
        self.waa.core.add("link");
        self.waa.core.add("map");
        self.waa.core.add("for")
        self.waa.core.add("print")
        
        # capabilities
        self.waa.core.register_capability(module, "a")
        self.waa.core.register_capability(module, "if")
        self.waa.core.register_capability(module, "eqi")
        self.waa.core.register_capability(module, "is")
        self.waa.core.register_capability(module, "link")
        self.waa.core.register_capability(module, "map")
        self.waa.core.register_capability(module, "for")
        self.waa.core.register_capability(module, "print")
        pass

    def do(self, what, params = None):
        if what.id == "if":
            logical_value = self.waa.core.do(params[0].id)
            
            print "logical value is : " + logical_value
            
            if logical_value == "False":
                return self.waa.core.do(params[2].id)
            else:
                return self.waa.core.do(params[1].id)
                
        elif what.id == "eqi":
            if self.waa.core.info(params[0].id) == self.waa.core.info(params[1].id):
                return "True"
            else:
                return "False"
            
        elif what.id == "is":
            ids = []
            for symbol in params:
                ids.append(symbol.id)
            symbol = self.waa.core.get_link(*ids)
            
            if symbol != None:
                return symbol.id
            else: 
                return "False"
            
        elif what.id == "link":
            ids = []
            for symbol in params:
                ids.append(self.waa.core.get(symbol.id).id)
            symbol = self.waa.core.link(None, None, ids)
            
            if symbol != None:
                return symbol
            else: 
                return "None"
            
        elif what.id == "map":
            self.waa.core.map(params[0].id, params[1].id)
            
            return params[1].id
        
        elif what.id == "print":
            ids = []
            for param in params:
                ids.append(self.waa.core.get(param.id))
            
            for id in ids:
                print id, " ",
            print ""
                        
            return "True"
        
        elif what.id == "for":
            
            options = self.waa.core.get(params[2].id)
            
            for s_option in options.symbols:
                self.waa.core.map(params[0].id, s_option.id)                
                self.waa.core.do(params[3].id)
            
            return "True"

        elif what.id == "a":
            # automatically set type to action for the given parameter
            self.waa.core.link(None, None, ["a", params[0].id])
            
            return "True"

        else:
            print "unknown action"
