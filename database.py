import sqlite3

conn = sqlite3.connect('enkripsi.db')
c = conn.cursor()

# Table Akun
c.execute("""CREATE TABLE IF NOT EXISTS akun(
                    Email VARCHAR(255) PRIMARY KEY,
                    Nama_lengkap VARCHAR(255) NOT NULL,
                    Password VARCHAR(255) NOT NULL);
          """)
conn.commit()

# Table Key
c.execute("""CREATE TABLE IF NOT EXISTS key(
                    Email VARCHAR(255) PRIMARY KEY,
                    Key VARCHAR(255) NOT NULL);
          """)
conn.commit()

# Table Sender
c.execute("""CREATE TABLE IF NOT EXISTS sender(
                    Id_sender INTEGER PRIMARY KEY,
                    From_Subject VARCHAR(255) NOT NULL,
                    To_Subject VARCHAR(255) NOT NULL,
                    Text VARCHAR(255) NOT NULL,
                    Time DATETIME NOT NULL,
                    Type VARCHAR(255) NOT NULL);
          """)
conn.commit()