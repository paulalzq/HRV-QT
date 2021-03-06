# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_generalWindow(object):
    def setupUi(self, generalWindow):
        generalWindow.setObjectName("generalWindow")
        generalWindow.resize(1024, 768)
        generalWindow.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.centralwidget = QtWidgets.QWidget(generalWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 0, 1021, 222))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setMaximumSize(QtCore.QSize(1677, 1677))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(1000, 90, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.accionDocumento1 = QtWidgets.QVBoxLayout()
        self.accionDocumento1.setSpacing(0)
        self.accionDocumento1.setObjectName("accionDocumento1")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.accionDocumento1.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.accionDocumento1.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_12.setObjectName("pushButton_12")
        self.accionDocumento1.addWidget(self.pushButton_12)
        self.horizontalLayout.addLayout(self.accionDocumento1)
        self.accionDocumento2 = QtWidgets.QVBoxLayout()
        self.accionDocumento2.setContentsMargins(-1, -1, 10, -1)
        self.accionDocumento2.setSpacing(0)
        self.accionDocumento2.setObjectName("accionDocumento2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName("pushButton")
        self.accionDocumento2.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.accionDocumento2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.accionDocumento2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.accionDocumento2)
        generalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(generalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuAarchivo = QtWidgets.QMenu(self.menubar)
        self.menuAarchivo.setObjectName("menuAarchivo")
        generalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(generalWindow)
        self.statusbar.setObjectName("statusbar")
        generalWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(generalWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(generalWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDownload = QtWidgets.QAction(generalWindow)
        self.actionDownload.setObjectName("actionDownload")
        self.actionExport_PDF = QtWidgets.QAction(generalWindow)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionExit = QtWidgets.QAction(generalWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAarchivo.addAction(self.actionOpen)
        self.menuAarchivo.addAction(self.actionSave)
        self.menuAarchivo.addAction(self.actionDownload)
        self.menuAarchivo.addAction(self.actionExport_PDF)
        self.menuAarchivo.addAction(self.actionExit)
        self.menubar.addAction(self.menuAarchivo.menuAction())

        self.retranslateUi(generalWindow)
        QtCore.QMetaObject.connectSlotsByName(generalWindow)

    def retranslateUi(self, generalWindow):
        _translate = QtCore.QCoreApplication.translate
        generalWindow.setWindowTitle(_translate("generalWindow", "AHRV"))
        self.label.setText(_translate("generalWindow", "<html><head/><body><p><img src=\":/logo/logo.svg\"/></p></body></html>"))
        self.pushButton_10.setText(_translate("generalWindow", "Complete brief"))
        self.pushButton_11.setText(_translate("generalWindow", "Normal Graphic"))
        self.pushButton_12.setText(_translate("generalWindow", "Base Line Correction"))
        self.pushButton.setText(_translate("generalWindow", "Picos R"))
        self.pushButton_3.setText(_translate("generalWindow", "Métricas de la Frecuencia"))
        self.pushButton_2.setText(_translate("generalWindow", "Export PDF"))
        self.menuAarchivo.setTitle(_translate("generalWindow", "File"))
        self.actionOpen.setText(_translate("generalWindow", "Open"))
        self.actionSave.setText(_translate("generalWindow", "Save"))
        self.actionDownload.setText(_translate("generalWindow", "Download"))
        self.actionExport_PDF.setText(_translate("generalWindow", "Export PDF"))
        self.actionExit.setText(_translate("generalWindow", "Exit"))
import resources_rc
