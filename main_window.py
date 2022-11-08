from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QFileDialog, QAction,
                             QToolTip, QCheckBox, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QLabel, QActionGroup)
from PyQt5.QtGui import (QPixmap, QFont, QIcon, QMovie)
from PyQt5.QtCore import (Qt, QCoreApplication, QThread, QObject, QUrl)
from PyQt5.QtMultimedia import (QMediaPlayer, QMediaContent)
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
        self.resize(1024, 800)
        self.statusBar()
        self.setStyleSheet('background-color: #dbdcff;')
        self.setWindowIcon(QIcon("ICON/titleicon.jpg"))

        menubar = self.menuBar()
        CreateCsv = menubar.addMenu('&Create Csv')
        gift = menubar.addMenu("Gift")

        self.GifLabel = QLabel(self)
        self.GifLabel.setGeometry(20, 20, 1000, 800)

        CreateCsv.setIcon(QIcon('ICON/icon.png'))
        gift.setIcon(QIcon('ICON/gifticon.png'))
        self.Gift = QAction("U a ready?")
        self.Gift.setIcon(QIcon("ICON/icon3.png"))
        self.CreateCsvDataset = QAction("Create Csv Dataset", self)
        self.CreateCsvDataset.setIcon(QIcon("ICON/csvicon.png"))
        self.CreateCsvRandom = QAction(
            "Create Csv + create Random Dataset", self)
        self.CreateCsvRandom.setIcon(QIcon("ICON/icon2.png"))
        self.CreateCsvAnother = QAction("Create Csv Another Dataset", self)
        self.CreateCsvAnother.setIcon(QIcon("ICON/icon1.png"))
        CreateCsv.addAction(self.CreateCsvDataset)
        CreateCsv.addAction(self.CreateCsvRandom)
        CreateCsv.addAction(self.CreateCsvAnother)
        gift.addAction(self.Gift)
        self.CreateCsvDataset.triggered.connect(self.Create_Csv_Dataset)
        self.CreateCsvAnother.triggered.connect(self.Create_Csv_AnotherDataset)
        self.CreateCsvRandom.triggered.connect(self.Create_Csv_RandomDataset)
        self.Gift.triggered.connect(self.gif)

        self.NextButtonCat = QtWidgets.QPushButton(self)
        self.NextButtonCat.setText("следующий кот")
        self.NextButtonCat.setIcon(QIcon('ICON/cat.png'))
        self.NextButtonCat.setIconSize(QtCore.QSize(45, 45))
        self.NextButtonCat.setGeometry(
            844, 750, 180, 50)
        self.NextButtonCat.setStyleSheet('background-color:#66A3D2;')
        self.NextButtonCat.clicked.connect(self.NextCat)

        self.PreviousButtonCat = QtWidgets.QPushButton(self)
        self.PreviousButtonCat.setText("следующая собака ")
        self.PreviousButtonCat.setIcon(QIcon('ICON/dog.png'))
        self.PreviousButtonCat.setIconSize(QtCore.QSize(45, 45))
        self.PreviousButtonCat.setGeometry(
            0, 750, 180, 50)
        self.PreviousButtonCat.setStyleSheet('background-color:#66A3D2;')
        self.PreviousButtonCat.clicked.connect(self.NextDog)

        self.CatLabel = QLabel(self)
        self.CatLabel.move(50,100)
        self.DogLabel = QLabel(self)
        self.DogLabel.move(50,100)
        self.IteratorCat = Iterator.iterator('annotation.csv', 'cat')
        self.IteratorDog = Iterator.iterator('annotation.csv', 'dog')

        self.movie = QMovie("GIF/zxcursed-dead-inside.gif")
        self.movie.setScaledSize(QtCore.QSize(1000, 800))
        self.GifLabel.setMovie(self.movie)
        self.player = QMediaPlayer()
        full_file_path = os.path.join(
            os.getcwd(), 'MP/fem-love-fotografiruyu-zakat-mp3.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)

    def Create_Csv_Dataset(self) -> None:
        first.main(self.folderpath)

    def Create_Csv_AnotherDataset(self) -> None:
        second.main(self.folderpath)

    def Create_Csv_RandomDataset(self) -> None:
        third.main(self.folderpath)

    def NextCat(self):
        self.ImagePathCat = next(self.IteratorCat)
        while self.ImagePathCat == None:
            self.ImagePathCat = next(self.IteratorCat)
        if os.path.isfile(str(self.ImagePathCat)):
            image = QPixmap(self.ImagePathCat)
            self.player.stop()
            self.GifLabel.hide()
            self.CatLabel.clear()
            self.CatLabel.setPixmap(image)
            self.CatLabel.adjustSize()
            self.CatLabel.move(545, 200)
            self.CatLabel.show()
        else:
            self.CatLabel.setText("Картинки закончились")

    def NextDog(self):
        self.ImagePathDog = next(self.IteratorDog)
        while self.ImagePathDog == None:
            self.ImagePathDog = next(self.IteratorDog)
        if os.path.isfile(str(self.ImagePathDog)):
            image = QPixmap(self.ImagePathDog)
            self.player.stop()
            self.GifLabel.hide()
            self.DogLabel.clear()
            self.DogLabel.setPixmap(image)
            self.DogLabel.adjustSize()
            self.DogLabel.move(0, 200)
            self.DogLabel.show()
        else:
            self.DogLabel.setText("Картинки закончились")
            #self.DogLabel.

    def gif(self):
        self.DogLabel.hide()
        self.CatLabel.hide()
        self.GifLabel.show()
        self.movie.start()
        self.player.play()



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
