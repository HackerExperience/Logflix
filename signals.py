from PySide.QtCore import QObject, Signal


class Signals(QObject):

    request_sent = Signal(str, str)
    request_recv = Signal(str, str)

    def __init__(self):
        QObject.__init__(self)
