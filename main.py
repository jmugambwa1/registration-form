from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry('600x470')
root.resizable("False", "False")

def register():
    name_info=nameValue.get()
    email_info=emailValue.get()
    gender_info=genderValue.get()
    phone_info=phoneValue.get()

    file=open(name_info +".txt","w")
    file.write(name_info + "\n")
    file.write(phone_info + "\n")
    file.write(gender_info + "\n")
    file.write(email_info + "\n")
    file.close()

    Label(text="Registered Successfully!", fg="green",font=("calibri", 11)).place(x=250,y=430)

    nameEntry.delete(0,"end")
    phoneEntry.delete(0,"end")
    genderEntry.delete(0, "end")
    emailEntry.delete(0,"end")


    

Label(root, text="Registration Form", font="Arial, 25").pack(pady=50)

Label(text="Name", font= 23).place(x=100,y=150)
Label(text="Phone", font= 23).place(x=100,y=200)
Label(text="Gender", font= 23).place(x=100,y=250)
Label(text="Email", font= 23).place(x=100,y=300)

#Entries
nameValue=StringVar()
phoneValue=StringVar()
genderValue=StringVar()
emailValue=StringVar()

nameEntry= Entry(font= 'arial, 18', textvariable= nameValue)
nameEntry.place(x=200, y=150)

phoneEntry= Entry(font= 'arial, 18', textvariable= phoneValue)
phoneEntry.place(x=200, y=200)

genderEntry= Entry(font= 'arial, 18', textvariable= genderValue)
genderEntry.place(x=200, y=250)

emailEntry= Entry(font= 'arial, 18', textvariable= emailValue)
emailEntry.place(x=200, y=300)

#check button
checkValue=IntVar()
checkbtn=Checkbutton(text="Remember me", variable= checkValue)
checkbtn.place(x=200, y=340)

Button(text="Register",font=22,width=11,height=2, command=register).place(x=250, y=380)

root.mainloop()