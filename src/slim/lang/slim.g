grammar slim;

options {
	language=Python;
}

@header{
from slim.symbolic.slim import Slim
}

@members{

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
}

start	:	command+;

command	:	{self.mode = "add"}{self.slim = Slim()} s = aslim {self.core.tell(self.slim); self.core.slim.dump()} | 
		{self.mode = "do"}{self.slim = Slim()} DO s = aslim {self.slim.dump()};

aslim	:	OPEN symbol+ CLOSE;
		
symbol	returns [s, tmp]: 	
                          GT ? 
                          (
                          (id {$s = self.symbol_id($id.text)} | l = link {$s = self.symbol_link(l.s_list)}) 
                          (COLON (i2 = info {self.set_info($s, $i2.text)} | s2 = symbol {self.map($s, s2.s)}) )?
			  )
			;		

link returns [s_list, tmp]	:	OPEN {$s_list = []} 
					(s1 = symbol {$s_list.append(s1.s)} | i1=info {$s_list.append(self.slim.add(None, $i1.text.strip()[1:-1]))})
					(s2 = symbol {$s_list.append(s2.s)} | i2=info {$s_list.append(self.slim.add(None, $i2.text.strip()[1:-1]))})*  CLOSE;

id 	:	ID;
info	:	STRING;






COMMENT
    :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    ;


DO 	:	'do';

OPEN 	:	'{';
CLOSE 	:	'}';
COLON 	:	':';
GT	:	'>';

ID  :	('a'..'z'|'A'..'Z'|'_'|'-') ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'-')*
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
