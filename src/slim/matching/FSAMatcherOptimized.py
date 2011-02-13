'''
Created on Jan 19, 2011

@author: Razvan
'''
import time

class FSAMatcher(object):
    
    # The list of patterns that the FSM recognizes
    patterns = []
   
    # Counter used for automatic ids given to symbols
    symbol_counter = 0 
    # The list of symbols that the automata recognizes
    symbols = []
    # Dictionary with a numeric ids for each symbol 
    ids = {}
    # Dictionary with the text for an ids
    text = {}
   
    # Dictionary indicating the transition table (its number) for each state
    state_ttable = {}
    # Dictionary indicating the transition table (its number) for each symbol
    symbol_ttable = {}
    # The index of each state in its corresponding transition table
    state_tindex = {}
    # The index of each symbol in its corresponding transition table
    symbol_tindex = {}
    # The matrix with the transition tables
    transitions = [[[]]]
    # The symbols in each transition table (except ?, { and } )
    tsymbols = [[]]
    # The states in each transition table
    tstates = [[0]]
    # The counter for transition tables
    tcounter = 1
    
    
    # The list with final states
    final_states = []
    # Dictionary with patterns corresponding to final states
    found_pattern = {}
    
    # Pattern parents (a pattern added because of a prefix has as parent the original pattern)
    parents = {}
        
    def __init__(self):
        """Initializations.
        
        """
        
        # The list of patterns that the FSM recognizes
        self.patterns = []
       
        # Counter used for automatic ids given to symbols
        self.symbol_counter = 0 
        # The list of symbols that the automata recognizes
        self.symbols = []
        # Dictionary with a numeric ids for each symbol 
        self.ids = {}
        # Dictionary with the text for an ids
        self.text = {}
       
        # Dictionary indicating the transition table (its number) for each state
        self.state_ttable = {}
        # Dictionary indicating the transition table (its number) for each symbol
        self.symbol_ttable = {}
        # The index of each state in its corresponding transition table
        self.state_tindex = {}
        # The index of each symbol in its corresponding transition table
        self.symbol_tindex = {}
        # The matrix with the transition tables
        self.transitions = [[[]]]
        # The symbols in each transition table (except ?, { and } )
        self.tsymbols = [[]]
        # The states in each transition table
        self.tstates = [[0]]
        # The counter for transition tables
        self.tcounter = 1
        
        
        # The list with final states
        self.final_states = []
        # Dictionary with patterns corresponding to final states
        self.found_pattern = {}
        
        # Pattern parents (a pattern added because of a prefix has as parent the original pattern)
        self.parents = {}
         
        self.add_symbol("?")
        self.add_symbol("{")
        self.add_symbol("}")
        
        self.transitions = [[[-1, -1, -1]]]
        
        # Transition table 0
        self.symbol_ttable[0] = 0
        self.symbol_ttable[1] = 0
        self.symbol_ttable[2] = 0
        self.state_ttable[0] = 0
    
        # indices in transition table 0    
        self.symbol_tindex[0] = 0
        self.symbol_tindex[1] = 1
        self.symbol_tindex[2] = 2
        self.state_tindex[0] = 0
       
    
    def add_symbol(self, symbol, tt = None):
        """ Adds a symbol to the list of symbols and gives it an ids.
        
        @param tt: Table table. The table to which the symbol belongs
        """
        if symbol in self.symbols:
            return self.ids[symbol]
        
        self.symbols.append(symbol)
        self.ids[symbol] = self.symbol_counter
        self.text[self.symbol_counter] = symbol
        self.symbol_counter = self.symbol_counter + 1
        
        if tt != None:
            
            self.symbol_ttable[self.ids[symbol]] = tt
            self.symbol_tindex[self.ids[symbol]] = len(self.transitions[tt][0])
            self.tsymbols[tt].append(self.ids[symbol])
            
            # add a new column to the transition matrix
            for l in range(len(self.transitions[tt])):
                self.transitions[tt][l].append(-1)
        
        return self.ids[symbol] 
        
    def add_pattern(self, pattern, parent = None):
        """Adds a pattern to the FSA.
        
        
        """
        tokens = self.get_tokens(pattern)
        # normalize
        pattern = " ".join(tokens)
        
        if pattern in self.patterns:
            return
        
        # print "Adding pattern: ", pattern
        self.patterns.append(pattern)
        
        state = 0
        
        while tokens != []:
            symbol = tokens[0]
            
            # Check if symbol exists
            if not symbol in self.symbols:
                self.add_symbol(symbol, self.state_ttable[state])
            
            id = self.ids[symbol]
            
            # If the symbol has a different transition table then the current state
            # then we have to merge the two tables (except for ?, { and } )
            if id > 2 and self.state_ttable[state] != self.symbol_ttable[id]:
                # first we create new columns for each symbol and move them to the destination table
                 
                dt = self.state_ttable[state]       # destination table
                st = self.symbol_ttable[id]          # source table
                
                #               print "Merging source table %s with destination table %s" % (st, dt)
            
                # will be used below, in the states part
                offset = [-1 for x in self.transitions[dt][0]]
            
                for sid in self.tsymbols[st]:
                    self.symbol_ttable[sid] = dt
                    self.symbol_tindex[sid] = len(self.transitions[dt][0])
                    self.tsymbols[dt].append(sid)
                
                    # add a new column to the transition matrix
                    for l in range(len(self.transitions[dt])):
                        self.transitions[dt][l].append(-1)
                
                # next we have to move the states to the new table
                
                for ss in self.tstates[st]:
                    old_sti = self.state_tindex[ss]
                    
                    self.state_ttable[ss] = dt
                    self.state_tindex[ss] = len(self.transitions[dt])
                    self.tstates[dt].append(ss)
                    
                    line = self.transitions[st][old_sti][0:3]
                    for x in offset[3:]:
                        line.append(x)
                    for x in self.transitions[st][old_sti][3:]:
                        line.append(x)
                        
                    self.transitions[dt].append(line)
                    
                # Delete the transitions for the old table
                self.transitions[st] = [[]]
                
            # here the tables should be merged    
            
            # Get next state
            next_state = self.transitions[self.state_ttable[state]][self.state_tindex[state]][self.symbol_tindex[id]]
            
            # if no next state that means this path is new and we have to create it
            if next_state == -1:
                #               print "Creating table %s" % self.tcounter
                next_state = self.tcounter
                self.tcounter = self.tcounter + 1
                
                self.state_ttable[next_state] = next_state
                self.state_tindex[next_state] = 0
                self.transitions.append([[-1, -1, -1]])
                self.tstates.append([next_state])
                self.tsymbols.append([])
                
                self.transitions[self.state_ttable[state]][self.state_tindex[state]][self.symbol_tindex[id]] = next_state
            
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
                id = self.ids[symbol]
            else:
                id = None
                
            # if there's a token not contained in a pattern
            if id == None:
                # if the current state has a jump on ? we take it
                if self.transitions[self.state_ttable[state]][self.state_tindex[state]][0] != -1:
                    next_state = self.transitions[self.state_ttable[state]][self.state_tindex[state]][0]
                else:
                    #print "Unexpected token '", symbol, "' in position ", position
                    return
            else:
                # if there's a jump on the current token and it is part of the same transition table as the state, we take it
                if (self.state_ttable[state] == self.symbol_ttable[id] or id < 3) and \
                    self.transitions[self.state_ttable[state]][self.state_tindex[state]][self.symbol_tindex[id]] != -1:
                    next_state = self.transitions[self.state_ttable[state]][self.state_tindex[state]][self.symbol_tindex[id]]
                else:
                    # we check if there's a transition on ?
                    if self.transitions[self.state_ttable[state]][self.state_tindex[state]][0] != -1:
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
                            # print "Expected symbol or { and found }"
                            return
                            
                        next_state = self.transitions[self.state_ttable[state]][self.state_tindex[state]][0]
                            
                    else:
                        # print "Unexpected token '", symbol, "' in position ", position
                        return
                        
            state = next_state
            position = position + 1
            tokens = tokens[1:]
            
        if not state in self.final_states:
            # print "I did not reach a final state: ", state
            return -1
        else:
            # print "Found match '", self.patterns[self.found_pattern[state]], "' for '", data.strip(), "'"
            return self.found_pattern[state]        
            
            
        
        
    def dump(self):
        print "There are ", len(self.symbols), " symbols:"
        
        for symbol in self.ids:
            print symbol, "-", self.ids[symbol], ",", 
        print ""
        
        print "There are ", len(self.patterns), " patterns:" 
        
        for pattern in self.patterns:
            print pattern
    
        print ""
        
        
        print "The transition tables are: "
        
        for t in range(self.tcounter):
            if self.transitions[t] == [[]]:
                continue
            
            print "Table ", t, " : "
            print "States: ",
            for s in self.tstates[t]:
                print s, " ",
            print ""
            
            print "Symbols: ",
            for s in self.tsymbols[t]:
                print self.text[s], " ",
            print ""
            
            for l in range(len(self.transitions[t])):
                print "%4s: " % l,
                for k in range(len(self.transitions[t][l])):
                    print "%4s" % self.transitions[t][l][k],
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
        
        t0 = time.clock()
        line = f.readline()
        nr = 0
        while line != "":
            self.match(line)
            line = f.readline()
            nr = nr + 1
        
        print time.clock() - t0, "seconds processing time for ", nr, " patterns "
        
        f.close()
        
if __name__ == '__main__':    
        
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
    
    new_estimate = 0
    table_count = 0
    for t in range(len(matcher.transitions)):
        if matcher.transitions[t] == [[]]:
            continue
    
        # print "Table ", t, " with size ", len(matcher.transitions[t]), " x ", len(matcher.transitions[t][0])
        
        table_count = table_count + 1
        new_estimate = new_estimate + len(matcher.transitions[t]) * len(matcher.transitions[t][0]) 
    
    
    print "No patterns: ", len(matcher.patterns)
    print "No symbols: ", len(matcher.symbols)
    print "No states: ", len(matcher.transitions)
    print "old Estimated memory: ", len(matcher.symbols) * len(matcher.transitions) * 4 / 1024, " kb"
    
    print "No tables: ", table_count    
    print "New Estimated memory: ", new_estimate * 4 / 1024, " kb"
    

