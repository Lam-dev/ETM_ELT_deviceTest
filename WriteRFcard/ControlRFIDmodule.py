from        UARTconnection.UARTconnection   import UART
from        PyQt5.QtCore                    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
import      math

CODE_DATA_IN_CARD = 0
CODE_NOT_CARD = 1
CODE_RESQUEST_WRITE_DATA_TO_CARD = 2
CODE_WRITE_SUCCESSFUL = 3
CODE_WRITE_FAIL = 4


class ControlRFIDmudule(QObject):
    SignalWritedNumber = pyqtSignal()
    SignalDataReadInCardByteArray = pyqtSignal(bytes)
    SignalDataReadInCardStr = pyqtSignal(str)
    SignalNotConnectUART = pyqtSignal()
    def __init__(self):
        QObject.__init__(self)
        self.uartObject = UART()
        self.uartObject.StartTimerReadUARTdata()
        self.uartObject.SignalReciptedData.connect(self.ProcessReciptData)
        self.uartObject.SignalNotConnectUART.connect(self.SignalNotConnectUART)
        self.chuaXuLy = b''

        self.timerWriteToCard = QTimer(self)
        self.timerWriteToCard.timeout.connect(lambda: self.SendRequestWriteToRFcard(self.lstByteWriteToCard))
        ## Test""""""
        #self.timerSendWriteToCard = QTimer(self)
        #self.timerSendWriteToCard.timeout.connect(lambda:self.WriteIDcardNumberToRFcard("21212121"))
        #self.timerSendWriteToCard.start(2000)
        self.lstByteWriteToCard = []
        self.callbackWriteNotify = object
        self.numberStrToSend = ""

    def WriteIDcardNumberToRFcard(self, strNumber):
        self.timerSendWriteToCard.stop()
        lstByte = []
        for charNumber in strNumber:
            lstByte.append(ord(charNumber))
                 
        #self.SendRequestWriteToRFcard(lstByte)

    def SetIDcarNumberToWriteToRFcard(self, strNumber):
        self.lstByteWriteToCard.clear()
        for charNumber in strNumber:
            self.lstByteWriteToCard.append(ord(charNumber))

    def StartWriteIDcardNumberToRFcard(self):
        self.timerWriteToCard.start(1000)

    def StopWriteIDcardNumberToRFcard(self):
        self.timerWriteToCard.stop()

    """
    Tach xu ly du lieu nhan
    """
    def ProcessReciptData(self, data):
        lstFrame = self.__TachCacKhungTruyen(data)
        for frame in lstFrame:
            self.SwitchRequest(frame)

    def SwitchRequest(self, frame):
        try:
            data, code = self.__CatLayPhanDataTrongFrame(frame)
            #reciptObj = self.json2obj(data)

            if(code == CODE_DATA_IN_CARD):
                self.DataReadInCard(data)

            elif(code == CODE_NOT_CARD):
                pass
            elif(code == CODE_RESQUEST_WRITE_DATA_TO_CARD):
                pass
            elif(code == CODE_WRITE_SUCCESSFUL):
                self.WriteSuccess()
                self.SignalWritedNumber.emit()

            elif(code == CODE_WRITE_FAIL):
                pass
        except NameError as e:
            print(e)
            pass
    
    def WriteSuccess(self):
        self.StopWriteIDcardNumberToRFcard()

    def DataReadInCard(self, data):
        self.SignalDataReadInCardByteArray.emit(data)
        strData = self.ConvertListByteToString(data)
        self.SignalDataReadInCardStr.emit(strData)
        
    def ConvertListByteToString(self, lstByte):
        try:
            cardData = lstByte[4:len(lstByte)]  # frame tra ve co 4 byte dau la ma the, con lai la du lieu trong the
            string = ""
            for byte in cardData:
                try:
                    string += chr(byte)
                except:
                    pass
            return string
        except:
            return False

    def SendRequestWriteToRFcard(self, data):
        self.uartObject.SendDataToUART(self.__BuildFrameToSend(data, CODE_RESQUEST_WRITE_DATA_TO_CARD)[0])


    def __CatLayPhanDataTrongFrame(self, frameNhan):
        code = frameNhan[3]
        chieuDaiDl = frameNhan[4] + frameNhan[5] * math.pow(2, 8)
        return frameNhan[6:6+int(chieuDaiDl)], code
    
    

        """
    khung truyen uart yeu cau module 3g gui file
    tham so
        tenFile: ten cua file can gui
    tra ve
        khungTruyen: khong truyen de gui cho ETM module
        tong : checksum cua khung truyen 
    """
    def __BuildFrameToSend(self, byteArray, code):

        highChieuDaiTen = int(len(byteArray) / 256)
        lowChieuDaiTen = int(len(byteArray) % 256)
        khungTruyen = [0x45, 0x54, 0x4D, code, lowChieuDaiTen, highChieuDaiTen]
        tong = code + highChieuDaiTen + lowChieuDaiTen
        j = 0
        for byte in byteArray:
            tong += byte
        
        khungTruyen.extend(byteArray)
        tong = -(~tong) % 256
        khungTruyen.append(0x00)
        khungTruyen[len(khungTruyen)-1] = tong
        return bytes(khungTruyen), tong
        

    def __TachCacKhungTruyen(self, duLieu):
        if(duLieu == b''):
            return []
        self.chuaXuLy = self.chuaXuLy + duLieu
        lstKhungDL = []
        i = 0
        while True:
            if(i == len(self.chuaXuLy)):
                break
            if( self.chuaXuLy[i:i+3].__str__().__contains__("ETM")):
                try:
                    chieuDaiDl = self.chuaXuLy[i+4] + self.chuaXuLy[i+5] * math.pow(2, 8)
                    chieuDaiKhung = i + int(chieuDaiDl) + 7
                    if(chieuDaiKhung + i <= len(self.chuaXuLy)):
                        lstKhungDL.append(self.chuaXuLy[i:chieuDaiKhung])
                        self.chuaXuLy = self.chuaXuLy[chieuDaiKhung: len(self.chuaXuLy)]
                        i = -1
                    else:
                        self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                        break
                except NameError as e:
                    self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                    print(e)
                    break
            i = i + 1
        return lstKhungDL
    """
    check sum mot frame
    """
    def __CheckSum(self, frame):
        # return True ## test
        try:
            sumValue = 0
            for i in range (3, len(frame) - 1):
                sumValue = sumValue + frame[i]
            sumValue = -(~sumValue) % 256
            # print("sum = ", tong) #test
            if(sumValue == frame[len(framframeeNhan)-1]):
                # print("checksum dung")
                return True
            else:
                # print("checksum sai")
                return False
        except:
            return False

