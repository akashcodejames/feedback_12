import mysql.connector as connector

mydb = connector.connect(
  host="localhost",
  user="root",
  password="jamesbond"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE newdb")
print("done").
# creating tables in database (MYSQL) -> feedCredential and loginpassword
con = connector.connect(host='localhost', port='3306', user='root',
                         password='jamesbond', database='newdb')
query = 'create table if not exists feedCredential(UserId varchar(50),UserName varchar(50) ,RollNo varchar(100) primary key,' \
         'email varchar(50),Course varchar(50),Rating varchar(2),FeedBACK varchar(300)) '
cur = con.cursor()
cur.execute(query)
con.commit()
print("Hello")
query = 'create table if not exists loginpassword(UserID varchar(50) primary key,Password varchar(100))'
cur = con.cursor()
cur.execute(query)
con.commit()
print("Done")

