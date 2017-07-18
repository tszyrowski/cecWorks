'''
Created on 18 Jul 2017

@author: cecylia
this is my aplication showing my favorite things
'''
import tkinter as tk

root = tk.Tk()

lblActivetise = tk.Label(root, text = "my Activites",bg = "blue")
lblActivetise.pack()

lblGames = tk.Label(root, text = "Animals", bg = "pink")
lblGames.pack()

root.mainloop()

