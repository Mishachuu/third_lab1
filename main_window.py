from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QFileDialog, QAction,
                             QToolTip, QCheckBox, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QLabel, QActionGroup)
from PyQt5.QtGui import (QPixmap, QFont, QIcon, QMovie)
from PyQt5.QtCore import (Qt, QCoreApplication, QThread, QObject)
import os
import sys
import Iterator
import first
import second
import third


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.folderpath = ""
        while self.folderpath == "":
            self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Выберите папку dataset')

        self.setWindowTitle("Чукарев Михаил 6211")
        self.resize(800, 600)
        self.statusBar()

        menubar = self.menuBar()
        CreateCsv = menubar.addMenu('&Create Csv')

        self.ImageLabel = QLabel(self)
        self.ImageLabel.setGeometry(20, 20, 700, 600)
        gift = menubar.addMenu("Gift")
        self.Gift = QAction("U a ready?")
        self.movie = QMovie("cat-cat-ghoul.gif")
        self.ImageLabel.setMovie(self.movie)
        #self.movie.start()
        self.CreateCsvDataset = QAction("Create Csv Dataset...", self)
        self.CreateCsvRandom = QAction(
            "Create Csv + create Random Dataset", self)
        self.CreateCsvAnother = QAction("Create Csv + Another Dataset", self)
        CreateCsv.addAction(self.CreateCsvDataset)
        CreateCsv.addAction(self.CreateCsvRandom)
        CreateCsv.addAction(self.CreateCsvAnother)
        gift.addAction(self.Gift)
        self.CreateCsvDataset.triggered.connect(Create_Csv_Dataset)
        self.CreateCsvAnother.triggered.connect(Create_Csv_AnotherDataset)
        self.CreateCsvRandom.triggered.connect(Create_Csv_RandomDataset)
        self.Gift.triggered.connect(gif)

        #self.ImageLabel = QtWidgets.QLabel(self)
        #self.ImageLabel.setGeometry(110, 59, 581, 321)

        self.nextbutton = QtWidgets.QPushButton(self)
        self.nextbutton.setIcon(QIcon('1.png'))
        self.nextbutton.setIconSize(QtCore.QSize(250, 150))
        self.nextbutton.setGeometry(
            670, 560, 130, 40)
        self.nextbutton.clicked.connect(next)
        self.previousbutton = QtWidgets.QPushButton(self)
        self.previousbutton.setIcon(QIcon('2.png'))
        self.previousbutton.setIconSize(QtCore.QSize(250, 150))
        self.previousbutton.setGeometry(
            0, 560, 130, 40)
        self.previousbutton.clicked.connect(previous)
        self.classbutton = QtWidgets.QPushButton(self)
        self.classbutton.setText("Cat")
        self.classbutton.setGeometry(
            310, 560, 200, 40)
        self.classbutton.clicked.connect(Class_)


def Create_Csv_Dataset(self) -> None:
    print(12)
    first.main(self.folderpath)


def Create_Csv_AnotherDataset(self) -> None:
    print(12)
    second.main(self.folderpath)


def Create_Csv_RandomDataset(self) -> None:
    print(12)
    third.main(self.folderpath)


def next(self):
    print(12)


def previous(self):
    print(12)


def Class_(self):
    print(12)


def gif(self):
    print(12)
 



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
