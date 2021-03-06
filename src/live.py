'''
Created on Dec 4, 2010

@author: Razvan
'''

import antlr3

import sys

from slim.lang.output.slimParser import slimParser
from slim.lang.output.slimLexer import slimLexer

from slim.core.slimcore import SlimCore
from slim.modules import Ping
from slim.modules.lang import Lang

def parse(stream, core):
    """ Parses the given stream with the slim grammar for a given core. 
    
    """
    lexer = slimLexer(stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = slimParser(tokens)
    parser.core = core
    parser.start()


def test():
    waa = SlimCore()
        
    # register required modules
    ping = Ping()
    ping.waa = waa
    waa.register(ping, "mPing")
    
    lang = Lang()
    lang.waa = waa
    waa.register(lang, "mLang")
    
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        file_stream = antlr3.ANTLRInputStream(f)
        parse(file_stream, waa)
        
    else:
        # launch the interpreter prompt
        command = ""
        
        while (True):
            print "\n# ", 
            command = sys.stdin.readline()
        
            # Exit the interpreter
            if command.startswith("exit"):
                break
            # Dump the structure
            elif command.startswith("dump"):
                waa.slim.dump()
            # Read command
            else:
                char_stream = antlr3.ANTLRStringStream(command)
                parse(char_stream, waa.slim)
                
                
if __name__ == '__main__':    
    print "SLiM python prototype."
 
    test()                