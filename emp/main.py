import sqlite3
# establishing  a database connection
con = sqlite3.connect('./emp/TEST.db')
# preparing a cursor object
cursor = con.cursor()

# preparing sql statement

records = [
    (123456, 'John', 25, 'M', 50000.00),
    (234651, 'Juli', 35, 'F', 75000.00),
    (345121, 'Fred', 48, 'M', 125000.00),
    (562412, 'Rosy', 28, 'F', 52000.00),
    ]

sql = '''
       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''

# executing sql statement using try ... except blocks
try:
    cursor.executemany(sql, records)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()

# closing the connection
con.close()