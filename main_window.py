from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QFont, QIcon
import Iterator
import first
import second
import third
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # описание  label  и итератора path
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 419, 160, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonPrevious = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.verticalLayout.addWidget(self.pushButtonPrevious)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(590, 420, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonNext = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.verticalLayout_2.addWidget(self.pushButtonNext)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(110, 59, 581, 321))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Image = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Image.setText("")
        #self.Image.setPixmap(QtGui.QPixmap(f"{path}"))
        self.Image.setObjectName("Image")
        self.verticalLayout_3.addWidget(self.Image)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCreate_csv = QtWidgets.QMenu(self.menubar)
        self.menuCreate_csv.setObjectName("menuCreate_csv")
        self.menuEnd = QtWidgets.QMenu(self.menubar)
        self.menuEnd.setObjectName("menuEnd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondataset = QtWidgets.QAction(MainWindow)
        self.actiondataset.setObjectName("actiondataset")
        self.actionchange_dataset = QtWidgets.QAction(MainWindow)
        self.actionchange_dataset.setObjectName("actionchange_dataset")
        self.actionrandom_dataset = QtWidgets.QAction(MainWindow)
        self.actionrandom_dataset.setObjectName("actionrandom_dataset")
        self.menuCreate_csv.addAction(self.actiondataset)
        self.menuCreate_csv.addAction(self.actionchange_dataset)
        self.menuCreate_csv.addAction(self.actionrandom_dataset)
        self.menubar.addAction(self.menuCreate_csv.menuAction())
        self.menubar.addAction(self.menuEnd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # верхнее меню

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Чукарев Михаил 6211"))
        self.pushButtonPrevious.setText(_translate("MainWindow", "Previous"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))
        self.menuCreate_csv.setTitle(_translate("MainWindow", "Create csv"))
        self.menuEnd.setTitle(_translate("MainWindow", "End"))
        self.actiondataset.setText(_translate("MainWindow", "dataset"))
        self.actionchange_dataset.setText(
            _translate("MainWindow", "change dataset"))
        self.actionrandom_dataset.setText(
            _translate("MainWindow", "random dataset"))

# добавить функцию некст и превью
# добавить функцию label для csv


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
