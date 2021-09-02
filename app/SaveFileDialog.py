import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class SaveFileDialog:

    root = None
    selectedFile = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('0x0')
        self.root.attributes('-alpha', 0)
        self.select_file()
        self.root.mainloop()

    def select_file(self):
        filetypes = (
            ('word files', '*.docx'),
        )

        filename = fd.asksaveasfile(
            title='Save file',
            initialdir='/',
            filetypes=filetypes,
            defaultextension = filetypes)

        print('python filename :  ',filename["name"])

        self.selectedFile = filename
        self.root.destroy()