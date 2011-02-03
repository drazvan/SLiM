grammar slim;

options {
	language=Python;
}

@members{

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
}

start	:	command+;

command	:	{self.mode = "add"} s1 = symbol| 
		{self.mode = "do"} DO s = symbol {self.do(s.s)};
		
symbol	returns [s, tmp]:	id {$s = self.symbol_id($id.text)} 
                               (COLON (info {self.set_info($s, $info.text)} | s2 = symbol {self.map($id.text, s2.s)}) )? 		 
			| l = link {$s = self.symbol_link(l.s_list)} 
			       (COLON (info {self.set_info($s, $info.text)} | s2 = symbol {self.map($s, s2.s)}) )?;		// 2

link returns [s_list, tmp]	:	OPEN {$s_list = []} s1 = symbol {$s_list.append(s1.s)} ( s2 = symbol {$s_list.append(s2.s)})*  CLOSE;

id 	:	ID;
info	:	STRING;






COMMENT
    :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    ;


DO 	:	'do';

OPEN 	:	'{';
CLOSE 	:	'}';
COLON 	:	':';

ID  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
    ;

INT :	'0'..'9'+
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;

STRING
    :  '"' ( ESC_SEQ | ~('\\'|'"') )* '"'
    ;

fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;
