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
        btn.clicked.connect(QCoreApplication.instance().quit) # 버튼 누르면 창 꺼짐
        #btn.center


        self.resize(320, 240)
        self.setWindowTitle('두 번째 시간')

        self.show()
    ######## 이벤트 연결 방법 ###########
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self,"종료 확인","종료하시겠습니까?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept() # CloseEvent 실행
        else:
            QCloseEvent.ignore() # CloseEvent 무시


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())