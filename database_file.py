import sqlite3

try:
    conn = sqlite3.connect('db.sqlite3')
    print("Opened database successfully")
except Exception as e:
    print("Error during connection: ", str(e))

# variable to store data
number = 'MNO123'

# sql query to update the slot
sql = "UPDATE vehicleStatus set veh_number=?, status = 1 where slot='Slot 4'"
cur = conn.cursor()
cur.execute(sql, (number,))
conn.commit()

# sql query to show all info of 'vehicleStatus' table
cursor1 = conn.execute("SELECT * from vehicleStatus")

for row in cursor1:
   print ("ID = ", row[0])
   print ("SLOT = ", row[1])
   print ("VEH_NUMBER = ", row[2])
   print ("STATUS = ", row[3], "\n")

# closing the connection with the database
conn.close()