import sys

from PySide.QtGui import QApplication

import cache
from logs.requests import Log
from signals import Signals
from logs.consumer import consumer, stop_consumer


cache.register('request', Log)
cache.register('signals', Signals)
cache.consumer = consumer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cache.call('request').show()
    app.exec_()
    stop_consumer()
