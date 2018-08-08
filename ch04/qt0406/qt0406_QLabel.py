# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt0406_QLabel.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 376)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setToolTip("")
        Form.setToolTipDuration(-1)
        Form.setAutoFillBackground(True)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 480, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMouseTracking(False)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/images/python.jpg"))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "這是一個文本標籤"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p>這是超連結</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><a href=\"https://shopee.tw/\"><span style=\" text-decoration: underline; color:#0000ff;\">歡迎使用Python GUI應用</span></a></p></body></html>"))
        self.label_3.setToolTip(_translate("Form", "這是一個圖像標籤"))
        self.label_4.setToolTip(_translate("Form", "這是一個購物網站"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><a href=\"https://shopee.tw/\"><span style=\" text-decoration: underline; color:#0000ff;\">蝦皮等你</span></a></p></body></html>"))


import apprcc_rc
