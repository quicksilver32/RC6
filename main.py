import sys
from PyQt5 import QtWidgets
from utils import *
# from RC6_GUI import *
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.decodeButton.setDisabled(True)
        self.encodeButton.setDisabled(True)
        self.chooseFileButton.clicked.connect(self.browse_file)
        self.encodeButton.clicked.connect(self.encode_file)
        self.decodeButton.clicked.connect(self.decode_file)

    def browse_file(self):
        # self.decodeButton.setDisabled(True)
        file = QtWidgets.QFileDialog.getOpenFileUrl(self, "Choose file")

        if file:
            self.decodeButton.setDisabled(False)
            self.encodeButton.setDisabled(False)
            self.fileLabel.setText(file[0].url()[8:])

    def encode_file(self):
        bytes_read = open(self.fileLabel.text(), "rb").read()
        bits_read = bytesToBin(bytes_read)
        secret_key = self.secretKeyBox.text()
        w = self.blockSize.currentText()
        r = self.roundsBox.value()
        # encoded_bits = encode(bits_read, secret_key, w, r)

    def decode_file(self):
        encoded_bits = self.bitsLabel.text()
        secret_key = self.secretKeyBox.text()
        w = self.blockSize.currentText()
        r = self.roundsBox.value()
        # decoded_bits = decode(encoded_bits, secret_key, w, r)
        extension = "." + self.fileLabel.text().split(".")[-1]
        file_url = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", extension)
        print(file_url[0] + file_url[1])
        with open(file_url[0] + file_url[1], "wb") as file:
            file.write(bytes("test", encoding="utf-8"))
        self.decodeButton.setDisabled(True)
        self.encodeButton.setDisabled(True)
        self.secretKeyBox.setText("")
        self.bitsLabel.setText("")
        self.fileLabel.setText("")



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
