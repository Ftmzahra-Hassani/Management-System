from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("600x500")
win.config(bg="#f8cde2")
from database import Database
db=Database()



#function
def clear():
    ent_course.delete(0 , END)
    ent_lname.delete(0 , END)
    ent_name.delete(0 , END)
    ent_pass.delete(0 , END)

def exit():
    result = messagebox.askquestion('exit' , 'Are you sure to exit?')
    if result=="yes":
        win.destroy()

def insert():
    name = ent_name.get()
    lname = ent_lname.get()
    password = ent_pass.get()
    course = ent_course.get()
    db.add_student(name , lname , password , course)
    messagebox.showinfo('insert' , 'record inserted')

def show():
    lst.delete(0 , END)
    users = db.show_student()
    for user in users:
        lst.insert(END , user)

def remove():
    index = lst.curselection()
    if index:
        users = db.select_record()
        record= users[index[0]]
        result=messagebox.askquestion("delete" , "Are you sure to delete?")
        if result=="yes":
            db.delete_student(record[0])
        
    else:
        messagebox.showwarning("raning" , "select one of them")
        
def enter():
    new_win = Toplevel(win)
    new_win.title("welcome")
    new_win.geometry('500x300')
    label=Label(new_win , text="welcome back")
    label.pack()

def sign_in():
    password = ent_entry_pass.get().strip()
    if not password:
        messagebox.showerror("Error" ,"Enter password")
        return
    users=db.check_login(password)
    print(users)
    
    if users is not  None:
        enter()
    else:
          messagebox.showerror("error" , "password not find")
      
        



#widget
lbl_enter_pass=Label(win , text="Password" , font="arial 15 bold",width=8 , bg="#800147" , fg="white")
lbl_enter_pass.place(x=400 , y=410 , height=45)
ent_entry_pass=Entry(win , width=60)
ent_entry_pass.place(x=12 , y=410,height=45)
lbl_name=Label(win , text="Name:" , font ="arial 13 bold" , width= 10, bg="#f8cde2")
lbl_name.place(x=10 , y=12 )

lbl_lname = Label(win , text="Last name:" , font="arial 13 bold" , width=10, bg="#f8cde2")
lbl_lname.place(x=300, y=12)

lbl_pass=Label(win , text="Password:" , font="arial 13 bold" , width=8 , bg="#f8cde2")
lbl_pass.place(x=10 , y=42)

lbl_course=Label(win , text="Course:" , font="arial 13 bold" , width=10 , bg = "#f8cde2")
lbl_course.place(x=300 , y=42)

lst=Listbox(win , width=60)
lst.place(x=10 , y=100 , height=290)

btn_show = Button(win , text="Show" , font="arial 15 bold" , width=8 , command=show )
btn_show.place(x=399 , y=100)

btn_add=Button(win , text="Add", font="arial 15 bold" , width=8 , command=insert)
btn_add.place(x=399 , y=150)

btn_clear=Button(win , text="Clear" , font ="arial 15 bold" , width=8 , command=clear)
btn_clear.place(x=399, y=200)


btn_delete=Button(win , text="Delete" , font ="arial 15 bold" , width=8 , command=remove)
btn_delete.place(x=399 , y=250)


btn_exit=Button(win , text="Exit" , font ="arial 15 bold" , width=8 , command=exit)
btn_exit.place(x=399 , y=300)

btn_enter=Button(win , text="Enter" , font="arial 15 bold" , width=8,command=sign_in)
btn_enter.place(x=399 , y=350)

ent_name=Entry(win , width=30)
ent_name.place(x=98 , y=13)

ent_lname=Entry(win , width=30)
ent_lname.place(x=399 , y=13)

ent_pass=Entry(win , width=30)
ent_pass.place(x=98 , y=43)

ent_course=Entry(win , width=30)
ent_course.place(x=399 , y=43)
win.mainloop()


