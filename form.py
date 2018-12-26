# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 203)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.exportButton = QtWidgets.QPushButton(Form)
        self.exportButton.setEnabled(False)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout.addWidget(self.exportButton, 4, 0, 1, 2)
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setEnabled(True)
        self.messageLabel.setTextFormat(QtCore.Qt.AutoText)
        self.messageLabel.setScaledContents(False)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.gridLayout.addWidget(self.messageLabel, 5, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.selectFileButton = QtWidgets.QPushButton(Form)
        self.selectFileButton.setMaximumSize(QtCore.QSize(23, 23))
        self.selectFileButton.setObjectName("selectFileButton")
        self.gridLayout.addWidget(self.selectFileButton, 1, 1, 1, 1)
        self.selectedDirectoryLineEdit = QtWidgets.QLineEdit(Form)
        self.selectedDirectoryLineEdit.setReadOnly(True)
        self.selectedDirectoryLineEdit.setObjectName("selectedDirectoryLineEdit")
        self.gridLayout.addWidget(self.selectedDirectoryLineEdit, 3, 0, 1, 1)
        self.selectedFileXlsLineEdit = QtWidgets.QLineEdit(Form)
        self.selectedFileXlsLineEdit.setText("")
        self.selectedFileXlsLineEdit.setReadOnly(True)
        self.selectedFileXlsLineEdit.setPlaceholderText("")
        self.selectedFileXlsLineEdit.setObjectName("selectedFileXlsLineEdit")
        self.gridLayout.addWidget(self.selectedFileXlsLineEdit, 1, 0, 1, 1)
        self.selectDirButton = QtWidgets.QPushButton(Form)
        self.selectDirButton.setMaximumSize(QtCore.QSize(23, 23))
        self.selectDirButton.setObjectName("selectDirButton")
        self.gridLayout.addWidget(self.selectDirButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ExportXlsToTxt"))
        self.exportButton.setText(_translate("Form", "Экспорт"))
        self.messageLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#4deb13;\">Завершено</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Директория для сохранения данных:"))
        self.selectFileButton.setText(_translate("Form", "..."))
        self.selectDirButton.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "Файл для экпорта:"))

