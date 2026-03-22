from tkinter import *
import random

def next_trun(rows,columns):# to decide whose turn it is tho
    global player
    if buttons[rows][columns]['text']==""and check_winner() is False:
        if player ==players[0]:
            buttons[rows][columns]['text']=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+'turn'))
            elif check_winner() is True:
                label.config(text=(players[0]+'Wins'))    
            elif check_winner()=='tie':
                label.config(text=('Wins'))   
        else:
            buttons[rows][columns]['text']=player
            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0]+'turn'))
            elif check_winner() is True:
                label.config(text=(players[1]+'Wins'))    
            elif check_winner()=='tie':
                label.config(text=('Wins'))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            
            return True 
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False
def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces -=1
    if spaces==0:
        return False
    else:
        return TRUE        

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

#GUI setup
window =Tk()
players=["x","o"] #our players
player= random.choice(players)
buttons=    [["o","o","o"],# 2D list for the button 
            ["o","o","o"],
            ["o","o","o"]]
label=Label(window,text=player+"Turn",font=('consolas',40))# to know whose turn it is right not
window.title("Tic-Tac-Toe")
label.pack(side='top')
reset_label=Button(window,text="restart",font=('consolas',20),command=new_game)
reset_label.pack(side='top')
frame=Frame(window)
frame.pack()
for rows in range(3):
    for columns in range(3):
        buttons[rows][columns] =Button(frame,text="",font=('consolas',30),width=5,height=2,
                                    command=lambda r=rows,c=columns: next_trun(r,c))
        buttons[rows][columns].grid(row=rows, column=columns)

window.mainloop()