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
    ST -> connect to string | LISTIFY | SELECT | NPAT
    LISTIFY -> list | list string | list edges string
    SELECT -> select OBJ from string where WHERE
              | select OBJ from string where WHERE with ALGO
    NPAT -> nt eq PATTERN
    OBJ -> UNIT | count UNIT | exists UNIT
    UNIT -> l ident par ident r | ident
    WHERE -> l VERT_EXPR r minus PATTERN minus gt l VERT_EXPR r
    VERT_EXPR -> ident | underline | ident dot id eq int
```

ST - Выражение обращения к БД:
    list                                       - список графов в текущей базе
    list `base`                                - список графов в базе `base`
    list edges `base/g.txt`                    - список ребер в `base/g.txt`
    connect to `base`                          - подключиться к базе `base`
    select `obj` from `base` where `condition` - запрос к базе `base`
    select `o` from `b` where `c` with `alg`   - запрос с помощью `alg`
    `nt` eq `regex`                            - задать правило `nt` -> `regex`

Алгоритмы для использования в запросах:
`hellings` - алгоритм Хеллингса для проверки КС-достижимости
`matrix` - алгоритм проверки КС-достижимости на основе произведения матриц
`tensor` - алгоритм проверки КС-достижимости на основе тензорного произведения 


Query examples presented in `resources/queries_examples.md`