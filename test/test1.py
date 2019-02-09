# Testing #1:
# Work with table by from file by path.
# Get table parameters.
# Get items from table.

import pypyrus_tables

table = tables.Table(path = 'data/table.tsv')

print('Count of fields in table:', table.COUNT_COLS)
print('Count of records in table:', table.COUNT_ROWS)

print(table.first_name)
print(table['first_name'])
print(table[2].first_name)
