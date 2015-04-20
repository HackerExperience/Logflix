import json
from time import strftime
from PySide.QtCore import Qt, Slot as slut
from PySide.QtGui import *
import cache


class RequestsRecv(QTextEdit):

    def __init__(self):
        QTextEdit.__init__(self)

    def generate(self):
        box = QGroupBox('Requests Received')
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        box.setLayout(vbox)
        return box

    @slut(dict)
    def on_received(self, request):
        self.setText(json.dumps(request))

    def update(self, request):
        cache.call('signals').request_recv.emit(request)


class RequestsSent(QTextEdit):

    def __init__(self):
        QTextEdit.__init__(self)

    def generate(self):
        box = QGroupBox('Request information')
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        self.form = QFormLayout()
        self.form.addRow(QPushButton('Submit again'))
        vbox.addLayout(self.form)
        box.setLayout(vbox)

        return box

    @slut(dict)
    def on_sent(self, request):
        self.setText(json.dumps(request))

    def update(self, request):
        cache.call('signals').request_sent.emit(request)


class RequestsList(QListWidget):

    def __init__(self):
        QListWidget.__init__(self)

        self.currentItemChanged.connect(self.on_item_changed)

    def generate(self):
        box = QGroupBox('Requests history')
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        box.setLayout(vbox)
        return box

    @slut(dict)
    def on_received(self, request):
        if request['request_id'] not in cache.__waiting_requests__:
            return
        self.addItem('{time} - {topic} - {request_id}'.format(
            time=strftime("%H:%M:%S"),
            topic=cache.__pending_requests__[0]['topic'],
            request_id=request['request_id']
        ))
        self.sortItems(order=Qt.DescendingOrder)


    @slut()
    def on_item_changed(self, current):
        if not current:
            return

        request_id = current.text().split(' - ')[2]

        if request_id not in cache.__requests__:
            print('Not found:', current.text())
            return

        request_info = cache.__requests__[request_id]

        request_sent = json.dumps(request_info['sent'])
        request_recv = json.dumps(request_info['recv'])

        cache.call('request').requests_sent.setText(request_sent)
        cache.call('request').requests_recv.setText(request_recv)
