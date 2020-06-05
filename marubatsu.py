# a simple maru-batsu game

import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk


class Board:
    def __init__(self):
        # counts turns. used to determine draws
        self.turns = 0

        # sets images to use
        self.white = ImageTk.PhotoImage(Image.open("images/white.png").resize((100, 100)))
        maru = ImageTk.PhotoImage(Image.open("images/circle.jpg").resize((100, 100)))
        batsu = ImageTk.PhotoImage(Image.open("images/batsu.png").resize((100, 100)))
        self.options = [maru, batsu]

        # used for win condition checking. 3 = maru, 4 = batsu
        self.values = [3, 4]

        # used to check who's turn it it
        self.current = 0

        # first value in pair has Button objects, second value has numbers (3 or 4)
        self.board = [[[0, 0], [0, 0], [0, 0]],
                      [[0, 0], [0, 0], [0, 0]],
                      [[0, 0], [0, 0], [0, 0]]]
        for i in range(3):
            for j in range(3):
                self.board[i][j][0] = tkinter.Button(image=self.white, command=lambda i=i, j=j: self.select(i, j))
                self.board[i][j][0].grid(row=i, column=j)

    def select(self, i=0, j=0):
        # set the clicked button image to maru/ batsu
        self.board[i][j][0]["image"] = self.options[self.current]
        self.board[i][j][0]["state"] = "disabled"

        # set the second value in board list to be 3 if maru, 4 if batsu
        self.board[i][j][1] = self.values[self.current]

        # check for end of game
        self.check()

        # set to next move
        self.turns += 1
        self.current = self.turns % 2

    def check(self):
        sums = []
        # check rows
        for i in range(3):
            s = sum(n for img, n in self.board[i])
            sums.append(s)
        # check columns
        for j in range(3):
            s = sum(n for img, n in list(zip(*self.board))[j])
            sums.append(s)
        # check diags
        s = sum(self.board[i][i][1] for i in range(3))
        sums.append(s)
        s = sum(self.board[i][3 - i - 1][1] for i in range(3))
        sums.append(s)

        # if there's a winner
        if 9 in sums:
            tkinter.messagebox.showinfo("Winner!", "Maru wins!")
            # disable further input
            for i in range(3):
                for j in range(3):
                    self.board[i][j][0]["state"] = "disabled"
            return
        elif 12 in sums:
            tkinter.messagebox.showinfo("Winner!", "Batsu wins!")
            for i in range(3):
                for j in range(3):
                    self.board[i][j][0]["state"] = "disabled"
            return

        # if all inputs are made
        if self.turns >= 8:
            tkinter.messagebox.showinfo("End of game!", "Draw!")


# initialize GUI
root = tkinter.Tk()

# make menu bar
menu = tkinter.Menu()
menu.add_command(label="Start new game", command=Board)
menu.add_command(label="Quit", command=exit)
# actually puts menu bar in GUI
root.config(menu=menu)

# make game boards
board = Board()

# show the window
root.mainloop()
