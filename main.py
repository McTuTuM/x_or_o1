from x_or_o import QtWidgets, Ui_MainWindow
from general import window
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        print(ui.graphicsView)
        sys.exit(app.exec_())