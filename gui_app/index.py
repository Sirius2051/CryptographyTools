from tkinter import *
from tkinter import ttk

# This list contain all letters of alphabet creating a form of Atbash table.  
lettersList = [
	'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
	'Z','z','Y','y','X','x','W','w','V','v','U','u','T','t','S','s','R','r','Q','q','P','p','O','o','N','n'
	]

# Convertion function
def convert():
    content = textToConvert.get(1.0, "end-1c" )
    textList = []
    for letter in content:
        if letter in lettersList and lettersList.index(letter) < (len(lettersList)//2):
            textList.append(lettersList[lettersList.index(letter)+26])
        elif letter in lettersList and lettersList.index(letter) >= (len(lettersList)//2):
            textList.append(lettersList[lettersList.index(letter)-26])
        else:
            textList.append(letter)
    textConverted.delete(1.0, END)
    textConverted.insert('insert', ''.join(textList))

# Window settings
window = Tk()
window.title("Atbash Code/Decode")
window.geometry("1000x500")
window.config(bg="#32414B")

# Text box to insert the text to convert
textToConvert = Text(window)
textToConvert.pack(fill = "none", expand = 1, side = "left")
textToConvert.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232D", foreground="#99E66A", width = 40)

# Text box to view the text converted
textConverted = Text(window)
textConverted.pack(fill = "none", expand = 1, side = "right")
textConverted.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232D", foreground="#99E66A", width = 40)

# Button to init convertion
convert = Button(window, width = 10, bg = "#ffffff", fg = "#3775a9", text = "CONVERT", command = convert)
convert.pack(fill = "none", expand = 1, side = "bottom")

# 
window.mainloop()