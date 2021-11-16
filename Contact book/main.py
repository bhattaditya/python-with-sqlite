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
    while True:
        try:
            index = int(input("Please enter this number carefully asa it can not be changed later: "))
            if index in contact_list:
                print("Index already exists")
                continue
            else:
                break
        except ValueError as e:
            print(e)   
            print("enter again") 
    return index

def adding_contact():

    index = index_generator()
    name = input("Enter Name: ")
    phone = phone_number()   
    email = email_address()
    city_name = input("City: ")
    contact_list[index] = [name, phone, email, city_name]
    
    return contact_list[index], index



def deleting_contact(contact, conn):
    if contact not in contact_list:
        return 0
    else:
        del contact_list[contact]   
        sql1 = "delete from contacts where index_value = ?"
        conn.execute(sql1, (contact,))
        conn.commit()



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
                            contact_list[index][2] = email   
                            break  
                    except ValueError as e:
                        print("please type 'e' or 'n'")


def show_contacts(conn):
    sql1 = "Select * from contacts "
    for index_v, name, phone, email, city_name in conn.execute(sql1):
        print(f"index: {index_v} Name: {name} Phone: {phone} Email: {email} City: {city_name}")
    # for index, details in contact_list.items():
    #     name, phone, email, city_name = details
    #     print(f"Index: {index} Name: {name} Email: {email} Phone: {phone} City: {city_name}")
    # print()
            

while True:
    try:
        choice = int(input("1. Adding contact\n2. Deleting contact\n3. Modiying contact\n4. Show contact list\n5. Exit\n"))
        conn = sqlite3.connect("contacts.sqlite")

        if choice == 1:
            # conn = sqlite3.connect("contacts.sqlite")
            # contact_list[index] = [name, phone, email, city_name]
            sql1 = "CREATE TABLE IF NOT EXISTS contacts (index_value integer, name text, phone integer, email text, city_name text)"
            conn.execute(sql1)

            record, index_value = adding_contact()

            name = record[0]
            phone = record[1]
            email = record[2]
            city_name = record[3]
            

            sql2 = "Insert into contacts values (?,?,?,?,?)"
            conn.execute(sql2,(index_value, name, phone, email, city_name))
            conn.commit()

            time.sleep(1)
            print("Contact added successfully!\n")
            
        if  choice == 2:
            
            delete_con = int(input("Enter index: "))
            # conn = sqlite3.connect("contacts.sqlite")
            status = deleting_contact(delete_con, conn)
            time.sleep(1)

            if status == 0:
                print("Index not found...\n")
            else:
                print(f"{delete_con} index removed!\n")

        if choice == 3:
            modify_ind = int(input("Enter index: "))
            status = modifying_contact(modify_ind, conn)

            time.sleep(1)
            if status == 0:
                print("Name not found...\n")
            else:
                print(f"{modify_ind} index modified!\n")

        if choice == 4:

            if len(contact_list) < 1:
                print("\ncontact list empty\n") 
            else:
                # conn = sqlite3.connect("contacts.sqlite")
                print("Listing contacts:-")
                time.sleep(1)
                show_contacts(conn)

        if choice == 5:
            time.sleep(1)
            break
        
        time.sleep(1)
    except ValueError as e:
        print(e)
    

