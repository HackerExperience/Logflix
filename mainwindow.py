import os
from base import loadUi, SCRIPT_DIRECTORY
from PySide.QtCore import Slot as slut
from PySide.QtGui import *
import cache


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'mainwindow.ui'), self)

    @slut()
    def on_btnUser_clicked(self):
        self.hide()
        cache.call('user').show()

    @slut()
    def on_btnReq_clicked(self):
        cache.call('request').show()
