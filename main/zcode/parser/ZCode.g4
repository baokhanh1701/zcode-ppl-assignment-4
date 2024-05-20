grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// //! --------------------------  Lexical structure ----------------------- //

// declared
program: NEWLINE* list_declared EOF;

list_declared:  declared list_declared |  declared;
declared: function | variables ignore;

variables: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR ID ASSIGNINIT expression;
keyword_var: type_prime ID ( | LBRACKET list_NUMBER_LIT RBRACKET) (ASSIGNINIT expression)?;
implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;

type_prime: BOOL | NUMBER | STRING;
list_NUMBER_LIT: NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;

function: FUNC ID LPAREN prameters_list? RPAREN  (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: prameters COMMA prameters_list | prameters;
prameters: type_prime ID | type_prime ID LBRACKET list_NUMBER_LIT RBRACKET;

// Expression
expression: expression1 CONCAT expression1                                         | expression1;
expression1: expression2 (EQ | EQSTRING | NE | LT | LE | GT | GE) expression2      | expression2;
expression2: expression2 (AND | OR) expression3                                    | expression3;
expression3: expression3 (ADD | SUB) expression4                                   | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5                             | expression5;
expression5: NOT expression5                                                       | expression6;
expression6: (SUB | ADD) expression6                                               | expression7;
expression7: (ID | ID LPAREN index_operators? RPAREN) LBRACKET index_operators  RBRACKET  | expression8;
expression8: ID  | literal | LPAREN expression RPAREN | ID LPAREN index_operators? RPAREN;
index_operators: expression COMMA index_operators | expression;

// Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET index_operators  RBRACKET;

//  Statements
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;
declaration_statement: variables ignore;
assignment_statement : lhs ASSIGNINIT expression ignore;
if_statement         : IF LPAREN expression RPAREN ignore? statement elif_list (ELSE ignore? statement )?;
for_statement        : FOR ID UNTIL expression BY expression ignore? statement;
break_statement      : BREAK ignore;
continue_statement   : CONTINUE  ignore;
return_statement     : RETURN expression? ignore;
call_statement       : ID LPAREN index_operators? RPAREN ignore;
block_statement      : BEGIN ignore statement_list END ignore;

lhs: ID LBRACKET index_operators  RBRACKET | ID;
statement_list: statement statement_list | ; 
elif_list:ELIF LPAREN expression RPAREN ignore? statement elif_list | ;

// kí tự bỏ qua
ignore: NEWLINE+;
//! --------------------------  Lexical structure ----------------------- //
// TODO KeyWord

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';
// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
ASSIGNINIT: '<-';
NE: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
CONCAT: '...';
EQSTRING: '==';

// TODO Separators
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal 
//! STRING_LIT nhớ dùng python bỏ đi " " đầu và cuối
fragment INT: [0-9]+;
NUMBER_LIT: INT ('.' INT?)? ([Ee] [-+]? INT)?;
STRING_LIT: '"' (~[\n\\"] | '\\' [bfrnt'\\] | '\'"' )* '"' {self.text = self.text[1:-1];};

NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [bfrnt'\\] | '\'"' )* (EOF | '\n') 
{
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (~[\n\\"] | '\\' [bfrnt'\\] | '\'"' )* '\\' ~[bfrnt'\\]
    {raise IllegalEscape(self.text[1:])};
//!  -------------------------- end Lexical structure ------------------- //