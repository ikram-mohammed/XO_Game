import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness
import random
import time 

set_dpi_awareness()
root = tk.Tk()


    

winframe = ttk.Entry(root)
winframe.pack()


Win = ttk.Label(winframe, text='', borderwidth=0)
Win.config(font=('Courier', 24))#
Win.config(foreground='red')
Win.pack(side='top')
Wintwo = ttk.Label(winframe, text='')
Wintwo.pack()

####################################################

def is_draw(a):
    for i in range(3):
        for j in range(3):
            if a[i][j] == '-':
                return False
    return True

def is_winner(a):
    global Win
    msg = ''
    if a[0][0] == a[1][1] and a[1][1] == a[2][2] and a[0][0] != '-':
        msg = f'{a[0][0]}' 
    if a[0][2] == a[1][1] and a[1][1] == a[2][0] and a[2][0] != '-':
        msg = f'{a[0][2]}' 
    if a[0][0] == a[0][1] and a[0][1] == a[0][2] and a[0][0] != '-':
        msg = f'{a[0][0]}' 
    if a[1][0] == a[1][1] and a[1][1] == a[1][2] and a[1][0] != '-':
        msg = f'{a[1][0]}'
    if a[2][0] == a[2][1] and a[2][1] == a[2][2] and a[2][0] != '-':
        msg = f'{a[2][0]}'
    if a[0][0] == a[1][0] and a[1][0] == a[2][0] and a[2][0] != '-':
        msg = f'{a[0][0]}'
    if a[0][1] == a[1][1] and a[1][1] == a[2][1] and a[0][1] != '-':
        msg = f'{a[0][1]}' 
    if a[0][2] == a[1][2] and a[1][2] == a[2][2] and a[0][2] != '-':
        msg = f'{a[0][2]}' 
 
    if len(msg)>0 and msg[0] == 'X':
        Win.config(text=msg, foreground='Red')
        Wintwo.config(text='is the winner')
    if len(msg)>0 and msg[0] == 'O':
        Win.config(text=msg, foreground='blue')
        Wintwo.config(text='is the winner')
        Wintwo.pack(side='top')
    if msg == '':
        return False
    else:
        return True
winframe.pack()


a = [['-','-','-'],['-','-','-'],['-','-','-']]
blank_image = Image.open('xo_blanck.png').resize((186, 186))
blank_photo = ImageTk.PhotoImage(blank_image)

x_image = Image.open('xo_x.png').resize((186, 186))
x_photo = ImageTk.PhotoImage(x_image)

o_image = Image.open('xo_o.png').resize((186, 186))
o_photo = ImageTk.PhotoImage(o_image)

buttons = [[None,None,None],[None,None,None],[None,None,None]]

rows = [None,None,None]
for i in range(3):
    rows[i] = ttk.Frame(root)
    rows[i].pack(side='top')







root.geometry('699x699')
root.resizable(False,False)
root.title('Widget examples')



def Click(r, c):
    def button_click():
        global a
        global blank_photo
        global x_photo
        global o_photo
        global buttons

        if a[r][c] != '-':
            print('Wrong choice!!')
            return
        
        if is_winner(a):
            print('Winner')
            return

        if is_draw(a):
            global Win
            Win.config(text='Draw', foreground='green')
            print('Draw!')
            return

        print(f'{r},{c}')
        a[r][c] = 'X'

        
        global buttons
        buttons[r][c].config(image = x_photo)
        if is_winner(a):
            print('Winner')
            return

        if is_draw(a):
            Win.config(text='Draw', foreground='green')
            print('Draw!')
            return

            
        # computer is playing
        empty_squares = []
        for i in range(3):
            for j in range(3):
                if a[i][j] == '-':
                    empty_squares = empty_squares + [(i,j)]

        row, column = empty_squares[random.randint(0, len(empty_squares) - 1)]
        a[row][column] = 'O'
        buttons[row][column].config(image = o_photo)

        if is_winner(a):
            print('Winner')
            return
            

        if is_draw(a):
            print('Draw!')
            return
            

    return button_click

#####################################################################################################
for i in range(3):
    for j in range(3):
        buttons[i][j] = ttk.Button(rows[i], image = blank_photo, padding = 5, command=Click(i,j))
        buttons[i][j].pack(side='left')

def restart():
    global buttons
    global Wintwo
    global a
    global blank_photo
    global Win
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(image = blank_photo)
    a = [['-','-','-'],['-','-','-'],['-','-','-']]
    Win.config(text='')
    Wintwo.config(text='')

def quit():
    exit()


restart_button = ttk.Button(root, text='restart', command=restart)
restart_button.pack()

quitbut = ttk.Button(root, text='quit', command=quit)
quitbut.pack()



root.mainloop()
