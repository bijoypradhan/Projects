import os
import sqlite3

SCR_DIR = os.path.dirname(os.path.realpath(__file__))
db_file = os.path.join(SCR_DIR, 'instance/lang_db.db')
con = sqlite3.connect(db_file)
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users (
            [username] PRIMARY_KEY,
            [firstname] VARCHAR(255),
            [lastname] VARCHAR(255),
            [email] VARCHAR(255),
            [password] VARCHAR(255)
        )""")
con.commit()
con.close()