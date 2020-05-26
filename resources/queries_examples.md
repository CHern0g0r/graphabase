Примеры запросов:

Подключение к базе:
```
    connect to "BASE_NAME" ;
```

Вывести список графов из текущей базы:
```
    list;
```

Вывести список графов с указанием базы:
```
    list "BASE_NAME";
```

Вывести список ребер данного графа:
```
    list "BASE_NAME/graph.txt";
```

Добавление правила к грамматике:
```
    S = abcd S vds | eps ;
```

Запрос к базе данных:
```
    select <something> from <graph_name> where () ;
    select exists (u, v) from "BASE_NAME" where (u) - S -> (v)
```

Запрос к базе данных с указанием алгоритма выполнения:
```
    select <something> from <graph_name> where () with <algo_name>;
    select exists (u, v) from "BASE_NAME" where (u) - S -> (v) with tensor
```