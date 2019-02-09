# Testing #8:
# Work with large table (1000 rows).
# Get item from large table.

import pypyrus_tables

table = tables.Table(path = 'data/large.tsv')

print('Count of fields in table:', table.COUNT_COLS)
print('Count of records in table:', table.COUNT_ROWS)

i = int(input('Enter the index of row you want to see: '))
table2 = table[i]
print(table2)
