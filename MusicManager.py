from imports import *
from enum import Enum

class Music(Enum):

    TITLE = "musics/title.wav"
    START = "musics/start.wav"
    GAME = "musics/game.wav"
    GAME_FAST = "musics/gameFast.wav"
    LAST_TURN = "musics/lastTurn.wav"
    FAILURE = "musics/failure.wav"

class Player(QSoundEffect):
    def __init__(self):
        super().__init__()

    def __init__(self, music):
        super().__init__()
        self.setSource(QUrl.fromLocalFile(music.value))

    def setMusic(self, music):
        self.setSource(QUrl.fromLocalFile(music.value))

    def infiniteLoopCount(self):
        self.setLoopCount(1000)
