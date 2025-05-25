import csv
import sqlite3
def connect_with_db():
    with sqlite3.connect('library_lesson21.db')as conn:
        cursor = conn.cursor()

        res = cursor.execute('SELECT * FROM students').fetchall()
        print(res)
    with open('library_csv.csv', 'w', encoding='utf-8')as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(res)
        conn.close()
connect_with_db()
