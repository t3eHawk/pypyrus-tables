import pypyrus_tables

table = tables.Table(path = 'data/table_double.tsv')
print(table)
table2 = table.select(gender = 'Male')
print(table2)
table3 = table.select(first_name = 'Melodie', last_name = 'Belhome')
print(table3)
