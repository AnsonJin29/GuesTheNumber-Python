#make any changes final touches
import random
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
window=ThemedTk(theme='equilux')
window.configure(themebg='equilux')
window.geometry('500x400')
window.title('Guess the Number')
window.resizable(False, False)
rb=StringVar()
window.iconbitmap("gn-logo_590037-185.ico")#My Logo Blue and Black.ico    Praga-Emblem steel.ico
counter=1
number=0
answer=''
empty=''
points=0
counter2=0
trys=0

diceimage=PhotoImage(file='dice.png')
upperarrow=PhotoImage(file='uparrow.png')
lowerarrow=PhotoImage(file='downarrow.png')
tick=PhotoImage(file='tick.png')
diceimage=diceimage.subsample(14)
upperarrow=upperarrow.subsample(3)
lowerarrow=lowerarrow.subsample(3)
tick=tick.subsample(14)

def randomise():
    global counter
    global number
    global counter2
    global trys
    image.configure(image=diceimage)
    hiddentext.configure(text='take a guess')
    hiddentext.place(x=330, y=360)
    counter2=0
    trys=0
    tryslabel.configure(text='Tries: ' + str(trys))
    if counter==1:
        startbutton.configure(text='Play again')
        revealbutton.place(x=300, y=270, height=80, width=170)
    counter=counter+1
    if rb.get()=='Choice1':
        number=random.randint(0,50)
    elif rb.get()=='Choice2':
        number=random.randint(0,100)
    elif rb.get()=='Choice3':
        number=random.randint(0,100000)
    entry.config(state="enable")
    entry.delete(0, 'end')

def reveal():
    global number
    global points
    global counter2
    startbutton.configure(text='Start again')
    hiddentext.configure(text='The number was:'+str(number))
    hiddentext.place(x=280, y=360)
    entry.delete(0, 'end')
    entry.config(state="disabled")
    if counter2==0:
        points = points - 1
        pointlabel.configure(text='Points: ' + str(points))

def check(event):
    global answer
    global number
    global points
    global counter2
    global trys
    answer=entry.get()
    if answer!='':
        trys = trys + 1
    tryslabel.configure(text='Tries: ' + str(trys))
    if trys==1:
        tryslabel.configure(foreground='lawngreen')
    elif trys<=4:
        tryslabel.configure(foreground='yellowgreen')
    elif trys<=7:
        tryslabel.configure(foreground='yellow')
    elif trys<=10:
        tryslabel.configure(foreground='orange')
    elif trys<=13:
        tryslabel.configure(foreground='firebrick2')
    elif trys<=16:
        tryslabel.configure(foreground='red')
    if answer==empty:
        image.configure(text='Type something')
    else:
        answer=int(answer)
        if answer==number:
            image.configure(image=tick)
            entry.delete(0, 'end')
            entry.config(state="disabled")
            points=points+1
            counter2=1
            pointlabel.configure(text='Points: '+str(points))
            hiddentext.configure(text='The number was:' + str(number))
            hiddentext.place(x=280, y=360)
        else:
            entry.delete(0,'end')
            if answer>number:
                image.configure(image=lowerarrow)
            elif answer<number:
                image.configure(image=upperarrow)

title=ttk.Label(window,text='Guess the Number',font=('Agency FB Bold',35))
title.place(x=100,y=0)

rad1=ttk.Radiobutton(window,text='Easy(0-50)',value='Choice1',variable=rb)
rad1.place(x=40,y=75)

rad2=ttk.Radiobutton(window,text='Hard(0-100)',value='Choice2',variable=rb)
rad2.place(x=190,y=75)

rad3=ttk.Radiobutton(window,text='Xtreme(0-100000)',value='Choice3',variable=rb)
rad3.place(x=340,y=75)
rb.set('Choice3')

description=ttk.Label(window,text='   Click the Start button to begin, then you have to try and guess it. An\n      arrow will show if your guess is too high or too low. Good luck',font=('Agency FB',16))
description.place(x=40,y=130)

image=ttk.Label(window,image=diceimage)
image.place(x=70,y=200)

hiddentext=ttk.Label(window,text='take a guess',font=('Unispace-Bold',13))
hiddentext.place(x=330,y=360)

startbutton=ttk.Button(window,text='Start',command=randomise)
startbutton.place(x=300,y=190,height=80,width=170)

revealbutton=ttk.Button(window,text='Reveal',command=reveal)

credit=ttk.Label(window,text='Made by Anson',font=('Tahoma Bold',10))
credit.place(x=280,y=47)

entry=ttk.Entry(window,state='disable')
entry.place(x=50,y=360,width=200)

pointlabel=ttk.Label(window,text='Points: '+str(points),font=('Unispace-Bold',11))
pointlabel.place(x=180,y=190)

tryslabel=ttk.Label(window,text='Tries: '+str(trys),font=('Unispace-Bold',11))#,foreground='lawngreen')
tryslabel.place(x=30,y=190)

window.bind('<Return>',check)

window.mainloop()