from PySide.QtCore import QObject, Signal


class Signals(QObject):

    request_sent = Signal(dict)
    request_recv = Signal(dict)

    def __init__(self):
        QObject.__init__(self)
