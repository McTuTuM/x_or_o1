from x_or_o import QtWidgets
from general import window
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.show()
    sys.exit(app.exec_())