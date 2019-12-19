import string
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry('300x100')
root.config(bg='black')
def getp():
    randoom = ''.join([random.choice(string.ascii_letters+ string.digits) for n in range(7)]) 
    messagebox.showinfo(title='PASSOWRD',message=f'YOUR PASSWORD IS: {randoom}')
Label(text='======PASSWORD GENERATOR======',font=10).pack(fill='x',pady=6)
button1 = Button(text='Generate',command=getp,padx=10).pack(pady=2)
root.mainloop()
