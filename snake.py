from tkinter import * 
import random

#constants, global variables. sizes, colors, speed, etc.
GAME_WIDTH = 700
GAME_HEIGHT = 700

SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3

SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# game objects & their functions
class Snake:

    # TODO: PUT IMAGE OF SNAKE INSTEAD OF SQUARES

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0]) # coordinates for each body part at the start of the game. will appear on top left corner

        for x, y in self.coordinates: # making squares. x, y because its a nested list.
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR, tag= 'snake')
            self.squares.append(square) # append each square created to the squares list

class Food:

    # TODO: PUT PICTURE OF APPLE INSTEAD OF CIRCLE

    def __init__(self):
        # cordinates, food needs to be ramdomly put somewhere on the screen
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE # 10 possible spots on the x axis because 500/50 = 10
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE # 10 possible spots on the x axis because 500/50 = 10

        self.coordinates = [x,y]

        canvas.create_oval(x, y, (x + SPACE_SIZE), (y + SPACE_SIZE), fill= FOOD_COLOR, tags="food")


def next_turn(snake, food): # this function is called when the game begins

    x, y = snake.coordinates[0] # snake head

    if direction == 'up': 
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y]) # update coordinates

    # create new square and put it as the new head
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square) 

    # eat the apple if it hits food object
    if x == food.coordinates[0] and y == food.coordinates[1]: # if snake head and food coordinates are the same, they are overlapping. 
        global score

        score += 1 # increase score
        label.config(text = f'Score: {score}') # show it
        canvas.delete("food") # delete eaten food by using the name of the tag
        food = Food() # create new food object

    # need to delete last coordinate and square 
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # check for any collisions, if no collision: update to next turn
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food) 

def change_directions(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right': # precaution to avoid a 180 turn 
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left': # precaution to avoid a 180 turn 
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up': # precaution to avoid a 180 turn 
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down': # precaution to avoid a 180 turn 
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0] # unpack snake head

    # checks for collisions with wall
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    # check for collisions with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False
        

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, 
                       canvas.winfo_height()/2, 
                       font = ('helvetica', 35, 'bold'), 
                       text = 'GAME OVER',
                       fill = 'red')

    # start over button, calls start game method
    button = Button(canvas, 
                    text = "Try again",
                    font = ('helvetica', 25, 'bold'), 
                    foreground = 'white',
                    background = 'green',
                    command = start_game)
    canvas.create_window(canvas.winfo_width() / 2,
                         canvas.winfo_height() / 2 + 45,
                         window= button)



def start_game():
    global snake, food, direction, score

    canvas.delete(ALL)
    score = 0
    direction = 'down'

    label.config(text = f'Score: {score}')

    snake = Snake()
    food = Food()
    
    next_turn(snake, food)


# other variables
score = 0
direction = 'down'

# window stuff
window = Tk() # our little window
window.title("snake game")
window.resizable(False, False) #makes the window not resiable

label = Label(window, text=f'Score: {score}', font=('helvetica', 25, 'bold'))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# dimensions, centering on the screen
window.update()

SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

x = (SCREEN_WIDTH - GAME_WIDTH) // 2
y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2

window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")

window.bind('<Left>', lambda event: change_directions('left'))
window.bind('<Right>', lambda event: change_directions('right'))
window.bind('<Down>', lambda event: change_directions('down'))
window.bind('<Up>', lambda event: change_directions('up'))

# creating instances of our objects 
snake = Snake()
food = Food()

# TODO: ONLY CALL THIS FUNCTION WHEN USER CLICKS ON ARROW
next_turn(snake, food)

window.mainloop()