from tkinter import*
import random
from tkinter.messagebox import *


class ErrName(Exception):
    pass


class ErrButton(Exception):
    pass


class Fenetre1:
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y):
        fenetre.title(titre)
        fenetre.geometry(str(width)+"x"+str(height)+"+"+str(pos_x)+"+"+str(pos_y))
        fenetre.minsize(width, height)
        fenetre.maxsize(width, height)
        fenetre['bg'] = color
        self.fenetre = fenetre
        self.color = color

    def play_clicked(self):
        global fenetre2
        self.fenetre.destroy()
        fenetre2 = Tk()
        obj2 = Fenetre2(fenetre2, "Tic tac toe", 400, 400, "black", 500, 250)
        obj2.create()
        fenetre2.mainloop()

    def create(self):
        frame = Frame(self.fenetre, bg=self.color)
        frame.pack()
        label = Label(frame, text="Tic-Toc-Toe", fg='red', bg="black", font=("Ink Free", 30))
        label.pack(padx=0, pady=20)
        bouton = Button(frame, text="PLAY", bg="gray", fg="white", width=15, height=3, relief=GROOVE, cursor="hand2",
                        command=self.play_clicked)
        bouton.pack(pady=(75, 5))


class Fenetre2(Fenetre1):
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y):
        Fenetre1.__init__(self, fenetre, titre, width, height, color, pos_x, pos_y)

    def player_player(self):
        global fenetre3
        fenetre3 = Toplevel(self.fenetre)
        obj3 = Fenetre3(fenetre3, "Player vs Player", 400, 400, "black", 540, 290)
        obj3.create()

    def player_computer(self):
        global fenetre4
        fenetre4 = Toplevel(self.fenetre)
        obj4 = Fenetre4(fenetre4, "Player vs Computer", 400, 400, "black", 540, 290)
        obj4.create()

    def create(self):
        frame = Frame(self.fenetre, bg=self.color)
        frame.pack()
        bouton1 = Button(self.fenetre, text="player VS computer", bg="gray", fg="white", width=15, cursor="hand2",
                         height=3, relief=GROOVE, command=self.player_computer)
        bouton1.pack(pady=(100, 40))
        bouton2 = Button(self.fenetre, text="player VS player", bg="gray", fg="white", width=15, cursor="hand2",
                         height=3, relief=GROOVE, command=self.player_player)
        bouton2.pack(pady=20)


class Fenetre3(Fenetre1):
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y):
        Fenetre1.__init__(self, fenetre, titre, width, height, color, pos_x, pos_y)

    def player_player_play(self):
        try:
            global name11, name12
            name11 = entry14_2.get()
            name12 = entry24_2.get()
            if name11 == "" or name12 == "":
                raise ErrName("Enter your names :")
            else:
                fenetre2.destroy()
                global fenetre5
                fenetre5 = Tk()
                obj = Fenetre5(fenetre5, "Tic Tac Toe", 400, 400, "black", 500, 250, 0, True)
                obj.create()
        except ErrName as msg:
            showerror("Error", msg, parent=self.fenetre)

    def create(self):
        frame1 = Frame(self.fenetre, bg="black")
        frame1.pack()
        label1 = Label(frame1, text="Name player1", font=("Ink Free", 20), width=14)
        label1.pack(side=LEFT, padx=(0, 10), pady=(70, 5))
        global entry14_2, entry24_2
        entry14_2 = Entry(frame1, bd=14, width=20)
        entry14_2.pack(padx=(10, 0), pady=(70, 5))
        frame2 = Frame(self.fenetre, bg="black")
        frame2.pack()
        label2 = Label(frame2, text="Name player2", font=("Ink Free", 20), width=14)
        label2.pack(side=LEFT, padx=(0, 10), pady=(10, 5))
        entry24_2 = Entry(frame2, bd=14, width=20)
        entry24_2.pack(padx=(10, 0), pady=(10, 5))
        frame3 = Frame(fenetre3, bg="black")
        frame3.pack()
        bouton = Button(frame3, text="play", font=("Ink Free", 25), width=10, relief=GROOVE,
                        command=self.player_player_play)
        bouton.pack(pady=45)


