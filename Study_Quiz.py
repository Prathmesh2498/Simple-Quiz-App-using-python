# -*- coding: utf-8 -*-
"""
Simple Quiz Application
"""

import pandas as pd
import tkinter
from tkinter import Label, Radiobutton, StringVar, PhotoImage, Button, LEFT, BOTTOM, Frame
from tkinter import *

df = pd.read_csv('FILE_NAME_HERE')

df.drop(df.columns[[i for i in range(5,12)]], axis = 1, inplace = True)


curr = 0
def Next():
    global curr
    global lblQuestion,lblans,r1,r2,r3,r4
    lblans.destroy()
    curr = (curr + 1)%len(df['Question'])
    lblQuestion.config(text= df['Question'][curr])
    r1['text'] = df['Option a'][curr]
    r2['text'] = df['Option b'][curr]
    r3['text'] = df['Option c'][curr]
    r4['text'] = df['Option d'][curr]
       
    
def Prev():
    global curr
    global lblQuestion,lblans,r1,r2,r3,r4
    if curr-1>=0:
        curr-=1
    else:
        curr = len(df['Question']) - 1
    lblans.destroy()
    lblQuestion.config(text= df['Question'][curr])
    r1['text'] = df['Option a'][curr]
    r2['text'] = df['Option b'][curr]
    r3['text'] = df['Option c'][curr]
    r4['text'] = df['Option d'][curr]
        

flag = False
def selected():
    global radiovar,user_answer
    global lblQuestion,lblans,r1,r2,r3,r4, flag,btnPrev,btnNext
    global curr
    btnPrev.destroy()
    btnNext.destroy()
    
    m = df['Correct Answer'][curr]
    ansindex = m.lower()
    finalkey = "Option {}".format(ansindex)
    ans = df[finalkey][curr]
    print(ans)
    flag = True
    x = radiovar.get()
    radiovar.set("X")
    
    var = StringVar()
    final = "Wrong, correct option was {}\n{}".format(m, ans)
    var.set(final)
    
    if x == m:
        lblans = Label(
        root,
        text = "Correct",
        font = ("Consolas", 16),
        width = 300,
        justify = "left",
        wraplength = 400,
        background = "#ffffff",
        )
        
    else:
       lblans = Label(
        root,
        textvariable = var,
        font = ("Consolas", 16),
        width = 300,
        justify = "left",
        wraplength = 400,
        background = "#ffffff",
        )
       
    btnPrev = Button(
    root,
    text="Prev",
    border = 10,
    command = Prev,
    justify = "left"
    )
    btnPrev.pack()
    
    btnNext = Button(
    root,
    text="Next",
    border = 10,
    command = Next,
    justify = "right"
    )
    btnNext.pack()
    
    lblans.pack(pady=(10,30))
        
       
def startquiz():
    global lblQuestion,lblans,r1,r2,r3,r4, flag, btnPrev, btnNext, top
    lblQuestion = Label(
        root,
        text = df['Question'][0],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = StringVar()
    radiovar.set("X")
    
    r1 = Radiobutton(
        root,
        text = df['Option a'][0],
        font = ("Times", 12),
        value = 'A',
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = df['Option b'][0],
        font = ("Times", 12),
        value = 'B',
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = df['Option c'][0],
        font = ("Times", 12),
        value = 'C',
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = df['Option d'][0],
        font = ("Times", 12),
        value = 'D',
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)
    
    btnPrev = Button(
    root,
    text="Prev",
    border = 10,
    command = Prev,
    justify = "left",
    anchor = "sw"
    )
    btnPrev.pack()
    
    btnNext = Button(
    root,
    text="Next",
    border = 10,
    command = Next,
    justify = "right",
    anchor = "se"
    )
    btnNext.pack()

root = tkinter.Tk()
root.title("Final Sem Exam")
root.geometry("900x800")
root.config(background="#ffffff")
root.resizable(0,0)





img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(20,0))

labeltext = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,30))

lblans = Label(
        root,
        text = "Correct",
        font = ("Consolas", 16),
        width = 300,
        justify = "left",
        wraplength = 400,
        background = "#ffffff",
        )
labeltext.pack(pady=(0,30))




def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    btnStart.destroy()
    startquiz()
    

btnStart = Button(
    root,
    text="Start",
    border = 0,
    command = startIspressed,
)
btnStart.pack()


root.mainloop()
