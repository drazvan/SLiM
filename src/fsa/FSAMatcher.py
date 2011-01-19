'''
Created on Jan 18, 2011

@author: Razvan
'''

class FSAMatcher(object):
    
    # The list of patterns that the FSM recognizes
    patterns = []
   
    # Counter used for automatic ids given to symbols
    symbol_counter = 0 
    # The list of symbols that the automata recognizes
    symbols = []
    # Dictionary with a numeric id for each symbol 
    id = {}
    
    # The matrix with the transitions
    transitions = [[]]
    
    
    # The list with final states
    final_states = []
    # Dictionary with patterns coresponding to final states
    found_pattern = {}
    
    # Pattern parents (a pattern added because of a prefix has as parent the original pattern)
    parents = {}
        
    def __init__(self):
        """Initializations.
        
        """
         
        self.add_symbol("?")
        self.add_symbol("{")
        self.add_symbol("}")
       
    
    def add_symbol(self, symbol):
        """ Adds a symbol to the list of symbols and gives it an id.
        
        """
        if symbol in self.symbols:
            return id[symbol]
        
        self.symbols.append(symbol)
        self.id[symbol] = self.symbol_counter
        self.symbol_counter = self.symbol_counter + 1
        
        # add a new column to the transition matrix
        for l in range(len(self.transitions)):
            self.transitions[l].append(-1)
        
        return self.id[symbol] 
        
    def add_pattern(self, pattern, parent = None):
        """Adds a pattern to the FSA.
        
        
        """
        tokens = self.get_tokens(pattern)
        # normalize
        pattern = " ".join(tokens)
        
        if pattern in self.patterns:
            return
        
        print "Adding pattern: ", pattern
        self.patterns.append(pattern)
        
        state = 0
        
        while tokens != []:
            symbol = tokens[0]
            
            # Check if symbol exists
            if not symbol in self.symbols:
                self.add_symbol(symbol)
            
            id = self.id[symbol]
            
            # Get next state
            next_state = self.transitions[state][id]
            
            # if no next state that means this path is new and we have to create it
            if next_state == -1:
                next_state = len(self.transitions)
                self.transitions.append([-1 for x in self.symbols])
                self.transitions[state][id] = next_state
            
            # otherwise we take the existing path
            else :
                pass
                
            state = next_state
            tokens = tokens[1:]
       
        # Check final state
        if state in self.final_states:
            print "ERROR: two patterns and in the same final state !"
            return
                
        if parent == None:
            parent = len(self.patterns) - 1
            
        self.parents[len(self.patterns) - 1] = parent
                
        self.final_states.append(state)
        self.found_pattern[state] = parent
        
        self.find_conflicts()
        
        
    def get_tokens(self, pattern):
        """Returns the tokens of a pattern."""
        
        tokens = pattern.replace("{", " { ").replace("}", " } ").split(" ")
        
        i = 0
        while i < len(tokens):
            if len(tokens[i].strip()) == 0:
                del tokens[i]
            else:
                i = i + 1
                
        return tokens
  
    def find_conflicts(self):
        """Checks to see if the last pattern has any conflicts with existing patterns .
        
        """
        last = self.patterns[-1]
        new_patterns = {}
        
        for i in range(len(self.patterns) - 1):
            p = self.patterns[i]
            t_p = self.get_tokens(p)
            t_last = self.get_tokens(last)
            
            
            k = 0
            
            while k < len(t_p) and k < len(t_last):
                s_p = t_p[k]
                s_last = t_last[k]
                
                # go forward if they're the same
                if s_p == s_last:
                    k = k + 1
                    
                # if none of them is "?"
                elif s_p != "?" and s_last != "?":
                    break
            
                # if p has ? then we must add a new instance of p
                elif s_p == "?":
                    # only if last is different than }
                    if s_last != "}":
                        repl = s_last
                        if repl == "{":
                            bcount = 0
                            j = k + 1
                            while t_last[j] != "}" or bcount > 0:
                                if t_last[j] == "{":
                                    bcount = bcount + 1
                                elif t_last[j] == "}":
                                    bcount = bcount - 1
                                
                                if bcount == 0:    
                                    repl = repl + " " + "?"
                                      
                                j = j + 1
                            
                            repl = repl + " " + "}"
                    
                        t_p[k] = repl
                        
                        new_pattern = " ".join(t_p)
                        new_patterns[new_pattern] = self.parents[i]
                        
                        #print "We need to add new pattern: ", new_pattern
                    break
                
                # if last has ? then we must add a new instance of last
                elif s_last == "?":
                    # only if p is different than }
                    if s_p != "}":
                        repl = s_p
                        if repl == "{":
                            bcount = 0
                            j = k + 1
                            while t_p[j] != "}" or bcount > 0:
                                if t_p[j] == "{":
                                    bcount = bcount + 1
                                elif t_p[j] == "}":
                                    bcount = bcount - 1
                                
                                if bcount == 0:    
                                    repl = repl + " " + "?"
                                      
                                j = j + 1
                            
                            repl = repl + " " + "}"
                    
                        t_last[k] = repl
                        
                        new_pattern = " ".join(t_last)
                        new_patterns[new_pattern] = self.parents[len(self.patterns) - 1]
                        
                        #print "We need to add new pattern: ", new_pattern
                    break
                    break
                    
        for pattern in new_patterns:
            self.add_pattern(pattern, new_patterns[pattern])         
            
        
    def match(self, data):
        """ Tries to match a given string with 
        
        """    
        tokens = self.get_tokens(data)

        state = 0
        
        position = 1
        while len(tokens) > 0:
            symbol = tokens[0]
            if symbol in self.symbols:
                id = self.id[symbol]
            else:
                id = None
                
            # if there's a token not contained in a pattern
            if id == None:
                # if the current state has a jump on ? we take it
                if self.transitions[state][0] != -1:
                    next_state = self.transitions[state][0]
                else:
                    print "Unexpected token '", symbol, "' in position ", position
                    return
            else:
                # if there's a jump on the current token we take it
                if self.transitions[state][id] != -1:
                    next_state = self.transitions[state][id]
                else:
                    # we check if there's a transition on ?
                    if self.transitions[state][0] != -1:
                        # if it's { we have to skip until the corresponding }
                        if id == 1:
                            bcount = -1
                            while tokens[0] != "}" or bcount > 0:
                                if tokens[0] == "{":
                                    bcount = bcount + 1
                                elif tokens[0] == "}":
                                    bcount = bcount - 1
                                    
                                tokens = tokens[1:]
                        
                        # however we don't make transitions on "}" for ?
                        elif id == 2:
                            print "Expected symbol or { and found }"
                            return
                            
                        next_state = self.transitions[state][0]
                            
                    else:
                        print "Unexpected token '", symbol, "' in position ", position
                        return
                        
            state = next_state
            position = position + 1
            tokens = tokens[1:]
            
        if not state in self.final_states:
            print "I did not reach a final state: ", state
        else:
            print "Found match '", self.patterns[self.found_pattern[state]], "' for '", data.strip(), "'"        
            
            
        
        
    def dump(self):
        print "There are ", len(self.symbols), " symbols:"
        
        for symbol in self.id:
            print symbol, "-", self.id[symbol], ",", 
        print ""
        
        print "There are ", len(self.patterns), " patterns:" 
        
        for pattern in self.patterns:
            print pattern
    
        print ""
        
        print "The transition table is:"
        
        for l in range(len(self.transitions)):
            print "%4s: " % l,
            for k in range(len(self.transitions[l])):
                print "%4s" % self.transitions[l][k],
            print ""
            
        print "There are ", len(self.final_states), " final states: "
        for state in self.final_states:
            print "State ", state, " for pattern ", self.patterns[self.found_pattern[state]]
        print ""
        
    def write_graph(self, filename):
        f = open(filename, "w")
        
        f.write("digraph g {\n")
        
        for l in range(len(self.transitions)):
            
            for k in range(len(self.transitions[l])):
                if self.transitions[l][k] != -1:
                    f.write('S%s -> S%s [label="%s"]\n' % (l, self.transitions[l][k], self.symbols[k]))
        f.write("}\n")
        f.close()
        
    def read_file(self, filename):
        f = open(filename)
        
        line = f.readline()
        while not "# CHECK" in line:
            self.add_pattern(line)
            line = f.readline()
        
        line = f.readline()
        while line != "":
            self.match(line)
            line = f.readline()
        
        f.close()
        
    
matcher = FSAMatcher()

#matcher.add_pattern("{call {phone ?} now}")
#matcher.add_pattern("{? stay}")
#matcher.add_pattern("{send file ? by email to ?}")
#matcher.add_pattern("{call {phone {razvan other}}}")

matcher.read_file("patterns.txt")

#matcher.match("{call {phone 012323} now}")
#matcher.match("{call {phone {razvan other}}}")
#matcher.match("{call {phone {razvan phone}} now}")
#matcher.match("{send file {documents readme txt } by email to razvan }")

#matcher.match("{{{{{{a}}}}} stay }")

matcher.write_graph("e:\\graph.dot")

#matcher.dump()

print "No patterns: ", len(matcher.patterns)
print "No symbols: ", len(matcher.symbols)
print "No states: ", len(matcher.transitions)
print "Estimated memory: ", len(matcher.symbols) * len(matcher.transitions) * 4 / 1024, " kb"



