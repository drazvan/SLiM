# $ANTLR 3.3 Nov 30, 2010 12:45:30 E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g 2010-12-05 01:26:07

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
OPEN=4
CLOSE=5
ID=6
STRING=7
COLON=8
INT=9
WS=10
ESC_SEQ=11
HEX_DIGIT=12
UNICODE_ESC=13
OCTAL_ESC=14

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "OPEN", "CLOSE", "ID", "STRING", "COLON", "INT", "WS", "ESC_SEQ", "HEX_DIGIT", 
    "UNICODE_ESC", "OCTAL_ESC"
]




class slimParser(Parser):
    grammarFileName = "E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:45:30")
    antlr_version_str = "3.3 Nov 30, 2010 12:45:30"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(slimParser, self).__init__(input, state, *args, **kwargs)






                


        

             

    core = None			# the SLiM core component




    # $ANTLR start "command"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:13:1: command : symbol ;
    def command(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:13:9: ( symbol )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:13:11: symbol
                pass 
                self._state.following.append(self.FOLLOW_symbol_in_command26)
                self.symbol()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "command"

    class symbol_return(ParserRuleReturnScope):
        def __init__(self):
            super(slimParser.symbol_return, self).__init__()

            self.s = None




    # $ANTLR start "symbol"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:15:1: symbol returns [s] : ( id | l= link );
    def symbol(self, ):

        retval = self.symbol_return()
        retval.start = self.input.LT(1)

        l = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:15:19: ( id | l= link )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == ID) :
                    alt1 = 1
                elif (LA1_0 == OPEN) :
                    alt1 = 2
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:15:21: id
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_symbol37)
                    self.id()

                    self._state.following.pop()
                    #action start
                    retval.s = self.core.add(self.input.toString(retval.start, self.input.LT(-1)))
                    #action end


                elif alt1 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:15:60: l= link
                    pass 
                    self._state.following.append(self.FOLLOW_link_in_symbol46)
                    l = self.link()

                    self._state.following.pop()
                    #action start
                    retval.s = l.s
                    #action end


                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "symbol"

    class link_return(ParserRuleReturnScope):
        def __init__(self):
            super(slimParser.link_return, self).__init__()

            self.s = None
            self.tmp = None




    # $ANTLR start "link"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:17:1: link returns [s, tmp] : OPEN s1= symbol (s2= symbol )+ CLOSE ;
    def link(self, ):

        retval = self.link_return()
        retval.start = self.input.LT(1)

        s1 = None

        s2 = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:17:23: ( OPEN s1= symbol (s2= symbol )+ CLOSE )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:17:25: OPEN s1= symbol (s2= symbol )+ CLOSE
                pass 
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_link60)
                #action start
                s_list = []
                #action end
                self._state.following.append(self.FOLLOW_symbol_in_link68)
                s1 = self.symbol()

                self._state.following.pop()
                #action start
                s_list.append(s1.s)
                #action end
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:17:78: (s2= symbol )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OPEN or LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:17:80: s2= symbol
                        pass 
                        self._state.following.append(self.FOLLOW_symbol_in_link78)
                        s2 = self.symbol()

                        self._state.following.pop()
                        #action start
                        s_list.append(s2.s)
                        #action end


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1
                self.match(self.input, CLOSE, self.FOLLOW_CLOSE_in_link85)
                #action start
                retval.s = self.core.quick_link(None, s_list)
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "link"


    # $ANTLR start "id"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:20:1: id : ID ;
    def id(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:20:5: ( ID )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:20:7: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_id101)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "id"


    # $ANTLR start "info"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:21:1: info : STRING ;
    def info(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:21:7: ( STRING )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:21:9: STRING
                pass 
                self.match(self.input, STRING, self.FOLLOW_STRING_in_info109)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "info"


    # Delegated rules


 

    FOLLOW_symbol_in_command26 = frozenset([1])
    FOLLOW_id_in_symbol37 = frozenset([1])
    FOLLOW_link_in_symbol46 = frozenset([1])
    FOLLOW_OPEN_in_link60 = frozenset([4, 6])
    FOLLOW_symbol_in_link68 = frozenset([4, 6])
    FOLLOW_symbol_in_link78 = frozenset([4, 5, 6])
    FOLLOW_CLOSE_in_link85 = frozenset([1])
    FOLLOW_ID_in_id101 = frozenset([1])
    FOLLOW_STRING_in_info109 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("slimLexer", slimParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
