from tkinter import *
from tkinter .messagebox import *
import sqlite3
with sqlite3.connect("Mydb.db") as mydb:
    curr=mydb.cursor()
curr.execute("create table IF NOT EXISTS rundetails (bus_id varchar(50), running varchar(10), seat_aval varchar(50))")

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=20)
Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=20)
Label(root,text="Add Bus Running Details",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=20,columnspan=20)
Label(root,text="Bus Id").grid(row=3,column=6)
a=Entry(root)
a.grid(row=3,column=7)
Label(root,text="Running Date").grid(row=3,column=8)
b=Entry(root)
b.grid(row=3,column=9)
Label(root,text="Seat Available").grid(row=3,column=10)
c=Entry(root)
c.grid(row=3,column=11 )
def fun4():
    first=a.get()
    second=b.get()
    third=c.get()
    curr.execute ("select count (*) from rundetails where bus_id= '" + first + "' ") 
    res=curr.fetchone()
     
    if int(res[0]) > 0:
        showerror('Error','Data already entered')
    
    else:
        showinfo('Inserted','Data successfully entered')
        curr.execute("INSERT INTO rundetails(bus_id,running,seat_aval) values(?,?,?)",(first,second,third))
        mydb.commit()

#column=[(bus_id,running_date,seat_available)]
#values=[(first,second,third)]
Button(root,text="Add Run",bg="green3",command=fun4).grid(row=3,column=12)
Button(root,text="Delete Run",bg="green3").grid(row=3,column=13,pady=30)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1).grid(row=4,column=12)
root.mainloop()

