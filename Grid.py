from imports import *
from Case import *

class Grid(QWidget):
    def __init__(self):
        super().__init__()
        self.score=0
        self.setFixedSize(450,450)
        pal = QPalette()
        pal.setColor(QPalette.Background,Qt.darkGray)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.initGrid()
        self.show()
        self.test()

    def initGrid(self):
        self.initGGrille()

    def test(self):
        self.moveLeft()
        print(self.getNGrille())

    def initGGrille(self):
        self.voidCases = []
        self.toUpdate=[]
        self.values = [2,2,2,2,2,2,2,2,2,4]
        bg=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        pos = [0,110,220,330]
        self.gGrille = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for y in range(4):
            for i in range(4):
                self.gGrille[i][y] = Case(0,self,pos[y]+10,pos[i]+10)
        for i in range(2):
            pass
        self.gGrille[0][0].setValue(4)
        self.gGrille[0][0].update()
        self.gGrille[0][1].setValue(4)
        self.gGrille[0][1].update()
        self.gGrille[0][2].setValue(2)
        self.gGrille[0][2].update()
        self.gGrille[0][3].setValue(2)
        self.gGrille[0][3].update()

    def addBloc(self):
        self.chekVoid()
        if not len(self.voidCases) == 0:
            x = randint(0,len(self.voidCases)-1)
            a = self.voidCases[x]
            del self.voidCases[x]
        self.gGrille[a[0]][a[1]].setValue(self.values[randint(0,9)])
        self.gGrille[a[0]][a[1]].update()

    def chekVoid(self):
        self.voidCases = []
        for i in range(4):
            for y in range(4):
                if self.gGrille[i][y].value == 0:
                    self.voidCases.append((i,y))

    def moveLeft(self):
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(4):
                for y in range(1,4):
                    if not self.gGrille[i][y].value == 0:
                        if self.gGrille[i][y-1].value == 0:
                            done = False
                            mvmt = True
                            self.gGrille[i][y].futur+=1
                            self.gGrille[i][y-1],self.gGrille[i][y] = self.gGrille[i][y],self.gGrille[i][y-1]
                        elif self.gGrille[i][y].value == self.gGrille[i][y-1].value  and self.gGrille[i][y-1].fusion:
                            done = False
                            mvmt = True
                            self.gGrille[i][y].futur+=1
                            self.gGrille[i][y].fusionWith=self.gGrille[i][y-1]
                            # self.gGrille[i][y].fusion=False
                            # self.score += self.gGrille[i][y].value*2
                            self.gGrille[i][y].value *= 2
                            self.gGrille[i][y-1].setValue(0)
                            self.gGrille[i][y-1],self.gGrille[i][y] = self.gGrille[i][y],self.gGrille[i][y-1]

        if mvmt :
            for i in range(4):
                for y in range(4):
                    if self.gGrille[i][y].futur > 0:
                        self.gGrille[i][y].leftEffect()
                    pass
            # QTimer.singleShot(130, self.update)
            # print(self.getNGrille())
            # self.allPositive()
            # self.addBloc()

    def moveRight(self):
        print(self.getNGrille())
        done = False
        mvmt = False
        while(not done):
            done = True
            for i in range(4):
                for y in range(0,3):
                    if not self.gGrille[i][y].value == 0:
                        if self.gGrille[i][y+1].value == 0:
                            done = False
                            mvmt = True
                            self.gGrille[i][y].futur+=1
                            self.gGrille[i][y+1],self.gGrille[i][y] = self.gGrille[i][y],self.gGrille[i][y+1]
        if mvmt :
            for i in range(4):
                for y in range(4):
                    self.gGrille[i][y].rightEffect()
            print(self.getNGrille())

    # def allPositive(self):
    #     for i in range(4):
    #         for y in range(4):
    #             if self.nGrille[i][y] < 0:
    #                 self.nGrille[i][y] *= -1

    def update(self):
        pos = [0,110,220,330]
        for y in range(4):
            for i in range(4):
                self.gGrille[i][y].update()
                self.gGrille[i][y].setGeometry(pos[y]+10,pos[i]+10,100,100)
        print(self.getNGrille())

    def getNGrille(self):
        ret = ""
        for i in range(4):
            for y in range(4):
                ret+= str(self.gGrille[i][y].value) + " "
            ret += "\n"
        return ret


app = Application(sys.argv)
win = Grid()
sys.exit(app.exec_())
