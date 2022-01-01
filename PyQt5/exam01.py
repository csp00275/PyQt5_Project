import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('push me', self)
        btn.resize(btn.sizeHint())
        # btn.setToolTip('툴팁입니다.<b>안녕하세요<b/>')
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit)
        #btn.center


        self.resize(320, 240)
        self.setWindowTitle('두 번째 시간')

        self.show()
    def closeEvent(self, QCloseEvent):
        QMessageBox.question()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())