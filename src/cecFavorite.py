'''
Created on 18 Jul 2017

@author: cecylia
this is my aplication showing my favorite things
'''
import tkinter as tk

def click(event):
    print("cecylia feels good")
    lblActivetise.configure(text = "hello people of the world")

def leftClick(event):
    print("awsome")
    lblActivetise.configure(text = "hi hi hi")

root = tk.Tk()

lblActivetise = tk.Label(root, text = " I love my Activites",bg = "lightblue", font="Helvetica 16 bold italic")
lblActivetise.pack()

lblGames = tk.Label(root, text = "Animals are great and I like them", bg = "pink")
lblGames.pack()

btnGames = tk.Button(root,text="push me")
btnGames.bind("<Button-3>", click)
btnGames.bind("<Button-1>", leftClick)
btnGames.pack()

root.mainloop()

