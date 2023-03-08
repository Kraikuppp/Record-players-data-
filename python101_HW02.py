from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog

GUI = Tk()
GUI.title('Football Maneager Database')
GUI.geometry('300x600')

label = Label(text='Players Database',font=("Arial Bold", 20)).place(x = 40,y = 50)

def mbappedata() :
    windows1 = Tk()
    windows1.title('Data of Kylian Mbappé')
    windows1.geometry('800x600')
    root = Frame(windows1)
    root.place(x=150,y=0)
    name1 = Label(root,text='Kylian Mbappé',font=("Arial Bold", 14))
    name1.pack()
    club = Label(windows1,text='Club : Paris Saint-Germain',font=("Arial", 10)).place(x=150,y=20)
    nation= Label(windows1,text='Nation : France',font=("Arial", 10)).place(x=150,y=40)
    age = Label(windows1,text='Age : 24',font=("Arial", 10)).place(x=150,y=60)
    pos = Label(windows1,text='Position : ST , RW , LW',font=("Arial", 10)).place(x=150,y=80)
    
    tec = Label(windows1,text='TECHNICAL',font=("Arial Bold", 10)).place(x=60,y=200)
    conner = Label(windows1,text='Corners                   13',font=("Arial", 10)).place(x=60,y=220)
    cross = Label(windows1,text='Crossing                  13',font=("Arial", 10)).place(x=60,y=240)
    drib = Label(windows1,text='Dribbling                  18',font=("Arial", 10)).place(x=60,y=260)
    finish = Label(windows1,text='Finishing                  17',font=("Arial", 10)).place(x=60,y=280)
    ft = Label(windows1,text='First Touch              18',font=("Arial", 10)).place(x=60,y=300)
    freekick = Label(windows1,text='Free Kick Taking      12',font=("Arial", 10)).place(x=60,y=300)
    head = Label(windows1,text='Heading                     7',font=("Arial", 10)).place(x=60,y=320)
    lshoot = Label(windows1,text='Long Shots               13',font=("Arial", 10)).place(x=60,y=340)
    lthrow = Label(windows1,text='Long Throws               4',font=("Arial", 10)).place(x=60,y=360)
    mark = Label(windows1,text='Marking                      4',font=("Arial", 10)).place(x=60,y=380)
    passing = Label(windows1,text='Passing                    15',font=("Arial", 10)).place(x=60,y=400)
    pen = Label(windows1,text='Penalty Taking          18',font=("Arial", 10)).place(x=60,y=420)
    tack = Label(windows1,text='Tackling                      4',font=("Arial", 10)).place(x=60,y=440)
    tech = Label(windows1,text='Technique                 17',font=("Arial", 10)).place(x=60,y=460)






    mental = Label(windows1,text='MENTAL',font=("Arial Bold", 10)).place(x=280,y=200)
    agg = Label(windows1,text='Aggression                   6',font=("Arial", 10)).place(x=280,y=220)
    anti = Label(windows1,text='Anticipation                 17',font=("Arial", 10)).place(x=280,y=240)
    brave = Label(windows1,text='Bravery                       12',font=("Arial", 10)).place(x=280,y=260)
    comp = Label(windows1,text='Composure                  18',font=("Arial", 10)).place(x=280,y=280)
    cons = Label(windows1,text='Concentration              14',font=("Arial", 10)).place(x=280,y=300)
    desci = Label(windows1,text='Decisions                    15',font=("Arial", 10)).place(x=280,y=320)
    determina = Label(windows1,text='Determination              15',font=("Arial", 10)).place(x=280,y=340)
    flair = Label(windows1,text='Flair                            18',font=("Arial", 10)).place(x=280,y=360)
    lead = Label(windows1,text='Leadership                  13',font=("Arial", 10)).place(x=280,y=380)
    offball = Label(windows1,text='Off the Ball                  18',font=("Arial", 10)).place(x=280,y=400)
    posi = Label(windows1,text='Positioning                   3',font=("Arial", 10)).place(x=280,y=420)
    teamw = Label(windows1,text='Teamwork                   10',font=("Arial", 10)).place(x=280,y=440)
    vision = Label(windows1,text='Vision                         15',font=("Arial", 10)).place(x=280,y=460)
    workrate = Label(windows1,text='Work Rate                  10',font=("Arial", 10)).place(x=280,y=480)
    
    physical = Label(windows1,text='PHYSICAL',font=("Arial Bold", 10)).place(x=500,y=200)
    acc = Label(windows1,text='Acceleration                20',font=("Arial", 10)).place(x=500,y=220)
    agi = Label(windows1,text='Agility                         16',font=("Arial", 10)).place(x=500,y=240)
    balance = Label(windows1,text='Balance                      15',font=("Arial", 10)).place(x=500,y=260)
    jump = Label(windows1,text='Jumping Reach             8',font=("Arial", 10)).place(x=500,y=280)
    fit = Label(windows1,text='Natural Fitness            15',font=("Arial", 10)).place(x=500,y=300)
    pace = Label(windows1,text='Pace                           20',font=("Arial", 10)).place(x=500,y=320)
    stamina = Label(windows1,text='Stamina                       14',font=("Arial", 10)).place(x=500,y=340)
    str = Label(windows1,text='Strength                       11',font=("Arial", 10)).place(x=500,y=360)

