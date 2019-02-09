import pypyrus_tables

table = tables.Table(path = 'data/table_double.tsv')
print(table)
table2 = table.filter(gender = 'Male')
print(table2)
