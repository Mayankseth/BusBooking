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
        root = Tk()
        root.title("SEAT BOOKING PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        def journey_to_home():
            root.destroy()
            self.home_page()

        def show_bus():
            tp=to_place.get()
            fp=from_place.get()
            jd=journey_date.get()

            if tp.isalpha() and fp.isalpha():
                if not jd=='':
                    tp = tp.lower()
                    fp = fp.lower()
                    cur.execute('select r_id from route where s_name=? and e_name=?', (fp, tp))
                    res_route = cur.fetchall()
                    if len(res_route)==0:
                        showerror('no route found','we are currently not running on this route')
                    else:
                        for i in res_route:
                            for j in i:
                                val_route = str(j)

                        cur.execute('select bus_id from bus where route_id=?', (val_route))
                        res_bid = cur.fetchall()

                        if len(res_bid)==0:
                            showerror('no bus found','we have not started any bus on this route yet!!')
                        else:
                            val_bid = []
                            for i in res_bid:
                                for j in i:
                                    val_bid.append(j)
                            res_new_bid=[]
                            for i in range(len(val_bid)):
                                cur.execute('select b_id from running where run_date=? and b_id=? ',(jd, val_bid[i]))
                                res_new_bid.append(cur.fetchall())
                            #print(res_new_bid)
                            b=[]
                            for i in res_new_bid:
                                for j in i:
                                    b.append(j[0])

                            #print(b)
                            if len(b)==0:
                                showerror('no running bus',"try another date!!")
                            else:
                                Label(root,text='select bus ',font='Arial 10 bold').grid(row=6,column=3)
                                Label(root, text='operator ', font='Arial 10 bold').grid(row=6, column=4)
                                Label(root, text='bus_type ', font='Arial 10 bold').grid(row=6, column=5)
                                Label(root, text='Available Capacity ', font='Arial 10 bold').grid(row=6, column=6)
                                Label(root, text='fare ', font='Arial 10 bold').grid(row=6, column=7)
                                r=7
                                bus_no=IntVar()
                                bus_select = IntVar()
                                serial_no=1
                                for i in b:
                                    bus_no=i
                                    cur.execute('select op_id from bus where bus_id=?',(i))
                                    res_opr_id=cur.fetchall()
                                    for j in res_opr_id:
                                        opr_id=j[0]

                                    cur.execute('select name from operator where opr_id=?',(opr_id))
                                    res_opr_name=cur.fetchall()
                                    for j in res_opr_name:
                                        opr_name=j[0]

                                    cur.execute('select bus_type from bus where bus_id=?',(i))
                                    res_bus_type=cur.fetchall()
                                    for j in res_bus_type:
                                        bus_type=j[0]

                                    cur.execute('select seat_avail from running where run_date=? and b_id=?',(jd,i))
                                    res_seat_avail=cur.fetchall()
                                    for j in res_seat_avail:
                                        seat_avail=j[0]

                                    cur.execute('select fair from bus where bus_id=?',(i))
                                    res_fare=cur.fetchall()
                                    for j in res_fare:
                                        fare=j[0]

                                    def show_button():
                                        Button(root, text='PROCEED', bg='green', fg='black', font='Arial 12 bold',
                                               command=proceed).grid(row=10, column=9, padx=30)

                                    var=Radiobutton(root,value=bus_no,variable=bus_select,command=show_button)
                                    var.grid(row=r,column=3)
                                    Label(root, text=opr_name, font='Arial 10 bold').grid(row=r, column=4)
                                    Label(root, text=bus_type, font='Arial 10 bold').grid(row=r, column=5)
                                    Label(root, text=seat_avail, font='Arial 10 bold').grid(row=r, column=6)
                                    Label(root, text=fare, font='Arial 10 bold').grid(row=r, column=7)

                                    r+=1
                                    serial_no+=1

                                def proceed():
                                    f_bus_id = bus_select.get()

                                    Label(root,text="\n\n\n").grid(row=10,columnspan=12)
                                    Label(root,text='Fill passenger details to book the bus', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=11,columnspan=12)
                                    Label(root, text="\n\n\n").grid(row=12,columnspan=12)

                                    Label(root,text='name',font='Arial 10 bold').grid(row=13,column=3)
                                    pname = Entry(root, font='Arial 12 bold', fg='black')
                                    pname.grid(row=13,column=4)

                                    gender = StringVar()
                                    gender.set("Select Gender")
                                    opt = ["M", "F", "T"]
                                    g_menu = OptionMenu(root, gender, *opt)
                                    g_menu.grid(row=13, column=6)

                                    Label(root, text='no of seats', font='Arial 10 bold').grid(row=13, column=7)
                                    pseat=Entry(root, font='Arial 12 bold', fg='black')
                                    pseat.grid(row=13,column=8)

                                    Label(root, text='mobile', font='Arial 10 bold').grid(row=14, column=3)
                                    pmobile = Entry(root, font='Arial 12 bold', fg='black')
                                    pmobile.grid(row=14, column=4)

                                    Label(root, text='age', font='Arial 10 bold').grid(row=14, column=5)
                                    page = Entry(root, font='Arial 12 bold', fg='black')
                                    page.grid(row=14, column=6)

                                    def book_seat():
                                        name=pname.get()
                                        gen=gender.get()
                                        seats=pseat.get()
                                        seats=int(seats)
                                        age=page.get()
                                        age=int(age)
                                        mobile=pmobile.get()
                                        bid=bus_select.get()
                                        if len(mobile)==10:
                                            if len(name)>0 and len(name)<20:
                                                if age>0 and age<150:
                                                    if seats>0 and seats<6:
                                                        #print(name, gen, age, mobile, seats, bid)
                                                        booking_ref=1
                                                        cur.execute('select booking_ref from booking_history')
                                                        res_ref=cur.fetchall()
                                                        ref=[]
                                                        for i in res_ref:
                                                            ref.append(i[0])
                                                        booking_ref=len(ref)+1
                                                        #print(booking_ref)
                                                        cur_date=date.today()
                                                        cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                        con.commit()
                                                        cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                        res_s=cur.fetchall()
                                                        s=res_s[0][0]
                                                        s=s-seats
                                                        cur.execute('update running set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                        con.commit()
                                                        showinfo("succefull","booking successfull")

                                                    else:
                                                        showerror("booking limit exceed","you can only book upto 5 seats")
                                                else:
                                                    showerror("incorrect age","enter valid age")
                                            else:
                                                showerror("incorrect name","enter valid name")
                                        else:
                                            showerror("invalid mobile no","enter valid mobile no")


                                    Button(root, text='BOOK SEAT', bg='green', fg='black', font='Arial 12 bold',
                                           command=book_seat).grid(row=16, column=9, padx=30)



                else:
                    showerror('error','enter journey date')


            else:
                showerror('ERROR',"enter correctly!!")


        bus = PhotoImage(file='Bus_for_project.png')
        Label(root, image=bus).grid(row=0, column=3, columnspan=12)
        Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=2,
                                                                                                          column=3,
                                                                                                          pady=20,
                                                                                                          columnspan=12)
        Label(root, text='Enter Journey Details', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=3,
                                                                                                                column=3,
                                                                                                                columnspan=12,
                                                                                                                pady=20)
        Label(root, text='To', fg='black', font='Arial 12 bold').grid(row=4, column=3, padx=30)
        to_place = Entry(root, font='Arial 12 bold', fg='black')
        to_place.grid(row=4, column=4, padx=50)

        Label(root, text='From', fg='black', font='Arial 12 bold').grid(row=4, column=5, padx=30)
        from_place = Entry(root, font='Arial 12 bold', fg='black')
        from_place.grid(row=4, column=6, padx=50)

        Label(root, text='Journey date', fg='black', font='Arial 12 bold').grid(row=4, column=7, padx=30)
        journey_date = Entry(root, font='Arial 12 bold', fg='black')
        journey_date.grid(row=4, column=8, padx=50)
        Label(root,text="date formate YYYY-MM-DD").grid(row=5,column=8)

        Button(root, text='Show Bus', bg='green', fg='black', font='Arial 12 bold',command=show_bus).grid(row=4, column=9, padx=30)

        home = PhotoImage(file='home.png')

        Button(root, image=home,command=journey_to_home).grid(row=4, column=10)

        root.mainloop()

    def check_booking_page(self):
        root = Tk()
        root.title("CHECK BOOKING PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='Bus_for_project.png')
        home=PhotoImage(file='home.png')

        def check_booking_to_home():
            root.destroy()
            self.home_page()
        def check_tkt():
            mobile=mob.get()
            if len(mobile)==10 and mobile.isdigit():
                cur.execute('select * from booking_history where phone=?',[mobile])
                res_tkt=cur.fetchall()
                for i in res_tkt:
                    name=i[0]
                    gen=i[1]
                    seat=i[2]
                    phone=i[3]
                    age=i[4]
                    ref=i[5]
                    book_date=i[6]
                    travel_date=i[7]
                    b_i_d=i[8]
                cur.execute('select fair,route_id from bus where bus_id=?',[b_i_d])
                res_bus=cur.fetchall()
                fare=res_bus[0][0]
                route_id=res_bus[0][1]
                cur.execute('select s_name,e_name from route where r_id=?',[route_id])
                res_route=cur.fetchall()
                s_name=res_route[0][0]
                e_name=res_route[0][1]
                cur.execute('select booking_ref from booking_history where phone=?',[phone])
                res_ref=cur.fetchall()
                b_ref=res_ref[0][0]


                Label(text="YOUR TICKET", font='Arial 12 bold', bg='blue',fg='white').grid(row=6,columnspan=12 )
                Label(text="booking ref = "+b_ref,font='Arial 12 bold', fg='blue').grid(row=7,column=4)
                Label(text="name = " + name, font='Arial 12 bold', fg='blue').grid(row=7, column=5)
                Label(text="gender = " + gen, font='Arial 12 bold', fg='blue').grid(row=7, column=6)
                Label(text="no of seats = " + str(seat), font='Arial 12 bold', fg='blue').grid(row=7, column=7)
                Label(text="age = " + str(age), font='Arial 12 bold', fg='blue').grid(row=7, column=8)
                Label(text="booked on = " + book_date, font='Arial 12 bold', fg='blue').grid(row=8, column=4)
                Label(text="travel date = " + travel_date, font='Arial 12 bold', fg='blue').grid(row=8, column=5)
                Label(text="fare = " + str(fare), font='Arial 12 bold', fg='blue').grid(row=8, column=6)
                Label(text="total fare = " + str(fare*seat), font='Arial 12 bold', fg='blue').grid(row=8, column=7)




        Label(root, image=bus).grid(row=0, column=0, columnspan=12, padx=80)
        Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='cyan2', fg='blue4').grid(row=2,
                                                                                                         column=0,
                                                                                                         columnspan=12,
                                                                                                         pady=20)
        Label(root, text="Check Your Booking", font='Arial 22 bold', bg='olivedrab1', fg='dark green').grid(row=3,
                                                                                                            column=0,
                                                                                                            pady=20,
                                                                                                            columnspan=12,
                                                                                                            padx=600)

        Label(root, text="Enter your mobile no.", font='Arial 12 bold', fg='black').grid(row=4, column=5)
        mob=Entry(root, font='Arial 12 bold')
        mob.grid(row=4, column=6)

        Button(root, text='Check Booking', font='Arial 12',command=check_tkt).grid(row=4, column=7)
        Button(root, image=home,command=check_booking_to_home).grid(row=5, column=7,pady=20)
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
