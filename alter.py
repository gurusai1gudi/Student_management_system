import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE enrollments ADD COLUMN fee_paid INTEGER DEFAULT 0")

conn.commit()
conn.close()

print("fee_paid column added")




