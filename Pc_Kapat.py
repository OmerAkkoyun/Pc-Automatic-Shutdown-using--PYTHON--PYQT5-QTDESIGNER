# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow,QMessageBox#Uyarı vereceğimiz için gerekli modul messegebox
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtWidgets import QInputDialog, QLineEdit,QAction,qApp,QFileDialog,QHBoxLayout
import numpy as np
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 306)
        Form.setFixedSize(400, 350)  # 378,550
        Form.setWindowIcon(QtGui.QIcon(os.path.expanduser("C:\File\kapat.ico")))
        font = QtGui.QFont()
        font.setPointSize(55)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        Form.setFont(font)
        self.baslik = QtWidgets.QLabel(Form)
        self.baslik.setEnabled(True)
        self.baslik.setGeometry(QtCore.QRect(20, 10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.baslik.setFont(font)
        self.baslik.setObjectName("baslik")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(40, 60, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.kapat = QtWidgets.QPushButton(Form)
        self.kapat.setGeometry(QtCore.QRect(40, 180, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kapat.setFont(font)
        self.kapat.setObjectName("kapat")
        self.iptal = QtWidgets.QPushButton(Form)
        self.iptal.setGeometry(QtCore.QRect(200, 180, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.iptal.setFont(font)
        self.iptal.setObjectName("iptal")
        self.bilgi = QtWidgets.QLabel(Form)
        self.bilgi.setGeometry(QtCore.QRect(46, 270, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bilgi.setFont(font)
        self.bilgi.setText("")
        self.bilgi.setObjectName("bilgi")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(190, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("dakika")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("saat")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        newpath = r'C:\File'
        if not os.path.exists(newpath):  # bu kodlar  klasör oluşturma kodudur.
            os.makedirs(newpath)

        urllib.request.urlretrieve(
            "https://www.iconfinder.com/icons/17902/download/ico/256",
            "C:\File\kapat.ico")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bilgisayarı Otomatik Kapat  "))
        self.baslik.setText(_translate("Form", "Bilgisayarı Otomatik Kapat"))
        self.kapat.setText(_translate("Form", "Kapat"))
        self.iptal.setText(_translate("Form", "İptal"))
        self.label.setText(_translate("Form", "dakika"))
        self.label_2.setText(_translate("Form", "saat"))

        # --------bağlantılar----------------
        self.kapat.clicked.connect(self.kapat_F)
        self.iptal.clicked.connect(self.iptal_F)

    def kapat_F(self):

        komut = str(self.timeEdit.text())
        komut=str(komut.split(':'))

        saat=(int(komut[2:4])*60*60)
        print(saat,"saniye")
        dakika=(int(komut[8:10])*60)
        print(dakika,"saniye")

        toplam=saat+dakika
        print("\ntoplam=",toplam,"saniye eder")
#-------------------------------------------------------------------------
        if toplam==0:

            buttonReply = QMessageBox.question(self, 'Uyarı', "Bilgisayar Hemen Kapansın mı ?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                os.system("shutdown -s -t "+str(toplam))

                a=komut[2:4]
                b=komut[8:10]
                self.bilgi.setText(a+" saat "+b+" dakika sonra kapanacak..." )
            elif buttonReply ==QMessageBox.No:
                pass

        else:
            os.system("shutdown -s -t " + str(toplam))

            a = komut[2:4]
            b = komut[8:10]
            self.bilgi.setText(a + " saat " + b + " dakika sonra kapanacak...")

    def iptal_F(self):
        os.system("shutdown -a")
        self.bilgi.setText("Kapatma İşlemi İptal Edildi..")








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

