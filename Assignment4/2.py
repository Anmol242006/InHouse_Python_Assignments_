import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students(
    id INTEGER,
    name TEXT,
    course TEXT
)
""")

cursor.execute("INSERT INTO students VALUES(1, 'Anmol', 'Python')")
cursor.execute("INSERT INTO students VALUES(2, 'Rahul', 'Java')")
cursor.execute("INSERT INTO students VALUES(3, 'Sneha', 'C++')")

conn.commit()

print("All Students:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("""
UPDATE students
SET course='Data Science'
WHERE name='Anmol'
""")

conn.commit()

print("\nAfter Update:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("""
DELETE FROM students
WHERE name='Sneha'
""")

conn.commit()

print("\nAfter Delete:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()