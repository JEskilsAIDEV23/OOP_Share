from numpy import random
import numpy as np

class Dice:

    @classmethod
    def set_Dice_type(cls, n = 6): #Skapar tärning utifrån antal möjliga utfall n
         cls.n = n
         cls.w = [(1/n) for i in range(1, n+1)] #sannolikheter för utfall
         cls.d = np.array([i for i in range(1, n+1)], dtype = int) #möjliga utfall

    @classmethod
    def get_Dice_type(cls): #Returnerar information om typ, sannolikhet och möjliga utfall
         return cls.n, cls.w, cls.d  
    
    @classmethod 
    def set_Dice_w(cls, w): #Medger manipulation av tärningens utfall som styrs av vektorn w
        cls.w = w

    def __init__(self):
        n, w, d = Dice.get_Dice_type() #initierar tärning utifrån n möjliga utfall
        self.n = n
        self.w = w
        self.d = d

class Dn1(Dice): #skapar ett kast med tärningen n som har n utfall

    def __init__(self):
        super().__init__()
        self.d3d = random.choice(self.d, size = 1, p= self.w)
        self.dice_1 = int(self.d3d[0])
        self.pd1 = str(self.dice_1)+'.png'   

def roll_d(): #metod för att returnera utfallet av tärning n

    d3d = Dn1()
    dice_1 = int(d3d.dice_1)
    pd1 = str(d3d.pd1)
    return dice_1, pd1

def decode_card(): #Spelkorts tärning n=52 utfall

    Dice.set_Dice_type(52)
    dice_1, pd1 = roll_d()

    if dice_1 >= 1 and dice_1 <= 13:
        color = 'Hearts'
    if dice_1 >= 14 and dice_1 <= 26:
        dice_1 = dice_1 - 13
        color = 'Clubs'
    if dice_1 >= 27 and dice_1 <= 39:
        dice_1 = dice_1 - 26
        color = 'Diamonds'
    if dice_1 >= 40 and dice_1 <= 52:
        dice_1 = dice_1 - 39
        color = 'Spades'
    if dice_1 >1 and dice_1 <=10:
        pd1 = str(dice_1)+'.png'
    if dice_1 == 1:
        pd1 = 'A.png'
    if dice_1 == 11:
        pd1 = 'J.png'
    if dice_1 == 12:
        pd1 = 'Q.png'
    if dice_1 == 13:
        pd1 = 'K.png'   

    card_color_value = color+' '+pd1
    return card_color_value
               
def dice_color(): #spelkortsfärger som tärning med n=4 utfall

    Dice.set_Dice_type(4)
    dice_1, pd1 = roll_d()

    if dice_1 == 1:
        color = 'Hearts'
    if dice_1 == 2:
        color = 'Clubs'
    if dice_1 == 3:
        color = 'Diamonds'
    if dice_1 == 4:
        color = 'Spades'

    return color

def dice_13(): #spelkorts värden för en tärning med n = 13 utfall

    Dice.set_Dice_type(13)
    dice_1, pd1 = roll_d()

    if dice_1 >1 and dice_1 <=10:
        pd1 = str(dice_1)+'.png'
    if dice_1 == 1:
        pd1 = 'A.png'
    if dice_1 == 11:
        pd1 = 'J.png'
    if dice_1 == 12:
        pd1 = 'Q.png'
    if dice_1 == 13:
        pd1 = 'K.png'

    return dice_1, pd1

def arb_dice(n): #metod för att skapa en arbitär tärning med n utfall
    Dice.set_Dice_type(n)
    dice_1, pd1 = roll_d()
    return dice_1

def arb_dice_check(n): #metod för att skapa en arbitär tärning med n utfall samt visar dess uppbyggnad
    Dice.set_Dice_type(n)
    d = Dn1()
    return print(f'Class info {d.get_Dice_type()}'), print(f'\nObject, Arbitary Dice Rolled: {d.dice_1}\n')

def p_calc(n): #metod för att skapa viktad tärning utifrån n utfall

    #w = [(1/n) for i in range(1, n+1)] #sannolikheter för utfall
    #d = np.array([i for i in range(1, n+1)], dtype = int) #möjliga utfall
    mt = np.ones([n], dtype = int)
    mn = np.ones([n], dtype = int)
    mt = mt+(n-1)
    mn = mn[:]*mt[:]*n

    for i in range(len(mt)):
        mt[i] = mt[i] - (n-i)+1+i        
    wm = mt[:]/mn[:]
    #print(mt,mn)
    return wm

def p_calc2(n): #metod för att skapa viktad tärning utifrån n > 2 utfall

    if n <= 2:
        exit()

    #w = [(1/n) for i in range(1, n+1)] #sannolikheter för utfall
    #d = np.array([i for i in range(1, n+1)], dtype = int) #möjliga utfall
    mt = np.ones([n], dtype = int)
    mn = np.ones([n], dtype = int)
    mt = mt+(n-1)
    mn = mn[:]*mt[:]*n
    mt = mt*10
    mn = mn*10

    if n%2 == 0:
        fh = int(n/2-1)
        mt[0:fh] = mt[0:fh]/2
        mt[fh+2::] = mt[fh+2::]+mt[0:fh]

    if n%2 != 0:
        fh = int((n-1)/2)
        mt[0:fh] = mt[0:fh]/2
        mt[fh+1::] = mt[fh+1::]+mt[0:fh]

    wm = mt[:]/mn[:]
    #print(mt,mn)
    return wm
