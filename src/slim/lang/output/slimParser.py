# $ANTLR 3.3 Nov 30, 2010 12:45:30 E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g 2011-02-05 23:45:52

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
        
from slim.symbolic.slim import Slim



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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DO", "OPEN", "CLOSE", "GT", "COLON", "ID", "STRING", "COMMENT", "INT", 
    "WS", "ESC_SEQ", "HEX_DIGIT", "UNICODE_ESC", "OCTAL_ESC"
]




class slimParser(Parser):
    grammarFileName = "E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:45:30")
    antlr_version_str = "3.3 Nov 30, 2010 12:45:30"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(slimParser, self).__init__(input, state, *args, **kwargs)






                


        

             

    core = None			
    """The SLiM core component"""

    slim = None
    """The tell-slim or do-slim that will be parsed"""

    mode = ""			
    """The current mode"""

    def symbol_id(self, id):
        """symbol rule, id branch"""
        
        if self.mode == "add" or self.mode == "do":
            s = self.slim.get(id)
            if s == None:
                s = self.slim.add(id)
            else:
                s = s.id
                
            return s
                
    def symbol_link(self, s_list):
        """symbol rule, link branch"""
        
        if self.mode == "add" or self.mode == "do":
            link = self.slim.get_link(*s_list)
            
            if link == None:
                return self.slim.link(None, None, s_list)
            else:
                return link.id

    def do(self, s):
        """Does something indicated by a symbol"""
        
        if s != None:
            self.core.do(s)
            
    def set_info(self, id, val):
        """Sets the information for a symbol"""
        
        s = self.slim.get(id)
        if s != None:
            self.slim.set_info(id, val.strip()[1:-1])
            
    def map(self, id1, id2):
        if id2 != None:
            self.slim.map(id1, id2)



    # $ANTLR start "start"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:63:1: start : ( command )+ ;
    def start(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:63:7: ( ( command )+ )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:63:9: ( command )+
                pass 
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:63:9: ( command )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((DO <= LA1_0 <= OPEN)) :
                        alt1 = 1


                    if alt1 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:63:9: command
                        pass 
                        self._state.following.append(self.FOLLOW_command_in_start31)
                        self.command()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "start"


    # $ANTLR start "command"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:65:1: command : (s= aslim | DO s= aslim );
    def command(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:65:9: (s= aslim | DO s= aslim )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == OPEN) :
                    alt2 = 1
                elif (LA2_0 == DO) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:65:11: s= aslim
                    pass 
                    #action start
                    self.mode = "add"
                    #action end
                    #action start
                    self.slim = Slim()
                    #action end
                    self._state.following.append(self.FOLLOW_aslim_in_command47)
                    self.aslim()

                    self._state.following.pop()
                    #action start
                    self.core.tell(self.slim); self.core.slim.dump()
                    #action end


                elif alt2 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:66:3: DO s= aslim
                    pass 
                    #action start
                    self.mode = "do"
                    #action end
                    #action start
                    self.slim = Slim()
                    #action end
                    self.match(self.input, DO, self.FOLLOW_DO_in_command59)
                    self._state.following.append(self.FOLLOW_aslim_in_command65)
                    self.aslim()

                    self._state.following.pop()
                    #action start
                    self.slim.dump()
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "command"


    # $ANTLR start "aslim"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:68:1: aslim : OPEN ( symbol )+ CLOSE ;
    def aslim(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:68:7: ( OPEN ( symbol )+ CLOSE )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:68:9: OPEN ( symbol )+ CLOSE
                pass 
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_aslim75)
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:68:14: ( symbol )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == OPEN or LA3_0 == GT or LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:68:14: symbol
                        pass 
                        self._state.following.append(self.FOLLOW_symbol_in_aslim77)
                        self.symbol()

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1
                self.match(self.input, CLOSE, self.FOLLOW_CLOSE_in_aslim80)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "aslim"

    class symbol_return(ParserRuleReturnScope):
        def __init__(self):
            super(slimParser.symbol_return, self).__init__()

            self.s = None
            self.tmp = None




    # $ANTLR start "symbol"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:70:1: symbol returns [s, tmp] : ( GT )? ( ( id | l= link ) ( COLON (i2= info | s2= symbol ) )? ) ;
    def symbol(self, ):

        retval = self.symbol_return()
        retval.start = self.input.LT(1)

        l = None

        i2 = None

        s2 = None

        id1 = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:70:24: ( ( GT )? ( ( id | l= link ) ( COLON (i2= info | s2= symbol ) )? ) )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:71:27: ( GT )? ( ( id | l= link ) ( COLON (i2= info | s2= symbol ) )? )
                pass 
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:71:27: ( GT )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == GT) :
                    alt4 = 1
                if alt4 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:71:27: GT
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_symbol121)



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:72:27: ( ( id | l= link ) ( COLON (i2= info | s2= symbol ) )? )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:73:27: ( id | l= link ) ( COLON (i2= info | s2= symbol ) )?
                pass 
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:73:27: ( id | l= link )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == ID) :
                    alt5 = 1
                elif (LA5_0 == OPEN) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:73:28: id
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_symbol181)
                    id1 = self.id()

                    self._state.following.pop()
                    #action start
                    retval.s = self.symbol_id(((id1 is not None) and [self.input.toString(id1.start,id1.stop)] or [None])[0])
                    #action end


                elif alt5 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:73:65: l= link
                    pass 
                    self._state.following.append(self.FOLLOW_link_in_symbol191)
                    l = self.link()

                    self._state.following.pop()
                    #action start
                    retval.s = self.symbol_link(l.s_list)
                    #action end



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:74:27: ( COLON (i2= info | s2= symbol ) )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == COLON) :
                    alt7 = 1
                if alt7 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:74:28: COLON (i2= info | s2= symbol )
                    pass 
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_symbol224)
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:74:34: (i2= info | s2= symbol )
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == STRING) :
                        alt6 = 1
                    elif (LA6_0 == OPEN or LA6_0 == GT or LA6_0 == ID) :
                        alt6 = 2
                    else:
                        nvae = NoViableAltException("", 6, 0, self.input)

                        raise nvae

                    if alt6 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:74:35: i2= info
                        pass 
                        self._state.following.append(self.FOLLOW_info_in_symbol231)
                        i2 = self.info()

                        self._state.following.pop()
                        #action start
                        self.set_info(retval.s, ((i2 is not None) and [self.input.toString(i2.start,i2.stop)] or [None])[0])
                        #action end


                    elif alt6 == 2:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:74:77: s2= symbol
                        pass 
                        self._state.following.append(self.FOLLOW_symbol_in_symbol241)
                        s2 = self.symbol()

                        self._state.following.pop()
                        #action start
                        self.map(retval.s, s2.s)
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

            self.s_list = None
            self.tmp = None




    # $ANTLR start "link"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:78:1: link returns [s_list, tmp] : OPEN (s1= symbol | i1= info ) (s2= symbol | i2= info )* CLOSE ;
    def link(self, ):

        retval = self.link_return()
        retval.start = self.input.LT(1)

        s1 = None

        i1 = None

        s2 = None

        i2 = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:78:28: ( OPEN (s1= symbol | i1= info ) (s2= symbol | i2= info )* CLOSE )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:78:30: OPEN (s1= symbol | i1= info ) (s2= symbol | i2= info )* CLOSE
                pass 
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_link272)
                #action start
                retval.s_list = []
                #action end
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:79:6: (s1= symbol | i1= info )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == OPEN or LA8_0 == GT or LA8_0 == ID) :
                    alt8 = 1
                elif (LA8_0 == STRING) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:79:7: s1= symbol
                    pass 
                    self._state.following.append(self.FOLLOW_symbol_in_link287)
                    s1 = self.symbol()

                    self._state.following.pop()
                    #action start
                    retval.s_list.append(s1.s)
                    #action end


                elif alt8 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:79:44: i1= info
                    pass 
                    self._state.following.append(self.FOLLOW_info_in_link295)
                    i1 = self.info()

                    self._state.following.pop()
                    #action start
                    retval.s_list.append(self.slim.add(None, ((i1 is not None) and [self.input.toString(i1.start,i1.stop)] or [None])[0].strip()[1:-1]))
                    #action end



                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:80:6: (s2= symbol | i2= info )*
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OPEN or LA9_0 == GT or LA9_0 == ID) :
                        alt9 = 1
                    elif (LA9_0 == STRING) :
                        alt9 = 2


                    if alt9 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:80:7: s2= symbol
                        pass 
                        self._state.following.append(self.FOLLOW_symbol_in_link310)
                        s2 = self.symbol()

                        self._state.following.pop()
                        #action start
                        retval.s_list.append(s2.s)
                        #action end


                    elif alt9 == 2:
                        # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:80:44: i2= info
                        pass 
                        self._state.following.append(self.FOLLOW_info_in_link318)
                        i2 = self.info()

                        self._state.following.pop()
                        #action start
                        retval.s_list.append(self.slim.add(None, ((i2 is not None) and [self.input.toString(i2.start,i2.stop)] or [None])[0].strip()[1:-1]))
                        #action end


                    else:
                        break #loop9
                self.match(self.input, CLOSE, self.FOLLOW_CLOSE_in_link325)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "link"

    class id_return(ParserRuleReturnScope):
        def __init__(self):
            super(slimParser.id_return, self).__init__()





    # $ANTLR start "id"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:82:1: id : ID ;
    def id(self, ):

        retval = self.id_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:82:5: ( ID )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:82:7: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_id334)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "id"

    class info_return(ParserRuleReturnScope):
        def __init__(self):
            super(slimParser.info_return, self).__init__()





    # $ANTLR start "info"
    # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:83:1: info : STRING ;
    def info(self, ):

        retval = self.info_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:83:6: ( STRING )
                # E:\\Work\\waa\\waa-slim\\src\\slim\\lang\\slim.g:83:8: STRING
                pass 
                self.match(self.input, STRING, self.FOLLOW_STRING_in_info341)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "info"


    # Delegated rules


 

    FOLLOW_command_in_start31 = frozenset([1, 4, 5])
    FOLLOW_aslim_in_command47 = frozenset([1])
    FOLLOW_DO_in_command59 = frozenset([5])
    FOLLOW_aslim_in_command65 = frozenset([1])
    FOLLOW_OPEN_in_aslim75 = frozenset([5, 7, 9])
    FOLLOW_symbol_in_aslim77 = frozenset([5, 6, 7, 9])
    FOLLOW_CLOSE_in_aslim80 = frozenset([1])
    FOLLOW_GT_in_symbol121 = frozenset([5, 7, 9])
    FOLLOW_id_in_symbol181 = frozenset([1, 8])
    FOLLOW_link_in_symbol191 = frozenset([1, 8])
    FOLLOW_COLON_in_symbol224 = frozenset([5, 7, 9, 10])
    FOLLOW_info_in_symbol231 = frozenset([1])
    FOLLOW_symbol_in_symbol241 = frozenset([1])
    FOLLOW_OPEN_in_link272 = frozenset([5, 7, 9, 10])
    FOLLOW_symbol_in_link287 = frozenset([5, 6, 7, 9, 10])
    FOLLOW_info_in_link295 = frozenset([5, 6, 7, 9, 10])
    FOLLOW_symbol_in_link310 = frozenset([5, 6, 7, 9, 10])
    FOLLOW_info_in_link318 = frozenset([5, 6, 7, 9, 10])
    FOLLOW_CLOSE_in_link325 = frozenset([1])
    FOLLOW_ID_in_id334 = frozenset([1])
    FOLLOW_STRING_in_info341 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("slimLexer", slimParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
