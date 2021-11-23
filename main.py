from Window import Window
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = Window()
        # ui = Ui_MainWindow()
        # # ui.setupUi(MainWindow)
        MainWindow.show()
        # h = ui.graphicsView.height()
        # w = ui.graphicsView.width()  
        sys.exit(app.exec_())