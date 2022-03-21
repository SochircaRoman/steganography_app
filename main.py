from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from encryptedWindow import Ui_EncryptedWindow
from extractedWindow import Ui_ExtractedWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(490, 339)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_1Lb = QtWidgets.QLabel(self.centralwidget)
        self.text_1Lb.setGeometry(QtCore.QRect(10, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.text_1Lb.setFont(font)
        self.text_1Lb.setObjectName("text_1Lb")
        self.imageLb = QtWidgets.QLabel(self.centralwidget)
        self.imageLb.setGeometry(QtCore.QRect(10, 10, 251, 251))
        self.imageLb.setText("")
        self.imageLb.setPixmap(QtGui.QPixmap("background/monalisa_bg.jpg"))
        self.imageLb.setObjectName("imageLb")
        self.text_2Lb = QtWidgets.QLabel(self.centralwidget)
        self.text_2Lb.setGeometry(QtCore.QRect(10, 310, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(True)
        self.text_2Lb.setFont(font)
        self.text_2Lb.setObjectName("text_2Lb")
        self.encryptedBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptedBtn.setGeometry(QtCore.QRect(310, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.encryptedBtn.setFont(font)
        self.encryptedBtn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.encryptedBtn.setStyleSheet("")
        self.encryptedBtn.setObjectName("encryptedBtn")
        self.decryptedBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptedBtn.setGeometry(QtCore.QRect(310, 110, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.decryptedBtn.setFont(font)
        self.decryptedBtn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.decryptedBtn.setStyleSheet("")
        self.decryptedBtn.setObjectName("decryptedBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(310, 180, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.exitBtn.setStyleSheet("")
        self.exitBtn.setObjectName("exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganografie imagine"))
        self.text_1Lb.setText(_translate("MainWindow", "Creat de:"))
        self.text_2Lb.setText(_translate("MainWindow", "Roman Sochirca IS21Z USARB"))
        self.encryptedBtn.setText(_translate("MainWindow", "Ascunde"))
        self.decryptedBtn.setText(_translate("MainWindow", "Extrage"))
        self.exitBtn.setText(_translate("MainWindow", "Iesire"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))


    def add_functions(self):
        self.encryptedBtn.clicked.connect(lambda: self.openEncryptedWindow())
        self.decryptedBtn.clicked.connect(lambda: self.openExtractedWindow())
        self.exitBtn.clicked.connect(lambda: self.exitFromApp())



    def openEncryptedWindow(self):
        self.uiEncrypt = encryptedWindow()
        self.uiEncrypt.show()

    def openExtractedWindow(self):
        self.uiExtract = extractedWindow()
        self.uiExtract.show()

    def exitFromApp(self):
        ask = QMessageBox()
        ask.setWindowTitle("Iesire")
        ask.setText("Doriti sa iesiti din aplicatie?")
        ask.setIcon(QMessageBox.Warning)
        ask.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)

        ask.buttonClicked.connect(self.exitAction)
        ask.exec_()

    def exitAction(self, btn):
        if btn.text() == "&Yes":
            sys.exit()


class encryptedWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(encryptedWindow, self).__init__()
        self.uiEncrypt = Ui_EncryptedWindow()
        self.uiEncrypt.setupUi(self)

class extractedWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(extractedWindow, self).__init__()
        self.uiExtract = Ui_ExtractedWindow()
        self.uiExtract.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
