import csv
from tkinter import *

filepath = '/Users/Victor/Python-code/GUI/samletdata.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)


list_of_entries = []
for x in list(range(0,len(Data))):
	list_of_entries.append(Data[x][0])

root = Tk()
root.geometry('400x360')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0 , column=0)

def opdatere():
	index = listbox1.curselection()[0]
	Personlabel1.config(text=Data[index][0])
	Adhdlabel1.config(text=Data[index][20])
	Brugernavnlabel1.config(text=Data[index][21])
	Emaillabel1.config(text=Data[index][22])

	return None

button1 = Button(root, text="Opdatere", command=opdatere)
button1.grid(row=5, column=0)

Personlabel = Label(root, text="Person:").grid(row=1, column=0)
Brugernavnlabel = Label(root, text="Bruvernavn:").grid(row=1, column=0)
Emaillabel = Label(root, text="Emailadresse:").grid(row=2, column=0)
Adhdlabel = Label(root, text="Hjernestatus:").grid(row=3, column=0)

Personlabel1 = Label(root, text="")
Personlabel1.grid(row=1, column=0, sticky="w")
Brugernavnlabel1 = Label(root, text="")
Brugernavnlabel1.grid(row=1, column=1, sticky="w")
Emaillabel1 = Label(root, text="")
Emaillabel1.grid(row=2, column=1, sticky="w")
Adhdlabel1 = Label(root, text="")
Adhdlabel1.grid(row=3, column=1, sticky="w")


root.mainloop()
