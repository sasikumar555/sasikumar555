from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Notepad')
#root.geometry("500x400")

textarea = ScrolledText(root)
filename=None


def cmdNew():
    global filename
    if len(textarea.get("0.0", END))>0:
        if messagebox.askyesno("notepad" , "Do You Want To Save Changes?"):
            cmdSave()
        else:
            textarea.delete(0.0, END)
    root.title("Untitled - Notepad")

def cmdSave():
    global filename
    file= filedialog.asksaveasfile(mode='w', defaultextension='.txt')

def cmdOpen():
    global filename
    file= filedialog.askopenfile(parent=root ,mode="r")
    text=file.read()
    textarea.delete(0.0 , END)
    textarea.insert(0.0 ,text)

def cmdExit():
    if messagebox.askyesnocancel("notepad" , "Do you really want to exit?"):
        if len(textarea.get(0.0 , END))>0:
            cmdSave()
            root.destroy()


def cmdCut():
    textarea.event_generate("<<Cut>>")


def cmdCopy():
    textarea.event_generate("<<Copy>>")


def cmdPaste():
    textarea.event_generate("<<Paste>>")

def cmdDelete():
    textarea.event_generate("<<Clear>>")

def cmdZoom():
    pass


textareaMenu = Menu(root)
root.configure(menu=textareaMenu)

fileMenu = Menu(textareaMenu, tearoff = 0)
textareaMenu.add_cascade(label='File', menu = fileMenu)
fileMenu.add_cascade(label="New" , command=cmdNew)
fileMenu.add_cascade(label="Save" , command=cmdSave)
fileMenu.add_cascade(label="Open" , command=cmdOpen)
fileMenu.add_separator()
fileMenu.add_cascade(label="exit" , command=cmdExit)


editMenu = Menu(textareaMenu, tearoff = 0)
textareaMenu.add_cascade(label='Edit', menu = editMenu)
editMenu.add_command(label='Cut', command = cmdCut)
editMenu.add_command(label='Copy', command = cmdCopy)
editMenu.add_command(label='Paste', command = cmdPaste)
editMenu.add_cascade(label="delete" , command=cmdDelete)

viewMenu = Menu(textareaMenu , tearoff=0)
textareaMenu.add_cascade(label="view" , menu=viewMenu)
viewMenu.add_command(label="zoom" , command= cmdZoom)

textarea.pack()
root.mainloop()
