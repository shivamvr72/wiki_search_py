# wiki search having main intention to search on side with small screan and very simple functinality
from tkinter import*
import wikipedia
root = Tk()
root.title("Wiki Search")

def src ():
    entry_v = en1m.get()
    ans.delete(1.0, END)
    try:
        rece_v = wikipedia.summary(entry_v)
        ans.insert(INSERT, rece_v)
    except:
        ans.insert(INSERT, "Check Your Input Or Internet Connection!")

def clr():
    en1m.set("")


#structure
fm1 = Frame(root)
fm1.pack(side=TOP)

en1m = StringVar()
en1 = Entry(fm1, textvariable=en1m, width=36, bg="#fefeee", font="mossarate 13")
en1.pack(pady=7)

btn = Button(fm1, text="Search", command=src, bg="royalblue", fg="white")
btn.pack(side=RIGHT)
clear = Button(fm1, text="Clear", command=clr, bg="Black", fg="white")
clear.pack(side=RIGHT)

fm2 = Frame(root)
sb = Scrollbar(fm2)
sb.pack(side=RIGHT, fill=Y)
ans= Text(fm2, yscrollcommand=sb.set, width=39, wrap=WORD, bg="#fefeee")
ans.pack(side=LEFT)
sb.config(command=ans.yview)
fm2.pack()

root.config(bg="gray")
fm1.config(bg="gray")
fm2.config(bg="gray")
root.geometry("350x250+600+200")
# root.geometry("750x550+600+200")
root.resizable(1,1)
root.mainloop()