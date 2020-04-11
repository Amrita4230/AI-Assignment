from tkinter import*
import sqlite3
import tkinter.messagebox
root=Tk()
root.geometry("650x320")
root.title("LOG in")
regno = StringVar()
password = StringVar()
cur_user=""
con=sqlite3.connect("login.db")
root.configure(background="cyan4")
def new():
   root.destroy()
   root13 = Tk()
   root13.geometry('800x800')
   canvas= Canvas(root13,width = 800, height = 800,bg="Darkolivegreen2" )
   canvas.pack(expand = YES, fill = BOTH)
   root13.title("Registration Form")

   name=StringVar()
   username=StringVar()
   a=StringVar()
   b=StringVar()
   email=StringVar()
   password=StringVar()
   mobile=StringVar()
   b=StringVar()
   c=StringVar()
   conn=sqlite3.connect("login.db")

   def database():
       nm=name.get()
       usrnm=username.get()
       sts=a.get()
       gnr=b.get()
       mail=email.get()
       pswd=password.get()
       mbl=mobile.get()
       dpt=c.get()
       conn.execute("create table if not exists register(Name text,Username text, Status text,Gender text,Emailid text,Password text,Mobile text,Department text);")
       conn.execute("insert into register values(?,?,?,?,?,?,?,?)",(nm,usrnm,sts,gnr,mail,pswd,mbl,dpt))
       conn.commit()
       p=conn.execute("select * from register")
       for i in p:
           print("Username",i[1])
           print("Password",i[5])

       tkinter.messagebox.showinfo("Parking Management","Registered successfully")
       root13.destroy()



   label_0 = Label(root13, text="Registration form for Parking",width=25,font=("", "24", "bold"), foreground="white",bg="black")
   label_0.place(x=80,y=40)

   label_1 = Label(root13, text="Name",width=20,font=("bold", 10),bg="black",fg="white")
   label_1.place(x=80,y=130)

   entry_1 = Entry(root13,textvariable=name,bg="white",fg="black")
   entry_1.place(x=300,y=130)

   label_2 = Label(root13, text="Registration no.",width=20,font=("bold", 10),bg="black",fg="white")
   label_2.place(x=80,y=180)

   entry_2 = Entry(root13,textvariable=username,bg="white",fg="black")
   entry_2.place(x=300,y=180)

   label_3 = Label(root13, text="Status",width=20,font=("bold", 10),bg="black",fg="white")
   label_3.place(x=80,y=230)
   list1=['FACULTY','STUDENT']
   a=StringVar()
   droplist=OptionMenu(root13,a, *list1)
   droplist.config(width=40,height=1,bg="white",fg="black")
   a.set('Select your Status')
   droplist.place(x=300,y=230)                         

   label_4 = Label(root13, text="Gender",width=20,font=("bold", 10),bg="black",fg="white")
   label_4.place(x=80,y=280)
   list2=['MALE','FEMALE']
   b=StringVar()
   droplist=OptionMenu(root13,b, *list2)
   droplist.config(width=40,height=1,bg="white",fg="black")
   b.set('Select your Gender')
   droplist.place(x=300,y=280)

   label_5 = Label(root13, text="Email-id",width=20,font=("bold", 10),bg="black",fg="white")
   label_5.place(x=80,y=330)

   entry_5 = Entry(root13,textvariable=email,bg="white",fg="black")
   entry_5.place(x=300,y=330)

   label_6 = Label(root13, text="Password",width=20,font=("bold", 10),bg="black",fg="white")
   label_6.place(x=80,y=380)
   bullet="\u2022"
   entry_6 = Entry(root13,textvariable=password,show=bullet,bg="white",fg="black")
   entry_6.place(x=300,y=380)

   label_7 = Label(root13, text="Confirm Password",width=20,font=("bold", 10),bg="black",fg="white")
   label_7.place(x=80,y=430)

   entry_7 = Entry(root13,show=bullet,bg="white",fg="black")
   entry_7.place(x=300,y=430)

   label_8 = Label(root13, text="Mobile Number",width=20,font=("bold", 10),bg="black",fg="white")
   label_8.place(x=80,y=480)

   entry_8 = Entry(root13,textvariable=mobile,bg="white",fg="black")
   entry_8.place(x=300,y=480)

   label_9 = Label(root13, text="Department",width=20,font=("bold", 10),bg="black",fg="white")
   label_9.place(x=80,y=530)

   list3 = ['AGRICULTURE','BIOENGINEERING AND BIOSCIENCES','BUSINESS','ENGINEERING','COMPUTER APPLICATIONS','FASHION DESIGN','HOTEL MANAGEMENT','FINE ARTS','LAW','PHARMACY'];
   c=StringVar()
   droplist=OptionMenu(root13,c, *list3)
   droplist.config(width=40,height=1,bg="white",fg="black")
   c.set('Select your Department')
   droplist.place(x=300,y=530)

   Button(root13, text='Submit',width=20,bg='red',fg='black',command=database).place(x=240,y=600)

   root13.mainloop()
