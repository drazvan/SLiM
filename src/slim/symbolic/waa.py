'''
A simulation of a modular architecture.

@author: Razvan
'''
from symbolic.slim import SLiM


''' The wrapper of the SLiM structure
'''
class WAA(object):
    
    modules = {}            # The registered modules indexed by id
    core = SLiM()             # The SLiM core structure
    
    # Constructor.
    def __init__(self):
        pass
