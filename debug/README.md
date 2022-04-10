python preprocess_nl2sql.py

```shell
oov >= in select count (*) from plant_basic as t1 join dcc_basic as t2 on t1 . dcc_id = t2 . id where t1 . max_voltage_type >= value and t2 . n
ame_abbreviation = value
```





python preprocess_sql2nl.py

```
select sum(t1.TMR_GEN_VALUE) from PLANT_YEAR_QUANTITY as t1 join PLANT_BASIC as t2 on t1.ID = t2.ID where t1.YEAR like '%2020%' and t2.REGION like '江西' and t2.PLANT_TYPE like '%火力%'
```

preprocess_sql2nl.py:38

```python
find_match(no_value, i, yes_value)

no_value = ['select', 'sum', '(', 't1', '.', 'tmr_gen_value', ')', 'from', 'plant_year_quantity', 'as', 't1', 'join', 'plant_basic', 'as', 't2', 'on', 't1', '.', 'id', '=', 't2', '.', 'id', 'where', 't1', '.', 'year', 'like', 'value', 'and', 't2', '.', 'region', 'like', 'value', 'and', 't2', '.', 'plant_type', 'like', 'value']

i = 5

yes_value = ['select', 'sum(t1.TMR_GEN_VALUE)', 'from', 'PLANT_YEAR_QUANTITY', 'as', 't1', 'join', 'PLANT_BASIC', 'as', 't2', 'on', 't1.ID', '=', 't2.ID', 'where', 't1.YEAR', 'like', "'%2020%'", 'and', 't2.REGION', 'like', "'江西'", 'and', 't2.PLANT_TYPE', 'like', "'%火力%'"]
```

