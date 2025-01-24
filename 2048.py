# 2048

from tkinter import *
from random import randint

root = Tk()
root.title("2048")
root.geometry("1920x1080")
root.config(bg="grey")

Switch = False

matrice = [
    [StringVar(), StringVar(), StringVar() , StringVar()],
    [StringVar(), StringVar(), StringVar() , StringVar()],
    [StringVar(), StringVar(), StringVar() , StringVar()],
    [StringVar(), StringVar(), StringVar() , StringVar()]
]

matrice_label = []
Liste_frame = [Frame(), Frame(), Frame(), Frame()]

for i in Liste_frame:
    i.pack()

chiffre = 0
for i in matrice:
    matrice_label.append([])

    for j in i:
        lab = Label(Liste_frame[chiffre], textvariable=j, font=('Arial', 30), width=8, height=4, fg="bisque4", bg="bisque4", highlightcolor="grey", highlightthickness=3)
        lab.pack(side=LEFT)
        j.set(0)

        matrice_label[-1].append(lab)
    chiffre += 1

matrice[0][1].set(2)
matrice[2][3].set(2)

dico = {
    "2": "linen",
    "4": "bisque",
    "8": "navajo white",
    "16": "coral",
    "32": "salmon",
    "64": "red2",
    "128": "light goldenrod",
    "256": "khaki2",
    "512": "sandy brown",
    "1024": "goldenrod1",
    "2048": "gold",
    "4096": "indianRed1",
    "8192": "firebrick3",
    "16384": "red3",
    "32768": "turquoise",
    "65536": "deep sky blue",
    "131072": "RoyalBlue1"
}

def update():
    global Switch

    stopi = False
    if Switch:
        Switch = not Switch
        for i in matrice:
            for j in i:
                if randint(1, 10) == 8 and j.get() == "0" and stopi == False:
                    stopi = True
                    j.set(2)

    Switch = not Switch

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j].get() == "0":
                matrice_label[i][j].config(bg="bisque4", fg="bisque4")
            else:
                matrice_label[i][j].config(bg=dico[matrice[i][j].get()], fg="black")

def right():

    for _ in range(3):
        for i in matrice:
            for j in range(len(i)):
                if i[j].get() != "0" and j != len(i) - 1:
                    if i[j + 1].get() == "0":
                        i[j + 1].set(i[j].get())
                        i[j].set("0")
                    if i[j + 1].get() == i[j].get():
                        i[j + 1].set(int(i[j + 1].get()) + int(i[j].get()))
                        i[j].set("0")
    
    update()


def left():

    for _ in range(3):
        for i in matrice:
            for j in range(len(i) - 1, -1, -1):
                if i[j].get() != "0" and j != 0:
                    if i[j - 1].get() == "0":
                        i[j - 1].set(i[j].get())
                        i[j].set("0")
                    if i[j - 1].get() == i[j].get():
                        i[j - 1].set(int(i[j - 1].get()) + int(i[j].get()))
                        i[j].set("0")

    update()


def down():

    for _ in range(3):
        for j in range(4):
            for i in range(len(matrice)):
                if matrice[i][j].get() != "0" and i != 3:
                    if matrice[i + 1][j].get() == "0":
                        matrice[i + 1][j].set(matrice[i][j].get())
                        matrice[i][j].set("0")
                    if matrice[i + 1][j].get() == matrice[i][j].get():
                        matrice[i + 1][j].set(int(matrice[i + 1][j].get()) + int(matrice[i][j].get()))
                        matrice[i][j].set("0")

    update()


def up():

    for _ in range(3):
        for j in range(4):
            for i in range(len(matrice)):
                if matrice[i][j].get() != "0" and i != 0:
                    if matrice[i - 1][j].get() == "0":
                        matrice[i - 1][j].set(matrice[i][j].get())
                        matrice[i][j].set("0")
                    if matrice[i - 1][j].get() == matrice[i][j].get():
                        matrice[i - 1][j].set(int(matrice[i - 1][j].get()) + int(matrice[i][j].get()))
                        matrice[i][j].set("0")

    update()


Right_but = Button(text=">", command=right)
Right_but.pack(side=RIGHT)

Left_but = Button(text="<", command=left)
Left_but.pack(side=RIGHT)

down_but = Button(text="\/", command=down)
down_but.pack(side=RIGHT)

up_but = Button(text="/\\", command=up)
up_but.pack(side=RIGHT)

def KeyPressed(event):
    code = event.keycode

    if code == 38:
        up()
    elif code == 40:
        down()
    elif code == 37:
        left()
    elif code == 39:
        right()

root.bind("<KeyPress>", KeyPressed)

update()

root.mainloop()