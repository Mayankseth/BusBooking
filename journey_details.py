from tkinter import *
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

