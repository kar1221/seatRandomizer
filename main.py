import tkinter
from tkinter import messagebox
from visual import SubWindows

# Constant
FONT = ('Consolas', 16)


# Functions
def Generate():
    try:
        column, row, studentamo = int(entryColumn.get()), \
                                int(entryRow.get()), \
                                int(entryStudentAmount.get())
    except ValueError:
        messagebox.showerror(title="Data Error", message="Please enter numbers in required blank.")
        return
    
    if row * column > 150:
        messagebox.showerror(title="?!?!", message="How many student do you have!?!?")
        return
    
    SubWindows(abs(column), abs(row), abs(studentamo))


# UI Settings

mainWindows = tkinter.Tk()
mainWindows.title("Seat Randomizer")

labelColumn = tkinter.Label(text="Column: ", font=FONT)
labelColumn.grid(column=0, row=1, sticky="e")

labelRow = tkinter.Label(text="Row: ", font=FONT)
labelRow.grid(column=0, row=2, sticky="e")

labelStudentAmount = tkinter.Label(text="Student Amount: ", font=FONT, )
labelStudentAmount.grid(column=0, row=3, sticky="e")

entryColumn = tkinter.Entry(width=5)
entryColumn.grid(column=1, row=1)

entryRow = tkinter.Entry(width=5)
entryRow.grid(column=1, row=2)

entryStudentAmount = tkinter.Entry(width=5)
entryStudentAmount.grid(column=1, row=3)

buttonGenerate = tkinter.Button(text="Generate!", font=FONT, command=Generate)
buttonGenerate.grid(column=1, row=4, columnspan=2)

mainWindows.mainloop()
