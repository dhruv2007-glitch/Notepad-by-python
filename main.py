import customtkinter as custk
from customtkinter import CTk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def fileNew():
    global file
    TextArea.delete(1.0, tk.END)
    win.title("*Untitled")
    file = None

def fileOpen():
    global file
    file = filedialog.askopenfilename(defaultextension='.txt', 
                                      filetypes=[('All Files', "*.*"), ('Text Documents', '*.txt')])
    if file:
        win.title(f"TakeNotes - {os.path.basename(file)}")
        with open(file, 'r') as file_content:
            TextArea.delete(1.0, tk.END)
            TextArea.insert(1.0, file_content.read())

def save():
    global file
    if file:
        with open(file, "w") as file_content:
            file_content.write(TextArea.get(1.0, tk.END))
    else:
        saveAs()

def saveAs():
    global file
    file = filedialog.asksaveasfilename(defaultextension='.txt', 
                                        filetypes=[('All Files', "*.*"), ('Text Documents', '*.txt')])
    if file:
        with open(file, 'w') as file_content:
            file_content.write(TextArea.get(1.0, tk.END))
        win.title(f"TakeNotes - {os.path.basename(file)}")

def quitApp():
    win.quit()

def cut():
    copy()
    TextArea.delete("sel.first", "sel.last")

def copy():
    try:
        win.clipboard_clear()
        win.clipboard_append(TextArea.get("sel.first", "sel.last"))
    except tk.TclError:
        pass

def paste():
    try:
        TextArea.insert(tk.INSERT, win.clipboard_get())
    except tk.TclError:
        pass

def About():
    messagebox.showinfo("About","This is made for educational purpose, don't missuse this app.\n Developer - Dhruv Sharma\n Github - @dhruv2007-glitch")

win = CTk()

win.geometry("800x600")
win.title("TakeNotes")

#textarea
TextArea = custk.CTkTextbox(win, font=("Times New Roman", 18), wrap='word')
file = None
TextArea.pack(fill="both", expand=True)

#Menu bar
MenuBar = tk.Menu(win)

fileMenu = tk.Menu(MenuBar, tearoff=0)
fileMenu.add_command(label="New", font=('Times New Roman', 18), command=fileNew)
fileMenu.add_command(label="Open", font=('Times New Roman', 18), command=fileOpen)
fileMenu.add_command(label="Save", font=('Times New Roman', 18), command=save)
fileMenu.add_command(label="Save as", font=('Times New Roman', 18), command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", font=('Times New Roman', 18), command=quitApp)
MenuBar.add_cascade(label="File", font=('Times New Roman', 16), menu=fileMenu)

editMenu = tk.Menu(MenuBar, tearoff=0)
editMenu.add_command(label="Cut", font=('Times New Roman', 18), command=cut)
editMenu.add_command(label="Copy", font=('Times New Roman', 18), command=copy)
editMenu.add_command(label="Paste", font=('Times New Roman', 18), command=paste)
MenuBar.add_cascade(label="Edit", font=('Times New Roman', 16), menu=editMenu)

Aboutmenu = tk.Menu(MenuBar, tearoff=0)
Aboutmenu.add_command(label="About", font=('Times New Roman', 18), command=About)
MenuBar.add_cascade(label='About', font=('Times New Roman', 16), menu = Aboutmenu)

win.config(menu=MenuBar)

win.mainloop()
