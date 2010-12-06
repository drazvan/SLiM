'''
Created on Oct 6, 2010

@author: Razvan
'''

class Module(object):
    
    id = ""                 # The module's id
    core = None             # The SLiM core to which it is registered
    
    # Constructor
    def __init__(self, id):
        self.id = id
        
        
    # Triggered after the module is registered with the core.
    # @param s_module: The symbol created for the module in the core.
    def on_register(self, s_module):
        pass
    
    # Called when the module needs to do something
    def do(self, what, params = None):
        pass
        

class Ping(Module):
    
    # constructor
    def __init__(self):
        super(Ping, self).__init__("Ping")

    def on_register(self, s_module):
        # register things we can do
        self.core.owner.add(self.core.add("ping"), s_module)
        self.core.owner.add(self.core.add("pong"), s_module)
        self.core.owner.add(self.core.add("notify"), s_module)
        pass

    def do(self, what, params = None):
        if what.id == "ping":
            print "ping"
        elif what.id == "pong": 
            print "pong"
        elif what.id == "notify":
            print "notification: '", params[0].info, "'"
        else:
            print "unknown action"
