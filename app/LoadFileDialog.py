import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class LoadFileDialog:

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

        filename = fd.askopenfilename(
            title='Load file',
            initialdir='/',
            filetypes=filetypes)

        self.selectedFile = filename
        self.root.destroy()