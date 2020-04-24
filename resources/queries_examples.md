Примеры запросов:

Подключение к базе:
```
    connect to "BASE_NAME.txt" ;
```

Добавление правила к грамматике:
```
    S = abcd S vds | eps ;
```

Запрос к базе данных:
```
    select <something> from <graph_name> where () ;
    select exists (u, v) from "BASE_NAME.txt" where (u) - S -> (v)
```