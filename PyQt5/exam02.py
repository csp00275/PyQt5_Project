import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("csp00275@skku.edu")

        menu = self.menuBar()               # 메뉴바 생성
        menuFile = menu.addMenu("File")     # 그룹 생성
        menuEdit = menu.addMenu("Edit")     # 그룹 생성

        FileExit = QAction('Exit',self)     # 메뉴 객체 생성
        FileExit.setShortcut('Ctrl+Q')
        FileExit.setStatusTip("누르면 장재권 바보됨")

        FileNew = QMenu('New',self)

        menuFile.addMenu(FileNew)
        menuFile.addAction(FileExit)

        self.resize(450, 400)
        self.show()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())