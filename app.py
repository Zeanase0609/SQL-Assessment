#docstring- Sean Zheng- Spedrunner Database Application
#Imports
import sqlite3

#Constants and Variables
DATABASE = "speedrunner.db"


#Functions
def print_all_speedrunners():
    '''print all the speedrunners nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM speedrunner"
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
    sql = "SELECT * FROM speedrunner ORDER BY all_time_pb ASC"
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
    sql = "SELECT * FROM speedrunner ORDER BY season_pb ASC"
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
    sql = "SELECT * FROM speedrunner ORDER BY country;"
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
    sql = "SELECT * FROM speedrunner ORDER BY ranking_tier;"
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
        break
    else:
        print("\nThat was not an option\n")