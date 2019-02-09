# Testing #2:
# Work with table by using different constructor parameters.
# Get all table presentatoin for any case.

import pypyrus_tables

table = tables.Table(path = 'data/table.tsv')
print('\nTable #1 Presentations.')
print(table)
print('Path:\n', table.PATH)
print('Lines:\n', table.LINES)
print('Rows:\n', table.ROWS)
print('Columns:\n', table.COLUMNS)
print('Data:\n', table.DATA)

lines = table.LINES
table2 = tables.Table(lines = lines)
print('\nTable #2 Presentations.')
print(table2)
print('Path:\n', table2.PATH)
print('Lines:\n', table2.LINES)
print('Rows:\n', table2.ROWS)
print('Columns:\n', table2.COLUMNS)
print('Data:\n', table2.DATA)

rows = table.ROWS
table3 = tables.Table(rows = rows)
print('\nTable #3 Presentations.')
print(table3)
print('Path:\n', table3.PATH)
print('Lines:\n', table3.LINES)
print('Rows:\n', table3.ROWS)
print('Columns:\n', table3.COLUMNS)
print('Data:\n', table3.DATA)

columns = table.COLUMNS
table4 = tables.Table(columns = columns)
print('\nTable #4 Presentations.')
print(table4)
print('Path:\n', table4.PATH)
print('Lines:\n', table4.LINES)
print('Rows:\n', table4.ROWS)
print('Columns:\n', table4.COLUMNS)
print('Data:\n', table4.DATA)

data = table.DATA
table5 = tables.Table(data = data)
print('\nTable #5 Presentations.')
print(table5)
print('Path:\n', table5.PATH)
print('Lines:\n', table5.LINES)
print('Rows:\n', table5.ROWS)
print('Columns:\n', table5.COLUMNS)
print('Data:\n', table5.DATA)
