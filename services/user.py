import os
from PySide.QtGui import *
from PySide.QtCore import Slot as slut
from base import SCRIPT_DIRECTORY, loadUi, BaseDialog
from apps.requests.send import request_send


class ServiceUser(QMainWindow):

    class Login(BaseDialog):

        def __init__(self):
            BaseDialog.__init__(self)

            self.add_field('Username')
            self.add_field('Password')

            self.generate_form()

        @slut()
        def on_btnSubmit_clicked(self):

            username = self.input['username'].text()
            password = self.input['password'].text()

            if not username or not password:
                return self.popup('Empty values')

            request_send('user.1.login', {'username': username, 'password':
                password})

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(os.path.join(SCRIPT_DIRECTORY, 'user/service_user.ui'), self)

    @slut()
    def on_btnLogin_clicked(self):
        self.Login().show()

    @slut()
    def dialog_login(self):
        layout = QVBoxLayout()
        layout.addWidget(QLineEdit('oi'))
        layout.addWidget(QPushButton("Show Greetings"))
        self.login = layout
