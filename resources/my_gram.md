S eps
S ST div S
ST connect to string
ST list
ST SELECT
ST NPAT
NPAT nt eq PATTERN
SELECT select OBJ from string where WHERE
OBJ UNIT
OBJ count UNIT
OBJ exists UNIT
UNIT l ident par ident r
UNIT ident
WHERE l VERT_EXPR r minus PATTERN minus gt l VERT_EXPR r
VERT_EXPR ident
VERT_EXPR underline
VERT_EXPR ident dot id eq int
PATTERN ALT alt PATTERN
PATTERN ALT
ALT SEQ
ALT l r
SEQ SUB_SEQ SEQ
SEQ SUB_SEQ
SUB_SEQ SCOPED
SUB_SEQ SCOPED star
SUB_SEQ SCOPED plus
SUB_SEQ SCOPED quest
SCOPED ident
SCOPED nt
SCOPED l PATTERN r