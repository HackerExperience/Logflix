import os
from PySide.QtGui import *
import cache
from logs.widgets import LogRecv, LogList
from base import SCRIPT_DIRECTORY, loadUi


class Log(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'base_widget.ui'), self)

        self.signals = cache.call('signals')
        self.requests_list = LogList()
        self.requests_recv = LogRecv()
        #self.requests_sent = RequestsSent()

        self.signals.request_recv.connect(self.requests_recv.on_received)
        self.signals.request_recv.connect(self.requests_list.on_received)
        #self.signals.request_sent.connect(self.requests_sent.on_sent)

        layout = QGridLayout()
        layout.addWidget(self.requests_list.generate(), 0, 0)
        #layout.addWidget(self.requests_sent.generate(), 0, 1)
        layout.addWidget(self.requests_recv.generate(), 0, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)

        self.setLayout(layout)
