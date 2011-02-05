# $ANTLR 3.3 Nov 30, 2010 12:45:30 E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g 2011-02-05 23:45:52

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
DO=4
OPEN=5
CLOSE=6
GT=7
COLON=8
ID=9
STRING=10
COMMENT=11
INT=12
WS=13
ESC_SEQ=14
HEX_DIGIT=15
UNICODE_ESC=16
OCTAL_ESC=17


class slimLexer(Lexer):

    grammarFileName = "E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:45:30")
    antlr_version_str = "3.3 Nov 30, 2010 12:45:30"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(slimLexer, self).__init__(input, state)


        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:14: (~ ( '\\n' | '\\r' ) )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                    alt1 = 1


                if alt1 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:14: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:28: ( '\\r' )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 13) :
                alt2 = 1
            if alt2 == 1:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:91:28: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "DO"
    def mDO(self, ):

        try:
            _type = DO
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:95:5: ( 'do' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:95:7: 'do'
            pass 
            self.match("do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DO"



    # $ANTLR start "OPEN"
    def mOPEN(self, ):

        try:
            _type = OPEN
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:97:7: ( '{' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:97:9: '{'
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

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:98:8: ( '}' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:98:10: '}'
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

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:99:8: ( ':' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:99:10: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "GT"
    def mGT(self, ):

        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:100:4: ( '>' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:100:6: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GT"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:102:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )* )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:102:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            pass 
            if self.input.LA(1) == 45 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:102:35: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 45 or (48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:
                    pass 
                    if self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3



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

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:105:5: ( ( '0' .. '9' )+ )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:105:7: ( '0' .. '9' )+
            pass 
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:105:7: ( '0' .. '9' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:105:7: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1



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

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:108:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:108:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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

            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:116:5: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:116:8: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:116:12: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
            while True: #loop5
                alt5 = 3
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 92) :
                    alt5 = 1
                elif ((0 <= LA5_0 <= 33) or (35 <= LA5_0 <= 91) or (93 <= LA5_0 <= 65535)) :
                    alt5 = 2


                if alt5 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:116:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()


                elif alt5 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:116:24: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:120:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:120:13: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
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
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:124:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt6 = 3
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 92) :
                LA6 = self.input.LA(2)
                if LA6 == 34 or LA6 == 39 or LA6 == 92 or LA6 == 98 or LA6 == 102 or LA6 == 110 or LA6 == 114 or LA6 == 116:
                    alt6 = 1
                elif LA6 == 117:
                    alt6 = 2
                elif LA6 == 48 or LA6 == 49 or LA6 == 50 or LA6 == 51 or LA6 == 52 or LA6 == 53 or LA6 == 54 or LA6 == 55:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:124:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt6 == 2:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:125:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt6 == 3:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:126:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt7 = 3
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 92) :
                LA7_1 = self.input.LA(2)

                if ((48 <= LA7_1 <= 51)) :
                    LA7_2 = self.input.LA(3)

                    if ((48 <= LA7_2 <= 55)) :
                        LA7_4 = self.input.LA(4)

                        if ((48 <= LA7_4 <= 55)) :
                            alt7 = 1
                        else:
                            alt7 = 2
                    else:
                        alt7 = 3
                elif ((52 <= LA7_1 <= 55)) :
                    LA7_3 = self.input.LA(3)

                    if ((48 <= LA7_3 <= 55)) :
                        alt7 = 2
                    else:
                        alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae

            if alt7 == 1:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:14: ( '0' .. '3' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:15: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:25: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:36: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:131:37: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt7 == 2:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:132:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:132:14: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:132:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:132:25: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:132:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt7 == 3:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:133:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:133:14: ( '0' .. '7' )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:133:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:138:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:138:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
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
        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:8: ( COMMENT | DO | OPEN | CLOSE | COLON | GT | ID | INT | WS | STRING )
        alt8 = 10
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:10: COMMENT
            pass 
            self.mCOMMENT()


        elif alt8 == 2:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:18: DO
            pass 
            self.mDO()


        elif alt8 == 3:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:21: OPEN
            pass 
            self.mOPEN()


        elif alt8 == 4:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:26: CLOSE
            pass 
            self.mCLOSE()


        elif alt8 == 5:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:32: COLON
            pass 
            self.mCOLON()


        elif alt8 == 6:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:38: GT
            pass 
            self.mGT()


        elif alt8 == 7:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:41: ID
            pass 
            self.mID()


        elif alt8 == 8:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:44: INT
            pass 
            self.mINT()


        elif alt8 == 9:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:48: WS
            pass 
            self.mWS()


        elif alt8 == 10:
            # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:1:51: STRING
            pass 
            self.mSTRING()







    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\2\uffff\1\7\10\uffff\1\14\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\11\1\uffff\1\157\10\uffff\1\55\1\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\175\1\uffff\1\157\10\uffff\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\uffff"
        u"\1\2"
        )

    DFA8_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\2\11\2\uffff\1\11\22\uffff\1\11\1\uffff\1\12\12\uffff"
        u"\1\7\1\uffff\1\1\12\10\1\5\3\uffff\1\6\2\uffff\32\7\4\uffff\1\7"
        u"\1\uffff\3\7\1\2\26\7\1\3\1\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\2\uffff\12\7\7\uffff\32\7\4\uffff\1\7\1\uffff"
        u"\32\7"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(slimLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
