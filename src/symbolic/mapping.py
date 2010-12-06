'''
Created on Dec 4, 2010

@author: Razvan
'''

# A mapping in our model.    
class Mapping(object):
    
    id = ""             # The mapping's id
    map = {}            # A dictionary mapping symbol ids in list of symbols
        
    # Constructor.
    def __init__(self, id):
        self.id = id

        
    # Adds a new pair. 
    def add(self, x, y):
        if x in self.map:
            self.map[x].append(y)
        else:
            self.map[x] = [y]
            
           
    # Removes an existing pair.
    def remove(self, x, y):
        if x in self.map:
            if y in self.map[x]:
                self.map[x].remove(y)
        
    # Checks if a pair exists.
    def check(self, x, y):
        if x in self.map:
            if y in self.map[x]:
                return True
            else:
                return False
        else:
            return False   
    
    # To string.
    def __str__(self):
        s = self.id + ": "
        for x in self.map:
            for y in self.map[x]:
                s = s + "(" + str(x) + ", " + str(y) + ")" 
        return s
        
        