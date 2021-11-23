from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QWidget
from x_or_o import QtWidgets, Ui_MainWindow

class Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def button_click(self):
        self.pushButton.clicked.connect(lambda: self.grapView(self))


    def grapView(self):
        scene = QGraphicsScene()
        scene.addText('Hi')
        view = QGraphicsView(scene)
        view.show()
        