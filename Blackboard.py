#deb s

from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        top = 250
        left = 250
        width = 800
        height = 600

        icon = "icons/icon.png"

        self.setWindowTitle("Blackboard")
        self.setGeometry(top,left,width,height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.black)
        self.drawing = False
        self.brushSize=3
        self.brushColor = Qt.white

        self.lastPoint=QPoint()
        menubar = self.menuBar()
        menu = menubar.addMenu("File")
        #define actions 
        
        new = QAction(QIcon("icons/new.png"),"New",self)
        white = QAction(QIcon("icons/white.png"),"White",self)
        green = QAction(QIcon("icons/green.png"),"Green",self)       
        blue = QAction(QIcon("icons/blue.png"),"Blue",self)
        save = QAction(QIcon("icons/save.png"),"Save",self)

        #define shortcut for new & save
        new.setShortcut("Ctrl+N")
        save.setShortcut("Ctrl+S")

        #add to menu 
        
        menu.addAction(new)
        menu.addAction(white)
        menu.addAction(green)
        menu.addAction(blue)
        menu.addAction(save)

        #connect to function
        save.triggered.connect(self.save)
        new.triggered.connect(self.new)
        white.triggered.connect(self.whiteBrush)
        blue.triggered.connect(self.blueBrush)
        green.triggered.connect(self.greenBrush)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self,event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize,Qt.SolidLine,Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint,event.pos())
            self.lastPoint=event.pos()
            self.update()

    def mouseReleaseEvent(self,event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.drawImage(self.rect(),self.image,self.image.rect())

    def save(self):
        filepath,_= QFileDialog.getSaveFileName(self,"Save","","PNG(*.png);;JPEG(*.jpg *.jpeg);; All Files(*.*)")

        if filepath == "":
            return
        self.image.save(filepath)

    def new(self):
        self.image.fill(Qt.black)
        self.update()

    def greenBrush(self):
        self.brushColor = Qt.green

    def whiteBrush(self):
        self.brushColor = Qt.white

    def blueBrush(self):
        self.brushColor = Qt.blue



if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
        
