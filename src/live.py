'''
Created on Dec 4, 2010

@author: Razvan
'''

import sys
import antlr3
from slim.lang.output.slimLexer import slimLexer
from slim.lang.output.slimParser import slimParser

from slim.core.waa import SlimCore
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


if __name__ == '__main__':
    
    print "SLiM python prototype."
    
    waa = SlimCore()
        
    # register required modules
    ping = Ping()
    ping.waa = waa
    waa.core.register(ping, "mPing")
    
    lang = Lang()
    lang.waa = waa
    waa.core.register(lang, "mLang")
    
    
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        file_stream = antlr3.ANTLRInputStream(f)
        parse(file_stream, waa.core)
        
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
                waa.core.dump()
            # Read command
            else:
                char_stream = antlr3.ANTLRStringStream(command)
                parse(char_stream, waa.core)
                