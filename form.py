from tkinter import *
# from PIL import Image,ImageTk
from tkinter import ttk as gf
from tkinter import messagebox
aa = Tk()
aa.title('form validation')
aa.geometry('500x600+400+100')
aa.iconbitmap('fire.ico')


def trigger():
    firstn=haha.get()
    lastn = hehe.get()
    midn = coco.get()
    Gendere = bbh.get()
    spin = tri.get()
    spin2 = gin.get()
    hemail = ehm.get()
    pass1 = pssw.get()
    pass2 = pssw2.get()
    authenticate = pssw.get()
    authenticate2 = pssw2.get()

    if firstn == '' or lastn == '' or midn == '' or Gendere == '' or hemail == '' or '@gmail.com'not in hemail or '@yahoomail.com' not in hemail or '@hotmail.com' not in hemail or pass1 == ''or len(pass1) < 6 or pass2 == '' or len(pass2) < 6 or pass2 != pass1 :
        # FIRST NAME VALIDATION
        if firstn == '':print(messagebox.showinfo(title='error',message='first name cannot be left blank'))
        # LAST NAME VALIDATION
        elif lastn == '':print(messagebox.showinfo(title='error',message='last name cannot be left blank'))
        # MID-NAM VALIDATION
        elif midn == '':print(messagebox.showinfo(title='error',message='please enter the middle name'))
        # GENDER VALIDATION
        elif Gendere == '':print(messagebox.showinfo(title='error',message='choose Gender'))
        # EMAIL VALIDATION  INCOMPLETE AND COMPLEX
        elif hemail == '' or len(hemail) <= 5:print(messagebox.showinfo('error','email must be greater than 5 characters'))
        elif len(hemail)>5 and '@gmail.com'not in hemail or len(hemail)>5 and '@hotmail.com' not in hemail or len(hemail)>5 and '@yahoomail.com'not in hemail:print(messagebox.showinfo('invalid','not a valid mail address'))
        # PASSWORD VALIDATION
        elif authenticate == '':print(messagebox.showinfo(title='password',message='please enter password'))
        #  CONFIRM PASSWORD LENGHT
        elif len(authenticate) <= 5:print(messagebox.showinfo(title='to short',message='password must be longer than 6 string characters'))
        # CONFIRM PASSWORD MUST BE SAME WITH PASSWORD
        elif authenticate2 != authenticate:print(messagebox.showinfo(title='no match',message='confirrm password must be exactly the same with password '))
    else:
        print(messagebox.showinfo(title='success',message='you have registered succesfully'))

           

fram = LabelFrame(master=aa,width=500,height=600,bg='#40ff00',text='form',fg='white',pady=80,padx=10,font=('comic',30,'bold'))
fram.pack()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

labe = Label(master=fram,text='First Name',font=('comic',10,'bold'),bg='#40ff00',)                          
labe.place(x = 80,y=20)

haha=StringVar()                      
ent = Entry(master=fram,width=30,font=('comic',11,'bold'),relief=SUNKEN,textvariable=haha)                                    
ent.place(x = 160,y = 20)                                                                                 

labe1 = Label(master=fram,text='Last Name',font=('comic',10,'bold'),bg='#40ff00')
labe1.place(x = 80,y=60)

hehe=StringVar()
ent1 = Entry(master=fram,width=30,font=('comic',11,'bold'),relief=SUNKEN,textvariable=hehe)
ent1.place(x = 160,y = 60)

labe1 = Label(master=fram,text='Middle Name',font=('comic',10,'bold'),bg='#40ff00')
labe1.place(x = 70,y=100)

coco=StringVar()
ent2 = Entry(master=fram,width=30,font=('comic',11,'bold'),relief=SUNKEN,textvariable=coco)
ent2.place(x = 160,y = 100)

dob = Label(master=fram,text='Date o\' birth',font=('comic',10,'bold'),bg='#40ff00')
dob.place(x = 70,y=140)

tri = IntVar()
ent3 = Spinbox(master=fram,from_= 1,to = 31,textvariable = tri)
ent3.place(x = 160,y = 140)
ent3.config(width = 4,font=('ariel',10,'bold'))

kia=gf.Combobox(master=fram)
kia.place(x = 210,y = 140)
kia['value'] = ('january','february','march','April','may','june','july','August','September','October','November','December')
kia.current(0)

gin = IntVar()
ent4 = Spinbox(master=fram,from_= 1880,to = 2020,textvariable = gin)
ent4.place(x = 360,y = 140)
ent4.config(width = 4,font=('ariel',10,'bold'))

gen = Label(master=fram,text='Gender',font=('comic',10,'bold'),bg='#40ff00')
gen.place(x = 85,y=180)

bbh=StringVar()
rad = Radiobutton(master=fram,text='Male',value='male',variable=bbh,bg='#40ff00',activebackground='#40ff00')
rad.place(x = 160,y=180)

rad1 = Radiobutton(master=fram,text='Female',value='female',variable=bbh,bg='#40ff00',activebackground='#40ff00')
rad1.place(x = 220,y=180)

emai = Label(master=fram,text='Email',font=('comic',10,'bold'),bg='#40ff00')
emai.place(x=85,y=220)

ehm = StringVar()
emtx = Entry(master=fram,width=30,relief=SUNKEN,font=('comic',11,'bold'),textvariable=ehm)
emtx.place(x=160,y=220)


passs = Label(master=fram,text='Password',font=('comic',10,'bold'),bg='#40ff00')
passs.place(x=70,y=260)

pssw = StringVar()
psstx = Entry(master=fram,width=30,relief=SUNKEN,font=('comic',11,'bold'),textvariable=pssw,show = "x")
psstx.place(x=160,y=260)

passs2 = Label(master=fram,text='confirm Password',font=('comic',10,'bold'),bg='#40ff00')
passs2.place(x=40,y=300)

pssw2 = StringVar()
psstx2 = Entry(master=fram,width=30,relief=SUNKEN,font=('comic',11,'bold'),textvariable = pssw2,show = "x")
psstx2.place(x=160,y=300)

log = Button(master=fram,text='sign up',fg='black',bg='grey',relief=SUNKEN,width=8,height=1,activebackground='white',activeforeground='red',font=('ariel',11,'bold'),cursor='hand2',command = trigger)
log.place(x=340,y=340)


log = Button(master=fram,text='cancel',fg='black',bg='grey',relief=SUNKEN,width=8,height=1,activebackground='white',activeforeground='red',font=('ariel',11,'bold'),cursor='hand2',command=aa.quit)
log.place(x=160,y=340)

aa.mainloop()