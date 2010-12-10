# $ANTLR 3.3 Nov 30, 2010 12:45:30 E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g 2010-12-09 12:00:18

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
DO=4
COLON=5
OPEN=6
CLOSE=7
ID=8
STRING=9
COMMENT=10
INT=11
WS=12
ESC_SEQ=13
HEX_DIGIT=14
UNICODE_ESC=15
OCTAL_ESC=16

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DO", "COLON", "OPEN", "CLOSE", "ID", "STRING", "COMMENT", "INT", "WS", 
    "ESC_SEQ", "HEX_DIGIT", "UNICODE_ESC", "OCTAL_ESC"
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

    mode = ""			# the current mode

    def symbol_id(self, id):
        """symbol rule, id branch"""
        
        if self.mode == "add" or self.mode == "do":
            s = self.core.get(id)
            if s == None:
                s = self.core.add(id)
            else:
                s = s.id
                
            return s

        elif self.mode == "do":
            s = self.core.get(id)
            if s == None:
                print "Could not find symbol '", id, "'"
                return None
            return s.id
                
    def symbol_link(self, s_list):
        """symbol rule, link branch"""
        
        if self.mode == "add" or self.mode == "do":
            link = self.core.get_link(*s_list)
            
            if link == None:
                return self.core.link(None, None, s_list)
            else:
                return link.id

        elif self.mode == "do":
            if None in s_list:
                print "There is a None in the link."
                return None
                
            link = self.core.get_link(*s_list)
            
            if link == None:
                return None
            else:
                return link.id

    def do(self, s):
        """Does something indicated by a symbol"""
        
        if s != None:
            self.core.do(s)
            
    def set_info(self, id, val):
        """Sets the information for a symbol"""
        
        s = self.core.get(id)
        if s != None:
            self.core.set_info(id, val.strip()[1:-1])
            
    def map(self, id1, id2):
        if id2 != None:
            self.core.map(id1, id2)



    # $ANTLR start "start"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:1: start : ( command )+ ;
    def start(self, ):

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:7: ( ( command )+ )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:9: ( command )+
                pass 
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:9: ( command )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == DO or LA1_0 == OPEN or LA1_0 == ID) :
                        alt1 = 1


                    if alt1 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:73:9: command
                        pass 
                        self._state.following.append(self.FOLLOW_command_in_start26)
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
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:1: command : (s1= symbol | DO s= symbol );
    def command(self, ):

        s1 = None

        s = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:9: (s1= symbol | DO s= symbol )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == OPEN or LA2_0 == ID) :
                    alt2 = 1
                elif (LA2_0 == DO) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:75:11: s1= symbol
                    pass 
                    #action start
                    self.mode = "add"
                    #action end
                    self._state.following.append(self.FOLLOW_symbol_in_command41)
                    s1 = self.symbol()

                    self._state.following.pop()


                elif alt2 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:76:3: DO s= symbol
                    pass 
                    #action start
                    self.mode = "do"
                    #action end
                    self.match(self.input, DO, self.FOLLOW_DO_in_command49)
                    self._state.following.append(self.FOLLOW_symbol_in_command55)
                    s = self.symbol()

                    self._state.following.pop()
                    #action start
                    self.do(s.s)
                    #action end



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
            self.tmp = None




    # $ANTLR start "symbol"
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:78:1: symbol returns [s, tmp] : ( id ( COLON ( info | s2= symbol ) )? | l= link ( COLON ( info | s2= symbol ) )? );
    def symbol(self, ):

        retval = self.symbol_return()
        retval.start = self.input.LT(1)

        s2 = None

        l = None

        id1 = None

        info2 = None

        info3 = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:78:24: ( id ( COLON ( info | s2= symbol ) )? | l= link ( COLON ( info | s2= symbol ) )? )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == ID) :
                    alt7 = 1
                elif (LA7_0 == OPEN) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:78:26: id ( COLON ( info | s2= symbol ) )?
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_symbol70)
                    id1 = self.id()

                    self._state.following.pop()
                    #action start
                    retval.s = self.symbol_id(((id1 is not None) and [self.input.toString(id1.start,id1.stop)] or [None])[0])
                    #action end
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:79:32: ( COLON ( info | s2= symbol ) )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COLON) :
                        alt4 = 1
                    if alt4 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:79:33: COLON ( info | s2= symbol )
                        pass 
                        self.match(self.input, COLON, self.FOLLOW_COLON_in_symbol107)
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:79:39: ( info | s2= symbol )
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == STRING) :
                            alt3 = 1
                        elif (LA3_0 == OPEN or LA3_0 == ID) :
                            alt3 = 2
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            raise nvae

                        if alt3 == 1:
                            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:79:40: info
                            pass 
                            self._state.following.append(self.FOLLOW_info_in_symbol110)
                            info2 = self.info()

                            self._state.following.pop()
                            #action start
                            self.set_info(retval.s, ((info2 is not None) and [self.input.toString(info2.start,info2.stop)] or [None])[0])
                            #action end


                        elif alt3 == 2:
                            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:79:79: s2= symbol
                            pass 
                            self._state.following.append(self.FOLLOW_symbol_in_symbol120)
                            s2 = self.symbol()

                            self._state.following.pop()
                            #action start
                            self.map(((id1 is not None) and [self.input.toString(id1.start,id1.stop)] or [None])[0], s2.s)
                            #action end








                elif alt7 == 2:
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:80:6: l= link ( COLON ( info | s2= symbol ) )?
                    pass 
                    self._state.following.append(self.FOLLOW_link_in_symbol141)
                    l = self.link()

                    self._state.following.pop()
                    #action start
                    retval.s = self.symbol_link(l.s_list)
                    #action end
                    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:81:11: ( COLON ( info | s2= symbol ) )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COLON) :
                        alt6 = 1
                    if alt6 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:81:12: COLON ( info | s2= symbol )
                        pass 
                        self.match(self.input, COLON, self.FOLLOW_COLON_in_symbol157)
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:81:18: ( info | s2= symbol )
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == STRING) :
                            alt5 = 1
                        elif (LA5_0 == OPEN or LA5_0 == ID) :
                            alt5 = 2
                        else:
                            nvae = NoViableAltException("", 5, 0, self.input)

                            raise nvae

                        if alt5 == 1:
                            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:81:19: info
                            pass 
                            self._state.following.append(self.FOLLOW_info_in_symbol160)
                            info3 = self.info()

                            self._state.following.pop()
                            #action start
                            self.set_info(retval.s, ((info3 is not None) and [self.input.toString(info3.start,info3.stop)] or [None])[0])
                            #action end


                        elif alt5 == 2:
                            # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:81:58: s2= symbol
                            pass 
                            self._state.following.append(self.FOLLOW_symbol_in_symbol170)
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
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:83:1: link returns [s_list, tmp] : OPEN s1= symbol (s2= symbol )* CLOSE ;
    def link(self, ):

        retval = self.link_return()
        retval.start = self.input.LT(1)

        s1 = None

        s2 = None


        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:83:28: ( OPEN s1= symbol (s2= symbol )* CLOSE )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:83:30: OPEN s1= symbol (s2= symbol )* CLOSE
                pass 
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_link190)
                #action start
                retval.s_list = []
                #action end
                self._state.following.append(self.FOLLOW_symbol_in_link198)
                s1 = self.symbol()

                self._state.following.pop()
                #action start
                retval.s_list.append(s1.s)
                #action end
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:83:85: (s2= symbol )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == OPEN or LA8_0 == ID) :
                        alt8 = 1


                    if alt8 == 1:
                        # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:83:87: s2= symbol
                        pass 
                        self._state.following.append(self.FOLLOW_symbol_in_link208)
                        s2 = self.symbol()

                        self._state.following.pop()
                        #action start
                        retval.s_list.append(s2.s)
                        #action end


                    else:
                        break #loop8
                self.match(self.input, CLOSE, self.FOLLOW_CLOSE_in_link215)



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
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:85:1: id : ID ;
    def id(self, ):

        retval = self.id_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:85:5: ( ID )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:85:7: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_id224)



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
    # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:86:1: info : STRING ;
    def info(self, ):

        retval = self.info_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:86:6: ( STRING )
                # E:\\Work\\waa\\waa-slim\\src\\slimparser\\slim.g:86:8: STRING
                pass 
                self.match(self.input, STRING, self.FOLLOW_STRING_in_info231)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "info"


    # Delegated rules


 

    FOLLOW_command_in_start26 = frozenset([1, 4, 6, 8])
    FOLLOW_symbol_in_command41 = frozenset([1])
    FOLLOW_DO_in_command49 = frozenset([6, 8])
    FOLLOW_symbol_in_command55 = frozenset([1])
    FOLLOW_id_in_symbol70 = frozenset([1, 5])
    FOLLOW_COLON_in_symbol107 = frozenset([6, 8, 9])
    FOLLOW_info_in_symbol110 = frozenset([1])
    FOLLOW_symbol_in_symbol120 = frozenset([1])
    FOLLOW_link_in_symbol141 = frozenset([1, 5])
    FOLLOW_COLON_in_symbol157 = frozenset([6, 8, 9])
    FOLLOW_info_in_symbol160 = frozenset([1])
    FOLLOW_symbol_in_symbol170 = frozenset([1])
    FOLLOW_OPEN_in_link190 = frozenset([6, 8])
    FOLLOW_symbol_in_link198 = frozenset([6, 7, 8])
    FOLLOW_symbol_in_link208 = frozenset([6, 7, 8])
    FOLLOW_CLOSE_in_link215 = frozenset([1])
    FOLLOW_ID_in_id224 = frozenset([1])
    FOLLOW_STRING_in_info231 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("slimLexer", slimParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
