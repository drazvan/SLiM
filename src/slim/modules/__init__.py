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
        :param what: A symbol representing the name of the found pattern.
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
        
        # create the required symbols
        self.waa.slim.add("ping")
        self.waa.slim.add("notify")
        self.waa.slim.add("show")
        self.waa.slim.add("image")
        
        # create the slims for the patters
        (slim_ping, ping_entries) = self.waa.load_slim(">ping")
        (slim_notify, notify_entries) = self.waa.load_slim(">{notify msg:?}")
        (slim_show_image, show_image_entries) = self.waa.load_slim(">{show image img:?}")
        
        # register the patterns
        self.waa.register_capability(module, "ping", slim_ping, ping_entries[0]);
        self.waa.register_capability(module, "notify", slim_notify, notify_entries[0]);
        self.waa.register_capability(module, "show image", slim_show_image, show_image_entries[0]);

        

    def do(self, slim, what, params = None):
        """Called when the module needs to do something (i.e. capability).
        
        :param slim: The slim on which the module should perform its capability. 
        :param what: A symbol representing the name of the found pattern.
        :param params: A list of symbols representing the ordered list of parameters.
        """
        
        if what == "ping":
            print "ping"
        elif what == "notify":
            if slim.get("web") != None:
                print slim.info(params["msg"].id) + "<br/>"
            else:
                print "notification: '", slim.info(params["msg"].id), "'"
        elif what == "show image":
            if slim.get("web") != None:
                print '<img height=200px src="' + \
                    slim.info(slim.get_link(params["img"].id, "url").id) + '"/><br/>'
            else:
                print "can't show image in text mode"
        else:
            print "unknown action"