class Fenetre4(Fenetre1):
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y):
        Fenetre1.__init__(self, fenetre, titre, width, height, color, pos_x, pos_y)

    def player_computer_play(self):
        try:
            global name21
            name21 = entry1.get()
            if name21 == "":
                raise ErrName("Enter your name :")
            else:
                fenetre2.destroy()
                global fenetre6
                fenetre6 = Tk()
                obj6 = Fenetre6(fenetre6, "Tic Tac Toe", 400, 400, "black", 500, 250, 0)
                obj6.create()
        except ErrName as msg:
            showerror("Erreur", msg, parent=self.fenetre)

    def create(self):
        frame1 = Frame(self.fenetre, bg="black")
        frame1.pack()
        label = Label(frame1, text="Name", font=("Ink Free", 20), width=9)
        label.pack(side=LEFT, padx=(0, 10), pady=(70, 5))
        global entry1
        entry1 = Entry(frame1, bd=14, width=20)
        entry1.pack(padx=(10, 0), pady=(70, 5))
        frame2 = Frame(self.fenetre, bg="black")
        frame2.pack()
        bouton = Button(frame2, text="play", font=("Ink Free", 25), width=10, relief=GROOVE,
                        command=self.player_computer_play)
        bouton.pack(pady=45)


class Fenetre5(Fenetre1):
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y, iteration, a_play):
        Fenetre1.__init__(self, fenetre, titre, width, height, color, pos_x, pos_y)
        self.iteration = iteration
        self.a_play = a_play

    def ok_clicked(self):
        fenetre7.destroy()
        self.fenetre.destroy()
        fenetre5 = Tk()
        obj = Fenetre5(fenetre5, "Tic Tac Toe", 400, 400, "black", 500, 250, 0, True)
        obj.create()

    def gagne(self, val):
        global fenetre7
        fenetre7 = Toplevel(self.fenetre)
        fenetre7.title("Winner")
        fenetre7.geometry("350x80+550+280")
        fenetre7.minsize(350, 80)
        fenetre7.maxsize(350, 80)
        fenetre7['bg'] = 'white'  # couleur de fond
        frame1 = Frame(fenetre7, bg="white")
        frame1.pack()
        if val == "egalite":
            label = Label(frame1, text="{0}".format(val), fg='red', bg="white", font=("Ink Free", 22), width=50)
            label.pack(padx=0, pady=5)
        if val == "X":
            label = Label(frame1, text="The Winner is : {0}".format(name11), fg='red', bg="white",
                          font=("Ink Free", 22),
                          width=50)
            label.pack(padx=0, pady=5)
        if val == "O":
            label = Label(frame1, text="The Winner is : {0}".format(name12), fg='red', bg="white",
                          font=("Ink Free", 22),
                          width=50)
            label.pack(padx=0, pady=5)
        button = Button(frame1, text="Ok", fg="white", bg="red", font=("Ink Free", 14), width=10, command=self.ok_clicked)
        button.pack()

    def case_verification(self, char):
        if ((botn[0][0]["text"] == char) and (botn[0][1]["text"] == char) and (botn[0][2]["text"] == char)) or \
                ((botn[1][0]["text"] == char) and (botn[1][1]["text"] == char) and (botn[1][2]["text"] == char)) or \
                ((botn[2][0]["text"] == char) and (botn[2][1]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][0]["text"] == char) and (botn[1][0]["text"] == char) and (botn[2][0]["text"] == char)) or \
                ((botn[0][1]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][1]["text"] == char)) or \
                ((botn[0][2]["text"] == char) and (botn[1][2]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][0]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][2]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][0]["text"] == char)):
            self.gagne(char)
        elif self.iteration == 9:
            self.gagne("egalite")

    def button_clicked(self, i, j):
        try:
            if botn[i][j]["text"] == "X" or botn[i][j]["text"] == "O":
                raise ErrButton("Bouton deja utilisee !")
            else:
                self.iteration += 1
                if self.a_play:
                    char = "X"
                    botn[i][j].configure(text="X", font=("Times New Roman", 9), bg="red", fg="black")
                    self.case_verification(char)
                else:
                    char = "O"
                    botn[i][j].configure(text="O", font=("Times New Roman", 9), bg="white", fg="black")
                    self.case_verification(char)
                self.a_play = not self.a_play
        except ErrButton as msg:
            showerror("Erreur", msg, parent=self.fenetre)
    def create(self):
        frame1 = Frame(self.fenetre, bg="black")
        frame1.pack()
        label = Label(frame1, text="{0}  vs  {1}".format(name11, name12), fg='red', bg="black", font=("Ink Free", 30),
                      width=50)
        label.pack(padx=0, pady=5)
        frame2 = Frame(self.fenetre, bg="black")
        frame2.pack(pady=10)
        global botn
        botn = []
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append(Button(frame2, bg="gray", bd=1, relief=GROOVE, cursor="hand2", width=13, height=4,
                                    command=lambda x=i, y=j: self.button_clicked(x, y)))
                ligne[j].grid(row=i, column=j, padx=1, pady=1)
            botn.append(ligne)


