# QMainWindow 의 Menu Bar 사용하기
# Menu Bar를 생성하고, QAction을 등록한다.
# QAction은 slot 함수를 등록해, User가 원하는 동작을 수행할 수 있다.
# QAciont은 단축키를 등록해 쉽게 조작이 가능하다.

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("하하호호는까지는 아닌 메모장")
        self.setGeometry(0, 0, 300, 300)

        self.vlay = QVBoxLayout()
        # self.lbl = QLabel("KFC")
        # self.btn = QPushButton("클릭")
        # self.vlay.addWidget(self.lbl)
        # self.vlay.addWidget(self.btn)
        self.lineEdit = QPlainTextEdit(self)
        self.vlay.addWidget(self.lineEdit)
        self.bar = self.statusBar()

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # menuBar객체 menu 생성, menuBar() 는 QMainWindow 에 멤버함수
        self.menu = self.menuBar()
        # menuBar 에 File 메뉴 추가, &를 붙이면 단축키 사용이 가능하다. Alt+F
        self.menuFile = self.menu.addMenu("&File")
        # menuBar 에 Edit 메뉴 추가, &를 붙이면 단축키 사용이 가능하다. Alt+E
        self.menuEdit = self.menu.addMenu("&Help")

        # QAction() 객체 생성, 단축키 사용
        self.openAction = QAction("&Open", self)
        # openAction 과 open() 를 연결, Open 메뉴 클릭 시, open() 호출
        self.openAction.triggered.connect(self.open)
        # 키보드 단축키 추가, Ctrl+O 누르면 Open 메뉴 선택
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))

        # QAction() 객체 생성, 단축키 사용
        self.saveAction = QAction("&Save", self)
        # saveAction 과 save() 를 연결, Save 메뉴 클릭 시, save() 호출
        self.saveAction.triggered.connect(self.save)
        # 키보드 단축키 추가, Ctrl+O 누르면 Open 메뉴 선택
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))

        # QAction() 객체 생성, 단축키 사용
        self.saveAsAction = QAction("&SaveAs", self)
        # openAction 과 open() 를 연결, Open 메뉴 클릭 시, open() 호출
        self.saveAsAction.triggered.connect(self.saveAs)
        # 키보드 단축키 추가, Ctrl+O 누르면 Open 메뉴 선택
        self.saveAsAction.setShortcut(QKeySequence("Ctrl+Shift+S"))

        # QAction() 객체 생성, 단축키 사용
        self.closeAction = QAction("&Close", self)
        # openAction 과 open() 를 연결, Open 메뉴 클릭 시, open() 호출
        self.closeAction.triggered.connect(self.close)
        # # 키보드 단축키 추가, Ctrl+O 누르면 Open 메뉴 선택
        # self.closeAction.setShortcut(QKeySequence(""))

        # menuFile 에 openAction 객체 등록, File 메뉴 클릭 시, Open 메뉴 창이 나타난다.
        self.menuFile.addAction(self.openAction)
        self.menuFile.addAction(self.saveAction)
        self.menuFile.addAction(self.saveAsAction)
        self.menuFile.addAction(self.closeAction)


    def open(self):
        self.bar.showMessage("Open 메뉴 클릭")

    def save(self):
        self.bar.showMessage("Save 메뉴 클릭")

    def saveAs(self):
        self.bar.showMessage("Save As 메뉴 클릭")

    def close(self):
        quit()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()