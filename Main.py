from        MainScreen.MainScreen               import MainScreen
from        PyQt5                               import QtCore, QtGui, QtWidgets, Qt
from        PyQt5.QtCore                        import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from         PyQt5                              import QtCore, QtGui, QtWidgets
from         PyQt5                              import QtGui
from         PyQt5                              import QtWidgets
from         PyQt5.QtGui                        import QPixmap,QColor
from         PyQt5.QtWidgets                    import *
import       sys
import       os
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(800, 480)
        self.setMinimumSize(QtCore.QSize(800, 480))
        self.setMaximumSize(QtCore.QSize(800, 480))

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))

        self.frameContain = QtWidgets.QFrame(self.centralWidget)
        self.mainScreenObj = MainScreen(self.frameContain)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
