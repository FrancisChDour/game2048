from imports import *
from GGrille import *

class Duo_Window(QMainWindow):
    def __init__(self, parentWin):
        super().__init__()
        self.initUI()
        self.parentWin = parentWin
        self.parentWin.hide()

    def initUI(self):
        self.setFixedSize(550,550)
        self.raceLauched = False
        self.lastTurn = False
        self.setWindowTitle('Mario Kart 2048')
        self.statusBar().showMessage("Aucun événement")
        self.initMenu()
        self.mainBox = QWidget()
        self.grille = GGrille()
        self.grille2 = GGrille()
        self.score = QLabel()
        self.score2 = QLabel()
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.score2.setText("Score : " + str(self.grille2.grille.score))
        layout = QGridLayout()
        layout.setHorizontalSpacing(100)
        layout.addWidget(self.score,0,0)
        layout.addWidget(self.score2,0,1)
        layout.addWidget(self.grille,1,0)
        layout.addWidget(self.grille2,1,1)
        self.mainBox.setLayout(layout)
        self.setCentralWidget(self.mainBox)
        self.setCenter()
        self.show()

    def closeEvent(self,e):
        self.close()
        self.parentWin.show()

    def keyPressEvent(self, event):
        if not self.grille.grille.checkWon() and not self.grille.grille.checkLoose():
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
            if self.grille.grille.checkWon():
                self.itsWin()
            if self.grille.grille.checkLoose():
                self.itsLoose()
        self.score.setText("Score : " + str(self.grille.grille.score))
        self.score2.setText("Score : " + str(self.grille2.grille.score))


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
                                  # icon=QIcon('exit.svg'),
                                  shortcut="Ctrl+R",
                                  statusTip="Recharger le jeux",
                                  triggered=self.reload)
        fileMenu.addAction(self.reloadAction)

    def itsWin(self):
        QMessageBox.about(self, "Congrats !",
                "You won the game !")

    def itsLoose(self):
        QMessageBox.about(self, "So bad !",
                "You lost the game !")

    def reload(self):
        self.grille.grille = Grille(self.grille)
        self.grille.upGrid()
        self.score.setText("Score : " + str(self.grille.grille.score))

    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
