import random
import time
import sqlite3

# max nubmer
n = 10

# users list
user1_list = []
user2_list = []


def inserting_into_tambola_table(user1, user2):
    # database connection
    try:
        conn = sqlite3.connect("./Tambola/tambola.sqlite")
        cursor = conn.cursor()
        records = [(user1,), (user2,)]
        sql2 = "Insert into tambola_users(user) values (?);"
        cursor.executemany(sql2, records)
        conn.commit()
        cursor.close()
       
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table...", error)
    finally:
        if conn:
            conn.close()


def inserting_into_winner_table(user, stamp):
    # database connection
    try:
        conn = sqlite3.connect("./Tambola/tambola.sqlite")
        cursor = conn.cursor()
        record = (stamp, user)
        sql = "Insert into winner(time_taken, username) values (?, ?);"
        cursor.execute(sql, record)
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table...", error)
    finally:
        if conn:
            conn.close()

# generating 5 random numbers for 2 users
def generating_random():

    for i in range(5):
        user1_random = random.randint(1, n)
        user2_random = random.randint(1, n)
        
        # storing random values in user lists
        user1_list.append(user1_random)
        user2_list.append(user2_random)


def logic(p_boss):
   
    if p_boss in user1_list:
        time.sleep(1)
        user1_list.remove(p_boss)
        print(f"user1 list:  {user1_list} removed number: {p_boss}")

    if p_boss in user2_list:
        time.sleep(1)
        user2_list.remove(p_boss)
        print(f"user2 list:  {user2_list} removed number: {p_boss}")


def play_game():

    greet = "Welcome to game"
    print(greet)

    # usernames
    user1 = input("Enter full name for user1: ")
    user2 = input("Enter full name for user2: ")

    inserting_into_tambola_table(user1, user2)

    # generating user lists with random numbers
    generating_random()

    # newly randomly generated lists
    print(f"Originally generated lists --> user1 list: {user1_list}   user2 list: {user2_list}")

    t1 = time.perf_counter()

    while True:

        try:
            # database connection
            

            # boss = int(input(f"Enter between 1 and {n}: "))
            boss = random.randint(1, n)
            # print(boss)
            time.sleep(1)
            if boss in user1_list or boss in user2_list:  
                print("Boss shown value: ", boss)
                logic(boss)

                if len(user1_list) < 1 and len(user2_list) < 1:
                    print('Match tied... hard luck')
                    break

                if len(user1_list) < 1:
                    print(f'{user1} wins')
                    t2 = round((time.perf_counter() - t1), 2)

                    # storing record in winner table
                    inserting_into_winner_table(user1, t2)
                    break
                    
                if len(user2_list) < 1:
                    print(f"{user2} wins")
                    t2 = round((time.perf_counter() - t1), 2)

                    # storing record in winner table
                    inserting_into_winner_table(user2, t2)
                    break

            else:    
                print(f'Boss showing again : {boss}')

        except ValueError as e:
            print(e)    


# below if block prevents code from running if this file is imported in another file
if __name__ == "__main__":
    play_game()