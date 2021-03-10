#Author: Matthew Burns
#Date: 2/26/21
'''
Steps:
1. Create tkinter GUI with a file download option
2. Implement drag and drop feature
3. Detect file type and offer conversion options
4. If the type of file that was inputted has no valid conversions, display error
    message to user, check for this error in retrieve_compatable_conversions.
    Also ensure if the user at first clicks on the select file button and then
    closes out of the window, to ensure the code doesn't progress into the other 
    functions.
5. Automatically download the file to after a conversion is selected
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

#helper fuctions
def temp():
    return

def add_buttons(compatable_converstion):
    iter = 0
    for words in compatable_converstion:
        button = tk.Button(conversion_layout, text=words, command=temp)
        button.pack(expand=True)
    return

def open_selected_file():
    path_to_file = tk.filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    split = path_to_file.split('.')
    file_type = split[1]
    compatable_converstion = retrieve_compatable_conversions(file_type)
    if compatable_converstion:
        add_buttons(compatable_converstion)
    else:
        print("Invalid File Type")

def open_dropped_file(event):
    split = event.data.split('.')
    file_type = split[1]
    compatable_converstion = retrieve_compatable_conversions(file_type)
    if compatable_converstion:
        add_buttons(compatable_converstion)
    else:
        print("Invalid File Type")

def retrieve_compatable_conversions(file_type): 
    images = ["jpg", "jpeg", "tif", "tiff", "png", "gif"] 
    if file_type in images:
        return images
    else:
        return 0

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
#conversion_layout.rowconfigure(0, weight=1)
#conversion_layout.columnconfigure(1, weight=1)
conversion_layout.grid_propagate(0)

#declaring widgets for dropbox_layout
dropbox = tk.Listbox(dropbox_layout, selectmode=tk.SINGLE, background="#99ff99")
dropbox.drop_target_register(DND_FILES)
dropbox.dnd_bind("<<Drop>>", open_dropped_file)
select_file = tk.Button(dropbox_layout, text="Select File", command=open_selected_file)
dropbox_text_label = tk.Label(dropbox_layout, text="Drag and Drop or Select a File")
#canvas = tk.Canvas(dropbox_layout, width=100, height=100)
img = tk.PhotoImage(file="static/drag_and_drop.gif") #convert this to gif when you come back

#declaring widgets for conversion_layout
conversion_text_label = tk.Label(conversion_layout, text="Compatable Convertions")
#convserion_scrollbar = tk.Label(conversion_layout, orient=VERTICAL) 

#placing widgets for dropbox_layout
#canvas.grid(column=0, row=0)
#canvas.create_image(20, 20, image=img)
dropbox.grid(column=0, row=0, sticky="nesw")
select_file.grid(column=0, row=0)
#text_label.grid(column=0, row=0, pady=(50))

#placing widgets for conversion_layout

#runs application
root.mainloop()
