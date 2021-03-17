import sys
from PyQt5 import QtWidgets
from RC6_GUI import *
import design


def show_message(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(str(message))
    msgBox.setWindowTitle("Info")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()


class ExampleApp(QtWidgets.QMainWindow, design.Ui_RC6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.decodeButton.setDisabled(True)
        self.encodeButton.setDisabled(True)
        self.chooseFileButton.clicked.connect(self.browse_file)
        self.encodeButton.clicked.connect(self.encode_file)
        self.decodeButton.clicked.connect(self.decode_file)
        self.bitsTextArea.setDisabled(True)
        self.ECBradio.toggled.connect(self.set_mode)
        self.CBCradio.toggled.connect(self.set_mode)
        self.initInput.setVisible(False)
        self.initLabel.setVisible(False)

    def set_mode(self):
        if self.ECBradio.isChecked():
            self.initInput.setVisible(False)
            self.initLabel.setVisible(False)
        if self.CBCradio.isChecked():
            self.initInput.setVisible(True)
            self.initLabel.setVisible(True)

    def browse_file(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(self, "Choose file")

        if file:
            self.decodeButton.setDisabled(False)
            self.encodeButton.setDisabled(False)
            self.fileLabel.setText(file[0].url()[8:])

    def encode_file(self):
        bytes_read = open(self.fileLabel.text(), "rb").read()
        bits_read = bytesToBin(bytes_read)
        secret_key = self.secretKeyBox.text()
        w = int(self.blockSize.currentText())
        r = self.roundsBox.value()
        if secret_key == "":
            show_message("Type Secret Key")
            return
        try:
            if self.initLabel.isVisible():
                init_vector = self.initInput.text()
                if init_vector == "":
                    show_message("Type Init Vector")
                    return
                encoded_bits = encode_CBC(bits_read, secret_key, w, r, init_vector)
            else:
                encoded_bits = encode_ECB(bits_read, secret_key, w, r)

            self.bitsTextArea.setDisabled(False)
            self.bitsTextArea.setPlainText(encoded_bits)
        except Exception as e:
            show_message(e)

    def decode_file(self):
        encoded_bits = self.bitsTextArea.toPlainText()
        secret_key = self.secretKeyBox.text()
        w = int(self.blockSize.currentText())
        r = self.roundsBox.value()
        if secret_key == "":
            show_message("Type Secret Key")
            return
        try:
            if self.initLabel.isVisible():
                init_vector = self.initInput.text()
                if init_vector == "":
                    show_message("Type Init Vector")
                    return
                decoded_bits = decode_CBC(encoded_bits, secret_key, w, r, init_vector)
            else:
                decoded_bits = decode_ECB(encoded_bits, secret_key, w, r)
            extension = "." + self.fileLabel.text().split(".")[-1]
            file_url = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", extension)
            with open(file_url[0] + file_url[1], "wb") as file:
                file.write(binToBytes(decoded_bits))
            self.decodeButton.setDisabled(True)
            self.encodeButton.setDisabled(True)
            self.secretKeyBox.setText("")
            self.bitsTextArea.setPlainText("")
            self.fileLabel.setText("")
            self.bitsTextArea.setDisabled(True)
            self.initInput.setText("")
        except Exception as e:
            show_message(e)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
