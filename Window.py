from imports import *
from Solo_Window import *
from Duo_Window import *
from Solo_Window150cc import *
from Solo_Window100cc import *
from MusicManager import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500,600)
        self.setWindowTitle('Mario Kart 2048')
        self.setBg()
        self.initMenu()
        self.lauchMusic()
        self.setCenter()
        self.initButtons()
        self.show()

    def initButtons(self):

        font = QFont("Arial",40,QFont.Bold)

        button1 = QPushButton("Solo 50cc")
        button1.setFont(font)
        button1.clicked.connect(self.solo50cc)
        button1.setFixedSize(300,80)

        button2 = QPushButton("Solo 100cc")
        button2.setFont(font)
        button2.clicked.connect(self.solo100cc)
        button2.setFixedSize(300,80)

        button3 = QPushButton("Solo 150cc")
        button3.setFont(font)
        button3.clicked.connect(self.solo150cc)
        button3.setFixedSize(300,80)

        button4 = QPushButton("Duo")
        button4.setFont(font)
        button4.clicked.connect(self.duo)
        button4.setFixedSize(300,80)

        button5 = QPushButton("Quiter")
        button5.setFont(font)
        button5.clicked.connect(QApplication.instance().quit)
        button5.setFixedSize(300,80)

        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button1)
        mainLayout.addWidget(button2)
        mainLayout.addWidget(button3)
        mainLayout.addWidget(button4)
        mainLayout.addWidget(button5)
        mainLayout.setAlignment(Qt.AlignCenter)
        mainLayout.setSpacing(20)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def resizeEvent(self,e):
        self.setBg()

    def lauchMusic(self):
        self.music = Player(Music.TITLE)
        self.music.play()

    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Fichier')

        self.exitAction = QAction("&Quitter", self,
                                  icon=QIcon('images/exit.svg'),
                                  shortcut="Ctrl+Q",
                                  statusTip="Quitter l'app",
                                  triggered=QApplication.instance().quit)
        fileMenu.addAction(self.exitAction)

    def solo50cc(self):
        self.music.stop()
        self.win = Solo_Window(self)
        self.win.show()

    def solo100cc(self):
        self.music.stop()
        self.win = Solo_Window100cc(self)
        self.win.show()

    def solo150cc(self):
        self.music.stop()
        self.win = Solo_Window150cc(self)
        self.win.show()

    def duo(self):
        self.music.stop()
        self.win = Duo_Window(self)
        self.win.show()

    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setBg(self):
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("images/bg.jpg"))
        self.bg.setGeometry(0,0,self.geometry().width(),self.geometry().height())
        self.bg.show()
        QWidget.lower(self.bg)
