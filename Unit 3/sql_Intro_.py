# 1. bring in the sql lite module to get access to all the sql methods (functions) to work with our database.
import sqlite3

# 2. We need to establish an actual database file using the connect method.
connect = sqlite3.connect('myDb.db')

# 3. Create a object that will be sent to the new database.
cursor = connect.cursor()

# 4. We need to create a schema (structure) for our data.
# cursor.execute('''
#                CREATE TABLE gameSales(
#                id INTEGER PRIMARY KEY,
#                name TEXT,
#                platform TEXT, 
#                developer TEXT,
#                price INTEGER,
#                genre TEXT,
#                totalSales INTEGER
#                )
#                ''')
# 5. we can now create our first database object.
cursor.execute('''
               DELETE FROM gameSales

                WHERE id = 1
                ''')

# 6. once we have a new data object, we need to commit it to the database.
connect.commit()
connect.close()