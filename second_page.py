from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=700,columnspan=10)
Label(root,text="Online Bus Booking System",bg="LightSteelBlue3",font="Algerian 20 bold",fg="red").grid(row=1,column=0,pady=50,columnspan=10)
Button(root,text="Seat Booking",bg="green3",font="Algerian 15 bold").grid(row=2,column=3)
Button(root,text="Check Booked Seat",bg="green3",font="Algerian 15 bold").grid(row=2,column=4)
Button(root,text="Add Bus Details",bg="green3",font="Algerian 15 bold").grid(row=2,column=5)
root.mainloop()