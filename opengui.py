from tkinter import *
from tkinter import messagebox
from dictionary import dictionary

def searchWord():
    textInput = e1.get()
    if len(textInput) < 1:
        ans = "Please enter word..."
    else:
        ans =dictionary(textInput)
    l3.config(text=ans,wraplength=435,font=("Courier", 14),bg="#87cefa")

def ask_quit():
    if messagebox.askokcancel("Quit", "You want to exit now?"):
        window.destroy()


window=Tk()
window.geometry("450x350")
window.title("Avi Dictionary")
window.configure(bg="lightgreen")
window.resizable(FALSE,FALSE)
l1=Label(window,text="Welcome to Dictionary",bg="yellow",fg="red")
l1.config(font=("Courier", 24))
l1.pack(fill=X)

inputWord = StringVar()
e1=Entry(window,width=30,textvariable=inputWord)
e1.pack(padx=5,pady=10)
e1.focus()

b1=Button(window,text="SEARCH",command=searchWord,bg="#9400d3",fg="white")
b1.pack()

l2=Label(window,text="Definitions:",bg="pink")
l2.configure(font=("Courier", 16))
l2.place(x=10,y=140)

l3=Label(window,text="")
l3.place(x=10,y=170)

window.protocol("WM_DELETE_WINDOW", ask_quit)
window.mainloop()

