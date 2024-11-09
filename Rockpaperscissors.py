from tkinter import *
import random

# Screen configuration
main = Tk()
main.geometry("1000x500")
main.config(bg = "white")
main.title("Rock Paper Scissors")

# List that the computer will choose
options = [("Rock",0),("Paper",1) ,("Scissors",2) ]


# Handling the scores of both sides
computerscore = 0
playerscore = 0


# Title
title = Label(main, text = "Choose Rock Paper or Scissors!", font=("times new roman",18, "bold"))
title.grid(row=1,column=1,columnspan=3,padx=200)


# Extra text that will say who won the previous round
extraInfo = Label(main, text = "Start by picking an option", fg="green",font=("times new roman",14))
extraInfo.grid(row=2,column=2,pady = 20)



# if player picks rock
# for all 3 picks of player, it uses random to choose a random choice taht the computer chooses
# Then it edits the "playerChoiceLabel" and "computerChoiceLabel" to 

def rockPick():

    playerChoiceLabel.config(text=" Rock")
    computerPicked = random.choice(options)
    computerChoiceLabel.config(text=computerPicked[0])

    if computerPicked[1] == 0:
        Tie()
    if computerPicked[1] == 1:
        computerWins()
    if computerPicked[1] == 2:
        playerWins()

# If player picks paper

def paperPick():

    playerChoiceLabel.config(text=" Paper")
    computerPicked = random.choice(options)
    computerChoiceLabel.config(text=computerPicked[0])



    if computerPicked[1] == 0:
        playerWins()
    if computerPicked[1] == 1:
        Tie()
    if computerPicked[1] == 2:
        computerWins()

# If player picks scissors

def  scissorspick():

    playerChoiceLabel.config(text=" Scisssors")
    computerPicked = random.choice(options)
    computerChoiceLabel.config(text=computerPicked[0])

    if computerPicked[1] == 0:
        computerWins()
    if computerPicked[1] == 1:
        playerWins()
    if computerPicked[1] == 2:
        Tie()

# Creating the buttons for the 3 options of the player (rock paper and scissors)

rockButton = Button(main, text= "Rock", bg = "white", font=("times new roman",14), command = rockPick())
paperButton = Button(main, text ="Paper", bg = "white", font=("times new roman",14), command = paperPick())
scissorsButton = Button(main, text= "Scissors", bg = "white", font=("times new roman",14), command = scissorspick())


# Placing the buttons on the screen
rockButton.grid(row=3,column=1)
paperButton.grid(row=3,column=2)
scissorsButton.grid(row=3,column=3)


# Displaying score and computer and player choices on screen

#what player chose
playerChoiceLabel = Label(main, text= f"You chose: -- ", bg = "white", font=("times new roman",14))
playerChoiceLabel.grid(row=4,column=1)

#what computer chose
computerChoiceLabel = Label(main, text= f"Computer chose: --", bg="white", font=("times new roman",14))
computerChoiceLabel.grid(row=5,column=1)

# Functions for each of the outcomes of the game (the computer wins, the player wins, or it is a tie)
def computerWins():
    extraInfo.config(text="Computer Won")
    computerscore = computerscore + 1

def playerWins():
    extraInfo.config(text="Player Won")
    playerscore = playerscore + 1


def Tie():
    extraInfo.config(text="Tie")


main.mainloop()
