#!/home/anand/python_venv/bin/python

from uifunction import UI
from PySide6 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = UI()
    window.show()
    sys.exit(app.exec())
