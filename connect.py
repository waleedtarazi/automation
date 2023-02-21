import mysql.connector as connect
import pandas as pd 

try:

    db_connection = connect.connect(host = 'localhost',
                                 database = 'laravel',
                                 user = 'root',
                                 password = '',
                                 )
    db_cursor = db_connection.cursor()


except Exception as e:
    print(' connection couldnt be establesched code :', e)

print("Creating table Person ->")
db_cursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")


print("Add a recoreds to DB ->")
db_cursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ('Waleed',23))
db_cursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ('Wassim',27))
db_connection.commit()


db_cursor.execute("SELECT * FROM Person")
table = db_cursor.fetchall()

for x in table:
    print(x)


db_cursor.close()
db_connection.close()

data = pd.DataFrame(table)
data.to_csv('C:/Users/walee/Desktop/person.csv',index=False)


