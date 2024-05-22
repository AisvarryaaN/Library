import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
bid=""
if bid!="":
    d="update books set status='issued' where bid='%d'"%(bid)
    mycursor = mydb.cursor()
    mycursor.execute(d)
    mydb.commit()
    print("success")
else:
    print("fail")










