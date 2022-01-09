from tkinter import *
from tkinter import ttk
# 
lettersList = [
	'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
	'Z','z','Y','y','X','x','W','w','V','v','U','u','T','t','S','s','R','r','Q','q','P','p','O','o','N','n'
	]
#
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
    convertedText.delete(1.0, END)
    convertedText.insert('insert', ''.join(textList))
#
window = Tk()
window.title("Atbash")
window.geometry("1000x500")
window.config(bg="#32414b")
#
textToConvert = Text(window)
textToConvert.pack(fill = "none", expand = 1, side = "left")
textToConvert.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232d", foreground="#99e66a", width = 40)
#
convertedText = Text(window)
convertedText.pack(fill = "none", expand = 1, side = "right")
convertedText.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232d", foreground="#99e66a", width = 40)
# 
convert = Button(window, width = 10, bg = "#ffffff", fg = "#3775a9", text = "CONVERT", command = convert)
convert.pack(fill = "none", expand = 1, side = "bottom")
# 
window.mainloop()