grammar Gram;

full_script : script EOF;

script : statement DIV script
       |
       ;

statement : CONNECT TO STRING
          | LIST
          | select
          | named_pattern
          ;

select : SELECT obj FROM STRING WHERE where_expr ;

obj : unit
    | COUNT unit
    | EXISTS unit
    ;

unit : L IDENT PAR IDENT R
     | IDENT
     ;

where_expr : L vert_expr R SUB pattern RARR L vert_expr R ;

vert_expr : IDENT
          | UNDERLINE
          | IDENT DOT ID EQ INT
          ;

named_pattern : NT EQ pattern ;

pattern : alt ALT pattern
        | alt
        ;

alt : seq
    | L R
    ;

seq : subseq seq
    | subseq
    ;

subseq : scoped
       | scoped STAR
       | scoped PLUS
       | scoped QUEST
       ;

scoped : IDENT
       | NT
       | L pattern R
       ;

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

DIV : ';' ;

CONNECT : 'connect' ;

TO : 'to' ;

LIST : 'list' ;

SELECT : 'select' ;

FROM : 'from' ;

WHERE : 'where' ;

COUNT : 'count' ;

EXISTS : 'exists' ;

L : '(' ;

R : ')' ;

PAR : ',' ;

SUB : '-' ;

RARR : '->' ;

UNDERLINE : '_' ;

DOT : '.' ;

ID : 'id' ;

EQ : '=' ;

ALT : '|' ;

STAR : '*' ;

PLUS : '+' ;

QUEST : '?' ;

STRING : '"' (LOWERCASE | UPPERCASE | [0-9] | '-' | '_' | '/' | '.')* '"' ;

IDENT : LOWERCASE LOWERCASE* ;

INT : '0' | [1-9] [0-9]* ;

NT : UPPERCASE LOWERCASE* ;

WS : [ \n\t\r]+ -> skip;