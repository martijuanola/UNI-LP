grammar jsbach;

root : function* EOF ;

function : FUNC ident* '|:' statements ':|' ;

statements : statement* ;

statement
    : ident ASSIGN (expr | exprList)    #assign
    
    | FUNC expr*                        #procedureCall
    
    | IF expr '|:' statements ':|'
      (ELSE '|:' statements ':|')?      #if
    | WHILE expr '|:' statements ':|'   #while
    
    | READ ident                        #read
    | WRITE (string | expr)*            #write
    | PLAY (expr | exprList)            #play
    | TEMPO expr                        #tempo
    
    | ident APPEND expr                 #listAppend
    | REMOVE ident '[' expr ']'         #listRemove
    ;

expr 
    : '(' expr ')'                  #parenthesis
    | (SUM|SUB) expr                #unary
    | expr (MUL|DIV|MOD) expr       #arithmetic     
    | expr (SUM|SUB) expr           #arithmetic
    | expr (LT|LE|GT|GE) expr       #relational
    | expr (EQ|NEQ) expr            #equality

    | '#' ident                     #arrayLength
    | ident '[' expr ']'            #arrayElement
    | ident                         #variable

    | NOTE                          #note
    | NUM                           #value
    ;

exprList : '{' expr* '}';

string : STRING;

ident : VAR;

// ---------- Arithmetic Operators  ---------- //

MUL     : '*' ;
DIV     : '/' ;
MOD     : '%';

SUM     : '+' ;
SUB     : '-' ;

// ---------- Relational Operators  ---------- //

LT      : '<' ;
LE      : '<=' ;
GT      : '>' ;
GE      : '>=' ;

// ---------- Equality Operators  ---------- //

EQ      : '=' ;
NEQ     : '/=' ;

// ---------- Statements Operators  ---------- //

ASSIGN  : '<-' ;
IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while';
READ    : '<?>';
WRITE   : '<!>';
PLAY    : '<:>';
TEMPO   : '<t>';
APPEND  : '<<';
REMOVE  : '8<';

// ---------- Notes ---------- //

NOTE    : [A-G] [0-8]? ('#'|'b')?;

// ---------- ID's ---------- //

VAR     : [a-z]~('\r' | '\n' | '"' | '|' | ' ' | ':' | '{' | '}' | '['| ']' | ')' | '(')*;
FUNC    : [A-Z]~('\r' | '\n' | '"' | '|' | ' ' | ':' | '{' | '}' | '['| ']' | ')' | '(')*;

// ---------- Values & Constants ---------- //

NUM     : [0-9]+ ;
STRING  : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

ESC_SEQ : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

COMMENT : '~~~' .*? '~~~' /*'\n'*/ -> skip;
WS      : [ \n]+ -> skip ;