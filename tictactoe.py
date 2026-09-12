from tkinter import *
from tkinter import ttk
import random 

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:

        if player == players[0]: # check for player 1

            buttons[row][column]['text'] = player
            if check_winner() is False: # other players turn
                player = players[1]
                label.config(text=(players[1] + " turn"))

            # check for a winner
            if check_winner() is True:
                label.config(text= players[0] + " wins!")

            # check if it's a tie
            if check_winner() == 'Tie':
                label.config(text='Tie!')

        
        else: # otherwise its player 2
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            # check for a winner
            if check_winner() is True:
                label.config(text= players[1] + " wins!")

            # check if it's a tie
            if check_winner() == 'Tie':
                label.config(text='Tie!')


def check_winner():
    # check if player has 3 on a row, column or diagonal
    # check the text of each button on each row
    
    for row in range(3): # checking horizontal conditions
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(style='Win.TButton')
            buttons[row][1].config(style='Win.TButton')
            buttons[row][2].config(style='Win.TButton')
            return True

    for column in range(3): # checking vertical conditions
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column ]['text'] != '':
            buttons[0][column].config(style='Win.TButton') 
            buttons[1][column].config(style='Win.TButton')
            buttons[2][column].config(style='Win.TButton')
            return True

    # checking diagonal conditions from left
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(style='Win.TButton')
        buttons[1][1].config(style='Win.TButton')
        buttons[2][2].config(style='Win.TButton')
        return True

    # checking diagonal conditions from right
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(style='Win.TButton')
        buttons[1][1].config(style='Win.TButton')
        buttons[2][0].config(style='Win.TButton')
        return True

    # checking for empty spaces
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(style='Tie.TButton')

        return "Tie"

    else: # no winner and no tie
        return False 

def empty_spaces():
    #check for ties
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False # no space left
    return True
    

def new_game():
    # TODO: reset board
    pass

window = Tk()
window.title("tictactoe")

players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=f"{player} turn", font= ("helvetica", 30))
label.pack(side= "top")

reset_button = Button(text= 'Reset board', font = ('helvetica', 20), command = new_game)
reset_button.pack(side= 'top')

frame = Frame(window)
frame.pack()

style = ttk.Style() # use ttk for buttons because otherwise the coloring doesnt show
style.theme_use('clam')
style.configure('Win.TButton', background = 'green') # color for winning
style.configure('Tie.TButton', background = 'yellow') # color for tie
style.configure('TButton', font = ('helvetica', 30), padding = 20)
# the following removes the annoyinh hover/active state that comes with the clam theme
style.map('Win.TButton', background = [('active', 'green'),('!active', 'green')]) 
style.map('Tie.TButton', background = [('active', 'yellow'),('!active', 'yellow')])

for row in range(3):
    for column in range(3):
        buttons[row][column] = ttk.Button(frame, text= "", 
                                      width= 5, 
                                      command= lambda row=row, column=column : next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()