from tkinter import*
from tkinter import messagebox

gu = Tk()
gu.title('new stuff')
gu.geometry('400x500+40+30')
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
def shutdown():
    import subprocess
    subprocess.call(['shutdown','-f','-s','-t','600'])
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
def showus():
    print(messagebox.showinfo(title='about this page',message='this is a little project showing how an application works in python,\n do not click me will shutdown your computer\n and restart will do as described'))
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
def shutdown():
    import subprocess
    subprocess.call(['shutdown','-f','-r','-t','600'])

def cancel():
    import subprocess
    try:
        subprocess.call(['shutdown','-a'])
    except:
        print(messagebox.showinfo('no command to abbort'))

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

fact = Frame(master=gu,width=400,height=500,bg='green')
fact.pack()
# /////////////////////////////////////////////////////////////////////////////////////////////
bt=Button(master=fact,text='click  me',command=showus,width=20,height=1,bg='skyblue',font=('comic',15,'bold'))
bt.place(relx=0.200,rely=0.300)
# /////////////////////////////////////////////////////////////////////////////////////////////
bt2=Button(master=fact,text='do not click  me',width=20,height=1,bg='skyblue',font=('comic',15,'bold'),command=shutdown)
bt2.place(relx=0.200,rely=0.400)
# //////////////////////////////////////////////////////////////////////////////////////////////
bt3=Button(master=fact,text='restart',width=20,height=1,bg='skyblue',font=('comic',15,'bold'))
bt3.place(relx=0.200,rely=0.500)
# //////////////////////////////////////////////////////////////////////////////////////////////
btn4=Label(master=fact,text='if you want to control your computer',bg='green',font=('comic',14,'bold')).place(relx=0.100,rely=0.200)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
bt5=Button(master=fact,text='Abort shutdown protocol',width=20,height=1,bg='skyblue',font=('comic',15,'bold'),command=cancel)
bt5.place(relx=0.200,rely=0.600)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
bt6=Button(master=fact,text='Quit',width=20,height=1,bg='skyblue',font=('comic',15,'bold'),command=gu.quit)
bt6.place(relx=0.200,rely=0.700)

gu.mainloop()
