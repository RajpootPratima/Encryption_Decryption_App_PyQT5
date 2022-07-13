import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from encrypt import *


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.le = QLabel("Welcome to the encryption and decryption App")
        layout.addWidget(self.le)
        self.btn_enc = QPushButton("Click to Encrypt files")
        self.btn_enc.clicked.connect(self.encrypt_files)
        layout.addWidget(self.btn_enc)

        self.btn_dec = QPushButton("Click to Decrypt files")
        self.btn_dec.clicked.connect(self.decrypt_files)
        layout.addWidget(self.btn_dec)


        # self.btn1 = QPushButton("QFileDialog object")
        # self.btn1.clicked.connect(self.getfiles)
        # layout.addWidget(self.btn1)
        #
        # self.contents = QTextEdit()
        # layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("ENCRYPT/DECRYPT")
    def encrypt_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "*")
        print("filename", fname)
        encrypt(str(fname[0]))
        self.le.setPixmap(QPixmap())

    def decrypt_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "*")
        print("filename", fname)
        decrypt(str(fname[0]))
        self.le.setPixmap(QPixmap())

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "*")
        print("filename",fname)
        encrypt(str(fname[0]))
        self.le.setPixmap(QPixmap())

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()