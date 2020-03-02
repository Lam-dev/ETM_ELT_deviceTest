# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 480)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(14, 16, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(2, 4, 463, 189))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox_choseConnectForFGPsensor = QtWidgets.QComboBox(self.frame)
        self.comboBox_choseConnectForFGPsensor.setGeometry(QtCore.QRect(244, 4, 207, 43))
        self.comboBox_choseConnectForFGPsensor.setObjectName("comboBox_choseConnectForFGPsensor")
        self.comboBox_choseConnectForFGPsensor.addItem("")
        self.comboBox_choseConnectForFGPsensor.addItem("")
        self.comboBox_choseConnectForFGPsensor.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(8, 16, 229, 19))
        self.label_2.setObjectName("label_2")
        self.pushButton_addFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_addFGP.setGeometry(QtCore.QRect(20, 58, 125, 59))
        self.pushButton_addFGP.setObjectName("pushButton_addFGP")
        self.label_forShowFGPnotify = QtWidgets.QLabel(self.frame)
        self.label_forShowFGPnotify.setGeometry(QtCore.QRect(12, 130, 431, 51))
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(0, 132, 0);\n"
"font: 75 bold 12pt \"Ubuntu\";")
        self.label_forShowFGPnotify.setText("")
        self.label_forShowFGPnotify.setObjectName("label_forShowFGPnotify")
        self.pushButton_findFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_findFGP.setGeometry(QtCore.QRect(158, 58, 125, 59))
        self.pushButton_findFGP.setObjectName("pushButton_findFGP")
        self.pushButton_deleteFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteFGP.setGeometry(QtCore.QRect(298, 58, 125, 59))
        self.pushButton_deleteFGP.setObjectName("pushButton_deleteFGP")
        self.frame_2 = QtWidgets.QFrame(Frame)
        self.frame_2.setGeometry(QtCore.QRect(470, 4, 325, 189))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox_chooseTextToSpeech = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_chooseTextToSpeech.setGeometry(QtCore.QRect(2, 2, 321, 53))
        self.comboBox_chooseTextToSpeech.setObjectName("comboBox_chooseTextToSpeech")
        self.comboBox_chooseTextToSpeech.addItem("")
        self.comboBox_chooseTextToSpeech.addItem("")
        self.pushButton_playSpeech = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_playSpeech.setGeometry(QtCore.QRect(88, 72, 151, 73))
        self.pushButton_playSpeech.setObjectName("pushButton_playSpeech")
        self.frame_3 = QtWidgets.QFrame(Frame)
        self.frame_3.setGeometry(QtCore.QRect(4, 196, 461, 279))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_forShowCamera = QtWidgets.QLabel(self.frame_3)
        self.label_forShowCamera.setGeometry(QtCore.QRect(22, 10, 397, 257))
        self.label_forShowCamera.setObjectName("label_forShowCamera")
        self.frame_4 = QtWidgets.QFrame(Frame)
        self.frame_4.setGeometry(QtCore.QRect(470, 196, 325, 279))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(14, 20, 103, 17))
        self.label_5.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 57 bold 18pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.label_forShowMAC = QtWidgets.QLabel(self.frame_4)
        self.label_forShowMAC.setGeometry(QtCore.QRect(8, 48, 301, 47))
        self.label_forShowMAC.setStyleSheet("color: rgb(209, 0, 0);\n"
"font: 75 bold 18pt \"Ubuntu\";")
        self.label_forShowMAC.setText("")
        self.label_forShowMAC.setObjectName("label_forShowMAC")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(12, 114, 117, 17))
        self.label_7.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 bold 18pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.label_forShowSerial = QtWidgets.QLabel(self.frame_4)
        self.label_forShowSerial.setGeometry(QtCore.QRect(10, 158, 301, 47))
        self.label_forShowSerial.setStyleSheet("color: rgb(209, 0, 0);\n"
"font: 75 bold 18pt \"Ubuntu\";")
        self.label_forShowSerial.setText("")
        self.label_forShowSerial.setObjectName("label_forShowSerial")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.comboBox_choseConnectForFGPsensor.setItemText(0, _translate("Frame", "UART1"))
        self.comboBox_choseConnectForFGPsensor.setItemText(1, _translate("Frame", "UART2"))
        self.comboBox_choseConnectForFGPsensor.setItemText(2, _translate("Frame", "UART3"))
        self.label_2.setText(_translate("Frame", "Kết nối cảm biến vân tay"))
        self.pushButton_addFGP.setText(_translate("Frame", "Lấy vân tay "))
        self.pushButton_findFGP.setText(_translate("Frame", "Thử vân tay"))
        self.pushButton_deleteFGP.setText(_translate("Frame", "Xóa vân tay"))
        self.comboBox_chooseTextToSpeech.setItemText(0, _translate("Frame", "Xin cảm ơn"))
        self.comboBox_chooseTextToSpeech.setItemText(1, _translate("Frame", "Xin vui lòng thử lại"))
        self.pushButton_playSpeech.setText(_translate("Frame", "Phát"))
        self.label_forShowCamera.setText(_translate("Frame", "TextLabel"))
        self.label_5.setText(_translate("Frame", "MAC"))
        self.label_7.setText(_translate("Frame", "Serial"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
