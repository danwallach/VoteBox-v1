# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gaurav/work_qt5/src_qt5/ui5/systrayframe_base.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 653)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(11, 11, 201, 114))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName("gridlayout1")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.gridlayout1.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridlayout1.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridlayout1.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(232, 11, 197, 136))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridlayout2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2, 0, 0, 1, 1)
        self.MessageShowComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.MessageShowComboBox.setObjectName("MessageShowComboBox")
        self.gridlayout2.addWidget(self.MessageShowComboBox, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 385, 411, 241))
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout3.setObjectName("gridlayout3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.gridlayout3.addWidget(self.listWidget, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout3.addWidget(self.label, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 130, 411, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 331, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(50, 44, 221, 17))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setGeometry(QtCore.QRect(270, 40, 55, 27))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(365)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(329, 45, 67, 17))
        self.label_4.setObjectName("label_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(49, 78, 301, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(50, 129, 331, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(50, 107, 61, 17))
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "System tray icon visibility"))
        self.radioButton.setText(_translate("Dialog", "Always show"))
        self.radioButton_2.setText(_translate("Dialog", "Hide when inactive"))
        self.radioButton_3.setText(_translate("Dialog", "Always hide"))
        self.groupBox_3.setTitle(_translate("Dialog", "System tray icon messages"))
        self.label_2.setText(_translate("Dialog", "Which messages to show:"))
        self.groupBox.setTitle(_translate("Dialog", "Monitor button presses on devices"))
        self.label.setText(_translate("Dialog", "Devices to monitor:"))
        self.groupBox_4.setTitle(_translate("Dialog", "Update Settings"))
        self.checkBox.setText(_translate("Dialog", "Check for HPLIP Updates"))
        self.label_3.setText(_translate("Dialog", "Repeat Check for Updates every "))
        self.label_4.setText(_translate("Dialog", "Days"))
        self.checkBox_2.setText(_translate("Dialog", "Check when ever new version available"))
        self.label_5.setText(_translate("Dialog", "Status:"))

