from tkinter import *
from tkinter .messagebox import *
import sqlite3
with sqlite3.connect("Mydb.db") as mydb:
    curr=mydb.cursor()
curr.execute("create table IF NOT EXISTS busdetails (busid varchar(50), type varchar(10), capacity int(50), fare int(10), operid varchar(50), routid varchar(50))");
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
# global bus_type
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=20)
Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=20)
Label(root,text="Add Bus Details",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=20,columnspan=20)
def fun1():
    bid1=bid.get()
    bus_type1=bus_type.get()
    cap1=cap.get()
    fare1=fare.get()
    operid1=operid.get()
    rid1=rid.get()
    
    curr.execute ("select count (*) from busdetails where busid= '" + bid1 + "' ") 
    res=curr.fetchone()
     
    if int(res[0]) > 0:
        showerror('Error','Data already entered')
    
    else:
        showinfo('Inserted','Data successfully entered')
        curr.execute("INSERT INTO busdetails(busid,type,capacity,fare,operid,routid) values(?,?,?,?,?,?)",(bid1,bus_type1,cap1,fare1,operid1,rid1))
        mydb.commit()




Label(root,text="Bus Id").grid(row=3,column=6)
bid=Entry(root)
bid.grid(row=3,column=7)
Label(root,text="Bus Type").grid(row=3,column=8)
# def bus_choice():
bus_type=StringVar()
option=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non-AC Sleeper 2X1"]
d_menu=OptionMenu(root,bus_type,*option)
d_menu.grid(row=3,column=9)
# Label(root,text="Bus Type",bg="RoyalBlue1",)
    
Label(root,text="Capacity").grid(row=3,column=10)
cap=Entry(root)
cap.grid(row=3,column=11)
Label(root,text="Fare Rs").grid(row=3,column=12)
fare=Entry(root)
fare.grid(row=3,column=13)
Label(root,text="operator Id").grid(row=3,column=14,pady=50)
operid=Entry(root)
operid.grid(row=3,column=15)
Label(root,text="Route Id").grid(row=3,column=16)
rid=Entry(root)
rid.grid(row=3,column=17)
Button(root,text="Add Bus",command=fun1,bg="green3",font="Arial 10").grid(row=4,column=12)
Button(root,text="Edit Bus",bg="green3",font="Arial 10").grid(row=4,column=13)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1).grid(row=4,column=14)
root.mainloop()
