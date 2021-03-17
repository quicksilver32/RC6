# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RC6(object):
    def setupUi(self, RC6):
        RC6.setObjectName("RC6")
        RC6.resize(580, 557)
        RC6.setMinimumSize(QtCore.QSize(580, 557))
        RC6.setMaximumSize(QtCore.QSize(580, 557))
        self.centralwidget = QtWidgets.QWidget(RC6)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setGeometry(QtCore.QRect(140, 20, 431, 21))
        self.fileLabel.setText("")
        self.fileLabel.setObjectName("fileLabel")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(330, 490, 121, 51))
        self.encodeButton.setObjectName("encodeButton")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(460, 490, 101, 51))
        self.decodeButton.setObjectName("decodeButton")
        self.secretKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.secretKeyLabel.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.secretKeyLabel.setObjectName("secretKeyLabel")
        self.secretKeyBox = QtWidgets.QLineEdit(self.centralwidget)
        self.secretKeyBox.setGeometry(QtCore.QRect(80, 70, 211, 20))
        self.secretKeyBox.setInputMask("")
        self.secretKeyBox.setMaxLength(32767)
        self.secretKeyBox.setObjectName("secretKeyBox")
        self.blockSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.blockSizeLabel.setGeometry(QtCore.QRect(310, 70, 71, 21))
        self.blockSizeLabel.setObjectName("blockSizeLabel")
        self.blockSize = QtWidgets.QComboBox(self.centralwidget)
        self.blockSize.setGeometry(QtCore.QRect(380, 70, 51, 22))
        self.blockSize.setObjectName("blockSize")
        self.blockSize.addItem("")
        self.blockSize.addItem("")
        self.blockSize.addItem("")
        self.roundsLabel = QtWidgets.QLabel(self.centralwidget)
        self.roundsLabel.setGeometry(QtCore.QRect(470, 70, 61, 21))
        self.roundsLabel.setObjectName("roundsLabel")
        self.roundsBox = QtWidgets.QSpinBox(self.centralwidget)
        self.roundsBox.setGeometry(QtCore.QRect(520, 70, 42, 22))
        self.roundsBox.setMinimum(1)
        self.roundsBox.setProperty("value", 20)
        self.roundsBox.setObjectName("roundsBox")
        self.bitsTextArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bitsTextArea.setGeometry(QtCore.QRect(80, 200, 481, 271))
        self.bitsTextArea.setObjectName("bitsTextArea")
        self.bitsLabel = QtWidgets.QLabel(self.centralwidget)
        self.bitsLabel.setGeometry(QtCore.QRect(10, 200, 71, 16))
        self.bitsLabel.setObjectName("bitsLabel")
        self.ECBradio = QtWidgets.QRadioButton(self.centralwidget)
        self.ECBradio.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.ECBradio.setChecked(True)
        self.ECBradio.setObjectName("ECBradio")
        self.modeButtonGroup = QtWidgets.QButtonGroup(RC6)
        self.modeButtonGroup.setObjectName("modeButtonGroup")
        self.modeButtonGroup.addButton(self.ECBradio)
        self.CBCradio = QtWidgets.QRadioButton(self.centralwidget)
        self.CBCradio.setGeometry(QtCore.QRect(10, 160, 82, 17))
        self.CBCradio.setObjectName("CBCradio")
        self.modeButtonGroup.addButton(self.CBCradio)
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.modeLabel.setObjectName("modeLabel")
        self.initLabel = QtWidgets.QLabel(self.centralwidget)
        self.initLabel.setGeometry(QtCore.QRect(70, 160, 61, 16))
        self.initLabel.setObjectName("initLabel")
        self.initInput = QtWidgets.QLineEdit(self.centralwidget)
        self.initInput.setGeometry(QtCore.QRect(130, 160, 161, 20))
        self.initInput.setObjectName("initInput")
        RC6.setCentralWidget(self.centralwidget)

        self.retranslateUi(RC6)
        QtCore.QMetaObject.connectSlotsByName(RC6)

    def retranslateUi(self, RC6):
        _translate = QtCore.QCoreApplication.translate
        RC6.setWindowTitle(_translate("RC6", "RC6"))
        self.chooseFileButton.setText(_translate("RC6", "Choose File"))
        self.encodeButton.setText(_translate("RC6", "Encode"))
        self.decodeButton.setText(_translate("RC6", "Decode"))
        self.secretKeyLabel.setText(_translate("RC6", "Secret Key:"))
        self.blockSizeLabel.setText(_translate("RC6", "Block size: 4 x "))
        self.blockSize.setItemText(0, _translate("RC6", "16"))
        self.blockSize.setItemText(1, _translate("RC6", "32"))
        self.blockSize.setItemText(2, _translate("RC6", "64"))
        self.roundsLabel.setText(_translate("RC6", "Rounds:"))
        self.bitsLabel.setText(_translate("RC6", "Encoded file"))
        self.ECBradio.setText(_translate("RC6", "ECB"))
        self.CBCradio.setText(_translate("RC6", "CBC"))
        self.modeLabel.setText(_translate("RC6", "Mode:"))
        self.initLabel.setText(_translate("RC6", "Init vector:"))
