# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 259)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 191, 16))
        self.label.setObjectName("label")
        self.plainEdit = QtWidgets.QLineEdit(Dialog)
        self.plainEdit.setGeometry(QtCore.QRect(40, 30, 321, 21))
        self.plainEdit.setObjectName("plainEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.keyEdit = QtWidgets.QLineEdit(Dialog)
        self.keyEdit.setGeometry(QtCore.QRect(40, 80, 321, 21))
        self.keyEdit.setObjectName("keyEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 161, 16))
        self.label_3.setObjectName("label_3")
        self.resultEdit = QtWidgets.QLineEdit(Dialog)
        self.resultEdit.setGeometry(QtCore.QRect(40, 160, 321, 21))
        self.resultEdit.setObjectName("resultEdit")
        self.runButton = QtWidgets.QPushButton(Dialog)
        self.runButton.setGeometry(QtCore.QRect(140, 110, 113, 32))
        self.runButton.setObjectName("runButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 321, 51))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.runButton.clicked.connect(Dialog.slotOne)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Plaintext"))
        self.label_2.setText(_translate("Dialog", "Input Key"))
        self.label_3.setText(_translate("Dialog", "Result (Cypertext)"))
        self.runButton.setText(_translate("Dialog", "Run DES"))
        self.label_4.setText(_translate("Dialog", "ERRORLIST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

