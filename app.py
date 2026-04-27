import sqlite3

db = sqlite3.connect("speedrunner.db")
cursor = db.cursor()
sql = "SELECT * FROM speedrunner"
cursor.execute(sql)
results = cursor.fetchall()
print(results)

db.close
