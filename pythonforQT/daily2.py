from PySide6.QtWidgets import *
from PySide6.QtGui import *

names=[]
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Inmac Management System")
        self.setGeometry(900, 300, 300, 300)

        self.vlay = QVBoxLayout()
        self.edit = QLineEdit()
        self.lbl = QLabel("name")
        self.hl = QHBoxLayout()
        self.hl.addWidget(self.lbl)
        self.hl.addWidget(self.edit)
        self.vlay.addLayout(self.hl)

        self.hlay = QHBoxLayout()
        self.btnAdd = QPushButton("추가")
        self.btnAdd.clicked.connect(self.add)
        self.btnRmv = QPushButton("제거")
        self.btnRmv.clicked.connect(self.remove)
        self.hlay.addWidget(self.btnAdd)
        self.hlay.addWidget(self.btnRmv)

        self.vlay.addLayout(self.hlay)

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # statusBar() 객체 생성
        self.bar = self.statusBar()

        # menuBar객체 menu 생성, menuBar() 는 QMainWindow 에 멤버함수
        self.menu = self.menuBar()
        # menuBar 에 File 메뉴 추가, &를 붙이면 단축키 사용이 가능하다. Alt+F
        self.menuMenu = self.menu.addMenu("메뉴")
        # menuBar 에 Edit 메뉴 추가, &를 붙이면 단축키 사용이 가능하다. Alt+E
        self.menuQuit = self.menu.addMenu("종료")

        self.addAction = QAction("추가", self)
        self.addAction.triggered.connect(self.add)
        self.rmvAction = QAction("제거", self)
        self.rmvAction.triggered.connect(self.remove)

        self.doneAction = QAction("종료", self)
        self.doneAction.triggered.connect(self.done)

        # menuFile 에 openAction 객체 등록, File 메뉴 클릭 시, Open 메뉴 창이 나타난다.
        self.menuMenu.addAction(self.addAction)
        self.menuMenu.addAction(self.rmvAction)
        self.menuQuit.addAction(self.doneAction)

    def add(self):
        name = self.edit.text()
        if name in names:
            self.bar.showMessage("이미 존재하는 이름입니다.")
        elif len(name)==0:
            self.bar.showMessage("이름을 입력하세요.")
        else:
            names.append(name)
            self.bar.showMessage("추가되었습니다.")

    def remove(self):
        name = self.edit.text()
        if len(name) == 0:
            self.bar.showMessage("이름을 입력하세요.")
        elif name not in names:
            self.bar.showMessage("등록되어 있지 않은 이름입니다.")
        else:
            names.remove(name)
            self.bar.showMessage("제거되었습니다.")

    def done(self):
        quit()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()