
import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.db =connector.connect(host="localhost", user="root", password="L@xman17490" , database="student")


        query = 'create table if not exists  STUDENT(Student_No int(3),Student_Name varchar(30), Student_DOB date , Student_DOJ date)'

        cur=self.db.cursor()
        cur.execute(query)
        print("created")

    
    #insert

    def insert(self, Student_No , Student_Name, Student_DOB , Student_DOJ):
        query="insert into STUDENT(Student_No , Student_Name , Student_DOB , Student_DOJ)  values('{}' , '{}' , '{}')".format(Student_No,Student_Name,Student_DOB,Student_DOJ)
        print(query)
        cur=self.db.cursor()
        self.db.commit()
        print("STUDENT saved to db")
    

    # fetch all

    def fetch_all(self):
        query="select * from student"
        cur=self.db.cursor()
        cur.execute(query)
        for row in cur:
            print("Student_No:",row[0])
            print("Student_Name:",row[1])
            print("Student_DOB:",row[2])
            print("Student_DOJ:",row[3])

            print()
            print()

    # delete

    def delete(self,Student_NO):
        query="delete from student where Student_no={}".format(Student_NO)
        print(query)
        cur=self.db.cursor()
        self.db.commit()
        cur.execute(query)
        print("deleted")

    # update

    def update(self, Student_No,newStudent_Name , newStudent_DOB , newStudent_DOJ):
        query="update student set Student_name='{}', Student_DOB='{}' , Student_DOJ='{}' where Student_No={}".format(newStudent_Name , newStudent_DOB, newStudent_DOJ,Student_No)
        print(query)
        cur=self.db.cursor()
        cur.execute(query)
        self.db.commit()

        print("update")





helper =DBHelper()
#helper.insert(1,"sima",'1995-09-22','2021-08-11')
#helper.insert(2,"abcd",'1990-11-11','2021-1-30')
#helper.insert(3,"pqrs",'2012-02-28','2020-11-19')
#helper.insert(4,"klmn",'1992-01-21','2010-07-25')

helper.delete(2)

helper.fetch_all()

helper.update(1 , "eeee", '1996-02-22', '2020-02-20')
    

    