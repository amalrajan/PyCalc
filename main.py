# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from ui import UserInterface

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UserInterface()
        self.ui.initialize_ui(self)
        self.show()

app = QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec_())