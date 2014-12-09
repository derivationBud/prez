import Tkinter as tk
import xmlrpclib

def new(): 
    server.new()
    guess.set("-"*8)

def submit():
    propalValue = propal.get()
    result=server.guess(propalValue)
    if len(propalValue)==1: 
        letters=list(guess.get())
        for index in result: letters[index]=propalValue 
        guess.set("".join(letters))
    else:
        if result: message = "Congrats"
        else:      message = "No luck"
        guess.set(message)
        
if 1:
    server = xmlrpclib.Server('http://localhost:8081')
    gui=tk.Tk()
    propal = tk.StringVar()
    guess  = tk.StringVar()
    guess.set("-"*8)
    tk.Label( gui,text="1 Letter or 8-letter word:").pack()
    tk.Entry( gui,textvariable=propal              ).pack()
    tk.Label( gui,textvariable=guess               ).pack()
    tk.Button(gui,text="Submit",command=submit     ).pack()
    tk.Button(gui,text="New",command=new           ).pack()
    gui.mainloop()