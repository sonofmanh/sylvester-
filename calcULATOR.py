from tkinter import *
bc = Tk()
bc.title('calculator')
bc.iconbitmap('fire.ico')
bomb = ''

def btn(number):
    global bomb
    bomb =bomb + str(number)
    eenter.set(bomb)

def klear():
    global bomb
    bomb = ''
    eenter.set('')

def equal():
    global bomb
    sumup = str(eval(bomb))
    eenter.set(sumup)

eenter = StringVar()
Entry(bc, font=('comic',15,'bold'),fg='green',bd='20',justify='right',textvariable=eenter).grid(row=0,columnspan=4,ipady=40)
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='7',command=lambda :btn('7')).grid(row=1,column='0')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='8',command=lambda :btn('8')).grid(row=1,column='1')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='9',command=lambda :btn('9')).grid(row=1,column='2')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='+',command=lambda :btn('+')).grid(row=1,column='3')

Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='4',command=lambda :btn('4')).grid(row=2,column='0')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='5',command=lambda :btn('5')).grid(row=2,column='1')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='6',command=lambda :btn('6')).grid(row=2,column='2')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='-',command=lambda :btn('-')).grid(row=2,column='3')

Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='1',command=lambda :btn('1')).grid(row=3,column='0')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='2',command=lambda :btn('2')).grid(row=3,column='1')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='3',command=lambda :btn('3')).grid(row=3,column='2')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='/',command=lambda :btn('//')).grid(row=3,column='3')

Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='0',command=lambda :btn('0')).grid(row=4,column='0')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='cls',command= klear).grid(row=4,column='1')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='=',command=equal).grid(row=4,column='2')
Button(bc, font=('comic',15,'bold'),fg='white',bg='grey',width=5,height=3,text='*',command=lambda :btn('*')).grid(row=4,column='3')

bc.mainloop()