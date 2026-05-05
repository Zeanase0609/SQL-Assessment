#docstring- Sean Zheng- Spedrunner Database Application
#Imports
import sqlite3

#Constants and Variables
DATABASE = "speedrunner.db"
country_data = ["USA", "AUS", "CAN", "UKR", "RUS", "BEL", "DEU", "ESP", "FIN", "DEU"]

#Functions
def print_all_speedrunners():
    '''print all the speedrunners nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            num_speedrunners = int(input("How many speedrunners?\n"))
            if num_speedrunners > 0:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    sql = f"SELECT * FROM speedrunner LIMIT {num_speedrunners}"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print("Username                      Country   Rank  Elo    Tier         Season Personal Best  All Time Best")
    for speedrunner in results:
        print(f"{speedrunner[2]:<30}{speedrunner[3]:<10}{speedrunner[4]:<6}{speedrunner[5]:<7}{speedrunner[6]:<13}{speedrunner[7]:<22}{speedrunner[8]:<9}")
    #loop finished here
    db.close()


def speedrunner_all_time_pb():
    '''print all the speedrunners by their all time bests'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            minutes = int(input("How many minutes?\n"))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        try:
            seconds = input("How many seconds?\n")
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        comparitive = input("Greater or less than?\n")
        if comparitive == "Greater than":
            symbol = ">"
            break
        elif comparitive == "Lesser than":
            symbol = "<"
            break
        else:
            print("Invalid answer")
    while True:
        try:
            num_speedrunners = int(input("How many speedrunners?\n"))
            if num_speedrunners > 0:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    sql = f"SELECT * FROM speedrunner WHERE all_time_pb {symbol} '{minutes}:{seconds}' ORDER BY all_time_pb ASC LIMit {num_speedrunners};"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print("Username                      Country   Rank  Elo    Tier         Season Personal Best  All Time Best")
    for speedrunner in results:
        print(f"{speedrunner[2]:<30}{speedrunner[3]:<10}{speedrunner[4]:<6}{speedrunner[5]:<7}{speedrunner[6]:<13}{speedrunner[7]:<22}{speedrunner[8]:<9}")
    #loop finished here
    db.close()


def speedrunner_season_pb():
    '''print all the speedrunners by their season bests'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            minutes = int(input("How many minutes?\n"))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        try:
            seconds = input("How many seconds?\n")
            break
        except ValueError:
            print("Invalid input. Please try again.")
    while True:
        comparitive = input("Greater or less than?\n")
        if comparitive == "Greater than":
            symbol = ">"
            break
        elif comparitive == "Lesser than":
            symbol = "<"
            break
        else:
            print("Invalid answer")
    while True:
        try:
            num_speedrunners = int(input("How many speedrunners?\n"))
            if num_speedrunners > 0:
                break
        except ValueError:
            print("Invalid input. Please try again.")            
    sql = f"SELECT * FROM speedrunner WHERE season_pb {symbol} '{minutes}:{seconds}' ORDER BY season_pb ASC LIMIT {num_speedrunners};"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print("Username                      Country   Rank  Elo    Tier         Season Personal Best  All Time Best")
    for speedrunner in results:
        print(f"{speedrunner[2]:<30}{speedrunner[3]:<10}{speedrunner[4]:<6}{speedrunner[5]:<7}{speedrunner[6]:<13}{speedrunner[7]:<22}{speedrunner[8]:<9}")
    #loop finished here
    db.close()


def speedrunner_country():
    '''print all the speedrunners by their country'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        country = input("Which country? ")
        if country in country_data:
            break
        elif country == "All":
            country = "USA', 'AUS', 'CAN', 'UKR', 'RUS', 'BEL', 'DEU', 'ESP', 'FIN', 'DEU"
            break
        elif country not in country_data:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f"SELECT country FROM speedrunner WHERE country IN ('{country}');"
            cursor.execute(sql)
            results = cursor.fetchall()
            missing_country = [result[0] for result in results]
            if len(results) > 0:
                print("You've added a new country intp the system")
                country_data.append(missing_country[0])
                break
            else:
                print("That isn't a country in the system")
    while True:
        try:
            num_speedrunners = int(input("How many speedrunners?\n"))
            if num_speedrunners > 0:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    sql = f"SELECT * FROM speedrunner WHERE country IN ('{country}') ORDER BY country LIMIT {num_speedrunners};"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print("Username                      Country   Rank  Elo    Tier         Season Personal Best  All Time Best")
    for speedrunner in results:
        print(f"{speedrunner[2]:<30}{speedrunner[3]:<10}{speedrunner[4]:<6}{speedrunner[5]:<7}{speedrunner[6]:<13}{speedrunner[7]:<22}{speedrunner[8]:<9}")
    #loop finished here
    db.close()


def speedrunner_tier():
    '''Print all the speedrunners by their tier'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            num_speedrunners = int(input("How many speedrunners?\n"))
            if num_speedrunners > 0:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    tier = input("Which tier?\n Netherite\n Diamond\n Gold\n Iron\n Coal\n")
    if tier == "All":
        sql = f"SELECT * FROM speedrunner ORDER BY ranking_tier LIMIT {num_speedrunners};"
    else:
        sql = f"SELECT * FROM speedrunner WHERE ranking_tier = '{tier}' ORDER BY username LIMIT {num_speedrunners};"
    
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results 
    print("Username                      Country   Rank  Elo    Tier         Season Personal Best  All Time Best")
    for speedrunner in results:
        print(f"{speedrunner[2]:<30}{speedrunner[3]:<10}{speedrunner[4]:<6}{speedrunner[5]:<7}{speedrunner[6]:<13}{speedrunner[7]:<22}{speedrunner[8]:<9}")
    #loop finished here
    db.close()


#Main Code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all speedrunners\n2. Print speedrunners by all-time PB\n3. Print speedrunners by season PB\n4. Print speedrunners by their country\n5. Print speedrunners by their tier\n6. Exit\n")
    if user_input == "1":
        print_all_speedrunners()
    elif user_input == "2":
        speedrunner_all_time_pb()
    elif user_input == "3":
        speedrunner_season_pb()
    elif user_input == "4":
        speedrunner_country()
    elif user_input == "5":
        speedrunner_tier()
    elif user_input == "6":
        print("\nGoodbye!")
        break
    else:
        print("\nThat was not an option\n")