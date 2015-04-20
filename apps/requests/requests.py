import os
from PySide.QtCore import Qt, QRegExp
from PySide.QtGui import *
from base import SCRIPT_DIRECTORY, loadUi
from apps.requests.widgets import RequestsRecv, RequestsList, RequestsSent
import cache


class Request(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'base_widget.ui'), self)

        self.signals = cache.call('signals')
        self.requests_list = RequestsList()
        self.requests_recv = RequestsRecv()
        self.requests_sent = RequestsSent()

        self.signals.request_recv.connect(self.requests_recv.on_received)
        self.signals.request_recv.connect(self.requests_list.on_received)
        self.signals.request_sent.connect(self.requests_sent.on_sent)

        layout = QGridLayout()
        layout.addWidget(self.requests_list.generate(), 0, 0)
        layout.addWidget(self.requests_sent.generate(), 0, 1)
        layout.addWidget(self.requests_recv.generate(), 1, 1)

        self.setLayout(layout)

class JSONSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        """ Constructor
        """
        super(JSONSyntaxHighlighter, self).__init__(parent)

        self.symbol_format = QTextCharFormat()
        self.symbol_format.setForeground(Qt.red)
        self.symbol_format.setFontWeight(QFont.Bold)

        self.name_format = QTextCharFormat()
        self.name_format.setForeground(Qt.blue)
        self.name_format.setFontWeight(QFont.Bold)
        self.name_format.setFontItalic(True)

        self.value_format = QTextCharFormat()
        self.value_format.setForeground(Qt.darkGreen)

    def highlightBlock(self, text):
        """ Highlight a block of code using the rules outlined in the Constructor
        """
        expression = QRegExp("(\\{|\\}|\\[|\\]|\\:|\\,)")
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length, self.symbol_format)
            index = expression.indexIn(text, index + length)

        text.replace("\\\"", "  ")

        expression = QRegExp("\".*\" *\\:")
        expression.setMinimal(True)
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length - 1, self.name_format)
            index = expression.indexIn(text, index + length)

        expression = QRegExp("\\: *\".*\"")
        expression.setMinimal(True)
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length - 1, self.value_format)
            index = expression.indexIn(text, index + length)