def request(curr_user):
   root12 = Tk()
   root12.title(" Check for Parking Availability")
   root12.geometry("640x400")
   db = sqlite3.connect("login.db")
   root12.configure(background='#90CAF9')
   reg_no = StringVar()
   block=IntVar()
   fare=StringVar()
   currr=StringVar()
   currr.set(curr_user)
   fare.set("-")
   drop=StringVar(root12)
   print("current user::",curr_user)
   drop.set("Choose Time Period(in Hrs.)")
   db.execute("Create table if not exists parking(regno varchar(20),block int,fare int);")
   def reserve():
       print("in Reserve")
       if(fare.get() is '-'):
           tkinter.messagebox.showinfo("Warning","Calculate the fare first by Selecting time Period")
       elif(reg_no.get() == ""):
            tkinter.messagebox.showinfo("Warning","Please Provide a Registration Number")
       else:
          _Reg_no = reg_no.get()
          _Block = block.get()
          _Fare = fare.get()
          print(_Reg_no)
          db.execute("insert into parking values(?,?,?)",(_Reg_no,_Block,_Fare))
          db.commit()
          if(_Block == 0):
             confirm = "You Can Park Vehice at Block 29 with Fare: "+ _Fare
             tkinter.messagebox.showinfo("Confirmation",confirm)
          else:
             confirm = "You Can Park Vehice at Block 30 with Fare: "+ _Fare 
             tkinter.messagebox.showinfo("Confirmation",confirm)
       db.close()
   def calculate_fare():
       _drop = drop.get()
       if(_drop == "Choose Time Period(in Hrs.)"):
           tkinter.messagebox.showinfo("Warning","Calculate the fare first by Selecting time Period")
           fare.set("-")
       elif(_drop == "3"):
           fare.set(3*20)
       elif(_drop == "6"):
           fare.set(6*20)
       elif(_drop == "8"):
           fare.set(8*20)
           
   # GUI DESIGN FOR PARKING REQUEST
   title=Label(root12,text=" Booking Slot").place(x=600,y=330)
   canvas=Canvas(root12,height=300,width=600,relief="raised",bg="grey").place(x=250,y=300)
   Label(root12,text="Parking Request",bg="yellow",fg="black",font=("Courier", 24)).place(x=390,y=290)
   l1=Label(root12,text="Reg.No:",fg="black",bg="olivedrab2").place(x=300,y=340)
   reg_entry=Entry(root12,bd=2,textvariable=reg_no).place(x=360,y=340)
   Label(root12,text="Block:",bg="olivedrab2",fg="black").place(x=330,y=380)
   blk1=Radiobutton(root12,text="Near-block:1",variable=block,value=0,bg="olivedrab2",fg="black").place(x=400,y=380)
   blk30=Radiobutton(root12,text="Near-Block:30",variable=block,value=1,bg="olivedrab2",fg="black").place(x=500,y=380)
   Label(root12,text="Time Period:",bg="olivedrab2",fg="black").place(x=300,y=420)
   Timeprd=OptionMenu(root12,drop,"3","6","8").place(x=400,y=420)
   Fare=Label(root12,bg="olivedrab2",fg="black",textvariable=fare).place(x=370,y=490)
   f=Label(root12,text="Fare(in Rs):",bg="olivedrab2",fg="black").place(x=300,y=490)
   Label(root12,text="Current User::",bg="olivedrab2",fg="black").place(x=600,y=350)
   currentuser=Label(root12,textvariable=currr,bg="olivedrab2",fg="black",font=("Courier", 15,"bold")).place(x=680,y=350)
   # calculate fare button 
   FareCal=Button(root12,text="Calculate Fare",bg="red",command=calculate_fare).place(x=410,y=460)
   # booking slot button for parking
   park=Button(root12,text="Reserve Parking Slot",bg="red",command=reserve).place(x=380,y=520)
   root12.mainloop()
 
def punch():
   name=regno.get()
   pword=password.get()
   if name == "" and pword == "":
      tkinter.messagebox.showinfo( "Parking Management", "Login UNSuccessful \n Enter your Name and Password")
   elif name=="":
         tkinter.messagebox.showinfo( "Parking Management", "Login UNSuccessful \n Enter your Reg No.")
   elif pword =="":
         tkinter.messagebox.showinfo( "Parking Management", "Login UNSuccessful \n Enter your Password")
         
   else:
      con.execute("create table if not exists Login1(regno varchar(20),password varchar(20))")
      con.execute("insert into Login1 values(?,?)",(name,pword))
      currentuser=name
      con.commit()
      d = con.execute("select * from register")
      count=0
      for i in d:
         if name==i[1] and pword==i[5]:
            count=count+1
            cur_user=i[0]
      if count!=0:
         tkinter.messagebox.showinfo( "Parking Management", "Login Successful")
         root.destroy()
         request(cur_user)
      else:
         tkinter.messagebox.showinfo( "Parking Management", "Login UnSuccessful")
         regno.set("")
         password.set("")
                     
labelfont = ('Arial', 20, 'bold')
e4=Label(root,text="Parking Management System",bg="yellow",font=labelfont).place(x=490,y=120)
c1=Canvas(root,relief="raised",border=2,width=400,height=200,bg="#b2fab4").place(x=480,y=200)



l1=Label(c1,text="Registration No.",bg="#b2fab4",font = "Verdana 8 bold italic").place(x=490,y=230)
e1=Entry(c1,bd=2,textvariable=regno).place(x=600,y=230)
l2=Label(c1,text="Password",bg="#b2fab4",font = "Verdana 10 bold italic").place(x=490,y=260)
bullet="\u2022"
e2=Entry(c1,bd=2,textvariable=password,show=bullet).place(x=600,y=260)
l3=Label(c1,text="Or",bg="#b2fab4",font="Elephant 8").place(x=650,y=330)

b1=Button(c1,text="LOGIN",bg="#7DCEA0" ,font="Verdana 8 bold",activebackground="#85929E",command=punch,width=15).place(x=600,y=310)
b2=Button(c1,text="Sign Up",bg="#7DCEA0",font="Verdana 8 bold",activebackground="#85929E",width=15,command=new).place(x=600,y=350)
root.mainloop()

