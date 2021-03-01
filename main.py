#Author: Matthew Burns
#Date: 2/26/21
'''
Steps:
1. Create tkinter GUI with a file download option
2. Implement drag and drop feature
3. Detect file type and offer conversion options
4. Automatically download the file to after a conversion is selected
'''
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("File Converter")
        self.master.minsize(1000,600)
        self.master.maxsize(1200,800)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #file explorer button  
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Open File"
        self.hi_there["command"] = self.open_file
        self.hi_there.pack(side="top")

    def  open_file(self):
        tk.filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()