from turtle import Screen
from clickableturtle import ClickableTurtle
from keyboardturtle import KeyboardTurtle
from wall import Wall

# set up instance of the screen
window = Screen()

#window.addshape(image)
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

#list setup
wall_list = []


#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)

w1 = Wall(100,0,1,3)
wall_list.append(w1)
wall_list.appendwall(0, 100, 5, 1)

# This is needed at the end to listen for inputs
window.listen()
window.mainloop()


