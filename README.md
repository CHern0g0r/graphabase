# GRAPHABASE
[![Build Status](https://travis-ci.org/CHern0g0r/graphabase.svg?branch=master)](https://travis-ci.org/CHern0g0r/graphabase)

## Graph database with Formal languages

From graphabase folder.

To build project use:
```
  ./build.sh
```

To run tests use command:

```
  python3 -m pytest test
```

## Context free queries

Query grammar described in `resources/my_gram.md`

## Syntax:

```
    S -> ST div S | eps
    ST -> connect to string | list | SELECT | NPAT
    SELECT -> select OBJ from string where WHERE
    NPAT -> nt eq PATTERN
    OBJ -> UNIT | count UNIT | exists UNIT
    UNIT -> l ident par ident r | ident
    WHERE -> l VERT_EXPR r minus PATTERN minus gt l VERT_EXPR r
    VERT_EXPR -> ident | underline | ident dot id eq int
    PATTERN -> ALT alt PATTERN | ALT
    ALT -> SEQ | l r
    SEQ -> SUB_SEQ SEQ | SUB_SEQ
    SUB_SEQ -> SCOPED | SCOPED star | SCOPED plus | SCOPED quest
    SCOPED -> ident | nt | l PATTERN r
```

ST - Выражение обращения к БД:
    list                                       - вывести список графов
    connect to `base`                          - подключиться к базе `base`
    select `obj` from `base` where `condition` - запрос к базе `base`
    `nt` eq `regex`                            - задать правило `nt` -> `regex`

PATTERN - регулярное выражение над терминальным и нетерминальным алфавитами.

Query examples presented in `resources/queries_examples.md`