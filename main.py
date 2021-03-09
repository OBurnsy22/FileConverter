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
import tkinter.filedialog
from TkinterDnD2 import DND_FILES, TkinterDnD
from conversion import *

#root window
root = TkinterDnD.Tk()
root.title("FileCNVTR")
root.geometry('{}x{}'.format(960, 540))
root.maxsize(960, 540)
root.minsize(960, 540)

#global variables
path_to_file = " "
file_type = " "
compatable_converstion = []
images = ["jpg", "jpeg", "tif", "tiff", "png"]

#helper fuctions
def open_selected_file():
    path_to_file = tk.filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    temp_str = " "
    for chars in reversed(path_to_file):
        if(chars == '.'):
            break
        temp_str += chars
    file_type = temp_str[::-1]
    compatable_converstion = retrieve_compatable_conversions(file_type)

def retrieve_compatable_conversions(file_type):
    if file_type in images:
        return images

#container layouts
dropbox_layout = tk.Frame(root, bg='green', width=700, height=520)
conversion_layout = tk.Frame(root, bg='yellow', width=230, height=520)

#layout main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
dropbox_layout.grid(column=0, row=0,pady=10)
conversion_layout.grid(column=1, row=0, padx=10)
#runs application
root.mainloop()