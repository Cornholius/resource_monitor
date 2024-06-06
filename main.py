import psutil
import os
from time import sleep
from PyQt5 import QtWidgets, uic
import sys
from ui.main import MainWindow, Window


from PyQt5.QtCore import Qt

app = QtWidgets.QApplication([])
win = MainWindow()
win.show()

# window = Window()
# window.show()
sys.exit(app.exec())
