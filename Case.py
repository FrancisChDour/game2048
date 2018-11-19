from imports import *
from enum import Enum

class Case(QLabel):

    def __init__(self, value, parent):
        super().__init__(parent)
        self.parent=parent
        self.setPixmap(QPixmap("images/" + str(value) + ".png"))

    def setVoid(self):
        self.setValue(0)

    def setValue(self, value):
        self.setPixmap(QPixmap("images/"+str(value)+".png"))
