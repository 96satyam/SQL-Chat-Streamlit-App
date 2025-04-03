import sqlite3

# Conect to sqlite

connection = sqlite3.connect("student.db")

# Cursor object to insert record, create table

cursor = connection.cursor()

# Create the table
 

table_info = """
CREATE TABLE students(
name VARCHAR(50),
class VARCHAR(20),
section VARCHAR(20),
marks INT
)
"""

cursor.execute(table_info)

## Insert some records
cursor.execute('''INSERT INTO students VALUES("Satyam","Data Science",'B', 85)''')
cursor.execute('''INSERT INTO students VALUES("Shivam","Data Science",'A', 80)''')
cursor.execute('''INSERT INTO students VALUES("Vinayak","Machine Learning",'B', 95)''')
cursor.execute('''INSERT INTO students VALUES("Himanshu","Machine Learning",'A', 75)''')
cursor.execute('''INSERT INTO students VALUES("Ichha","IOT",'B', 90)''')

# Display all records
print("Inserted records are")
data = cursor.execute('''SELECT * FROM students''')
for row in data:
    print(row)

# Comit changes in the database
connection.commit()
connection.close()