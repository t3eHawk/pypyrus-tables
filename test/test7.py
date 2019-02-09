# Testing #7:
# Export table to the file.

import pypyrus_tables

table = tables.Table(path = 'data/table.tsv')
table.write('data/output.tsv')

table2 = tables.Table(path = 'data/output.tsv')
print(table2)
