import cv2
import threading
from   PyQt5.QtCore     import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from   PyQt5.QtGui      import QPixmap,QColor
from   PyQt5            import QtCore, QtGui
import time

Camera_Number = 0
Camera_Object = cv2.VideoCapture(Camera_Number)

class GetImageFromCamera(QObject):

    def __init__(self, frameCut = ((0, 640), (0, 480)), size = (280, 480), scale = 0.3, time = 50, labelObject = ""):
        super().__init__()
        self.cameraObj = Camera_Object
        self.timerReadImage = QTimer(self)
        self.timerReadImage.timeout.connect(self.__ThreadReadCamera)
        self.size = size
        self.labelObject = labelObject
        

    def __ThreadReadCamera(self):
        threadReadCam = threading.Thread(target= self.__GetImageFromCamera, args=(), daemon=True)
        threadReadCam.start()

    def __GetImageFromCamera(self):

        global frame, frameNoFaceMark
        global FaceLocationInImage
        # global NumberFrameNotFace
        # while True:
        
        ret, frameFullSize = self.cameraObj.read()
        rgbImage = cv2.cvtColor(frameFullSize, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                        QtGui.QImage.Format_RGB888)
        convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
        pixmap = QPixmap(convertToQtFormat)
        resizeImage = pixmap.scaled(self.size[0], self.size[1], QtCore.Qt.KeepAspectRatio)
        # self.PixmapFromCamera.emit(resizeImage)
        # time.sleep(0.05)
        # if(not self.toBeReadImage):
        #     return
        self.labelObject.setPixmap(resizeImage)

            
    def StopReadImage(self):
        self.timerReadImage.stop()

    def StartReadImage(self):
        self.timerReadImage.start(50)
        







            
