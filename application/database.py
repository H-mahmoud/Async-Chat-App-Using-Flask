from flask import current_app
from flask_mysqldb import MySQL

class Database:
    
    conn = None

    @classmethod
    def establish_connection(cls):
        try:
            cls.conn = MySQL(current_app)
        except:
            print("Faild to connect Database")
            return False
        
        return True

    @staticmethod
    def add_user(name, ip):
        try:
            cur = Database.conn.connection.cursor()
            cur.execute(f"INSERT into users(name, ip) values ('{name}', '{ip}')")
            cur.close()
            Database.conn.connection.commit()
        
        except Exception as e:
            return e.args
        
        return True

    @staticmethod
    def delete_user(name, ip):
        try:
            cur = Database.conn.connection.cursor()
            cur.execute(f"DELETE from users where name = '{name}' and ip = '{ip}'")
            cur.close()
            Database.conn.connection.commit()

        except Exception as e:
            return e.args
        
        return True