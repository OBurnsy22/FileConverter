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
dropbox_layout = tk.Frame(root, bg='#DCDCDC', width=690, height=520)
conversion_layout = tk.Frame(root, bg='#DCDCDC', width=240, height=520)

#size containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
dropbox_layout.grid(column=0, row=0,pady=10, sticky="nsew")
conversion_layout.grid(column=1, row=0, padx=10, sticky="nsew")
dropbox_layout.rowconfigure(0, weight=1)
dropbox_layout.columnconfigure(0, weight=1)

#declaring widgets for dropbox_layout
dropbox = tk.Listbox(dropbox_layout, selectmode=tk.SINGLE, background="#99ff99")
dropbox.drop_target_register(DND_FILES)
dropbox.dnd_bind("<<Drop>>", open_dropped_file)
select_file = tk.Button(dropbox_layout, text="Select File", command=open_selected_file)
text_label = tk.Label(dropbox_layout, text="Drag and Drop or Select a File")
canvas = tk.Canvas(dropbox_layout, width=100, height=100)
img = tk.PhotoImage(file="static/drag_and_drop.png") #convert this to gif when you come back

#placing widgets for dropbox_layout
dropbox.grid(column=0, row=0, sticky="nesw")
select_file.grid(column=0, row=0)
canvas.grid(column=0, row=0)
canvas.create_image(20, 20, anchor=NW, image=img)
#text_label.grid(column=0, row=0, pady=(50))
#widgets for conversion_layout

#runs application
root.mainloop()