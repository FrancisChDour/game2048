from imports import *
from GGrille import *
from time import sleep
from Solo_Window import *
from Solo_Window100cc import *

class Solo_Window150cc(Solo_Window100cc):
    def __init__(self,parentWin):
        super().__init__(parentWin)

    def keyPressEvent(self, event):
        if not self.grille.grille.checkWon() and not self.grille.grille.checkLoose() and self.raceLauched:
            self.grille.grille.checkLoose()
            key = event.key()
            if key == Qt.Key_D :
                self.timer.setValue(0)
                self.grille.grille.mooveLeft()
            elif key == Qt.Key_Q :
                self.timer.setValue(0)
                self.grille.grille.mooveRight()
            elif key == Qt.Key_S :
                self.timer.setValue(0)
                self.grille.grille.mooveTop()
            elif key == Qt.Key_Z :
                self.timer.setValue(0)
                self.grille.grille.mooveBottom()
            if self.grille.grille.checkWon():
                self.itsWin()
            if self.grille.grille.checkLoose():
                self.itsLoose()
        self.score.setText("Score : " + str(self.grille.grille.score))
