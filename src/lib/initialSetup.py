import sqlite3
import bcrypt

#1. Function defination is one time process
#self.db_manager = DatabaseManager()

#1. DB Connection Open
dbname='accounting.db'
sqlfile='accounting.sql'
connection = sqlite3.connect('./data/'+dbname)
cursor = connection.cursor()
def import_sql():
    
    # Step 1: Open a database connection
                # module.method(aa)
    try:
        # Step 2: Open the SQL file and read its contents
        with open('./data/'+sqlfile, 'r') as sql_file:
            sql_script = sql_file.read()

        # Step 3: Execute the SQL commands in the file
        cursor.executescript(sql_script)
        # Insert some data into the table
        #cursor.execute("DELETE FROM users;")
        # Hash the password before inserting into the database
        #hashed_password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
        # Insert some data into the table with the hashed password
       #object.method("string",(tuple1,tuple2,tuple3))
        #cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",('admin', hashed_password, 'admin'))

        # Commit the changes
        connection.commit()
        print("SQL file imported successfully.")
        

    except Exception as e:
        print("Error importing SQL file:", e)

    finally:    
        pass
    # Step last: Close the database connection
    pass

def checkIfAdminRegister():
    try:
        
        #2 Build the query
        cursor.execute("SELECT COUNT(*) FROM users where role='admin'")
        
        # Execute the query and fetch the result
        result = cursor.fetchone()
        print(result)
        print(result[0])
        # Check if the count is greater than zero
        if result[0] > 0:
            return True
        else:
            return False
        pass
    except Exception as e:
        print('Failed')
        print('Hello',e)
        
        pass
    finally:
        
        pass
