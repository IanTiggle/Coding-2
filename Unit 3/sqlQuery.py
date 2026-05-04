# imports all the methods we will need to send/ receive data from the database
import sqlite3

# just a function
def getAllData():
    # setting up the connection to our database (the road)
    # to/from the database (the vehicle)
    connect = sqlite3.connect('myDb.db')
    cursor = connect.cursor()

    # the data we want to get
    # SELECT = our selection
    query = 'SELECT  platform FROM gameSales'

    # turns the vehicle on to get the data
    cursor.execute(query)

    # tells the cursor to fetch/ get ALL data
    results = cursor.fetchall()

    # shows our results in terminal
    print(results)

#getAllData()

def get1data():
    connect = sqlite3.connect('myDb.db')
    
    cursor = connect.cursor()

    query = "SELECT name FROM gameSales WHERE developer = 'Bethesda'"

    cursor.execute(query)

    result = cursor.fetchone()

    print(result)
#get1data()

def deleteData():
    connect = sqlite3.connect('myDb.db')
    
    cursor = connect.cursor()

    query = "DELETE FROM gameSales WHERE id = 2"

    cursor.execute(query)

    connect.commit()
    connect.close()