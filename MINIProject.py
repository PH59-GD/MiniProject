import mysql.connector
import time
#http://localhost/phpmyadmin5.2.3/index.php?route=/sql&pos=0&db=college_management_database&table=faculty


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="College_Management_Database"
    )
    cursor = db.cursor()
except:
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE College_Management_Database")
    print("Database created!")
    print("Please Restart the program.")
    exit()


cursor.execute( """
        CREATE TABLE IF NOT EXISTS Student (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(50),
        Major VARCHAR(50),
        Courses VARCHAR(50),
        GPA VARCHAR(50)
        )
""")

cursor.execute( """
        CREATE TABLE IF NOT EXISTS Faculty (
        FacultyID INT PRIMARY KEY,
        Name VARCHAR(50),
        Department VARCHAR(50),
        Teaches_Courses VARCHAR(50)
        
        )
""")
class Student_Master:
    def __init__(self):
        self.StuID = ""
        self.StuName = ""
        self.StuMajor = ""
        self.StuCourses = []
        self.StuGpa = ""
        self.SaveCourses = ""
    def Create_Student(self):
        try:
            self.StuID = int(input("Enter Student ID: "))
            self.StuName = input("Enter Student Name: ")
            self.StuMajor = input("Enter Student's Major: ")
            AC = int(input("How many courses to add to student?: "))
            for i in range(AC):
                self.StuCourses.append(input("Enter Course Name: "))
            for b in range(len(self.StuCourses)):
                self.SaveCourses += self.StuCourses[b] +", "
            self.StuGpa = input("Enter Student's GPA: ")
            sql = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s)"
            values = (self.StuID, self.StuName, self.StuMajor, self.SaveCourses, self.StuGpa)
            cursor.execute(sql, values)
            db.commit()
        except:
            print("Critical Error! You may be attempting to enter a value other than an INT for Student ID, or entered a value other than an INT for the amount of courses to add to the student.")

    def Display_Student(self):
        cursor.execute("SELECT * FROM Student")
        for row in cursor.fetchall():
            print(row)
    def Modify_Student(self):
        try:
            self.StuID = int(input("Enter Student ID: "))
            self.StuName = input("Enter New Student Name: ")
            self.StuMajor = input("Enter New Student's Major: ")
            AC = int(input("How many courses to add to student?: "))
            for i in range(AC):
                self.StuCourses.append(input("Enter Course Name: "))
            for b in range(len(self.StuCourses)):
                self.SaveCourses += self.StuCourses[b] +", "
            self.StuGpa = input("Enter Student's New GPA: ")
            sql = """
            UPDATE Student
            SET Name = %s, 
            Major = %s,
            Courses = %s,
            GPA = %s
            WHERE StudentID = %s
            """
            cursor.execute(sql,(self.StuName, self.StuMajor, self.SaveCourses, self.StuGpa, self.StuID)) 
            db.commit()
            print("Student Updated!")
        except:
            print("Critical Error! You may be attempting to edit a student that doesn't exist, entered a value other than an INT for Student ID, or entered a value other than an INT for the amount of courses to add to the student.")
    def Delete_Student(self):
        try:
            print("Warning! You are deleting a student record permanently. Leave the field blank and press enter to cancel.")
            StuID = int(input("Enter Student ID: "))
            if(StuID == ""):
                pass
            else:
                sql = "DELETE FROM Student WHERE StudentID = %s"
                cursor.execute(sql, (StuID,))
                db.commit()
                print("Student Record Deleted!")
        except:
            print("Critical Error! You may have attempted to delete a student that doesn't exist, or entered a value other than INT for the StudentID.")
    def Download_Student(self):
        cursor.execute("SELECT * FROM Student")
        file1 = open("Student_Table_Download.txt", "w")
        for row in cursor.fetchall():
            file1.writelines(str(row)+"\n")
        file1.close()
        print("Student Table Downloaded!")

