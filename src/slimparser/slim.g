grammar slim;

options {
	language=Python;
}

@members{

core = None			# the SLiM core component

}

command	:	symbol;

symbol	returns [s]:	id {$s = self.core.add($symbol.text)}| l = link {$s = l.s};

link returns [s, tmp]	:	OPEN {s_list = []} s1 = symbol {s_list.append(s1.s)} ( s2 = symbol {s_list.append(s2.s)})+  CLOSE 
				{$s = self.core.quick_link(None, s_list)};

id 	:	ID;
info 	:	STRING;


















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
