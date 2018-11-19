#!/bin/python3

from random import randint

class Grille:

    def __init__(self, win):
        self.score = 0
        self.win = win
        self.grille = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.voidCases = []
        self.values = [2,2,2,2,2,2,2,2,2,4]
        for i in range(4):
            for y in range(4):
                self.voidCases.append((i,y))
        for i in range(2):
            self.addBloc()

    def __str__(self):
        ret = ""
        for i in range(4):
            for y in range(4):
                ret+= str(self.grille[i][y]) + " "
            ret += "\n"
        return ret

    def addBloc(self):
        self.chekVoid()
        if not len(self.voidCases) == 0:
            x = randint(0,len(self.voidCases)-1)
            a = self.voidCases[x]
            del self.voidCases[x]
        self.grille[a[0]][a[1]] = self.values[randint(0,9)]

    def mooveLeft(self):
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(4):
                for y in range(1,4):
                    if not self.grille[i][y] == 0:
                        if self.grille[i][y-1] == 0:
                            done = False
                            mvmt = True
                            self.grille[i][y-1] = self.grille[i][y]
                            self.grille[i][y] = 0
                        elif self.grille[i][y] == self.grille[i][y-1]  and self.grille[i][y] > 1:
                            done = False
                            mvmt = True
                            self.score += self.grille[i][y]*2
                            self.grille[i][y-1] *=-2
                            self.grille[i][y] = 0

        if mvmt :
            self.allPositive()
            self.addBloc()
            self.win.upGrid()

    def mooveRight(self):
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(4):
                for y in range(0,3):
                    if not self.grille[i][y] == 0:
                        if self.grille[i][y+1] == 0:
                            done = False
                            mvmt = True
                            self.grille[i][y+1] = self.grille[i][y]
                            self.grille[i][y] = 0
                        elif self.grille[i][y] == self.grille[i][y+1]  and self.grille[i][y] > 1:
                            done = False
                            mvmt = True
                            self.score += self.grille[i][y]*2
                            self.grille[i][y+1] *=-2
                            self.grille[i][y] = 0

        if mvmt:
            self.allPositive()
            self.addBloc()
            self.win.upGrid()

    def mooveTop(self):
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(1,4):
                for y in range(0,4):
                    if not self.grille[i][y] == 0:
                        if self.grille[i-1][y] == 0:
                            done = False
                            mvmt = True
                            self.grille[i-1][y] = self.grille[i][y]
                            self.grille[i][y] = 0
                        elif self.grille[i][y] == self.grille[i-1][y]  and self.grille[i][y] > 1:
                            done = False
                            mvmt = True
                            self.score += self.grille[i][y]*2
                            self.grille[i-1][y] *=-2
                            self.grille[i][y] = 0

        if mvmt:
            self.allPositive()
            self.addBloc()
            self.win.upGrid()

    def mooveBottom(self):
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(0,3):
                for y in range(0,4):
                    if not self.grille[i][y] == 0:
                        if self.grille[i+1][y] == 0:
                            done = False
                            mvmt = True
                            self.grille[i+1][y] = self.grille[i][y]
                            self.grille[i][y] = 0
                        elif self.grille[i][y] == self.grille[i+1][y] and self.grille[i][y] > 1:
                            done = False
                            mvmt = True
                            self.score += self.grille[i][y]*2
                            self.grille[i+1][y] *=-2
                            self.grille[i][y] = 0

        if mvmt:
            self.allPositive()
            self.addBloc()
            self.win.upGrid()

    def chekVoid(self):
        self.voidCases = []
        for i in range(4):
            for y in range(4):
                if self.grille[i][y] == 0:
                    self.voidCases.append((i,y))

    def checkWon(self):
        for i in range(4):
            for y in range(4):
                if self.grille[i][y] == 2048:
                    return True
        return False

    def checkLoose(self):
        if len(self.voidCases) == 0:
            for i in range(4):
                for y in range(0,3):
                    if self.grille[i][y] == self.grille[i][y+1]:
                        return False
            for i in range(0,3):
                for y in range(4):
                    if self.grille[i][y] == self.grille[i+1][y]:
                        return False
            return True

    def allPositive(self):
        for i in range(4):
            for y in range(4):
                if self.grille[i][y] < 0:
                    self.grille[i][y] *= -1
