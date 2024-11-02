from tkinter import *
import random

main = Tk()

main.geometry("1000x500")

main.config(bg = "white")

main.title("Rock Paper Scissors")

options = [("Rock",0),("Paper",1) ,("Scissors",2) ]

playerChoice = "--"

computerscore = 0
playerscore = 0

infoText = "Start by picking an option"

title = Label(main, text = "Choose Rock Paper or Scissors!", font=("times new roman",18, "bold"))
title.grid(row=1,column=1,columnspan=3,padx=200)

extraInfo = Label(main, text = infoText, fg="green",font=("times new roman",14))
extraInfo.grid(row=2,column=2,pady = 20)

def computerChoice():
    random.choice(options)

def rockPick():
    playerChoice = ["rock", 0]
    computerChoice()

def paperPick():
    playerChoice = ["paper", 1] 
    computerChoice()


def  scissorspick():
    playerChoice = ["scissors", 2]
    computerChoice()


rockButton = Button(main, text= "Rock", bg = "white", font=("times new roman",14), command = rockPick())
paperButton = Button(main, text ="Paper", bg = "white", font=("times new roman",14), command = paperPick())
scissorsButton = Button(main, text= "Scissors", bg = "white", font=("times new roman",14), command = scissorspick())

rockButton.grid(row=3,column=1)
paperButton.grid(row=3,column=2)
scissorsButton.grid(row=3,column=3)

# Displaying score and computer and player choices on screen
#what player chpse
playerChoiceLabel = Label(main, text= f"You chose: -- ", bg = "white", font=("times new roman",14))
playerChoiceLabel.grid(row=4,column=1)
#what computer chose
computerChoiceLabel = Label(main, text= f"Computer chose:  --", bg="white", font=("times new roman",14))
computerChoiceLabel.grid(row=5,column=1)


# Create a win for each scenario (computer, player, tie)
# Within each function, change the labels of the player chose and what computer chose, and who gains a point
# Create nested if loops. Check if player rock, then if 
def computerWins():
    extraInfo.config(text="Computer Won")
    computerscore+=1

def playerWins():
    extraInfo.config(text="Player Won")
    playerscore+=1


def Tie():
    extraInfo.config(text="Tie")
    


main.mainloop()
