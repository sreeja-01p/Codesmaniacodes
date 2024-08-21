from tkinter import *
from string import ascii_uppercase
import random
from tkinter import messagebox

window=Tk()
window.title("HANGMAN - FOOD ITEMS")

word_list = ["BURGER", "PIZZA", "PASTA", "RISOTTO", "RICE", "SUSHI", "SALMON", "SUNDAE",
             "CHOCOLATE", "CAKE", "SOUP", "CHICKEN", "SALAD", "ROTI", "CHURROS", "MANCHURIA", "EGGS", "DHOKLA",
             "NOODLES", "SPAGHETTI", "CHIPS", "JALEBI", "BIRYANI", "LADDOO", "BREAD", "SANDWICH", "PRETZEL",
             "YOGHURT"]

photos = [PhotoImage(file="0.png"), PhotoImage(file="1.png"), PhotoImage(file="2.png"),
        PhotoImage(file="3.png"), PhotoImage(file="4.png"), PhotoImage(file="5.png"),
        PhotoImage(file="6.png"), PhotoImage(file="7.png")]


def newGame():
    global the_word_withSpaces
    global numberofGuesses
    numberofGuesses = 0
    imgLabel.config(image=photos[0])
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set("".join("_ " * len(the_word)))

def guess(letter):
    global numberofGuesses,the_word_withSpaces
    if numberofGuesses < 7:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))

        else:
            numberofGuesses+=1
            imgLabel.config(image=photos[numberofGuesses])
            if numberofGuesses==7:
                messagebox.showwarning("Hangman", "Game Over")
                Label(text="".join(guessed))

imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(window, textvariable=lblWord, font=("MS Gothic", 24, "bold")).grid(row=0, column=3, columnspan=6, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("MS Gothic", 22), bg="salmon2", width=5).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="Replay", command=lambda: newGame(), font=("MS Gothic", 10, " bold"), bg="saddle brown", fg="white").grid(row=3, column=8, sticky="NSWE")

newGame()
window.mainloop()
