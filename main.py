__author__ = 'Hector Guerrero'

from PySide.QtGui import *
from PySide.QtCore import *
import sys
from mainwindowrelay import *


def main():

    app = QApplication(sys.argv)

    main_win = MainWindowRelay()

    main_win.show()

    app.exec_()

if __name__ == '__main__':

    main()
