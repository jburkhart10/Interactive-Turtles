from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle


# set up instance of the screen
window = Screen()
window.setup(800, 500)

# set up clickable instance
button = ClickableTurtle()

#set up players
player_1 = KeyboardTurtle(window)


player_1.goto(-350,200)

# set target of other player(our collison check) to the opposite player



# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment