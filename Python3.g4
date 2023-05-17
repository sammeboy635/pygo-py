grammar Python3;

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

// Literals
BOOLEAN : 'True' | 'False';
STRING : '"' (~["\\] | '\r' | '\n' | '\t' | '\\' .)* '"';
INTEGER : [0-9]+;
FLOAT : [0-9]* '.' [0-9]+;
ID : [a-zA-Z_][a-zA-Z0-9_]*;


// Unknown
// UNKNOWN : . ;

WS : [ \t]+ -> skip; // skip spaces, tabs, newlines


// Parser rules

program : stat* ;

function_def : DEF ID OPEN_PAREN params_id? CLOSED_PAREN COLON suite ;

params_id : ID (COMMA ID)* ;

stat: function_def
	| assignment
	| expr END  // expression statement
	| function_call END
    ;

assignment: ID ASSIGNMENT expr END | function_call;
function_call: ID OPEN_PAREN arg_list? CLOSED_PAREN ;  // function call

arg_list: expr (COMMA expr)* ;  // list of arguments

suite: END TAB? (stat END TAB?)*;

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
	  | var //load var
      | number  // number literal
      | STRING  // string literal
      ;

number: INTEGER  // integer literal
      	| FLOAT  // floating point literal
      ;

var : ID ;// load var