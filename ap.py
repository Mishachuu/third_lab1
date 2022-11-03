# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ap.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 419, 160, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonPrevious = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.verticalLayout.addWidget(self.pushButtonPrevious)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 420, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonNext = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.verticalLayout_2.addWidget(self.pushButtonNext)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(110, 59, 581, 398))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Image = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("../OneDrive/Рабочий стол/dataset/cat/0001.jpg"))
        self.Image.setObjectName("Image")
        self.verticalLayout_3.addWidget(self.Image)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(320, 420, 160, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButtonCatDog = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonCatDog.setObjectName("pushButtonCatDog")
        self.verticalLayout_4.addWidget(self.pushButtonCatDog)
        self.widgetPath = QtWidgets.QWidget(self.centralwidget)
        self.widgetPath.setGeometry(QtCore.QRect(70, 130, 621, 181))
        self.widgetPath.setStyleSheet("background-color: rgb(255, 255, 210);")
        self.widgetPath.setObjectName("widgetPath")
        self.labelPath = QtWidgets.QLabel(self.widgetPath)
        self.labelPath.setGeometry(QtCore.QRect(150, 40, 321, 31))
        self.labelPath.setStyleSheet("background-color: rgb(255, 230, 169);")
        self.labelPath.setObjectName("labelPath")
        self.textEdit = QtWidgets.QTextEdit(self.widgetPath)
        self.textEdit.setGeometry(QtCore.QRect(130, 100, 361, 41))
        self.textEdit.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPrevious.setText(_translate("MainWindow", "Previous"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))
        self.pushButtonCatDog.setText(_translate("MainWindow", "Cat"))
        self.labelPath.setText(_translate("MainWindow", "                     Введите путь до папки dataset"))
        self.menuCreate_csv.setTitle(_translate("MainWindow", "Create csv"))
        self.menuEnd.setTitle(_translate("MainWindow", "End"))
        self.actiondataset.setText(_translate("MainWindow", "dataset"))
        self.actionchange_dataset.setText(_translate("MainWindow", "change dataset"))
        self.actionrandom_dataset.setText(_translate("MainWindow", "random dataset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())