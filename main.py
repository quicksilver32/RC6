import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

import design
import os


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encodeButton.clicked.connect(self.browse_file)

    def browse_file(self):
        # self.listWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getOpenFileUrl(self, "Choose file")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        # if directory:  # не продолжать выполнение, если пользователь не выбрал директорию


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
