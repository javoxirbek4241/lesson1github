import psycopg2
conn = psycopg2.connect(dbname = 'cars', user = 'postgres', port = 5432, password='4241')
cursor = conn.cursor()
# 1-mashq
# name = 'cars2'
# yil = 'year'
# query = f"alter table {name} drop column {yil}"
# cursor.execute(query)
# conn.commit()
#
# cursor.close()
# conn.close()
# query = "SELECT * FROM cars2;"
# cursor.execute(query)
#
# rows = cursor.fetchall()
# print(rows)
# 2-mashq

# query = f"delete from cars2 where id%2=0"
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()
# query = "SELECT * FROM cars2;"
# cursor.execute(query)
#
# rows = cursor.fetchall()
# print(rows)
# 3-mashq
# conn.autocommit = True
# query = f'drop database books'
# cursor.execute(query)
# cursor.close()
# conn.close()

# 4-mashq
# query = "update cars2 set make = 'gm' where id%%3=0"
# cursor.execute(query,('gm',))
# conn.commit()
# cursor.close()
# conn.close()
# query = "SELECT * FROM cars2;"
# cursor.execute(query)
#
# rows = cursor.fetchall()
# print(rows)
# 5-mashq
# query = "alter table cars2 rename to cars"
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()

# 6-mashq
# query = "alter table cars rename column make  to ishlangan"
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()
# query = "SELECT * FROM cars;"
# cursor.execute(query)
# print(cursor.fetchall())
# 7-mashq
# query = 'ALTER TABLE cars ALTER COLUMN name TYPE VARCHAR(30);'
# cursor.execute(query)
# conn.commit()
# cursor.close()
# conn.close()







