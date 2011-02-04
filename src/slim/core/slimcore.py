'''
A simulation of a modular architecture.

@author: Razvan
'''
from slim.symbolic.slim import Slim


class SlimCore(object):
    """The middleware based on the SLiM model.
    
    It maintains a "big" slim, the set of registered modules, the patterns and 
    the two automata that perform the matching. 
    """
    
    modules = {}            # The registered modules indexed by id
    core = Slim()             # The Slim core structure
    
    # Constructor.
    def __init__(self):
        pass
