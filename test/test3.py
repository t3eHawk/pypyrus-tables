# Testing #3:
# Work with empty table.

import pypyrus_tables

table = tables.Table(path = 'data/empty.tsv')

print('Count of fields in table:', table.COUNT_COLS)
print('Count of records in table:', table.COUNT_ROWS)
print(table)
