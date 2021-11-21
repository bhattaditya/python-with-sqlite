import sqlite3
import time

contact_list = {}
     
def phone_number():
    while True:
        try:
            phone = int(input("Phone number: "))
            break
        except ValueError as e:
            print(e)
            print("Please enter again ")
            continue 

    return phone    


def email_address():
    while True:
        email = input("Email: ")
        if not email.__contains__("@"):
            print("please enter a valid one ")
            continue
        else: 
            break
    return email    


def index_generator():
    generated = False

    while not generated:
        try:
            index_value = int(input("Please enter this number carefully as it can not be changed later: "))
            if index_value in contact_list:
                print("Index already exists")
            else:
                try:
                    print("checking in DB")
                    found = 0
                    time.sleep(2)
                    conn = sqlite3.connect("./Contact book/contacts.sqlite")
                    cursor = conn.cursor()
                    sql = "Select index_value from contacts"
                    result = cursor.execute(sql)
                    for res in result:
                        if (index_value,) == res:
                            found = 1
                            print("Index already exists...")
                            time.sleep(1)

                    if found == 0:
                        print("Please enter below details")
                        generated = True

                except sqlite3.Error as e:
                    print(e)    

                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()

        except ValueError as e:
            print(e)   
            print("enter again") 

    return index_value


def adding_contact():
    index_value = index_generator()
    name = input("Name: ")
    phone = phone_number()   
    email = email_address()
    city_name = input("City: ")
    contact_list[index_value] = [name, phone, email, city_name]

    try:
        conn = sqlite3.connect("./Contact book/contacts.sqlite")
        cursor = conn.cursor()

        sql = "Insert into contacts values (?,?,?,?,?)"
        cursor.execute(sql,(index_value, name, phone, email, city_name))
        conn.commit()
        time.sleep(1)
        print("Contact added successfully!\n")       

    except sqlite3.Error as e:
        print("Cannot add record into table contacts... ", e)    

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    

def deleting_contact(contact):
    if contact not in contact_list:
        return 0
    else:
        del contact_list[contact]   
        try:
            conn = sqlite3.connect("./Contact book/contacts.sqlite")
            cursor = conn.cursor()

            sql = "delete from contacts where index_value = ?"
            cursor.execute(sql, (contact,))
            conn.commit()

        except sqlite3.Error as e:
            print("Cannot delete record from table contacts... ", e)    

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


def modifying_contact(contact, conn):
    if contact not in contact_list.keys():
        return 0
    else:
        for index in contact_list.keys():
            if index == contact:
                while True:
                    try:
                        edit = input("Do you want to edit email address or phone no (e/n): ")
                        if edit == 'n':
                            
                            phone = phone_number()
                            sql1 = "update contacts set phone = ? where index_value = ?"
                            conn.execute(sql1, (phone, contact,))
                            contact_list[index][1] = phone  
                            conn.commit()
                            break
                        elif edit == 'e':
                            email = email_address()
                            sql1 = "update contacts set email = ? where index_value = ?"
                            conn.execute(sql1, (email, contact,))
                            contact_list[index][2] = email   
                            conn.commit()
                            break  
                    except ValueError as e:
                        print("please type 'e' or 'n'")

def show_contacts_length():
    try:
        conn = sqlite3.connect("./Contact book/contacts.sqlite")
        cursor = conn.cursor()
        sql = "Select * from contacts"
        result  = cursor.execute(sql)
        return len(result.fetchall()) 

    except sqlite3.Error as e:
        print(e)    

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def show_contacts():
    try:
        conn = sqlite3.connect("./Contact book/contacts.sqlite")
        cursor = conn.cursor()

        if show_contacts_length() < 1:
            time.sleep(1)
            print("Contact book is empty...")
        else:  
            print("Fetching details...")
            time.sleep(1)  
            sql = "Select * from contacts"
            for index_v, name, phone, email, city_name in cursor.execute(sql):
                print(f"index: {index_v} Name: {name} Phone: {phone} Email: {email} City: {city_name}")           
        
    except sqlite3.Error as e:
        print(e)    

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def menu():
    while True:
        try:
            choice = int(input("1. Adding contact\n2. Deleting contact\n3. Modiying contact\n4. Show contacts list\n5. Exit\n\n>: "))
            conn = sqlite3.connect("./Contact book/contacts.sqlite")

            if choice == 1:
                adding_contact()

                print()
                
            if  choice == 2:
                if show_contacts_length() < 1:
                    time.sleep(1)
                    print("Contacts length is empty...")
                else:
                    delete_con = int(input("Enter index: "))
                    status = deleting_contact(delete_con)
                    time.sleep(1)
                    if status == 0:
                        print("Index not found...\n")
                    else:
                        print(f"{delete_con} index removed!\n")

                print()

            if choice == 3:
                modify_ind = int(input("Enter index: "))
                status = modifying_contact(modify_ind, conn)
                time.sleep(1)
                if status == 0:
                    print("Index not found...\n")
                else:
                    print(f"{modify_ind} index modified!\n")

                print()

            if choice == 4:
                show_contacts()

                print()


            if choice == 5:
                print()
                time.sleep(1)
                break
            
            time.sleep(1) 

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    menu()        
