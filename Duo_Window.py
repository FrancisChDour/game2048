from imports import *
from GGrille import *
from time import sleep
from Solo_Window import *

class Duo_Window(Solo_Window):
    def __init__(self,parentWin):
        super().__init__(parentWin)

    def initUI(self):
        self.setFixedSize(1200,550)
        self.setWindowTitle('Mario Kart 2048')
        self.statusBar().showMessage("Aucun événement")
        self.initMenu()
        self.background()
        self.initClock()
        self.mainBox = QWidget()
        self.grille = GGrille()
        self.grille2 = GGrille()
        self.score = QLabel()
        self.score2 = QLabel()
        self.score.setFont(QFont('Arial',30))
        self.score2.setFont(QFont('Arial',30))
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.score2.setText("Score : " + str(self.grille2.grille.score))
        layout = QGridLayout()
        layout.setHorizontalSpacing(100)
        layout.addWidget(self.score,0,0)
        layout.addWidget(self.score2,0,1)
        layout.addWidget(self.grille,1,0)
        layout.addWidget(self.grille2,1,1)
        self.mainBox.setLayout(layout)
        self.startRace()
        self.setCentralWidget(self.mainBox)
        self.setCenter()
        self.show()

    def keyPressEvent(self, event):
        if not self.grille.grille.checkWon() and not self.grille.grille.checkLoose() and self.raceLauched:
            self.grille.grille.checkLoose()
            key = event.key()
            if key == Qt.Key_Q :
                self.grille.grille.mooveLeft()
            elif key == Qt.Key_D :
                self.grille.grille.mooveRight()
            elif key == Qt.Key_Z :
                self.grille.grille.mooveTop()
            elif key == Qt.Key_S :
                self.grille.grille.mooveBottom()
            elif key == Qt.Key_Left:
                self.grille2.grille.mooveLeft()
            elif key == Qt.Key_Right:
                self.grille2.grille.mooveRight()
            elif key == Qt.Key_Down:
                self.grille2.grille.mooveBottom()
            elif key == Qt.Key_Up:
                self.grille2.grille.mooveTop()
            if self.grille.grille.checkWon() or self.grille2.grille.checkWon():
                self.itsWin()
            if self.grille.grille.checkLoose() or self.grille2.grille.checkLoose():
                self.itsLoose()

        self.score.setText("Score : " + str(self.grille.grille.score))
        self.score2.setText("Score : " + str(self.grille2.grille.score))
