from tkinter import *
from tkinter .messagebox import *
import sqlite3
with sqlite3.connect("Mydb.db") as mydb:
    curr=mydb.cursor()
curr.execute("create table IF NOT EXISTS OP (opid varchar(50), name varchar(10), address varchar(50), phone varchar(10), email varchar(50))");
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=20)


Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=20)
Label(root,text="Add Bus Operator Details",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=20,columnspan=20)

def fun():
    OPI1 = OPI.get()
    name1 = name.get()
    add1 = add.get()
    phone1 = phone.get()
    mail1=mail.get()
    curr.execute ("select count (*) from OP where opid= '" + OPI1 + "' ") 
    res=curr.fetchone()
    if int(res[0]) > 0:
        showerror('Error','Data already entered')
    
    else:
        showinfo('Inserted','Data successfully entered')
        curr.execute("INSERT INTO OP(opid,name,address,phone,email) values(?,?,?,?,?)",(OPI1,name1,add1,phone1,mail1))
        mydb.commit()




Label(root,text="Operator Id").grid(row=3,column=6)
OPI = Entry(root)
OPI.grid(row=3,column=7)
Label(root,text="Name").grid(row=3,column=8)
name = Entry(root)
name.grid(row=3,column=9)
Label(root,text="Address").grid(row=3,column=10)
add = Entry(root)
add.grid(row=3,column=11)
Label(root,text="Phone").grid(row=3,column=12)
phone = Entry(root)
phone.grid(row=3,column=13)
Label(root,text="Email").grid(row=3,column=14,pady=50)
mail = Entry(root)
mail.grid(row=3,column=15)
Button(root,text="Add", command=fun,bg="green3").grid(row=3,column=16)
Button(root,text="Edit",bg="green3").grid(row=3,column=17)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1).grid(row=4,column=14)
root.mainloop()