from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=500,columnspan=10)
Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=30,columnspan=10)
Label(root,text="Add New Details To DataBase",fg="green4",font="Arial 18 bold").grid(row=2,column=0,pady=30,columnspan=10)
Button(root,text="New Operator",bg="green3",font="Arial 15").grid(row=3,column=3)
Button(root,text="New Bus",bg="IndianRed2",font="Arial 15").grid(row=3,column=4)
Button(root,text="New Route",bg="RoyalBlue3",font="Arial 15").grid(row=3,column=5)
Button(root,text="New Run",bg="salmon4",font="Arial 15").grid(row=3,column=6)