def haalanddata() :
    windows1 = Tk()
    windows1.title('Data of Erling Haaland')    
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def vinidata() :
    windows1 = Tk()
    windows1.title('Data of Vinicius Junior')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def judedata() :
    windows1 = Tk()
    windows1.title('Data of Jude Bellingham ')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def fodendata() :
    windows1 = Tk()
    windows1.title('Data of Phil Foden')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def pedridata() :
    windows1 = Tk()
    windows1.title('Data of Pedri')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)

def musialadata() :
    windows1 = Tk()
    windows1.title('Data of Jamal Musiala')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def sakadata() :
    windows1 = Tk()
    windows1.title('Data of Bukayo Saka')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
        
def valverdedata() :
    windows1 = Tk()
    windows1.title('Data of Federico Valverde')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)
    
def gavidata() :
    windows1 = Tk()
    windows1.title('Data of Gavi')
    windows1.geometry('600x600')
    root = Frame(windows1)
    root.place(x=0,y=150)

f1 = Frame(GUI)
f1.place(x=0,y=150)
b1 = Button(f1,text='Kylian Mbappé                France            €180.00m',command=mbappedata)
b1.pack(ipadx=40, ipady=5 )

f2 = Frame(GUI)
f2.place(x=0,y=180)
b2 = Button(f2,text='Erling Haaland                Norway            €170.00m',command=haalanddata)
b2.pack(ipadx=40, ipady=5 )

f3 = Frame(GUI)
f3.place(x=0,y=210)
b3 = Button(f3,text='Vinicius Junior                 Brazil                €120.00m',command=vinidata)
b3.pack(ipadx=40, ipady=5 )

f4 = Frame(GUI)
f4.place(x=0,y=240)
b4 = Button(f4,text='Jude Bellingham            England            €110.00m',command=judedata)
b4.pack(ipadx=40, ipady=5 )

f5 = Frame(GUI)
f5.place(x=0,y=270)
b5 = Button(f5,text='Phil Foden                      England            €110.00m',command=fodendata)
b5.pack(ipadx=40, ipady=5 )

f6 = Frame(GUI)
f6.place(x=0,y=300)
b6 = Button(f6,text='Pedri                                  Spain               €100.00m',command=pedridata)
b6.pack(ipadx=40, ipady=5 )

f7 = Frame(GUI)
f7.place(x=0,y=330)
b7 = Button(f7,text='Jamal Musiala               Germany           €100.00m',command=musialadata)
b7.pack(ipadx=40, ipady=5 )

f8 = Frame(GUI)
f8.place(x=0,y=360)
b8 = Button(f8,text='Bukayo Saka                  England             €100.00m',command=sakadata)
b8.pack(ipadx=40, ipady=5 )

f9 = Frame(GUI)
f9.place(x=0,y=390)
b9 = Button(f9,text='Federico Valverde         Uruguay            €100.00m',command=valverdedata)
b9.pack(ipadx=40, ipady=5 )

f10 = Frame(GUI)
f10.place(x=0,y=420)
b10 = Button(f10,text='Gavi                                  Spain                  €90.00m',command=gavidata)
b10.pack(ipadx=40, ipady=5 )

GUI.mainloop()