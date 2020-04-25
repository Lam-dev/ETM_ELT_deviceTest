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
        self.frame.setGeometry(QtCore.QRect(4, 4, 405, 105))
        self.frame.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_addFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_addFGP.setGeometry(QtCore.QRect(8, 6, 111, 47))
        self.pushButton_addFGP.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton_addFGP.setObjectName("pushButton_addFGP")
        self.label_forShowFGPnotify = QtWidgets.QLabel(self.frame)
        self.label_forShowFGPnotify.setGeometry(QtCore.QRect(6, 58, 371, 39))
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(0, 132, 0);\n"
"font: 75 bold 12pt \"Ubuntu\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_forShowFGPnotify.setText("")
        self.label_forShowFGPnotify.setObjectName("label_forShowFGPnotify")
        self.pushButton_findFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_findFGP.setGeometry(QtCore.QRect(140, 6, 103, 47))
        self.pushButton_findFGP.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton_findFGP.setObjectName("pushButton_findFGP")
        self.pushButton_deleteFGP = QtWidgets.QPushButton(self.frame)
        self.pushButton_deleteFGP.setGeometry(QtCore.QRect(274, 6, 101, 47))
        self.pushButton_deleteFGP.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton_deleteFGP.setObjectName("pushButton_deleteFGP")
        self.frame_2 = QtWidgets.QFrame(Frame)
        self.frame_2.setGeometry(QtCore.QRect(4, 114, 405, 83))
        self.frame_2.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox_chooseTextToSpeech = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_chooseTextToSpeech.setGeometry(QtCore.QRect(4, 22, 241, 37))
        self.comboBox_chooseTextToSpeech.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.comboBox_chooseTextToSpeech.setObjectName("comboBox_chooseTextToSpeech")
        self.comboBox_chooseTextToSpeech.addItem("")
        self.comboBox_chooseTextToSpeech.addItem("")
        self.pushButton_playSpeech = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_playSpeech.setGeometry(QtCore.QRect(262, 16, 115, 49))
        self.pushButton_playSpeech.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton_playSpeech.setObjectName("pushButton_playSpeech")
        self.frame_3 = QtWidgets.QFrame(Frame)
        self.frame_3.setGeometry(QtCore.QRect(4, 204, 405, 271))
        self.frame_3.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_forShowCamera = QtWidgets.QLabel(self.frame_3)
        self.label_forShowCamera.setGeometry(QtCore.QRect(12, 8, 371, 257))
        self.label_forShowCamera.setObjectName("label_forShowCamera")
        self.frame_4 = QtWidgets.QFrame(Frame)
        self.frame_4.setGeometry(QtCore.QRect(414, 4, 379, 131))
        self.frame_4.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(14, 14, 103, 17))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 127);\n"
