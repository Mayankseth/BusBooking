from tkinter import*
from tkinter .messagebox import *
import sqlite3
with sqlite3.connect("Mydb.db") as mydb:
    curr=mydb.cursor()
class bus_booking:
    def first():
        
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=3,padx=700)
        Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Arial 30 bold",fg="red").grid(row=1,column=3,pady=50)
        Label(root,text="Name : MAYANK SETH",font="Arial 20 bold",fg="dark slate blue").grid(row=3,column=3,pady=20)
        Label(root,text="Er : 211B180",font="Arial 20 bold",fg="dark slate blue").grid(row=4,column=3,pady=20)
        Label(root,text="Mobile : 00000000",font="Arial 20 bold",fg="dark slate blue").grid(row=5,column=3,pady=20)
        Label(root,text="Submitted To : Dr Mahesh Kumar",bg="LightSteelBlue3",font="Arial 20 bold",fg="red").grid(row=6,column=3,pady=40)
        Label(root,text="project based learning",font="Arial 15 bold",fg="red").grid(row=7,column=3)
        def des(c=0):
            root.destroy()
            tr.second()

        root.bind('<KeyPress>',des)
        root.mainloop()
    def second():
        root=Tk()

        def des1(e=0):
            root.destroy()
            tr.seatbook()
        def des2(a=0):
             root.destroy()
             tr.checkseat()
        def des3(q=0):
            root.destroy()
            tr.addbus()


        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=700,columnspan=10)
        Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=50,columnspan=10)
        Button(root,text="Seat Booking",command=des1,bg="green3",font="Algerian 15 bold").grid(row=2,column=3)
        Button(root,text="Check Booked Seat",command=des2,bg="green3",font="Algerian 15 bold").grid(row=2,column=4)
        Button(root,text="Add Bus Details",command=des3,bg="green3",font="Algerian 15 bold").grid(row=2,column=5)
        root.mainloop()
        root.mainloop()
    
    def seatbook():
        curr.execute("create table IF NOT EXISTS customer (cname varchar(50), gender varchar(10), NOS varchar(50), phoneno varchar(50), age varchar(50), Bus_id varchar(50) )");

        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=8)
        Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=8)
        Label(root,text="Enter Journey Details",bg="SpringGreen2",fg="green4",font="Arial 15 bold").grid(row=2,column=0,pady=20,columnspan=8)
        Label(root,text="To").grid(row=3,column=0)
        Entry(root).grid(row=3,column=1)
        Label(root,text="From").grid(row=3,column=2)
        Entry(root).grid(row=3,column=3)
        Label(root,text="Journey Date").grid(row=3,column=4)
        Entry(root).grid(row=3,column=5)
        img1=PhotoImage(file='.\\home.png')
        Button(root,image=img1).grid(row=3,column=7)
        def proceed_book():
            Label(root,text="Select Bus",fg="green4",font="Arial 10 bold").grid(row=4,column=0)
            Label(root,text="Operator",fg="green4",font="Arial 10 bold").grid(row=4,column=1)
            Label(root,text="Bus Type",fg="green4",font="Arial 10 bold").grid(row=4,column=2)
            Label(root,text="Available Capacity",fg="green4",font="Arial 10 bold").grid(row=4,column=3)
            Label(root,text="Fare",fg="green4",font="Arial 10 bold").grid(row=4,column=4)
            #Button(root,text="Proceed to Book",bg="springGreen2").grid(row=5,column=6)
        Button(root,text="Show Bus",bg="green4",command=proceed_book).grid(row=3,column=6)
        
        def passenger_detail():
            Label(root,text="Fill Passenger Details to book the bus ticket",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=6,column=0,pady=15,columnspan=10)    
            Label(root,text="Name").grid(row=7,column=0)
            Entry(root).grid(row=7,column=1)
            Label(root,text="Gender").grid(row=7,column=2)
            gender_select=StringVar()
            option=["Male","female","Other"]
            d_menu=OptionMenu(root,gender_select,*option)
            d_menu.grid(row=7,column=3)
            Label(root,text="No of seats").grid(row=7,column=4)
            Entry(root).grid(row=7,column=5)
            Label(root,text="Mobile No.").grid(row=7,column=6)
            Entry(root).grid(row=7,column=7)
            Label(root,text="Age").grid(row=7,column=8)
            Entry(root).grid(row=7,column=9)
            Button(root,text="Book Seat",bg="springGreen2").grid(row=7,column=10)
        Button(root,text="Proceed to Book",bg="springGreen2",command=passenger_detail).grid(row=5,column=6)
        root.mainloop()
    def checkseat():
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=400,columnspan=30)
        Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=30)
        Label(root,text="Check Your Booking",bg="SpringGreen2",fg="green4",font="Arial 15 bold").grid(row=2,column=0,pady=20,columnspan=30)
        Label(root,text="Enter Your Mobile No: ").grid(row=3,column=12)
        Entry(root).grid(row=3,column=13)
        Button(root,text="Check Booking").grid(row=3,column=14)
        root.mainloop()
    def addbus():
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        def des4(w=0):
            root.destroy()
            tr.operdetail()
        def des5(p=0):
            root.destroy()
            tr.busdetail()
        def des6(o=0):
            root.destroy()
            tr.routedetails()
        def des7(z=0):
            root.destroy()
            tr.newrun()
        Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=10)
        Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=10)
        Label(root,text="Add New Details To DataBase",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=30,columnspan=10)
        Button(root,text="New Operator",command=des4,bg="green3",font="Arial 15").grid(row=3,column=3)
        Button(root,text="New Bus",command=des5,bg="IndianRed2",font="Arial 15").grid(row=3,column=4)
        Button(root,text="New Route",command=des6,bg="RoyalBlue3",font="Arial 15").grid(row=3,column=5)
        Button(root,text="New Run",command=des7,bg="salmon4",font="Arial 15").grid(row=3,column=6)
        root.mainloop()
    def operdetail():
        
            
        curr.execute("create table IF NOT EXISTS OP (opid varchar(50) primary key, name varchar(10), address varchar(50), phone varchar(10), email varchar(50))");
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
    def busdetail():
        
        curr.execute("create table IF NOT EXISTS busdetails (busid varchar(50) primary key, type varchar(10), capacity int(50), fare int(10), operid varchar(50) , routid varchar(50), FOREIGN KEY (operid) REFERENCES operdetail(opid), FOREIGN KEY (routid) REFERENCES routedetails(routeid))");
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

    def routedetails():
        curr.execute("create table IF NOT EXISTS routedetails (routeid PRIMARY KEY, varchar(50), station varchar(10), stationid varchar(50))");

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
    def newrun():
        curr.execute("create table IF NOT EXISTS rundetails (bus_id varchar(50) PRIMARY KEY, running varchar(10), seat_aval varchar(50))")

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













tr = bus_booking
tr.first()
