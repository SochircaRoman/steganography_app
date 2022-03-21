from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
import numpy as np
import PIL.Image


class Ui_EncryptedWindow(object):
    def setupUi(self, encryptedWindow):
        encryptedWindow.setWindowIcon(QtGui.QIcon('background/data-encryption.png'))
        encryptedWindow.setObjectName("encryptedWindow")
        encryptedWindow.resize(461, 376)
        font = QtGui.QFont()
        font.setItalic(False)
        encryptedWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(encryptedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addImage = QtWidgets.QPushButton(self.centralwidget)
        self.addImage.setGeometry(QtCore.QRect(250, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addImage.setFont(font)
        self.addImage.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.addImage.setObjectName("addImage")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 180, 121, 21))
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
        self.addText = QtWidgets.QPushButton(self.centralwidget)
        self.addText.setGeometry(QtCore.QRect(40, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addText.setFont(font)
        self.addText.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.addText.setObjectName("addText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(40, 340, 131, 21))
        self.inputPassword.setObjectName("inputPassword")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.confirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBtn.setGeometry(QtCore.QRect(310, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmBtn.setFont(font)
        self.confirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.confirmBtn.setObjectName("confirmBtn")
        encryptedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(encryptedWindow)
        QtCore.QMetaObject.connectSlotsByName(encryptedWindow)

        self.add_functions()

    def retranslateUi(self, encryptedWindow):
        _translate = QtCore.QCoreApplication.translate
        encryptedWindow.setWindowTitle(_translate("encryptedWindow", "Ascunderea Textului"))
        self.addImage.setText(_translate("encryptedWindow", "Alegeti o imagine"))
        self.comboBox.setItemText(0, _translate("encryptedWindow", "1"))
        self.comboBox.setItemText(1, _translate("encryptedWindow", "2"))
        self.comboBox.setItemText(2, _translate("encryptedWindow", "3"))
        self.label.setText(_translate("encryptedWindow", "Pas 1: Alegeti numarul de culori pentru ascundere (1-3)"))
        self.label_2.setText(_translate("encryptedWindow", "Pas 2: Alegeti un fisier text care va fi inserat in imagine (.txt)"))
        self.addText.setText(_translate("encryptedWindow", "Alegeti un text"))
        self.label_3.setText(_translate("encryptedWindow", "Pas 3: Alegeti imaginea in care va fi ascuns textul (.jpg.png)"))
        self.label_4.setText(_translate("encryptedWindow", "Pas 4: Introduceti o parola pentru securitate"))
        self.label_5.setText(_translate("encryptedWindow", "Pas 5: Confirmati alegerea"))
        self.label_6.setText(_translate("encryptedWindow", "Parola"))
        self.confirmBtn.setText(_translate("encryptedWindow", "Confirmati"))

    def add_functions(self):
        self.messageToHide = ""
        self.imagePath = ""
        self.addText.clicked.connect(lambda: self.openTextFile())
        self.addImage.clicked.connect(lambda: self.openImagePath())
        self.confirmBtn.clicked.connect(lambda: self.encryptedTextToImage())


    def openTextFile(self):
        file, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Text Files (*.txt)")
        if file == "":
            return
        with open(file) as f:
            data = f.read()

        if data == "":
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Fisierul text ales este gol!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            self.messageToHide = data
            success = QMessageBox()
            success.setWindowTitle("Succes")
            success.setText("Textul a fost adaugat cu succes!")
            success.setIcon(QMessageBox.Information)
            success.setStandardButtons(QMessageBox.Ok)
            success.exec_()

    def openImagePath(self):
        filePath, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "jpg images (*.jpg);;png images (*.png)")
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


    def encryptedTextToImage(self):
        if self.messageToHide == "":
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Fisierul text nu este incarcat!")
            error.setIcon(QMessageBox.Critical)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        elif self.inputPassword.text() == "":
            error = QMessageBox()
            error.setWindowTitle("Error")
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
            image = PIL.Image.open(self.imagePath, "r")
            width, height = image.size
            img_arr = np.array(list(image.getdata()))

            channels = 4 if image.mode == "RGBA" else 3
            pixels = img_arr.size // channels

            stop_indicator = f"${self.inputPassword.text()}$"

            self.messageToHide += stop_indicator
            byte_message = "".join(f"{ord(c):08b}" for c in self.messageToHide)
            bits = len(byte_message)

            if bits > pixels:
                error = QMessageBox()
                error.setWindowTitle("Error")
                error.setText("Imaginea este prea mica pentru a ascunde textul!")
                error.setIcon(QMessageBox.Critical)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                return 0
            else:
                index = 0
                for i in range(pixels):
                    for j in range(0, int(self.comboBox.currentText())):
                        if index < bits:
                            img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_message[index], 2)
                            index += 1
                img_arr = img_arr.reshape((height, width, channels))
                result = PIL.Image.fromarray(img_arr.astype('uint8'), image.mode)
                filePath, _ = QFileDialog.getSaveFileName(None, "Save Image", "", "PNG (*.png)")
                result.save(filePath)

                success = QMessageBox()
                success.setWindowTitle("Succes")
                success.setText("Imaginea a fost criptata cu succes")
                success.setIcon(QMessageBox.Information)
                success.setStandardButtons(QMessageBox.Ok)
                success.exec_()