"font: 57 bold 18pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.label_forShowMAC = QtWidgets.QLabel(self.frame_4)
        self.label_forShowMAC.setGeometry(QtCore.QRect(108, 2, 263, 47))
        self.label_forShowMAC.setStyleSheet("color: rgb(209, 0, 0);\n"
"font: 75 bold 18pt \"Ubuntu\";")
        self.label_forShowMAC.setText("")
        self.label_forShowMAC.setObjectName("label_forShowMAC")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(12, 58, 83, 17))
        self.label_7.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 bold 18pt \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.label_forShowSerial = QtWidgets.QLabel(self.frame_4)
        self.label_forShowSerial.setGeometry(QtCore.QRect(108, 50, 263, 47))
        self.label_forShowSerial.setStyleSheet("color: rgb(209, 0, 0);\n"
"font: 75 bold 18pt \"Ubuntu\";")
        self.label_forShowSerial.setText("")
        self.label_forShowSerial.setObjectName("label_forShowSerial")
        self.button_readMac = QtWidgets.QPushButton(self.frame_4)
        self.button_readMac.setGeometry(QtCore.QRect(22, 82, 43, 41))
        self.button_readMac.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.button_readMac.setObjectName("button_readMac")
        self.pushButton_close = QtWidgets.QPushButton(Frame)
        self.pushButton_close.setGeometry(QtCore.QRect(716, 396, 79, 73))
        self.pushButton_close.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.frame_5 = QtWidgets.QFrame(Frame)
        self.frame_5.setGeometry(QtCore.QRect(416, 140, 297, 125))
        self.frame_5.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 6, 213, 31))
        self.label_3.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 57 bold 18pt \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_forShowTimeFromDS1307 = QtWidgets.QLabel(self.frame_5)
        self.label_forShowTimeFromDS1307.setGeometry(QtCore.QRect(10, 44, 281, 73))
        self.label_forShowTimeFromDS1307.setStyleSheet("color: rgb(127, 0, 0);\n"
"font: 57 bold 14pt \"Ubuntu\";")
        self.label_forShowTimeFromDS1307.setLineWidth(1)
        self.label_forShowTimeFromDS1307.setText("")
        self.label_forShowTimeFromDS1307.setAlignment(QtCore.Qt.AlignCenter)
        self.label_forShowTimeFromDS1307.setWordWrap(True)
        self.label_forShowTimeFromDS1307.setObjectName("label_forShowTimeFromDS1307")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(714, 140, 79, 53))
        self.pushButton.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton__writeTime = QtWidgets.QPushButton(Frame)
        self.pushButton__writeTime.setGeometry(QtCore.QRect(714, 202, 79, 53))
        self.pushButton__writeTime.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.pushButton__writeTime.setObjectName("pushButton__writeTime")
        self.frame_6 = QtWidgets.QFrame(Frame)
        self.frame_6.setGeometry(QtCore.QRect(416, 270, 297, 199))
        self.frame_6.setStyleSheet("background-color: rgba(0, 170, 255, 70);\n"
"border-style:solid;\n"
"border-radius:5px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(10, 6, 213, 31))
        self.label_8.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 57 bold 18pt \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.label_forShowCardData = QtWidgets.QLabel(self.frame_6)
        self.label_forShowCardData.setGeometry(QtCore.QRect(6, 48, 281, 75))
        self.label_forShowCardData.setStyleSheet("color: rgb(127, 0, 0);\n"
"font: 57 bold 14pt \"Ubuntu\";")
        self.label_forShowCardData.setLineWidth(1)
        self.label_forShowCardData.setText("")
        self.label_forShowCardData.setAlignment(QtCore.Qt.AlignCenter)
        self.label_forShowCardData.setWordWrap(True)
        self.label_forShowCardData.setObjectName("label_forShowCardData")
        self.button_writeCard = QtWidgets.QPushButton(self.frame_6)
        self.button_writeCard.setGeometry(QtCore.QRect(12, 132, 89, 55))
        self.button_writeCard.setStyleSheet("background-color: rgb(226, 226, 169);")
        self.button_writeCard.setObjectName("button_writeCard")
        self.label_showRandomNumber = QtWidgets.QLabel(self.frame_6)
        self.label_showRandomNumber.setGeometry(QtCore.QRect(114, 136, 175, 47))
        self.label_showRandomNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_showRandomNumber.setText("")
        self.label_showRandomNumber.setObjectName("label_showRandomNumber")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_addFGP.setText(_translate("Frame", "Lấy vân tay "))
        self.pushButton_findFGP.setText(_translate("Frame", "Thử vân tay"))
        self.pushButton_deleteFGP.setText(_translate("Frame", "Xóa vân tay"))
        self.comboBox_chooseTextToSpeech.setItemText(0, _translate("Frame", "Xin cảm ơn"))
        self.comboBox_chooseTextToSpeech.setItemText(1, _translate("Frame", "Xin vui lòng thử lại"))
        self.pushButton_playSpeech.setText(_translate("Frame", "Phát"))
        self.label_forShowCamera.setText(_translate("Frame", "TextLabel"))
        self.label_5.setText(_translate("Frame", "MAC"))
        self.label_7.setText(_translate("Frame", "Serial"))
        self.button_readMac.setText(_translate("Frame", "Đọc"))
        self.pushButton_close.setText(_translate("Frame", "Tắt"))
        self.label_3.setText(_translate("Frame", "Giờ DS1307"))
        self.pushButton.setText(_translate("Frame", "Đọc giờ"))
        self.pushButton__writeTime.setText(_translate("Frame", "Ghi giờ"))
        self.label_8.setText(_translate("Frame", "Thẻ"))
        self.button_writeCard.setText(_translate("Frame", "Ghi thẻ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
