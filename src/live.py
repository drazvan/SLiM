'''
Created on Dec 4, 2010

@author: Razvan
'''

import sys
import antlr3
from slimparser.output.slimLexer import slimLexer
from slimparser.output.slimParser import slimParser

from symbolic.waa import WAA
from modules import Ping

if __name__ == '__main__':
    
    print "SLiM python prototype."
    
    waa = WAA()
    core = waa.core
    
    # register required modules
    waa.register(Ping())
        
    command = ""
    
    while (True):
        print "\n# ", 
        command = sys.stdin.readline()

        # exit
        if command.startswith("exit"):
            break
        elif command.startswith("show"):
            core.show()
        else:
            char_stream = antlr3.ANTLRStringStream(command)
            lexer = slimLexer(char_stream)
            tokens = antlr3.CommonTokenStream(lexer)
            parser = slimParser(tokens)
            parser.core = core
            parser.command()
