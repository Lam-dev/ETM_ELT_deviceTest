from        MainScreen.MainScreenUi  import Ui_Frame
from        CameraAndFaceRecognition.CameraAndFaceRecognition   import GetImageFromCamera
from        FingerPrintSensor.FingerPrint           import Fingerprint
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5.QtGui     import QPixmap
from        PyQt5           import QtWidgets, QtGui, QtCore
from        PIL             import Image, ImageQt
import      getmac
from        Sound.OrangePiSound   import Sound
import      subprocess
from        subprocess  import Popen, PIPE
import      random
from      WriteRFcard.ControlRFIDmodule     import   ControlRFIDmudule


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
        self.GetDS1307time()

        self.pushButton_addFGP.clicked.connect(self.GetAndSaveFGP)
        self.pushButton_findFGP.clicked.connect(self.FindFGP)
        self.pushButton_deleteFGP.clicked.connect(self.DeleteFGP)
        self.pushButton_close.clicked.connect(self.CloseProgram)
        self.pushButton.clicked.connect(self.GetDS1307time)
        self.button_writeCard.clicked.connect(self.WriteRandomNumberToCard)
        self.button_readMac.clicked.connect(self.ShowMacAndSerial)
            
        self.SoundObj = Sound()    

        self.pushButton_playSpeech.clicked.connect(self.PlaySound)
        self.rfModuleObj = ControlRFIDmudule()
        self.rfModuleObj.SignalDataReadInCardByteArray.connect(self.ShowDataWrited)
        self.rfModuleObj.SignalDataReadInCardStr.connect(self.CompareReadData)
        self.rfModuleObj.SignalNotConnectUART.connect(lambda: self.label_forShowCardData.setText("Không có kết nối uart"))
        #self.rfModuleObj.SignalWritedNumber.connect()
        self.randomNum = str

        

    def CompareReadData(self, strData):
        try:
            if((strData == self.randomNum) & (len(strData) > 5)):
                self.SoundObj.ThreadPlayXinCamOn()

            else:
                self.SoundObj.ThreadPlayVuiLongThuLai()
        except:
            pass



    def ShowDataWrited(self, data):
        self.label_forShowCardData.setText(str(data))

    def WriteRandomNumberToCard(self):
        self.randomNum = self.CreateRandomNumberWriteToCard()
        self.label_showRandomNumber.setText(str(self.randomNum))
        self.rfModuleObj.SetIDcarNumberToWriteToRFcard(self.randomNum)
        self.rfModuleObj.StartWriteIDcardNumberToRFcard()

    def CreateRandomNumberWriteToCard(self):
        strNumber = str(random.randint(10000000, 99999999))
        return strNumber

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
        try:
            macString = getmac.get_mac_address()
            if(macString == ""):
                self.label_forShowMAC.setText("Kết nối LAN")
                return
            self.label_forShowMAC.setText(macString)
            lstByteStrType = macString.split(":")
            lstByteMacIntType = [int(elem, 16) for elem in lstByteStrType]
            seriString = "  "
            for i in range(3, 6):
                seriElem = lstByteMacIntType[i] ^ 69
                seriString += self.__ToHex8bit(seriElem)

            self.label_forShowSerial.setText(seriString)
        except:
            self.label_forShowMAC.setText("Kết nối LAN")
    
    def __ToHex8bit(self, number):
        hexStr = hex(number)[2:]
        if(len(hexStr) == 1):
            return "0"+ hexStr
        else:
            return hexStr
    
    def GetDS1307time(self):
        try:
            proc = Popen("hwclock -f /dev/rtc0 -r".split(" "),stdout=PIPE)
            response ,err= proc.communicate()
            timeStringArr = []
            for i in response:
                timeStringArr.append(chr(i))
                timeString = ''.join(timeStringArr)
            self.label_forShowTimeFromDS1307.setText(timeString)
        except:
            self.label_forShowTimeFromDS1307.setText("Lỗi")