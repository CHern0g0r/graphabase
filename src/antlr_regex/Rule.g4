grammar Rule;

regex : pattern EOF
      | EOF
      ;

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

L : '(' ;

R : ')' ;

ALT : '|' ;

STAR : '*' ;

PLUS : '+' ;

QUEST : '?' ;

IDENT : LOWERCASE LOWERCASE* ;

NT : UPPERCASE LOWERCASE* ;

WS : [ \n\t\r]+ -> skip;