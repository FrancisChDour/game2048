from imports import *
from GGrille import *
from time import sleep
from MusicManager import *

class Solo_Window(QMainWindow):
    def __init__(self,parentWin):
        super().__init__()
        self.parentWin = parentWin
        self.initUI()
        self.parentWin.hide()

    def initUI(self):
        self.setFixedSize(550,550)
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
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.score,0,0)
        layout.addWidget(self.clock,0,1)
        layout.addWidget(self.grille,1,0,1,2)
        self.mainBox.setLayout(layout)
        self.startRace()
        self.setCentralWidget(self.mainBox)
        self.setCenter()
        self.show()

    def initClock(self):
        self.clock = QLCDNumber()
        self.clock.setFixedWidth(150)
        self.initDate = QDate.currentDate()
        self.clockTimer = QTimer()
        self.clockTimer.timeout.connect(self.updateClock)

    def updateClock(self):
        self.clock.display(self.clock.value()+1)
        self.clockTimer.start(1000)

    def background(self):
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("images/bg.jpg"))
        self.bg.setGeometry(0,0,self.geometry().width(),self.geometry().height())
        QWidget.lower(self.bg)
        self.bg.show()

    def initScore(self):
        self.score = QLabel()
        self.score.setFixedWidth(300)
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.score.setFont(QFont("Arial",30,QFont.Bold))


    def startRace(self):
        self.statusBar().showMessage("3 - 2 - 1 ...")
        self.raceLauched = False
        self.lastTurn = False
        self.music = self.parentWin.music
        self.music = Player(Music.START)
        self.music.play()

        QTimer.singleShot(3500, self.lauchRace)

    def lauchRace(self):
        self.statusBar().showMessage("Partez !")
        self.raceLauched = True
        QTimer.singleShot(1000, self.lauchMusic)
        self.clockTimer.start(1000)

    def lauchMusic(self):
        self.music.setMusic(Music.GAME)
        self.music.infiniteLoopCount()
        self.music.play()

    def lastTurnMusic(self):
        self.music.setMusic(Music.LAST_TURN)
        self.music.play()
        QTimer.singleShot(3500, self.fastMusic)

    def fastMusic(self):
        self.music.setMusic(Music.GAME_FAST)
        self.music.infiniteLoopCount()
        self.music.play()

    def closeEvent(self,e):
        self.music.setMuted(True)
        self.close()
        self.parentWin.show()
        self.parentWin.lauchMusic()

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

    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Fichier')

        self.exitAction = QAction("&Quitter", self,
                                  icon=QIcon('images/exit.svg'),
                                  shortcut="Ctrl+Q",
                                  statusTip="Quitter l'app",
                                  triggered=self.closeEvent)
        fileMenu.addAction(self.exitAction)

        self.reloadAction = QAction("&Reload", self,
                                  shortcut="Ctrl+R",
                                  statusTip="Recharger le jeux",
                                  triggered=self.reload)
        fileMenu.addAction(self.reloadAction)

    def itsWin(self):
        QMessageBox.about(self, "Congrats !","You won the game !")

    def itsLoose(self):
        self.clockTimer.stop()
        self.music = Player(Music.FAILURE)
        self.music.play()
        QMessageBox.about(self, "So bad !","You lost the game !")

    def reload(self):
        self.clockTimer.stop()
        self.clock.display(0)
        self.grille.grille = Grille(self.grille)
        self.grille.upGrid()
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.startRace()

    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