class Fenetre6(Fenetre1):
    def __init__(self, fenetre, titre, width, height, color, pos_x, pos_y, iteration):
        Fenetre1.__init__(self, fenetre, titre, width, height, color, pos_x, pos_y)
        self.iteration = iteration

    def ok_clicked(self):
        fenetre7.destroy()
        self.fenetre.destroy()
        fenetre6 = Tk()
        obj = Fenetre6(fenetre6, "Tic Tac Toe", 400, 400, "black", 500, 250, 0)
        obj.create()

    def gagne(self, val):
        global fenetre7
        fenetre7 = Toplevel(self.fenetre)
        fenetre7.title("Gagnat")
        fenetre7.geometry("350x50+550+280")
        fenetre7.minsize(350, 80)
        fenetre7.maxsize(350, 80)
        fenetre7['bg'] = 'white'  # couleur de fond
        frame1 = Frame(fenetre7, bg="white")
        frame1.pack()
        if val == "egalite":
            label = Label(frame1, text="{0}".format(val), fg='red', bg="white", font=("Ink Free", 22), width=50)
            label.pack(padx=0, pady=5)
        if val == "X":
            label = Label(frame1, text="The Winner is : {0}".format(name21), fg='red', bg="white",
                          font=("Ink Free", 22),
                          width=50)
            label.pack(padx=0, pady=5)
        if val == "O":
            label = Label(frame1, text="The Winner is : {0}".format("Computer"), fg='red', bg="white",
                          font=("Ink Free", 22),
                          width=50)
            label.pack(padx=0, pady=5)
        button = Button(frame1, text="Ok", fg="white", bg="red", font=("Ink Free", 14), width=10,
                        command=self.ok_clicked)
        button.pack()

    def case_verification(self, char):
        if ((botn[0][0]["text"] == char) and (botn[0][1]["text"] == char) and (botn[0][2]["text"] == char)) or \
                ((botn[1][0]["text"] == char) and (botn[1][1]["text"] == char) and (botn[1][2]["text"] == char)) or \
                ((botn[2][0]["text"] == char) and (botn[2][1]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][0]["text"] == char) and (botn[1][0]["text"] == char) and (botn[2][0]["text"] == char)) or \
                ((botn[0][1]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][1]["text"] == char)) or \
                ((botn[0][2]["text"] == char) and (botn[1][2]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][0]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][2]["text"] == char)) or \
                ((botn[0][2]["text"] == char) and (botn[1][1]["text"] == char) and (botn[2][0]["text"] == char)):
            self.gagne(char)
            global win
            win = True
        elif self.iteration == 9:
            self.gagne("egalite")
        else:
            win = False

    def button_clicked(self, i, j):
        try:
            if botn[i][j]["text"] == "X" or botn[i][j]["text"] == "O":
                raise ErrButton("Button already used !")
            else:
                self.iteration += 1
                char = "X"
                botn[i][j].configure(text="X", font=("Times New Roman", 9), bg="red", fg="black")
                self.case_verification(char)
                if win == False:
                    char = "O"
                    choices = []
                    for i in range(3):
                        for j in range(3):
                            if botn[i][j]["text"] != "X" and botn[i][j]["text"] != "O":
                                x = botn[i][j]
                                choices.append(x)
                    chosen = random.choice(choices)
                    chosen.configure(text="O", font=("Times New Roman", 9), bg="white", fg="black")
                    self.iteration += 1
                    self.case_verification(char)
        except ErrButton as msg:
            showerror("Erreur", msg, parent=self.fenetre)

    def create(self):
        frame1 = Frame(self.fenetre, bg="black")
        frame1.pack()
        label = Label(frame1, text="welcome {0}".format(name21), fg='red', bg="black", font=("Ink Free", 30), width=50)
        label.pack(padx=0, pady=5)
        frame2 = Frame(self.fenetre, bg="black")
        frame2.pack(pady=10)
        global botn
        botn = []
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append(Button(frame2, bg="gray", bd=1, relief=GROOVE, cursor="hand2", width=13, height=4,
                                    command=lambda x=i, y=j: self.button_clicked(x, y)))
                ligne[j].grid(row=i, column=j, padx=1, pady=1)
            botn.append(ligne)


if __name__ == "__main__":
    root = Tk()
    obj1 = Fenetre1(root, "tic tac toe", 400, 400, "black", 500, 250)
    obj1.create()
    root.mainloop()
