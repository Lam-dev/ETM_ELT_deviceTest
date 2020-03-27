from    FingerPrintSensor.FingerprintLib    import PyFingerprint
from    PyQt5.QtCore       import QRect, QPropertyAnimation, QTimer, pyqtSignal, pyqtSlot, QObject
import  time
from    PIL import Image
import  _thread
import  threading

class Fingerprint(QObject):
    SignalNewFGPadded = pyqtSignal()
    SignalRecognizedFGP = pyqtSignal()
    SignalFGPnotFind = pyqtSignal()
    SignalHandPushed = pyqtSignal()
    SignalNotFGPsensor = pyqtSignal()
    def __init__(self, port = '/dev/ttyACM0', baudRate = 57600, address = 0xFFFFFFFF, password = 0xFFFFFFFF):
        super().__init__()
        self.port = port
        self.baudRate = baudRate
        self.address = address
        self.password = password
        try:
            self.fingerprintObj = PyFingerprint(port, baudRate, address, password)
            # self.fingerprintObj.verifyPassword()
        except:
            self.fingerprintObj = False
        
        self.TimerThemVanTay = QTimer()
        self.TimerThemVanTay.timeout.connect(self.ThemVanTay)
        self.TimerLayVanTayDangNhap = QTimer()
        self.TimerLayVanTayDangNhap.timeout.connect(self.ThreadLayVanTayDangNhap)
        self.FlagFGPfree = True
        
    def BatThemVanTay(self):
        if(not self.TimerThemVanTay.isActive()):
            self.TimerThemVanTay.start(1500)
            
    def TatThemVanTay(self):
        if(self.TimerThemVanTay.isActive()):
            self.TimerThemVanTay.stop()
    
    def BatLayVanTayDangNhap(self):
        self.TimerLayVanTayDangNhap.stop()
        self.TimerLayVanTayDangNhap.start(1500)
    
    def TatLayVanTayDangNhap(self):
        if(self.TimerLayVanTayDangNhap.isActive()):
            self.TimerLayVanTayDangNhap.stop()

    def XoaDataBase(self):
        try:
            if(type(self.fingerprintObj) is not bool):
                self.fingerprintObj.clearDatabase()
        except:
            pass

    def ThemVanTay(self):
        try:
            if(type(self.fingerprintObj) is not bool):
                if(self.fingerprintObj.readImage()):
                    self.SignalHandPushed.emit()
                    self.fingerprintObj.convertImage(0x01)
                    self.fingerprintObj.readImage()
                    self.fingerprintObj.convertImage(0x02)
                    if(self.fingerprintObj.compareCharacteristics() > 0):
                        self.fingerprintObj.storeTemplate(1, 0x01)
                        self.SignalNewFGPadded.emit()
                        self.TatThemVanTay()
            else:
                self.SignalNotFGPsensor.emit()
                self.fingerprintObj = PyFingerprint(self.port, self.baudRate, self.address, self.password)
                self.fingerprintObj.verifyPassword()
        except:
            self.SignalNotFGPsensor.emit()
            self.fingerprintObj = False

    
    def ThreadLayVanTayDangNhap(self):
        if(self.FlagFGPfree):
            self.FlagFGPfree = False
            thread = threading.Thread(target = self.LayVanTayDangNhap, args=(), daemon= True)
            thread.start()
    
    def LayVanTayDangNhap(self):
        
        try:
            if(self.fingerprintObj.readImage()):
                self.fingerprintObj.convertImage(0x01)
                ketqua = self.fingerprintObj.searchTemplate()
                if(len(ketqua) == 2):
                    if(ketqua[0] == 1):
                        self.SignalRecognizedFGP.emit()

        except:
            self.SignalNotFGPsensor.emit()
        self.FlagFGPfree = True

