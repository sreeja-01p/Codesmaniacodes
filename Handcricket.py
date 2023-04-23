from tkinter import *
import random

class HandCricketGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Hand Cricket Game")
        self.window.geometry("300x450")

        self.player_score = 0
        self.computer_score = 0
        self.target_score = 0

        self.start_label = Label(self.window, text="\nHAND CRICKET\n", font=('MS Gothic',18,"bold"))
        self.start_label.pack()

        self.player_choice_label = Label(self.window, text="Enter your number between 1 and 6:\n",font=("Arial",10))
        self.player_choice_label.pack()

        self.player_choice_entry = Entry(self.window)
        self.player_choice_entry.pack()
        self.a=Label(self.window,text="\n")
        self.a.pack()
        self.play_button = Button(self.window, text="Play",bg="light blue",font=("Comic Sans MS",9), width=6, command=self.play_game)
        self.play_button.pack()

        self.score_label = Label(self.window, text="\nPlayer Score: {}  \nComputer Score: {}  \nTarget Score: {}".format(self.player_score,self.computer_score,self.target_score))
        self.score_label.pack()
        self.commands = Label(self.window, text="\nCOMMANDS:", fg="red", font=("Arial", 10, "bold"))
        self.commands.pack()

    def play_game(self):
        self.player_choice = int(self.player_choice_entry.get())
        self.computer_choice = random.randint(1,6)
        if self.player_choice == self.computer_choice:
            self.out = Label(self.window, text="You lose :(", font=("Arial", 10),fg="red")
            self.out.pack()
            self.play_button.config(state="disabled")
            self.player_choice_entry.config(state="disabled")
            return

        if self.computer_score == 0:
            self.comp_bat = Label(self.window, text="Computer's turn to bat!", font=("Arial", 10), fg="red")
            self.comp_bat.pack()
            self.computer_choice = random.randint(1, 6)
            self.computer_score += self.computer_choice
            self.score_label.config(text="\nPlayer Score: {} \nComputer Score: {} \nTarget Score: {}".format(self.player_score,self.computer_score,self.target_score))
        else:
            self.player_score += self.player_choice
            self.score_label.config(text="\nPlayer Score: {} \nComputer Score: {} \nTarget Score: {}".format(self.player_score,self.computer_score,self.target_score))
            if self.target_score == 0 and self.computer_score > 0:
                self.target_score = self.computer_score + 1
                self.bat = Label(self.window, text="Your turn to bat!", font=("Arial", 10),fg="red")
                self.bat.pack()
                self.computer_choice = 0
                self.computer_score = 0
                self.score_label.config(text="\nPlayer Score: {} \nComputer Score: {} \nTarget Score: {}".format(self.player_score,self.computer_score,self.target_score))
            elif self.player_score >= self.target_score:
                self.win=Label(self.window,text="You win!!!", font=("Arial",10),fg="red")
                self.win.pack()
                self.play_button.config(state="disabled")
                self.player_choice_entry.config(state="disabled")

root = Tk()
game = HandCricketGame(root)
root.mainloop()
