# Testing #4:
# Work with no head table.

import pypyrus_tables

table = tables.Table(path = 'data/nohead.tsv', head = False)

print('Count of fields in table:', table.COUNT_COLS)
print('Count of records in table:', table.COUNT_ROWS)
print(table)
