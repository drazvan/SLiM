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
        self.waa.slim.add("then")
        self.waa.slim.add("else")
        self.waa.slim.add("eqi")
        self.waa.slim.add("is");
        self.waa.slim.add("link");
        self.waa.slim.add("map");
        self.waa.slim.add("for")
        self.waa.slim.add("print")
        self.waa.slim.add("copy")

        # capabilities
        
        #self.waa.register_capability(module, "a")
        
        (slim, entries) = self.waa.load_slim(">{if cond:? then true:? else false:?}")
        self.waa.register_capability(module, "if-then-else", slim, entries[0]);
        
        (slim, entries) = self.waa.load_slim(">{if cond:? then true:?}")
        self.waa.register_capability(module, "if-then", slim, entries[0]);
        
        #self.waa.register_capability(module, "eqi")
        (slim, entries) = self.waa.load_slim(">{eqi s1:? s2:?}")
        self.waa.register_capability(module, "eqi", slim, entries[0]);
        
        
        #self.waa.register_capability(module, "is")
        #self.waa.register_capability(module, "link")
        #self.waa.register_capability(module, "map")
        #self.waa.register_capability(module, "for")
        #self.waa.register_capability(module, "print")
        
        (slim, entries) = self.waa.load_slim(">{copy dest:? else src:?}")
        self.waa.register_capability(module, "copy", slim, entries[0]);
        pass

    def do(self, slim, what, params = None):
        if "if-then" in what:
            logical_value = self.waa.do(slim, [params["cond"].id])
            
            print "logical value is : " + logical_value
            
            if logical_value == "True":
                return self.waa.do(slim, [params["true"].id])
            else:
                if "false" in params:
                    return self.waa.do(slim, [params["false"].id])
                else:
                    return None
                
        elif what == "eqi":
            if slim.info(params["s1"].id) == slim.info(params["s2"].id):
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
