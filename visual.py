import tkinter
import random




class CusButton(tkinter.Button):
    FONT = ('Consolas', 16)
    emptySpace = ' '
    
    def __init__(self, master):
        super().__init__(master=master, text='X', command=self.toggle, width=4, height=1, font=self.FONT)
    
    def toggle(self):
        if self['text'] == self.emptySpace:
            self.config(text='X')
        else:
            self.config(text=self.emptySpace)


class SubWindows(tkinter.Toplevel):
    MAIN_FONT = ('Consolas', 12, 'bold')
    
    def __init__(self, column, row, studentamount):
        super().__init__()
        self.title("Seat Randomizer")

        # Variable Init
        self.geometry()
        self.buttonList = []
        self.studentAmount = studentamount
        self.column = column
        self.row = row

        # UI Init
        self.addColumnButton = tkinter.Button(master=self, text='Add New Column', command=self.addNewColumn,
                                              font=self.MAIN_FONT, width=13)
        self.addColumnButton.grid(column=0, row=0, columnspan=2)

        self.addRowButton = tkinter.Button(master=self, text='Add New Row', command=self.addNewRow,
                                           font=self.MAIN_FONT, width=13)
        self.addRowButton.grid(column=0, row=1, columnspan=2)

        self.randomizeButton = tkinter.Button(master=self, text='Randomize!', command=self.randomizer,
                                              font=self.MAIN_FONT, width=13)
        self.randomizeButton.grid(column=2, row=0, columnspan=2)

        self.resetButton = tkinter.Button(master=self, text='Reset', command=self.reset,
                                          font=self.MAIN_FONT, width=13)
        self.resetButton.grid(column=2, row=1, columnspan=2)

        self.removeColumnButton = tkinter.Button(master=self, text="Remove Column", command=self.removeColumn,
                                                 font=self.MAIN_FONT, width=13)
        self.removeColumnButton.grid(column=4, row=0, columnspan=2)

        self.removeRowButton = tkinter.Button(master=self, text="Remove Row", command=self.removeRow,
                                              font=self.MAIN_FONT, width=13)
        self.removeRowButton.grid(column=4, row=1, columnspan=2)

        # Button Init
        for r in range(row):
            tmpList = []
            for c in range(column):
                tmpButton = CusButton(self)
                tmpButton.grid(column=c, row=r + 2)
                tmpList.append(tmpButton)
            self.buttonList.append(tmpList)

    # Button[Row][Column]

    def addNewColumn(self):
        for x in range(self.row):
            tmpButton = CusButton(self)
            tmpButton.grid(column=self.column, row=x + 2)
            self.buttonList[x].append(tmpButton)

        self.column += 1

    def addNewRow(self):
        tmpList = []
        for x in range(self.column):
            tmpButton = CusButton(self)
            tmpButton.grid(column=x, row=self.row + 2)
            tmpList.append(tmpButton)

        self.buttonList.append(tmpList)
        self.row += 1

    def randomizer(self):
        self.addColumnButton.config(state='disabled')
        self.addRowButton.config(state='disabled')
        self.removeColumnButton.config(state='disabled')
        self.removeRowButton.config(state='disabled')

        numList = [x for x in range(1, self.studentAmount + 1)]
        random.shuffle(numList)
        for x in self.buttonList:
            for y in x:
                y.config(state='disabled')
                if not y['text'] == ' ':
                    y['text'] = 'X'

                if y['text'] == 'X' and len(numList) > 0:
                    y.config(text=f"{numList[0]}")
                    numList.pop(0)

    def reset(self):
        self.addColumnButton.config(state='active')
        self.addRowButton.config(state='active')
        self.removeRowButton.config(state='active')
        self.removeColumnButton.config(state='active')
        for x in self.buttonList:
            for y in x:
                y.config(state='active')
                if not y['text'] == ' ':
                    y.config(text='X')

    def removeColumn(self):
        if self.column > 1:
            for x in self.buttonList:
                lastButton = x[-1]
                lastButton.grid_forget()
                x.pop()
            self.column -= 1

    def removeRow(self):
        if self.row > 1:
            for x in self.buttonList[-1]:
                x.grid_forget()
            self.buttonList.pop()
            self.row -= 1
