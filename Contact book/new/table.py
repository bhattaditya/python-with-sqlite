import sqlite3

try:
    conn = sqlite3.connect("./Contact book/new/contacts.sqlite")
    cursor = conn.cursor()

    sql1 = "CREATE TABLE IF NOT EXISTS contacts (index_value INTEGER PRIMARY KEY, name TEXT, phone INTEGER, email TEXT, city_name TEXT)"
    cursor.execute(sql1)
    print("contacts table created ...")
    cursor.close()
    conn.commit()

except sqlite3.Error as e:
    print("Error while creating a sqlite table ", e) 

finally:
    conn.close()
