grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

program : decllist EOF;

decllist : decl decllist | decl;
decl : vardecl | funcdecl;
// var declare 
vardecl : ('int' idenlist SEMI | 'float' idenlist SEMI);
idenlist : ID COMMA idenlist | ID;

// funcion declare 
funcdecl: ('float' | 'int') ID LB paralist RB body;
parameter : 'int' idenlist | 'float' idenlist;
paralist : paraprime | ;
paraprime : parameter SEMI paraprime | parameter;

// body declare 
body : LP stmllist RP;

stmllist : stmt SEMI stmllist | ;
stmt : (('int' | 'float') idenlist) | assignstmt | callstmt | returnstmt;

assignstmt : ID EQUAL expr;
callstmt : ID LB exprlist RB;
returnstmt : 'return' expr;

// expression declare
expr : expr1 '+' expr |expr1;
expr1 : expr2 '-' expr2 |expr2;
expr2 : expr2 ('/'|'*') expr3 | expr3;
expr3 : operator;

operator : INTLIT | FLOATLIT | callstmt | subexpr | ID; 

subexpr : LB expr LB ;

exprlist : exprime | ;
exprime : expr COMMA exprime | expr;

// const 
EQUAL : '=';
SEMI : ';';
COMMA : ',';
ID : [a-zA-Z]+;
INTLIT : [0-9]+;
FLOATLIT : [0-9]+ '.' [0-9]+;
LB : '(';
RB : ')';
LP : '{';
RP : '}';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;