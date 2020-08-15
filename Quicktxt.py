#Developed by Jaspreet Singh



#importing lib
from tkinter import *
from tkinter import simpledialog,messagebox
from tkinter import filedialog
import os

#Global init
root = Tk()


# Defining Functions



#function to open files
def openfile():
    file_path = filedialog.askopenfilename()
    
    try:
        with open(file_path, "r+") as f:
            read = f.readlines()
        text.delete('1.0', END)
        for i in read:
            text.insert("end-1c", i)
    except Exception as e:
            messagebox.showerror("Not Supported file format","Please open .txt file")

#function to about us msg box
def aboutus():
    messagebox.showinfo("Developed by","Jaspreet Singh")


#function to save files
def Submitmenu():
    USER_INP = simpledialog.askstring(title="Save as",
                                      prompt="File name ?")

    with open(USER_INP+".txt", "a+") as f:
        f.write(text.get('1.0', END))




#Starting point of my code ie Main Function
if __name__ == '__main__':
    root.title("Quick Text")

    #Making Menu Bar
    menu = Menu(root)
    m1 = Menu(menu, tearoff=0)
    m1.add_command(label="About", command=aboutus)
    m1.add_command(label="Open", command=openfile)
    m1.add_command(label="Save", command=Submitmenu)
    menu.add_cascade(label="File", menu=m1)
    root.config(menu=menu)

    #Making wire frames on root
    frame = Frame(root, bg="grey")
    frame.pack(side=LEFT, fill=Y)

    #Adding scroll bar to text layout
    scroll = Scrollbar(root)
    text = Text(root, undo=1, tabs=1, yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(fill=BOTH, ipady=190)
    scroll.config(command=text.yview)

    #Adding font style to textview
    text.configure(font=("Gotham", 16))
    # Ending code
    root.mainloop()
