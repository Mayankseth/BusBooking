from tkinter import *
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
    import second_page

root.bind('<KeyPress>',des)

root.mainloop()