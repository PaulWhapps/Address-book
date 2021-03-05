import sqlite3

# Connects to database
con = sqlite3.connect('contact.db')

cursor = con.cursor()

cursor.execute("""CREATE TABLE contacts (
        first_name text,
        last_name text,
        phone_number integer,
        email text
    )""")



con.commit()
print('Data added successfully!')

con.close()
