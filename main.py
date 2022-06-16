import sys
from PyQt5.QtWidgets import *
from Gui.MainActivity.MainActivity import MainActivity

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainActivity = MainActivity()
    sys.exit(app.exec_())
