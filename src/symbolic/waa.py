'''
A simulation of a modular architecture.

@author: Razvan
'''
from symbolic.slim import SLiM
from symbolic.link import Link

''' The wrapper of the SLiM structure
'''
class WAA(object):
    
    modules = {}            # The registered modules indexed by id
    core = None             # The SLiM core structure
    
    # Constructor.
    def __init__(self):
        self.core = SLiM()
        
    
    # Register a new module.
    def register(self, module):
        self.modules[module.id] = module
        
        # create a symbol corresponding to the module
        s_module = self.core.add(module.id, module.id);
        
        # trigger the on_register event
        module.core = self.core
        module.on_register(s_module)
      
      
    # Does some stuff
    def do(self, what):
        # search if the symbol exists
        if (not what in self.core.symbols):
            print "Don't know how to do ", what
            return
        s_what = self.core.symbols[what]
        
        # see if it has a owner module 
        if (s_what in self.core.owner.map):
            # get the module symbol
            s_module = self.core.owner.map[s_what][0]
            module_name = s_module.info
            
            # check if the module exists
            if (not module_name in self.modules):
                print "Could not find the module ", module_name
                return
            module = self.modules[module_name]
            
            # finally do the stuff
            module.do(s_what);
        
        else:
            # check if it's a link
            if isinstance(s_what, Link):
                
                # take the first symbol in the link
                first = s_what.symbols[0]
                
                # see if it has a owner module 
                if (first in self.core.owner.map):
                    # get the module symbol
                    s_module = self.core.owner.map[first][0]
                    module_name = s_module.info
                    
                    # check if the module exists
                    if (not module_name in self.modules):
                        print "Could not find the module ", module_name
                        return
                    module = self.modules[module_name]
                    
                    # finally do the stuff
                    module.do(first, s_what.symbols[1:]);
                
                
            else:
                print "Don't know how to do ", what
    