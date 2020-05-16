import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = QMainWindow()
  gui = Ui_MainWindow()
  gui.setupUi(win)
  win.show()
  sys.exit(app.exec_())
