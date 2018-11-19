#! /usr/bin/env python
# -*- coding: utf-8 -*-

from imports import *
from Case import Case

class GGrille(QWidget):
    def __init__(self):
        super().__init__()
        self.lastTurn = False
        self.setFixedSize(QSize(450,450))
        self.grille = Grille(self)
        pos = [0,110,220,330]
        self.grid = []
        pal = QPalette()
        pal.setColor(QPalette.Background,Qt.darkGray)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        for i in range(4):
            self.grid.append([])
            for y in range(4):
                self.grid[i].append(0)
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            for y in range(4):
                self.grid[i][y] = Case(0,self)
                self.grid[i][y].move(pos[i]+10,pos[y]+10)
        self.show()
        self.upGrid()

    def upGrid(self):
        for i in range(4):
            for y in range(4):
                self.grid[i][y].setValue(self.grille.grille[y][i])
