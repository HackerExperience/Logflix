from PySide.QtGui import QApplication
import sys
import cache
from mainwindow import MainWindow
from apps.requests.requests import Request
from signals import Signals
from services.user import ServiceUser
from websocket import ws


cache.register('main', MainWindow)
cache.register('request', Request)
cache.register('user', ServiceUser)
cache.register('signals', Signals)
cache.ws = ws


def main():
    app = QApplication(sys.argv)
    cache.call('main').show()
    app.exec_()

if __name__ == '__main__':
    main()