class Faculty_Master:
    def __init__(self):
        self.FacID = ""
        self.FacName = ""
        self.FacDepartment = ""
        self.FacTeachesCourses = []
        self.SaveTaughtCourses = ""
    def Create_Faculty(self):
        try:
            self.FacID = int(input("Enter Faculty ID: "))
            self.FacName = input("Enter Faculty Name: ")
            self.FacDepartment = input("Enter Faculty's Department: ")
            AC = int(input("How many courses does this faculty teach?: "))
            for i in range(AC):
                self.FacTeachesCourses.append(input("Enter Course Name: "))
            for b in range(len(self.FacTeachesCourses)):
                self.SaveTaughtCourses += self.FacTeachesCourses[b] +", "
            sql = "INSERT INTO Faculty VALUES (%s, %s, %s, %s)"
            values = (self.FacID, self.FacName, self.FacDepartment, self.SaveTaughtCourses)
            cursor.execute(sql, values)
            db.commit()
        except:
            print("Critical Error! You may be attempting to enter a value other than an INT for Faculty ID, or entered a value other than an INT for the amount of courses this faculty teaches.")
    def Display_Faculty(self):
        cursor.execute("SELECT * FROM Faculty")
        for row in cursor.fetchall():
            print(row)

    def Modify_Faculty(self):
        try:
            self.FacID = int(input("Enter Faculty ID: "))
            self.FacName = input("Enter New Faculty Name: ")
            self.FacDepartment = input("Enter New Faculty's Department: ")
            AC = int(input("How many courses does this faculty teach?: "))
            for i in range(AC):
                self.FacTeachesCourses.append(input("Enter Course Name: "))
            for b in range(len(self.FacTeachesCourses)):
                self.SaveTaughtCourses += self.FacTeachesCourses[b] + ", "
            sql = """
                    UPDATE Faculty
                    SET Name =%s, 
                    Department =%s,
                    Teaches_Courses =%s
                    WHERE FacultyID =%s
                    """
            cursor.execute(sql, (self.FacName, self.FacDepartment, self.SaveTaughtCourses, self.FacID))
        except:
                print("Critical Error! You may be attempting to edit a faculty that doesn't exist, entered a value other than an INT for Faculty ID, or entered a value other than an INT for the amount of courses this faculty teaches.")

    def Delete_Faculty(self):
            try:
                print("Warning! You are deleting a faculty record permanently. Leave the field blank and press enter to cancel.")
                FacID = int(input("Enter Faculty ID: "))
                if(FacID == ""):
                    pass
                else:
                    sql = "DELETE FROM Faculty WHERE FacultyID = %s"
                    cursor.execute(sql, (FacID,))
                    db.commit()
                    print("Faculty Record Deleted!")
            except:
                print("Critical Error! You may have attempted to delete a faculty that doesn't exist, or entered a value other than INT for the FacultyID.")
    def Download_Faculty(self):
            cursor.execute("SELECT * FROM Faculty")
            file2 = open("Faculty_Table_Download.txt", "w")
            for row in cursor.fetchall():
                file2.writelines(str(row)+"\n")
            file2.close()
            print("Faculty Table Downloaded!")




while True:
    print("")
    print("[1] Student")
    print("[2] Faculty")
    print("[3] Exit")
    print("")
    UC = input("Input: ")
    if(UC == "1"):
        while True:
            print("")
            print("[1] Create Student")
            print("[2] Display Student")
            print("[3] Modify Student")
            print("[4] Delete Student")
            print("[5] Download Student Table")
            print("[6] Back")
            print("")
            UC1 = input("Input: ")
            if(UC1 == "1"):
                NewStu = Student_Master()
                NewStu.Create_Student()
            elif(UC1 == "2"):
                DSPLYStu = Student_Master()
                DSPLYStu.Display_Student()
            elif(UC1 == "3"):
                ModStu = Student_Master()
                ModStu.Modify_Student()
            elif(UC1 == "4"):
                DelStu = Student_Master()
                DelStu.Delete_Student()
            elif(UC1 == "5"):
                DowStu = Student_Master() 
                DowStu.Download_Student()
            elif(UC1 == "6"):
                break
    elif(UC == "2"):
        while True:
            print("")
            print("[1] Create Faculty")
            print("[2] Display Faculty")
            print("[3] Modify Faculty")
            print("[4] Delete Faculty")
            print("[5] Download Faculty Table")
            print("[6] Back")
            print("")
            UC2 = input("Input: ")
            if(UC2 == "1"):
                NewFac = Faculty_Master()
                NewFac.Create_Faculty()
            elif(UC2 == "2"):
                DSPLYFac = Faculty_Master()
                DSPLYFac.Display_Faculty()
            elif(UC2 == "3"):
                ModFac = Faculty_Master()
                ModFac.Modify_Faculty()
            elif(UC2 == "4"):
                DelFac = Faculty_Master()
                DelFac.Delete_Faculty()
            elif(UC2 == "5"):
                DowFac = Faculty_Master()
                DowFac.Download_Faculty()
            elif(UC2 == "6"):
                break
    elif(UC == "3"):
        break
        
        
        
        
        
        
        
        
        
