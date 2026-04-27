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

#Main Code
print_all_speedrunners()
