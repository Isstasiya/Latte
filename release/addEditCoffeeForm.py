# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frames(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(216, 232)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 18))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 58, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 111, 18))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 110, 91, 16))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 201, 21))
        self.comboBox.setObjectName("comboBox")
        self.spinBox = QtWidgets.QSpinBox(Frame)
        self.spinBox.setGeometry(QtCore.QRect(160, 50, 52, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Frame)
        self.spinBox_2.setGeometry(QtCore.QRect(141, 140, 71, 21))
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.spinBox_3 = QtWidgets.QSpinBox(Frame)
        self.spinBox_3.setGeometry(QtCore.QRect(140, 170, 71, 21))
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setObjectName("spinBox_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Название"))
        self.label_2.setText(_translate("Frame", "Степень обжарки"))
        self.label_4.setText(_translate("Frame", "Описание вкуса"))
        self.label_5.setText(_translate("Frame", "Цена"))
        self.label_6.setText(_translate("Frame", "Объем упаковки"))
        self.pushButton.setText(_translate("Frame", "Выполнить"))
