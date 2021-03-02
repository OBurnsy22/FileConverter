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

#global variables
path_to_file = " "
file_type = " "
compatable_converstion = []

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
        #Drag and drop files area
        self.drop_box = tk.Listbox(root, selectmode=tk.SINGLE, background="#99ff99")
        self.drop_box.pack(ipadx=170)
        self.drop_box.pack(ipady=120)
        self.drop_box.pack(side="left")
        self.drop_box.drop_target_register(DND_FILES)
        self.drop_box.dnd_bind("<<Drop>>", open_dropped_file)
        #Select file button
        self.select_file = tk.Button(self)
        self.select_file["text"] = "Select File"
        self.select_file["command"] = self.open_selected_file
        self.select_file.place(relx=1.0, rely=1.0)
        #Instructional Text
        sentence = "Drag and drop or select your file"
        self.instructions = tk.Text(root)
        self.instructions.insert(tk.END, sentence)
        self.instructions.place(relx=1.0, rely=1.0)

    def open_selected_file(self):
        path_to_file = tk.filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        temp_str = " "
        for chars in reversed(path_to_file):
            if(chars == '.'):
                break
            temp_str += chars
        file_type = temp_str[::-1]
        compatable_converstion = retrieve_compatable_conversions(file_type)
    '''
    def open_dropped_file(self, event):
        compatable_converstion = retrieve_compatable_conversions_select(event.data)
        breakpoint()
    '''


def main():
    global root
    root = TkinterDnD.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()


