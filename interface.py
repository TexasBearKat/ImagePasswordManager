#packages
import tkinter as tk
import ttkbootstrap as ttk

#window
window = tk.Tk()
window.title("Image Password Manager")
#WidthxHeight
window.geometry("500x500")

title_label = ttk.Label(master = window, text = "Image Password Manager", font = 'Calibri 24 bold')
title_label.pack()





window.mainloop()