from time import strftime
from PySide.QtCore import Qt, Slot as slut
from PySide.QtGui import *
import cache


class LogRecv(QTextEdit):

    def __init__(self):
        QTextEdit.__init__(self)

    def generate(self):
        box = QGroupBox('Log Stream')
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        box.setLayout(vbox)
        return box

    @slut(str, str)
    def on_received(self, log, request_id):
        self.append(log + '\n\n')

    def update(self, log, request_id):
        cache.call('signals').request_recv.emit(log, request_id)


class LogList(QListWidget):

    def __init__(self):
        QListWidget.__init__(self)

        self.currentItemChanged.connect(self.on_item_changed)

    def generate(self):
        box = QGroupBox('Requests history')
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        box.setLayout(vbox)
        return box

    @slut(str, str)
    def on_received(self, log, request_id):
        if request_id in cache.__list__:
            return
        cache.__list__.append(request_id)
        self.addItem('{time} - {request_id}'.format(
            time=strftime("%H:%M:%S"),
            request_id=request_id
        ))
        self.sortItems(order=Qt.DescendingOrder)

    @slut()
    def on_item_changed(self, current):
        if not current:
            return

        request_id = current.text().split(' ')[2]

        if request_id not in cache.__logs__:
            print('Not found:', current.text())
            return

        debug_info = cache.__logs__[request_id]

        debug_text = ''
        for entry in debug_info:
            debug_text += entry + '\n\n'

        cache.call('request').requests_recv.setText(debug_text)
