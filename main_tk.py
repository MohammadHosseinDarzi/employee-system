from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
import mysql.connector as mysql
#ديتابيس************
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "112331",
    database = "employee"
)
cursor = db.cursor()
#*****************
win=Tk()
win.title("mohammad")
win.state("zoomed")
win.config(bg="blue")
top_frame=LabelFrame(win,text="employee system",bg="#857cd3")
top_frame.pack(fill=BOTH,expand=True)
bottom_frame=LabelFrame(win,text="information List",bg="gray")
bottom_frame.pack(fill=BOTH,expand=True)
#############

#########variables
g1=StringVar()
c1=StringVar()
s1=StringVar()
s2=StringVar()

name=StringVar()
Last_name=StringVar()
city=StringVar()
gmail=StringVar()
phone=StringVar()
#___________label frame_________#
tv=ttk.Treeview(bottom_frame)
tv.grid(row=1,column=1,padx=20,pady=20)
tv["columns"]=("1","2","3","4","5","6","7","8","9","10")
tv["show"]="headings"
##tv.column("1",width=135,anchor="c")
##tv.column("2",width=135,anchor="c")
##tv.column("3",width=135,anchor="c")
##tv.column("4",width=135,anchor="c")
##tv.column("5",width=135,anchor="c")
##tv.column("6",width=135,anchor="c")
##tv.column("7",width=135,anchor="c")
##tv.column("8",width=135,anchor="c")
##tv.column("9",width=135,anchor="c")
##tv.column("10",width=135,anchor="c")
#___________________________#
tv.heading("1",text="name")
tv.heading("2",text="Last_name")
tv.heading("3",text="CITY")
tv.heading("4",text="gmail")
tv.heading("5",text="PHONE NUMBER")
tv.heading("6",text="Nationality")
tv.heading("7",text="month of birth")
tv.heading("8",text="Year of birth")
tv.heading("9",text="Day of birth")
tv.heading("10",text="Gender")


#_____________________
def Add():
    tv.insert("",END,values=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),c1.get(),s1.get(),s2.get(),g1.get()))
def delete():
    xx=tv.selection()
    tv.delete(xx)
def clear():
    name.set("")
    Last_name.set("")
    city.set("")
    gmail.set("")
    phone.set("")
    g1.set("")
    c1.set("")
    s1.set("")
    s2.set("")
def update_employee():
    selected=tv.focus()
    tv.item(selected,values=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),w.get(),q.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    w.delete(0,END)
    q.delete(1.0,END)
    
    b4.config(command=dispalyAll)
def dispalyAll ():
      clear()
      selected=tv.focus()
      values=tv.item(selected,"values")
      e1.insert(0,values[0])
      e2.insert(0,values[1])
      e3.insert(0,values[2])
      e4.insert(0,values[3])
      e5.insert(0,values[4])
      e6.insert(0,values[5])
      w.insert(0,values[6])
      q.insert(0,values[7])
   
     
      b4.config(command=update_employee) 
      
def save():
#f=filedialog.asksaveasfile(mode='a',defaultextension='.txt')
#info="\n"+"name:"+e1.get()+"***"+e2.get()+"***"+e3.get()+"***"+e4.get()+"***"+e5.get()+"***"+e6.get()+"***"+w.get()+"***"+q.get()
#f.write(info)
#f.close()

    sql="INSERT INTO person(name,last_name,city,gmail,phone,month,year,day,gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),c1.get(),s1.get(),s2.get(),g1.get())
    cursor.execute(sql,val)
    db.commit()    
    messagebox.showinfo("ok","your information saved successfully")
def n():
    win1=Tk()
def opn():
    filedialog.askopenfile(mode='r')
#_________________
a=Label(top_frame,text="name")
a.place(x=20,y=20)
b=Label(top_frame,text="Last_name")
b.place(x=20,y=60)
J=Label(top_frame,text="CITY")
J.place(x=20,y=100)
y=Label(top_frame,text="gmail")
y.place(x=20,y=140)
P=Label(top_frame,text="PHONE NUMBER")
P.place(x=20,y=170)
o=Label(top_frame,text="Nationality")
o.place(x=20,y=220)
#####entry of lables
e1=Entry(top_frame,textvariable=name)
e1.place(x=130,y=20)
e2=Entry(top_frame,textvariable=Last_name)
e2.place(x=130,y=60)
e3=Entry(top_frame,textvariable=city)
e3.place(x=130,y=100)
e4=Entry(top_frame,textvariable=gmail)
e4.place(x=130,y=140)
e5=Entry(top_frame,textvariable=phone)
e5.place(x=130,y=170)
e6=Entry(top_frame)
e6.place(x=130,y=220)
#_____________               #________
g=Label(top_frame,text="moth of berthday")
g.place(x=300,y=20)
w=ttk.Combobox(top_frame,values=("farvardin","ordibehesht","khordad","tir","mordad","shahrivar","mehr","aban","azar","day","bahman","sfand"),textvariable=c1)
w.place(x=400,y=20)
t=Label(top_frame,text="Year of berthday")
t.place(x=300,y=60)
q=Spinbox(top_frame,from_=1300,to=1403,textvariable=s1)
q.place(x=400,y=60)
i=Label(top_frame,text="Day of berthday")
i.place(x=300,y=100)
j=Spinbox(top_frame,from_=1,to=31,textvariable=s2 )
j.place(x=400,y=100)
h=Label(top_frame,text="Gender")
h.place(x=300,y=140)
r1=Radiobutton(top_frame,text="men",value="men",variable=g1)
r1.place(x=350,y=140)
r2=Radiobutton(top_frame,text="woman",value="woman",variable=g1)
r2.place(x=410,y=140)


#_______________________#


#_____________#
b1=Button(top_frame,text="save",command=save,bg="#1fc4b3",height=2,width=8)
b1.place(x=680,y=10)
b2=Button(top_frame,text="Add",command=Add,bg="#1fc4b3",height=2,width=8)
b2.place(x=740,y=10)
b3=Button(top_frame,text="Delete",command=delete,bg="#1fc4b3",height=2,width=8)
b3.place(x=680,y=50)
b4=Button(top_frame,text="Update",bg="#1fc4b3",height=2,width=8,command=dispalyAll)
b4.place(x=740,y=50)
b5=Button(top_frame,text="Search",bg="#1fc4b3",height=2,width=8)
b5.place(x=680,y=90)
b6=Button(top_frame,text="Clear",bg="#1fc4b3",height=2,width=8,command=clear)
b6.place(x=740,y=90)
#_________________________#
menubar=Menu(win)
filemenu=Menu(menubar,tearoff=0,bg="pink",fg="green")
editmenu=Menu(menubar,tearoff=0)
#_________________________________
filemenu.add_command(label="new",command=n)
filemenu.add_command(label="open",command=opn)
filemenu.add_command(label="save",command=save)
filemenu.add_separator()
filemenu.add_command(label="exit",command=exit)
#_____________________________-
editmenu.add_command(label="copy")
#_______________________________
menubar.add_cascade(label="file",menu=filemenu)
menubar.add_cascade(label="edit",menu=editmenu)
#________________________________________________
win.config(menu=menubar)

win.mainloop()

