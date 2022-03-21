from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox
import numpy as np
import PIL.Image


class Ui_ExtractedWindow(object):
    def setupUi(self, extractedWindow):
        extractedWindow.setObjectName("extractedWindow")
        extractedWindow.resize(474, 376)
        font = QtGui.QFont()
        font.setItalic(False)
        extractedWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(extractedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addImage = QtWidgets.QPushButton(self.centralwidget)
        self.addImage.setGeometry(QtCore.QRect(130, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addImage.setFont(font)
        self.addImage.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.addImage.setObjectName("addImage")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 160, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(40, 330, 131, 21))
        self.inputPassword.setObjectName("inputPassword")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.confirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBtn.setGeometry(QtCore.QRect(310, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmBtn.setFont(font)
        self.confirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.confirmBtn.setObjectName("confirmBtn")
        extractedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(extractedWindow)
        QtCore.QMetaObject.connectSlotsByName(extractedWindow)

        self.add_functions()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("extractedWindow", "Extragera Textului"))
        self.addImage.setText(_translate("extractedWindow", "Adaugati imaginea"))
        self.comboBox.setItemText(0, _translate("extractedWindow", "1"))
        self.comboBox.setItemText(1, _translate("extractedWindow", "2"))
        self.comboBox.setItemText(2, _translate("extractedWindow", "3"))
        self.label.setText(_translate("extractedWindow", "Pas 1: Alegeti numarul de culori introdus la ascundere (1-3)"))
        self.label_2.setText(_translate("extractedWindow", "Pas 2: Alegeti o imagine cu text ascuns pentru extragere (.png)"))
        self.label_4.setText(_translate("extractedWindow", "Pas 3: Introduceti parola introdusa la ascundere"))
        self.label_5.setText(_translate("extractedWindow", "Pas 4: Confirmati alegerea"))
        self.label_6.setText(_translate("extractedWindow", "Parola"))
        self.confirmBtn.setText(_translate("extractedWindow", "Confirmati"))

    def add_functions(self):
        self.imagePath = ""
        self.addImage.clicked.connect(lambda: self.openImagePath())
        self.confirmBtn.clicked.connect(lambda: self.extractTextFromImage())

    def openImagePath(self):
        filePath, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "png images (*.png)")
        if filePath == "":
            return

        self.imagePath = filePath
        if self.imagePath != "":
            success = QMessageBox()
            success.setWindowTitle("Succes")
            success.setText("Imaginea a fost adaugata cu succes!")
            success.setIcon(QMessageBox.Information)
            success.setStandardButtons(QMessageBox.Ok)
            success.exec_()

    def extractTextFromImage(self):
        if self.inputPassword.text() == "":
            error = QMessageBox()
            error.setWindowTitle("Eroare")
            error.setText("Nu a fost introdusa parola!")
            error.setIcon(QMessageBox.Critical)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        elif self.imagePath == "":
            error = QMessageBox()
            error.setWindowTitle("Eroare")
            error.setText("Nu a fost adaugata imaginea!")
            error.setIcon(QMessageBox.Critical)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            image = PIL.Image.open(self.imagePath)
            img_arr = np.array(list(image.getdata()))
            channels = 4 if image.mode == "RGBA" else 3
            pixels = img_arr.size // channels

            secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0, int(self.comboBox.currentText()))]
            secret_bits = ''.join(secret_bits)
            secret_bits = [secret_bits[i:i + 8] for i in range(0, len(secret_bits), 8)]

            secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]
            secret_message = ''.join(secret_message)
            stop_indicator = f"${self.inputPassword.text()}$"

            if stop_indicator in secret_message:
                textPath, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text (*.txt)")
                self.createTextFile(secret_message[:secret_message.index(stop_indicator)], textPath)
                print(secret_message[:secret_message.index(stop_indicator)])
            else:
                error = QMessageBox()
                error.setWindowTitle("Eroare")
                error.setText("Ceva nu a mers bine!")
                error.setIcon(QMessageBox.Critical)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()

    def createTextFile(self, text, textPath):
        with open(textPath, 'w') as f:
            f.write(text)
        success = QMessageBox()
        success.setWindowTitle("Succes")
        success.setText("Fisierul cu textul extras a fost creat!")
        success.setIcon(QMessageBox.Information)
        success.setStandardButtons(QMessageBox.Ok)
        success.exec_()
