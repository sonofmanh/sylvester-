from tkinter import *
from tkinter import ttk
from tkinter import messagebox
dd = Tk()
dd.title('greater menu')
dd.geometry('570x450')
# dd.iconbitmap('fire.ico')

# menur = Menu(dd)
# dd.config(menu = menur)

# top = Menu(menur,tearoff=0)
# menur.add_cascade(label='File',menu = top)
# top.add_command(label='open')
# top.add_separator()
# top.add_command(label='quite')

# def pressedbtn(number):


player = 1

def pressedbtn(number):
    global player
    if number == 1 and player == 1:
        but1.config(text='X')
        player = 2
    elif number == 1 and player == 2:
        but1.config(text='O')
        player = 1
    elif number == 2 and player == 1:
        but2.config(text='X')
        player = 2
    elif number == 2 and player == 2:
        but2.config(text='O')
        player = 1
    elif number == 3 and player == 1:
        but3.config(text='X')
        player = 2
    elif number == 3 and player == 2:
        but3.config(text='O')
        player = 1
    elif number == 4 and player == 1:
        but4.config(text='X')
        player = 2
    elif number == 4 and player == 2:
        but4.config(text='O')
        player = 1
    elif number == 5 and player == 1:
        but5.config(text='X')
        player = 2
    elif number == 5 and player == 2:
        but5.config(text='O')
        player = 1
    elif number == 6 and player == 1:
        but6.config(text='X')
        player = 2
    elif number == 6 and player == 2:
        but6.config(text='O')
        player = 1
    elif number == 7 and player == 1:
        but7.config(text='X')
        player = 2
    elif number == 7 and player == 2:
        but7.config(text='O')
        player = 1
    elif number == 8 and player == 1:
        but8.config(text='X')
        player = 2
    elif number == 9 and player == 2:
        but9.config(text='O')
        player = 1
    elif number == 9 and player == 1:
        but9.config(text='X')
        player = 2

    checkwinning()

    
def checkwinning():
    if but1['text'] == 'O' and but2['text'] == 'O' and but3['text'] == 'O' or but4['text'] == 'O' and but5['text'] == 'O' and but6['text'] == 'O' or but7['text'] == 'O' and but8['text'] == 'O' and but9['text'] == 'O' or but1['text'] == 'O' and but5['text'] == 'O' and but9['text'] == 'O' or but3['text'] == 'O' and but5['text'] == 'O' and but7['text'] == 'O' or but1['text'] == 'O' and but4['text'] == 'O' and but7['text'] == 'O' or but2['text'] == 'O' and but5['text'] == 'O' and but8['text'] == 'O' or but3['text'] == 'O' and but6['text'] == 'O' and but9['text'] == 'O':print(messagebox.showinfo(title='winner',message='player 2 wins'))
    
    elif but1['text'] == 'X' and but2['text'] == 'X' and but3['text'] == 'X' or but4['text'] == 'X' and but5['text'] == 'X' and but6['text'] == 'X' or but7['text'] == 'X' and but8['text'] == 'X' and but9['text'] == 'X' or but1['text'] == 'X' and but5['text'] == 'X' and but9['text'] == 'X' or but3['text'] == 'X' and but5['text'] == 'X' and but7['text'] == 'X' or but1['text'] == 'X' and but4['text'] == 'X' and but7['text'] == 'X' or but2['text'] == 'X' and but5['text'] == 'X' and but8['text'] == 'X' or but3['text'] == 'X' and but6['text'] == 'X' and but9['text'] == 'X':print(messagebox.showinfo(title='winner',message='player 1 wins'))

but1 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(1))
but1.grid(row=0,column=0,ipadx=30,ipady=50)
but2 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(2))
but2.grid(row=0,column=1,ipadx=30,ipady=50)
but3 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(3))
but3.grid(row=0,column=2,ipadx=30,ipady=50)
but4 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(4))
but4.grid(row=1,column=0,ipadx=30,ipady=50)
but5 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(5))
but5.grid(row=1,column=1,ipadx=30,ipady=50)
but6 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(6))
but6.grid(row=1,column=2,ipadx=30,ipady=50)
but7 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(7))
but7.grid(row=2,column=0,ipadx=30,ipady=50)
but8 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(8))
but8.grid(row=2,column=1,ipadx=30,ipady=50)
but9 = ttk.Button(dd,text=' ',width=20,command= lambda: pressedbtn(9))
but9.grid(row=2,column=2,ipadx=30,ipady=50)

# ............................................................................................................
btnquite=Button(dd,text='quite',fg='blue',bd=1,bg='grey',width=38,font=('comic',15,'bold'),command=dd.quit)
btnquite.grid(row=3,columnspan=3,ipadx=50,ipady=5,pady=5)


dd.mainloop()