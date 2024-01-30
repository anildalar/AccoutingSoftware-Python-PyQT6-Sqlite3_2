import sqlite3
import bcrypt

class DatabaseManager:
    def __init__(self, db_name='./data/accounting.db'):# default paramater/argument
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cur.execute('''
                            CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE,
                                password TEXT);
                            CREATE TABLE IF NOT EXISTS customers ( 
                                id   INTEGER PRIMARY KEY,
                                name TEXT NOT NULL COLLATE NOCASE
                            );
                            CREATE TABLE IF NOT EXISTS suppliers ( 
                                id   INTEGER PRIMARY KEY,
                                name TEXT NOT NULL COLLATE NOCASE
                            );
                            CREATE TABLE IF NOT EXISTS items ( 
                                id   INTEGER PRIMARY KEY,
                                name TEXT NOT NULL COLLATE NOCASE
                            );
                        ''')
        self.conn.commit()
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
    def register_user(self, username, password):
        try:
            # Hash the password before inserting into the database
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.cur.execute("INSERT INTO users (username, password,role) VALUES (?, ?, ?)", (username, hashed_password,'admin'))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Unique constraint violated, username already exists
            return False

    def close(self):
        self.conn.close()
