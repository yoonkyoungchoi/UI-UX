import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QLabel, QTextEdit, QVBoxLayout, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.Main()
        
        #윈도우 설정
        self.setWindowTitle('Secret Message')

    def Main(self):
        label1 = QLabel('삐빅 삐빅 알 수 없음', self)
        label1.move(290, 30)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        label2 = QLabel(' 좋아하는 단어와 문장을 영어로 작성하여',self)
        label2.move(260, 100)
        font2 = label2.font()
        font2.setPointSize(13)
        label2.setFont(font2)
        label3 = QLabel('암호문이 된 문장을 확인해보세요!', self)
        label3.move(290, 130)
        font3 = label3.font()
        font3.setPointSize(13)
        label3.setFont(font3)

        #암호화 할 키 입력 lable
        label4 = QLabel('암호화 할 키 입력', self)
        label4.move(360, 180)
        font4 = label4.font()
        font4.setPointSize(10)
        label4.setFont(font4)

        #key 입력하는 edit 박스
        self.text1 = QPlainTextEdit(self)
        self.text1.setGeometry(360, 199, 100, 31) # x, y, w, h

        #문자열 입력하는 lable
        label5 = QLabel('암호화 할 문장 입력', self)
        label5.move(350, 243)
        font5 = label5.font()
        font5.setPointSize(10)
        label5.setFont(font5)

        # 문자열 입력하는 lable
        self.text2 = QPlainTextEdit(self)
        self.text2.setGeometry(245, 270, 350, 40) # x, y, w, h

        #결과 출력 lable
        label6 = QLabel('결과 출력(암호화 된 문자열)', self)
        label6.move(330, 325)
        font6 = label6.font()
        font6.setPointSize(10)
        label6.setFont(font6)

        # 결과물 출력하는 text 창
        self.result_text = QPlainTextEdit(self)
        self.result_text.setGeometry(245, 349, 350, 40) # x, y, w, h

        # 결과 출력 lable
        label7 = QLabel('결과 출력(복호화 된 문자열)', self)
        label7.move(330, 400)
        font7 = label7.font()
        font7.setPointSize(10)
        label7.setFont(font7)

        # 복호화 출력하는 text 창
        self.result_text1 = QPlainTextEdit(self)
        self.result_text1.setGeometry(245, 420, 350, 40)  # x, y, w, h

        # 결과값 출력 버튼
        self.btn1 = QPushButton('결과 확인하기', self)
#        self.btn1.clicked.connect(self.show_secret())
        self.btn1.move(370, 630)
        self.btn1.resize(100, 30)

        #타이틀 메뉴
        self.setWindowTitle('Secret')
        self.setGeometry(600, 300, 800, 700) # x, y, w, h
        self.show()

        # 보안 코드

    def show_secret(self):
        self.answer_secrit = ''
        for line in self.text1.toPlainText():
            self.answer_secrit += line
#        self.result_text.insertPlainText(self.show_secret())


    def show_bokho(self):
        self.answer_secrit1 = ''
        for line2 in self.text2.toPlainText():
            self.answer_secrit1 += line2
#        self.result_text.insertPlainText(self.show_bokho())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

