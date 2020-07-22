from tkinter import *
from tkinter import filedialog
import os

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Create tests")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        pathButton = Button(self, text="Select Path",command=self.file_p)

        # placing the button on my window
        pathButton.place(x=0, y=0)
    
    def file_p(self):
        root.inputdirectory =  filedialog.askdirectory()
        root.outputdirectory =  filedialog.askdirectory()
        for file in os.listdir(root.inputdirectory):
            if file.endswith(".ts"):
                sep = '.ts'
                rest = file.split(sep, 1)[0]
                f = open(os.path.join(root.outputdirectory, rest+".spec.ts"), "w") 
                f.write("") 
                f.close() 
                print(rest)

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop() 