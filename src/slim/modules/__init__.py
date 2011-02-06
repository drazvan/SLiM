'''
Interface to modules in the SLiM architecture. 

@author: Razvan
'''

class Module(object):
    """A module that can be registered to a SLiM core. 
    
    """
    
    id = ""                 # The module's id
    waa = None              # The WAA to which this module belongs
    
    def __init__(self, id):
        """Constructor.
        
        """
        
        self.id = id
        
        
    def on_register(self, s_module):
        """Allows a module to perform initializations and register capabilities.
        
        :param s_module: The symbol corresponding to the module.
        """
        pass
    
    def do(self, slim, what, params = None):
        """Called when the module needs to do something (i.e. capability).
        
        :param slim: The slim on which the module should perform its capability. 
        :param what: A symbol describing what must be done.
        :param params: A list of symbols representing the ordered list of parameters.
        """
        
        pass
    
    def __str__(self):
        return "(module object '" + self.id + "')"
        

class Ping(Module):
    """A simple test module.
    
    'ping' and 'pong' are simple capabilities that require no parameters.
    'notify' uses one parameter whose information contains the message to be printed.
    """
    
    def __init__(self):
        """Constructor.
        
        """
    
        super(Ping, self).__init__("Ping")

    def on_register(self, module):
        """Allows a module to perform initializations and register capabilities.
        
        @param module: The if of the symbol corresponding to the module.
        """
        self.waa.slim.add("ping");
        self.waa.slim.add("pong");
        self.waa.slim.add("notify");
        
        self.waa.register_capability(module, "ping");
        self.waa.register_capability(module, "pong");
        self.waa.register_capability(module, "notify");
        pass

    def do(self, slim, what, params = None):
        """Called when the module needs to do something (i.e. capability).
        
        @param what: A symbol describing what must be done.
        @param params: A list of symbols representing the ordered list of parameters.
        """
        
        if what.id == "ping":
            print "ping"
        elif what.id == "pong": 
            print "pong"
        elif what.id == "notify":
            symbol = slim.get(params[0].id)
            print "notification: '", slim.info(symbol.id), "'"
        else:
            print "unknown action"
