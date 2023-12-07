from config import *
from parse import *
import mysql.connector
import subprocess

class Tabler:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=HOST,
            user=USERNAME,
            passwd=PASSWORD
            )

        self.cur = self.db.cursor()
        
        self.cur.execute("USE " + DATABASE_NAME)
        
        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS {} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    query VARCHAR(50),
                    IPv4 VARCHAR(500),
                    IPv6 VARCHAR(500))
                    """.format(TABLE_NAME))


    def get_table(self):
        self.cur.execute("SELECT * FROM " + TABLE_NAME)
        return self.cur.fetchall()


    def add_entry(self, query):
        if query in [elem[1] for elem in self.get_table()]: return
        print([elem[1] for elem in self.get_table()])
        ipv4s, ipv6s = parse(query)

        insert_query = "INSERT INTO {} (query, IPv4, IPv6) VALUES (%s, %s, %s)".format(TABLE_NAME, ipv4s, ipv6s)
        item_data = (query,
                     ", ".join(ipv4s),
                     ", ".join(ipv6s)
                    )

        self.cur.execute(insert_query, item_data)
        self.db.commit()
        
        return
    
    
    def remove_entry(self, query):
        self.cur.execute("DELETE FROM {} WHERE id = %s".format(TABLE_NAME), 
                         (query,))
        self.db.commit()
        return
    