from imports import *
from GGrille import *
from time import sleep
from Solo_Window import *

class Solo_Window100cc(Solo_Window):
    def __init__(self,parentWin):
        super().__init__(parentWin)

    def initUI(self):
        self.setFixedSize(550,600)
        self.raceLauched = False
        self.lastTurn = False
        self.background()
        self.setWindowTitle('Mario Kart 2048')
        self.statusBar().showMessage("Aucun événement")
        self.initMenu()
        self.initClock()
        self.mainBox = QWidget()
        self.grille = GGrille()
        self.initScore()
        self.initTimer()
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.score,0,0)
        layout.addWidget(self.clock,0,1)
        layout.addWidget(self.timer,1,0,1,2)
        layout.addWidget(self.grille,2,0,1,2)
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
                self.timer.setValue(0)
                self.grille.grille.mooveLeft()
                self.statusBar().showMessage("Gauche")
            elif key == Qt.Key_D :
                self.timer.setValue(0)
                self.grille.grille.mooveRight()
                self.statusBar().showMessage("Droite")
            elif key == Qt.Key_Z :
                self.timer.setValue(0)
                self.grille.grille.mooveTop()
                self.statusBar().showMessage("Haut")
            elif key == Qt.Key_S :
                self.timer.setValue(0)
                self.grille.grille.mooveBottom()
                self.statusBar().showMessage("Bas")
            if self.grille.grille.checkWon():
                self.itsWin()
            if self.grille.grille.checkLoose():
                self.itsLoose()
        self.score.setText("Score : " + str(self.grille.grille.score))

        if not self.lastTurn:
            for i in range(4):
                for y in range(4):
                    if self.grille.grille.grille[i][y] == 1024:
                        self.lastTurn = True
                        self.lastTurnMusic()

    def forcedMove(self):
        if not self.grille.grille.checkWon() and not self.grille.grille.checkLoose() and self.raceLauched:
            self.timer.setValue(0)
            self.grille.grille.checkLoose()
            possibleKeys = [Qt.Key_Q,Qt.Key_D,Qt.Key_Z,Qt.Key_S]
            key = possibleKeys[randint(0,3)]
            if key == Qt.Key_Q :
                self.grille.grille.mooveLeft()
            elif key == Qt.Key_D :
                self.grille.grille.mooveRight()
            elif key == Qt.Key_Z :
                self.grille.grille.mooveTop()
            elif key == Qt.Key_S :
                self.grille.grille.mooveBottom()
            if self.grille.grille.checkWon():
                self.itsWin()
            if self.grille.grille.checkLoose():
                self.itsLoose()
        self.score.setText("Score : " + str(self.grille.grille.score))

        if not self.lastTurn:
            for i in range(4):
                for y in range(4):
                    if self.grille.grille.grille[i][y] == 1024:
                        self.lastTurn = True
                        self.lastTurnMusic()

    def initTimer(self):
        self.timer = QProgressBar()
        self.timer.setFixedWidth(450)
        self.timer.setRange(0,100)
        self.pbTimer = QTimer()
        self.pbTimer.timeout.connect(self.incrementTimer)

    def incrementTimer(self):
        self.timer.setValue(self.timer.value()+1)
        if(self.timer.value()==self.timer.maximum()):
            self.forcedMove()
        self.pbTimer.start(10)

    def fastMusic(self):
        self.timer.setRange(0,50)
        self.music.setMusic(Music.GAME_FAST)
        self.music.infiniteLoopCount()
        self.music.play()

    def lauchRace(self):
        self.statusBar().showMessage("Partez !")
        self.raceLauched = True
        self.pbTimer.start(10)
        self.incrementTimer()
        QTimer.singleShot(1000, self.lauchMusic)
        self.clockTimer.start(1000)

    def reload(self):
        self.clockTimer.stop()
        self.pbTimer.stop()
        self.timer.setValue(0)
        self.clock.display(0)
        self.grille.grille = Grille(self.grille)
        self.grille.upGrid()
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.startRace()
