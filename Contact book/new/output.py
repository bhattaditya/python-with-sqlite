import sqlite3

conn = sqlite3.connect("./Contact book/new/contacts.sqlite")
cursor = conn.cursor()

sql1 = "select * from contacts"

print("-----------ALL Contacts---------------")

print(f"Index\t\tName\t\tPhone\t\tEmail\t\tCity")

for index_value, name, phone, email, city_name in cursor.execute(sql1):
    print(f"{index_value}\t\t{name}\t\t {phone}\t\t{email}\t\t{city_name}")


sql2 = "Select index_value from contacts"
result = cursor.execute(sql2)
index_value = 123

for res in result:
    if (index_value,) == res:
        print("hi")
