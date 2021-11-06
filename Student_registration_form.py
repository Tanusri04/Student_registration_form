from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('1300x900+0+0')
root.title("Registration Form")

#Specifying the variable names and the type of inputs we require for each of the fields 
StudentName = StringVar()
CollegeName = StringVar()
Specialisation = StringVar()
DegreeName = StringVar()
Internships = StringVar()
PhoneNumber = StringVar()
EmailID = StringVar()
Location = StringVar()
Gender = StringVar()
Notes = StringVar()
UserName = StringVar()
UserPass = StringVar()
UserStatus = StringVar()

#Taking all the information from the users for the given entries
def Database():
    name = StudentName.get()
    college = CollegeName.get()
    specialise_in = Specialisation.get()
    degree = DegreeName.get()
    Intern = Internships.get()
    phone = PhoneNumber.get()
    email = EmailID.get()
    location = Location.get()
    gender = Gender.get()
    notes = Notes.get()
    username = UserName.get()
    password = UserPass.get()
    status = UserStatus.get()
    conn = sqlite3.connect('Registered.db')
    with conn:
      cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student ( StudentName TEXT, CollegeName TEXT, Specialisation TEXT, DegreeName TEXT, Internships TEXT, PhoneNumber, EmailID, Location TEXT, Gender TEXT, Notes TEXT)')
    cursor.execute('INSERT INTO Student( StudentName, CollegeName, Specialisation, DegreeName, Internships, PhoneNumber, EmailID, Location, Gender, Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', (name, college, specialise_in, degree, Intern, phone, email, location, gender, notes,))
    cursor.execute('CREATE TABLE IF NOT EXISTS User (UserName TEXT, UserPass, UserStatus TEXT)')
    cursor.execute('INSERT INTO User( UserName, UserPass, UserStatus)VALUES (?, ?, ?)', (username, password, status,))
    conn.commit()

#heading of the form
heading = Label(root, text = "STUDENT REGISTRATION FORM", font= ("Times New Roman", 20))
heading.config(anchor = CENTER)
heading.pack()

#first entry
title_1 = Label(root, text = "Student Name", font = ("Times New Roman", 15))
title_1.pack(pady = 10, anchor = "w")
title_1 = Entry(root, textvar = StudentName)
title_1.place(x = 200, y = 50)

#second entry
title_2 = Label(root, text = "College Name", font = ("Times New Roman", 15))
title_2.pack(pady = 10, anchor = "w")
title_2 = Entry(root, textvar = CollegeName)
title_2.place(x = 200, y = 100)

#third entry
title_3 = Label(root, text = "Specialisation", font = ("Times New Roman", 15))
title_3.pack(pady = 10, anchor = "w")
title_3 = Entry(root, textvar = Specialisation)
title_3.place(x = 200, y = 148)

#fourth entry
title_4 = Label(root, text = "Degree Name", font = ("Times New Roman", 15))
title_4.pack(pady = 10, anchor = "w")
title_4 = Entry(root, textvar = DegreeName)
title_4.place(x = 200, y = 197)

#fifth entry
title_5 = Label(root, text = "Internships", font = ("Times New Roman", 15))
title_5.pack(pady = 10, anchor = "w")
title_5 = Entry(root, textvar = Internships)
title_5.place(x = 200, y = 243)

#sixth entry
title_6 = Label(root, text="Phone number", font= ("Times New Roman", 15))
title_6.pack(pady = 10, anchor = "w")
title_6 = Entry(root, textvar = PhoneNumber)
title_6.place(x = 200, y = 293)

#seventh entry
title_7 = Label(root, text = "Email ID", font= ("Times New Roman", 15))
title_7.pack(pady = 10, anchor = "w")
title_7 = Entry(root, textvar = EmailID)
title_7.place(x = 200, y = 340)

#eighth entry
title_8 = Label(root, text = "Location", font= ("Times New Roman", 15))
title_8.pack(pady = 10, anchor = "w")
title_8 = Entry(root, textvar = Location)
title_8.place(x = 200, y = 385)

#ninth entry
title_9 = Label(root, text = "Gender", font= ("Times New Roman", 15))
title_9.pack(pady = 10, anchor = "w")
title_9 = Entry(root, textvar = Gender)
title_9.place(x = 200, y = 435)

#tenth entry
title_10 = Label(root, text= "Notes", font=("Times New Roman", 15))
title_10.pack(pady = 10, anchor = "w")
title_10 = Entry(root, textvar = Notes)
title_10.place(x = 200, y = 483)

#eleventh entry
title_11 = Label(root, text= "User Name", font=("Times New Roman", 15))
title_11.pack(pady = 10, anchor = "w")
title_11 = Entry(root, textvar = UserName)
title_11.place(x = 200, y = 532)

#twelth entry
title_12 = Label(root, text= "User Password", font=("Times New Roman", 15))
title_12.pack(pady = 10, anchor = "w")
title_12 = Entry(root, textvar = UserPass)
title_12.place(x = 200, y = 580)

#thirteenth entry
title_13 = Label(root, text= "User Status", font=("Times New Roman", 15))
title_13.pack(pady = 10, anchor = "w")
title_13 = Entry(root, textvar = UserStatus)
title_13.place(x = 200, y = 628)

def msg1():
   messagebox.showinfo("Congratulations", "Sucessful Registration!")


#function to display all details from Table 'Student' in the database 'Registered'
def Display_Student():
      conn = sqlite3.connect("Registered.db")
      cursor = conn.cursor()
      s = "select * from Student"
      cursor.execute(s)
      records = cursor.fetchall()
      print("\nPrinting each row from Table Student \n")
      for row in records:
         print("Name = ", row[0])
         print("College = ", row[1])
         print("Specialisation  = ", row[2])
         print("Degree  = ", row[3])
         print("Internships  = ", row[4])
         print("Phone Number  = ", row[5])
         print("EmailID  = ", row[6])
         print("Location  = ", row[7])
         print("Gender  = ", row[8])
         print("Notes  = ", row[9])   
         print("\n")

#function to display all details from Table 'User' in the database 'Registered'
def Display_User():
   conn = sqlite3.connect("Registered.db")
   cursor = conn.cursor()
   r = "select * from User"
   cursor.execute(r)
   Records = cursor.fetchall()
   print("\nPrinting each row from Table User \n")
   for Row in Records:
      print("User Name = ", Row[0])
      print("Password = ", Row[1])
      print("Status = ", Row[2])
      print("\n")

#Submit button
button = Button(root, text="Submit", font = ("Times New Roman", 18), bg = "green", fg = "white", command=lambda:[Database(), msg1()]).place(x = 600, y = 700)

a = input("Do you want to display the entries from Table Student?(Y/N)")
if a == 'Y':
   Display_Student()
else:
   pass
b = input("Do you want to display the entries from Table User?(Y/N)")
if b == 'Y':
   Display_User()
else:
   pass

root.mainloop()