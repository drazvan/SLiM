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


class slimLexer(Lexer):

    grammarFileName = "E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:45:30")
    antlr_version_str = "3.3 Nov 30, 2010 12:45:30"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(slimLexer, self).__init__(input, state)







    # $ANTLR start "OPEN"
    def mOPEN(self, ):

        try:
            _type = OPEN
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:40:7: ( '{' )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:40:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPEN"



    # $ANTLR start "CLOSE"
    def mCLOSE(self, ):

        try:
            _type = CLOSE
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:41:8: ( '}' )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:41:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CLOSE"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:42:8: ( ':' )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:42:10: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:44:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:44:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:44:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:47:5: ( ( '0' .. '9' )+ )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:47:7: ( '0' .. '9' )+
            pass 
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:47:7: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:47:7: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:50:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:50:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:58:5: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:58:8: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:58:12: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
            while True: #loop3
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 92) :
                    alt3 = 1
                elif ((0 <= LA3_0 <= 33) or (35 <= LA3_0 <= 91) or (93 <= LA3_0 <= 65535)) :
                    alt3 = 2


                if alt3 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:58:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()


                elif alt3 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:58:24: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:62:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:62:13: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:66:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt4 = 3
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 92) :
                LA4 = self.input.LA(2)
                if LA4 == 34 or LA4 == 39 or LA4 == 92 or LA4 == 98 or LA4 == 102 or LA4 == 110 or LA4 == 114 or LA4 == 116:
                    alt4 = 1
                elif LA4 == 117:
                    alt4 = 2
                elif LA4 == 48 or LA4 == 49 or LA4 == 50 or LA4 == 51 or LA4 == 52 or LA4 == 53 or LA4 == 54 or LA4 == 55:
                    alt4 = 3
                else:
                    nvae = NoViableAltException("", 4, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:66:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt4 == 2:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:67:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt4 == 3:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:68:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt5 = 3
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 92) :
                LA5_1 = self.input.LA(2)

                if ((48 <= LA5_1 <= 51)) :
                    LA5_2 = self.input.LA(3)

                    if ((48 <= LA5_2 <= 55)) :
                        LA5_4 = self.input.LA(4)

                        if ((48 <= LA5_4 <= 55)) :
                            alt5 = 1
                        else:
                            alt5 = 2
                    else:
                        alt5 = 3
                elif ((52 <= LA5_1 <= 55)) :
                    LA5_3 = self.input.LA(3)

                    if ((48 <= LA5_3 <= 55)) :
                        alt5 = 2
                    else:
                        alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:14: ( '0' .. '3' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:15: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:25: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:36: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:37: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt5 == 2:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:74:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:74:14: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:74:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:74:25: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:74:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt5 == 3:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:14: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:80:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:80:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:8: ( OPEN | CLOSE | COLON | ID | INT | WS | STRING )
        alt6 = 7
        LA6 = self.input.LA(1)
        if LA6 == 123:
            alt6 = 1
        elif LA6 == 125:
            alt6 = 2
        elif LA6 == 58:
            alt6 = 3
        elif LA6 == 65 or LA6 == 66 or LA6 == 67 or LA6 == 68 or LA6 == 69 or LA6 == 70 or LA6 == 71 or LA6 == 72 or LA6 == 73 or LA6 == 74 or LA6 == 75 or LA6 == 76 or LA6 == 77 or LA6 == 78 or LA6 == 79 or LA6 == 80 or LA6 == 81 or LA6 == 82 or LA6 == 83 or LA6 == 84 or LA6 == 85 or LA6 == 86 or LA6 == 87 or LA6 == 88 or LA6 == 89 or LA6 == 90 or LA6 == 95 or LA6 == 97 or LA6 == 98 or LA6 == 99 or LA6 == 100 or LA6 == 101 or LA6 == 102 or LA6 == 103 or LA6 == 104 or LA6 == 105 or LA6 == 106 or LA6 == 107 or LA6 == 108 or LA6 == 109 or LA6 == 110 or LA6 == 111 or LA6 == 112 or LA6 == 113 or LA6 == 114 or LA6 == 115 or LA6 == 116 or LA6 == 117 or LA6 == 118 or LA6 == 119 or LA6 == 120 or LA6 == 121 or LA6 == 122:
            alt6 = 4
        elif LA6 == 48 or LA6 == 49 or LA6 == 50 or LA6 == 51 or LA6 == 52 or LA6 == 53 or LA6 == 54 or LA6 == 55 or LA6 == 56 or LA6 == 57:
            alt6 = 5
        elif LA6 == 9 or LA6 == 10 or LA6 == 13 or LA6 == 32:
            alt6 = 6
        elif LA6 == 34:
            alt6 = 7
        else:
            nvae = NoViableAltException("", 6, 0, self.input)

            raise nvae

        if alt6 == 1:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:10: OPEN
            pass 
            self.mOPEN()


        elif alt6 == 2:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:15: CLOSE
            pass 
            self.mCLOSE()


        elif alt6 == 3:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:21: COLON
            pass 
            self.mCOLON()


        elif alt6 == 4:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:27: ID
            pass 
            self.mID()


        elif alt6 == 5:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:30: INT
            pass 
            self.mINT()


        elif alt6 == 6:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:34: WS
            pass 
            self.mWS()


        elif alt6 == 7:
            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:1:37: STRING
            pass 
            self.mSTRING()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(slimLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
