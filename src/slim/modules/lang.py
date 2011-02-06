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
        self.waa.slim.add("True")
        self.waa.slim.add("False")
        self.waa.slim.add("None")
        self.waa.slim.add("in")
        
        self.waa.slim.add("a")
        
        self.waa.slim.add("if")
        self.waa.slim.add("eqi")
        self.waa.slim.add("is");
        self.waa.slim.add("link");
        self.waa.slim.add("map");
        self.waa.slim.add("for")
        self.waa.slim.add("print")
        self.waa.slim.add("copy")

        # capabilities
        
        #self.waa.register_capability(module, "a")
        #self.waa.register_capability(module, "if")
        #self.waa.register_capability(module, "eqi")
        #self.waa.register_capability(module, "is")
        #self.waa.register_capability(module, "link")
        #self.waa.register_capability(module, "map")
        #self.waa.register_capability(module, "for")
        #self.waa.register_capability(module, "print")
        #self.waa.register_capability(module, "copy")
        (slim, entries) = self.waa.load_slim(">{copy dest:? src:?}")
        self.waa.register_capability(module, "copy", slim, entries[0]);
        pass

    def do(self, slim, what, params = None):
        if what == "if":
            logical_value = self.waa.do(params[0].id)
            
            print "logical value is : " + logical_value
            
            if logical_value == "False":
                return self.waa.do(params[2].id)
            else:
                return self.waa.do(params[1].id)
                
        elif what == "eqi":
            if slim.info(params[0].id) == slim.info(params[1].id):
                return "True"
            else:
                return "False"
            
        elif what == "is":
            ids = []
            for symbol in params:
                ids.append(symbol.id)
            symbol = slim.get_link(*ids)
            
            if symbol != None:
                return symbol.id
            else: 
                return "False"
            
        elif what == "link":
            ids = []
            for symbol in params:
                ids.append(slim.get(symbol.id).id)
            symbol = slim.link(None, None, ids)
            
            if symbol != None:
                return symbol
            else: 
                return "None"
            
        elif what == "map":
            slim.map(params[0].id, params[1].id)
            
            return params[1].id
        
        elif what == "print":
            ids = []
            for param in params:
                ids.append(slim.get(param.id))
            
            for id in ids:
                print id, " ",
            print ""
                        
            return "True"
        
        elif what == "for":
            
            options = slim.get(params[2].id)
            
            for s_option in options.symbols:
                slim.map(params[0].id, s_option.id)                
                self.waa.do(params[3].id)
            
            return "True"

        elif what == "a":
            # automatically set type to action for the given parameter
            slim.link(None, None, ["a", params[0].id])
            
            return "True"
        
        elif what == "copy":
            slim.set_info(params["dest"].id, slim.info(params["src"].id))            
            return "True"

        else:
            print "unknown action"
