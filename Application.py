#! /usr/bin/env python
# -*- coding: utf-8 -*-

from imports import *

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        self.setStyle(QStyleFactory.create('fusion'))
        p = self.palette()
        p.setColor(QPalette.Window, QColor(0,0,54))
        p.setColor(QPalette.Button, QColor(200,200,200  ))
        p.setColor(QPalette.Highlight, QColor(53,53,53))
        p.setColor(QPalette.ButtonText, QColor(53,53,53))
        p.setColor(QPalette.WindowText, QColor(255,255,255))
        self.setPalette(p)
