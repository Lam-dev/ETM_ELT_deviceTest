from        MainScreen.MainScreenUi  import Ui_Frame
from        CameraAndFaceRecognition.CameraAndFaceRecognition   import GetImageFromCamera
from        FingerPrintSensor.FingerPrint           import Fingerprint
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5.QtGui     import QPixmap
from        PyQt5           import QtWidgets, QtGui, QtCore
from        PIL             import Image, ImageQt
import      getmac
from        Sound.OrangePiSound   import Sound

class MainScreen(Ui_Frame, QObject):
    SignalCloseProgram = pyqtSignal()

    def __init__(self, Frame):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        Ui_Frame.setupUi(self, Frame)
        self.cameraObj = GetImageFromCamera(labelObject = self.label_forShowCamera)
        self.cameraObj.StartReadImage()

        self.FGPobj = Fingerprint()
        self.FGPobj.SignalNewFGPadded.connect(self.NotifyFGPadded)
        self.FGPobj.SignalRecognizedFGP.connect(self.NotifyFGPrecognized)
        self.FGPobj.SignalNotFGPsensor.connect(self.NotFGPsensor)

        self.ShowMacAndSerial()

        self.pushButton_addFGP.clicked.connect(self.GetAndSaveFGP)
        self.pushButton_findFGP.clicked.connect(self.FindFGP)
        self.pushButton_deleteFGP.clicked.connect(self.DeleteFGP)
        self.pushButton_close.clicked.connect(self.CloseProgram)
            
        self.SoundObj = Sound()    

        self.pushButton_playSpeech.clicked.connect(self.PlaySound)

    def CloseProgram(self):
        self.SignalCloseProgram.emit()

    def PlaySound(self):
        if(self.comboBox_chooseTextToSpeech.currentText().__contains__("ơn")):
            self.SoundObj.ThreadPlayXinCamOn()
        else:
            self.SoundObj.ThreadPlayVuiLongThuLai()

    def NotFGPsensor(self):
        self.label_forShowFGPnotify.setText("Không kết nối được cảm biến")

    def DeleteFGP(self):
        self.FGPobj.TatLayVanTayDangNhap()
        self.FGPobj.TatThemVanTay()
        self.FGPobj.XoaDataBase()
        self.label_forShowFGPnotify.setText("Đã xóa toàn bộ vân tay")

    def NotifyFGPrecognized(self):
        self.label_forShowFGPnotify.setText("Đã nhận ra vân tay")
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(0, 132, 0);\nfont: 75 bold 12pt 'Ubuntu';")

    def NotifyFGPadded(self):
        self.label_forShowFGPnotify.setText("Đã thêm vân tay")
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(0, 132, 0);\nfont: 75 bold 12pt 'Ubuntu';")

    def GetAndSaveFGP(self):
        self.label_forShowFGPnotify.setText("Đặt tay lên cảm biến")
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(132, 0, 0);\nfont: 75 bold 12pt 'Ubuntu';")
        self.FGPobj.BatThemVanTay()

    def FindFGP(self):
        self.label_forShowFGPnotify.setText("Đặt tay lên cảm biến")
        self.label_forShowFGPnotify.setStyleSheet("color: rgb(132, 0, 0);\nfont: 75 bold 12pt 'Ubuntu';")
        self.FGPobj.TatThemVanTay()
        self.FGPobj.BatLayVanTayDangNhap()

    def ShowMacAndSerial(self):
        self.label_forShowMAC.setText(getmac.get_mac_address())
