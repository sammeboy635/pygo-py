grammar MathGrammar;

// Keywords
IMPORT : 'import' ;
FROM : 'from' ;
CLASS : 'class' ;
DEF : 'def' ;
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
WHILE : 'while';
FOR : 'for';
TRY : 'try';
EXCEPT : 'except';
FINALLY : 'finally';
WITH : 'with';
PASS : 'pass';
BREAK : 'break';
CONTINUE : 'continue';
RETURN : 'return';
RAISE : 'raise';
YIELD : 'yield';
ASYNC : 'async';
AWAIT : 'await';
GLOBAL : 'global';
NONLOCAL : 'nonlocal';
ASSERT : 'assert';
LAMBDA : 'lambda';

// Types
T_INT : 'int';
T_FLOAT : 'float';
T_STRING : 'str';

// Literals
ID : [a-zA-Z_][a-zA-Z0-9_]*;
BOOLEAN : 'True' | 'False';
STRING : '"' (~["\\]* ('\\' .)*)* '"' | '\'' (~['\\]* ('\\' .)*)* '\'';
INTEGER : [0-9]+;
FLOAT : [0-9]* '.' [0-9]+;

// Operators
ADDITION : '+';
SUBTRACTION : '-';
MULTIPLICATION : '*';
DIVISION : '/';
FLOOR_DIVISION : '//';
MODULO : '%';
EXPONENT : '**';
EQUALITY : '==';
INEQUALITY : '!=';
LESS_THAN : '<';
GREATER_THAN : '>';
LESS_THAN_OR_EQUAL_TO : '<=';
GREATER_THAN_OR_EQUAL_TO : '>=';
LOGICAL_AND : 'and';
LOGICAL_OR : 'or';
LOGICAL_NOT : 'not';
BITWISE_AND : '&';
BITWISE_OR : '|';
BITWISE_XOR : '^';
BITWISE_NOT : '~';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ASSIGNMENT : '=';
ADDITION_ASSIGNMENT : '+=';
SUBTRACTION_ASSIGNMENT : '-=';
MULTIPLICATION_ASSIGNMENT : '*=';
DIVISION_ASSIGNMENT : '/=';
FLOOR_DIVISION_ASSIGNMENT : '//=';
MODULO_ASSIGNMENT : '%=';
EXPONENTIATION_ASSIGNMENT : '**=';
BITWISE_AND_ASSIGNMENT : '&=';
BITWISE_OR_ASSIGNMENT : '|=';
BITWISE_XOR_ASSIGNMENT : '^=';
LEFT_SHIFT_ASSIGNMENT : '<<=';
RIGHT_SHIFT_ASSIGNMENT : '>>=';

// Parenthesis
OPEN_PAREN : '(';
CLOSED_PAREN : ')';

// Brackets
OPEN_BRACKET : '[';
CLOSED_BRACKET : ']';

// Format
COLON : ':';
END : '\r'? '\n';
TAB : '\t';
COMMA : ',';

// Unknown
// UNKNOWN : . ;

WS : [ \t]+ -> skip; // skip spaces, tabs, newlines


// Parser rules
prog: stat+ ;
stat: function_def
	| expr END  // expression statement
    | ASSIGNMENT expr END  // assignment statement
	| function_call
    ;

function_call: STRING OPEN_PAREN arg_list? CLOSED_PAREN ;  // function call

arg_list: expr (COMMA expr)* ;  // list of arguments

function_def: 'def' STRING OPEN_PAREN arg_list_literal? CLOSED_PAREN COLON ;  // function call

arg_list_literal: STRING (COMMA STRING)* ;  // list of arguments

suite: '\n' TAB stat*;

expr: expr ADDITION term  // addition
    | expr SUBTRACTION term  // subtraction
    | function_call // function call
    | term  // term
    ;

term: term MULTIPLICATION factor  // multiplication
    | term DIVISION factor  // division
    | term EXPONENT factor  // exponentiation
    | factor  // factor
    ;

factor: OPEN_PAREN expr CLOSED_PAREN  // parenthesized expression
      | number  // number literal
      | STRING  // string literal
      ;

number: INTEGER  // integer literal
      | FLOAT  // floating point literal
      ;