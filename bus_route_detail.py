from tkinter import *
from tkinter .messagebox import *
import sqlite3
with sqlite3.connect("Mydb.db") as mydb:
    curr=mydb.cursor()
curr.execute("create table IF NOT EXISTS routedetails (routeid varchar(50), station varchar(10), stationid varchar(50))");

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=20)
Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=20)
Label(root,text="Add Bus Route Details",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=20,columnspan=20)
def fun2():
    sname1=sname.get()
    rtid1=rtid.get()
    sid1=sid.get()
    curr.execute ("select count (*) from routedetails where routeid= '" + rtid1 + "' ") 
    res=curr.fetchone()
     
    if int(res[0]) > 0:
        showerror('Error','Data already entered')
    
    else:
        showinfo('Inserted','Data successfully entered')
        curr.execute("INSERT INTO routedetails(routeid,station,stationid) values(?,?,?)",(rtid1,sname1,sid1))
        mydb.commit()
Label(root,text="Route Id").grid(row=3,column=6)
rtid=Entry(root)
rtid.grid(row=3,column=7)
Label(root,text="Station Name").grid(row=3,column=8)
sname=Entry(root)
sname.grid(row=3,column=9)
Label(root,text="Station Id").grid(row=3,column=10)
sid=Entry(root)
sid.grid(row=3,column=11)
Button(root,text="Add Route",command=fun2,bg="green3").grid(row=3,column=16)
Button(root,text="Delete Route",bg="green3",fg="red").grid(row=3,column=17,pady=30)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1).grid(row=4,column=14)

root.mainloop(

)