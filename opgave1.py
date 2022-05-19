#Husk at downloade tkinter, Cryptography og pymysql

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import csv

class Login:
   def __init__(self,root):
      self.root=root
      self.root.title("Log ind og registrering for Curvex")
      self.root.geometry("1366x700+0+0")
      self.root.resizable(False,False)
      self.forgotpass()
      self.dataform()
      self.loginform()


   def visdata(self):
       age_of_employees = [25,26,27,28,29,30,31,32,33,34,35]
       salaries_in_IT = [30000, 34000, 35000, 36000, 38000,38500, 39500, 40000, 42000, 45000, 48000]
       salaries_in_admin = [28000, 28500, 30000, 32000, 33000,34500, 35000, 36000, 37500, 38750, 40000]
       salaries_in_economy = [48000, 58500, 60000, 72000, 83000,84500, 85000, 96000, 97500, 98750, 10000]
       plt.xlabel('Uger')
       plt.ylabel('Stressniveau')
       plt.title('Hjerneaktivitet')
       plt.style.use('seaborn-ticks')
       plt.grid()
       plt.plot(age_of_employees, salaries_in_IT, label ='Ludvigs sessioner')
       plt.plot(age_of_employees, salaries_in_admin, label = 'Jørgens sessioner',)
       plt.plot(age_of_employees, salaries_in_economy, label = 'Marks sessioner',)
       plt.legend()
       plt.show()


   def dataform(self):
      Frame_dataform=Frame(self.root,bg="white")
      Frame_dataform.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="databaggrund.jpg")
      img=Label(Frame_dataform,image=self.img).place(x=0,y=0,width=1366,height=700)

      btn1=Button(Frame_dataform,text="Visualisere din data", cursor="hand2", command=self.visdata,
                   font=('times new roman',32,'bold'),
                   fg="black",bg='Green')
      btn1.place(x=470,y=350)

      btn2=Button(Frame_dataform,text="Log ud",command=self.loginform,cursor="hand2",
                  font=("times new roman",15, "bold"),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn2.place(x=1000,y=10)

      btn3=Button(Frame_dataform, text="Tilbage til startsiden",command=self.appscreen,cursor="hand2",
                  font=("times new roman",15, "bold"),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn3.place(x=1000,y=80)


   def forgotpass(self):
      Frame_forgotpass=Frame(self.root,bg="white")
      Frame_forgotpass.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="password.png")
      img=Label(Frame_forgotpass,image=self.img).place(x=0,y=0,width=1366,height=700)

      label1=Label(Frame_forgotpass,text="Har du glemt dit kodeord? Så send en mail ind til os på 'Curvexhjalp@gmail.com' så hjælper vi dig."
      ,font=('Times new Roman',20),fg="white",bg='gray')
      label1.place(x=120, y=350)

      btn1=Button(Frame_forgotpass, text="Tilbage til startsiden",command=self.loginform,cursor="hand2",
                  font=("times new roman",15, "bold"),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn1.place(x=1000,y=80)



   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="baggrund.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)

      label1=Label(frame_input,text="Login Her",font=('Times new Roman',25),
                   fg="red",bg='white')
      label1.place(x=110,y=20)

      label2=Label(frame_input,text="Emailadresse",font=("Times new Roman",20),
                   fg='Blue',bg='white')
      label2.place(x=30,y=95)

      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.email_txt.place(x=30,y=135,width=270,height=35)

      label3=Label(frame_input,text="Kodeord",font=("Times new Roman",20,),
                   fg='Blue',bg='white')
      label3.place(x=30,y=180)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.password.place(x=30,y=220,width=270,height=35)

      btn1=Button(frame_input,text="Glemt dit kodeord?", command=self.forgotpass,
            cursor='hand2',font=('Times new Roman',12),bg='white',fg='black',bd=0)
      btn1.place(x=120,y=270)

      btn2=Button(frame_input,text="Medarbejdere login",command=self.Mlog,cursor="hand2",
                  font=("times new roman",15),fg="White",bg="Blue",
                  bd=0,width=15,height=1)
      btn2.place(x=90,y=350)

      btn3=Button(frame_input,text="Login",command=self.login,cursor="hand2",
                  font=("times new roman",15),fg="Black",bg="Orangered",
                  bd=0,width=15,height=1)
      btn3.place(x=90,y=305)

      btn4=Button(frame_input,command=self.Register,text="Ikke registeret?"
                  ,cursor="hand2",font=("Times new Roman",12),bg='white',fg="black",bd=0)
      btn4.place(x=125,y=390)

   def Mlog(self):
      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Fejl","Alle faner skal udfyldes",parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='Password',
                                database='medarblogin')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s and password=%s'
                        ,(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror('Dette er et login for medarbejdere','Ugyldig email eller kodeord'
                                    ,parent=self.root)
               self.loginclear()
               self.email_txt.focus()
            else:
               self.Mscreen()
               con.close()
         except Exception as es:
            messagebox.showerror('Fejl',f'Fejl pga. {str(es)}'
                                 ,parent=self.root)

   def login(self):
      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Fejl","Alle faner skal udfyldes",parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='Password',
                                database='pythongui')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s and password=%s'
                        ,(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror('Fejl','Ugyldig email eller kodeord'
                                    ,parent=self.root)
               self.loginclear()
               self.email_txt.focus()
            else:
               self.appscreen()
               con.close()
         except Exception as es:
            messagebox.showerror('Fejl',f'Fejl pga. {str(es)}'
                                 ,parent=self.root)

   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="baggrund.jpg")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)

      label1=Label(frame_input2,text="Registrere dig her",font=('Times new Roman',25,'bold'),
                   fg="Blue",bg='white')
      label1.place(x=45,y=20)

      label2=Label(frame_input2,text="Brugernavn",font=("Times new Roman",18,),
                   fg='Green',bg='white')
      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input2,text="Kodeord",font=("Times new Roman",18),
                   fg='Green',bg='white')
      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=35)

      label4=Label(frame_input2,text="Emailadresse",font=("Times new Roman",18),
                   fg='Green',bg='white')
      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=35)

      label5=Label(frame_input2,text="Bekræft kodeord",
                   font=("Times new Roman",18),fg='Green',bg='white')
      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=35)

      btn2=Button(frame_input2,command=self.register,text="Registrere dig!"
                  ,cursor="hand2",font=("times new roman",15),fg="white",
                  bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)

      btn3=Button(frame_input2,command=self.loginform,
                  text="Alleredet registreret?",cursor="hand2",
                  font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=110,y=390)


   def register(self):
      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
         messagebox.showerror("Fejl","Alle faner skal udfyldes",parent=self.root)
      elif self.entry2.get()!=self.entry4.get():
         messagebox.showerror("Fejl","Kodeordene skal stemme overens med hinanden."
                              ,parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="Password",
                                database="pythongui")
            cur=con.cursor()
            cur.execute("select * from register where emailid=%s"
                        ,self.entry3.get())
            row=cur.fetchone()
            if row!=None:
               messagebox.showerror("Fejl","Emailen er allerede taget, prøv med en anden email"
                                    ,parent=self.root)
               self.regclear()
               self.entry.focus()
            else:
               cur.execute("insert into register values(%s,%s,%s,%s)"
                           ,(self.entry.get(),self.entry3.get(),
                           self.entry2.get(),
                           self.entry4.get()))
               con.commit()
               con.close()
               messagebox.showinfo('Succes','Registering succesfuld'
                                   ,parent=self.root)
               self.regclear()
         except Exception as es:
            messagebox.showerror("Fejl",f"Fejl pga.:{str(es)}"
                                 ,parent=self.root)


   def appscreen(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="startside.jpeg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      label1=Label(Frame_login,text="Hej og velkommen til din startside."
                   ,font=('times new roman',32),
                   fg="black",bg='orangered')
      label1.place(x=375,y=100)

      label2=Label(Frame_login,text="Tryk på MIN DATA for at visualisere din data"
                   ,font=('times new roman',32),
                   fg="black",bg='orangered')
      label2.place(x=375,y=160)

      btn2=Button(Frame_login,text="Log ud",command=self.loginform,cursor="hand2",
                  font=("times new roman",15),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn2.place(x=1000,y=10)

      btn3=Button(Frame_login,text="MIN DATA",command=self.dataform,cursor="hand2",
                  font=("times new roman",30),fg="white",bg="Blue",
                  bd=0,width=30,height=1)
      btn3.place(x=375,y=450)


   def Mscreen(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="medarb.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      label1=Label(Frame_login,text="Medarbejdere"
                   ,font=('times new roman',32),
                   fg="black",bg='orangered')
      label1.place(x=375,y=100)

      btn1=Button(Frame_login,text="Log ud",command=self.loginform,cursor="hand2",
                  font=("times new roman",15),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn1.place(x=1000,y=10)


      btn3=Button(Frame_login,text="Tryk her for at se data",command=self.loginform,cursor="hand2",
                  font=("times new roman",15),fg="white",bg="orangered",
                  bd=0,width=15,height=1)
      btn3.place(x=1000,y=10)

      filepath = '/Users/Victor/Python-code/GUI/samletdata.csv'

      File = open(filepath)
      Reader = csv.reader(File)
      Data = list(Reader)


      list_of_entries = []
      for x in list(range(0,len(Data))):
      	list_of_entries.append(Data[x][0])

      root = Tk()
      root.geometry('400x360')
      var = StringVar(value = list_of_entries)
      listbox1 = Listbox(root, listvariable = var)
      listbox1.grid(row=0 , column=0)

      def opdatere():
      	index = listbox1.curselection()[0]
      	Personlabel1.config(text=Data[index][0])
      	Adhdlabel1.config(text=Data[index][20])
      	Brugernavnlabel1.config(text=Data[index][21])
      	Emaillabel1.config(text=Data[index][22])

      	return None

      button1 = Button(root, text="Opdatere", command=opdatere)
      button1.grid(row=5, column=0)

      Personlabel = Label(root, text="Person:").grid(row=1, column=0)
      Brugernavnlabel = Label(root, text="Bruvernavn:").grid(row=1, column=0)
      Emaillabel = Label(root, text="Emailadresse:").grid(row=2, column=0)
      Adhdlabel = Label(root, text="Hjernestatus:").grid(row=3, column=0)

      Personlabel1 = Label(root, text="")
      Personlabel1.grid(row=1, column=0, sticky="w")
      Brugernavnlabel1 = Label(root, text="")
      Brugernavnlabel1.grid(row=1, column=1, sticky="w")
      Emaillabel1 = Label(root, text="")
      Emaillabel1.grid(row=2, column=1, sticky="w")
      Adhdlabel1 = Label(root, text="")
      Adhdlabel1.grid(row=3, column=1, sticky="w")


      root.mainloop()


   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)

   def loginclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)

root=Tk()
ob=Login(root)
root.mainloop()
