#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox


def about():
    tkMessageBox.showinfo("Map colorizer", "Input: description of lands on map by set of segments \
    (land is polygon).\nOutput: minimal set of colors, needed to colorize this map\
    \n(2 subcontract lands can`t have same colors),and draw picture.\
    \nNote: Program with visualization.\nLook for documentation !Documentation.txt\
    \n\ntask_map.py v2.0\n\nMuzafarov Makc")


def visualization(world):
    color = world.color
    lands = world.lands
    graph = world.graph
    root = Tk()
    root.title(u'Map colorizer')
    canv = Canvas(root,
                  width=800, height=500,
                  bg="lightgray", cursor="pencil")
    canv.pack()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
    colors = (0, "red", "blue", "green", "yellow", "brown")
    land = []
    for i in range(len(lands)):
        a = map(lambda x: map(lambda y: map(lambda z: z * 100, y), x),
                lands[graph[i][0]])
        land.append(canv.create_polygon(a, fill="gray", outline="black"))

    def painting(event):
        for i in range(len(lands)):
            canv.itemconfig(land[i], fill=colors[color[i]])

    canv.create_text(400, 450, text="For colorize map, left click",
                     fill="Black", font=("Helvectica", "14"))
    max = 0
    for i in range(len(color)):
        if color[i] > max:
            max = color[i]
    canv.create_text(400, 480, text="Nubmer of colors = {0}".format(max),
                     fill="purple", font=("Helvectica", "14"))
    canv.bind("<Button-1>", painting)
    root.mainloop()
