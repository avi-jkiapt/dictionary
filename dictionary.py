import json
from difflib import get_close_matches
from tkinter import messagebox

def CheckError(UserWord):
    MsgBox = messagebox.askquestion ('Typed Incorrectly?','Did you mean %s instead' % UserWord,icon = 'warning')
    if MsgBox == 'yes':
        # messagebox.showinfo('Return','Yes')
        return "y"
    else:
        messagebox.showinfo('Oops','Sorry No any match.')
        return "n"

data = json.load(open("dictionary.json"))

def dictionary(word):
    word = word.upper()
    if word in data:
         return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        ins = get_close_matches(word,data.keys())[0]
        option = CheckError(ins)
        if option=="y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Sorry! We can't find that word."

    else:
        return "Please check spelling."


