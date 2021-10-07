# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(960,1000)
        MainWindow.setGeometry(-2, 33, 1920, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920,1000))
        MainWindow.setMaximumSize(QtCore.QSize(1920,1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxImageOrVideo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxImageOrVideo.setGeometry(QtCore.QRect(970, 10, 940, 720))          
        self.groupBoxImageOrVideo.setAutoFillBackground(True)
        self.groupBoxImageOrVideo.setObjectName("groupBoxImageOrVideo")
        self.labelImageOrVideo = QtWidgets.QLabel(self.groupBoxImageOrVideo)
        self.labelImageOrVideo.setGeometry(QtCore.QRect(10, 20, 920, 690))
        self.labelImageOrVideo.setAutoFillBackground(True)
        self.labelImageOrVideo.setText("")
        self.labelImageOrVideo.setPixmap(QtGui.QPixmap("src/default.png"))
        self.labelImageOrVideo.setScaledContents(True)
        self.labelImageOrVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImageOrVideo.setObjectName("labelImageOrVideo")
        self.groupBoxVideoSample = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxVideoSample.setGeometry(QtCore.QRect(10, 402, 940, 547))
        self.groupBoxVideoSample.setAutoFillBackground(True)
        self.groupBoxVideoSample.setObjectName("groupBoxVideoSample")
        self.labelVideoSample = QtWidgets.QLabel(self.groupBoxVideoSample)
        self.labelVideoSample.setGeometry(QtCore.QRect(10, 20, 920, 517))
        self.labelVideoSample.setText("")
        self.labelVideoSample.setPixmap(QtGui.QPixmap(""))
        self.labelVideoSample.setScaledContents(True)
        self.labelVideoSample.setObjectName("labelVideoSample")
        self.groupBoxLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxLog.setGeometry(QtCore.QRect(240, 20, 710, 370))
        self.groupBoxLog.setAutoFillBackground(True)
        self.groupBoxLog.setObjectName("groupBoxLog")
        self.textLog = QtWidgets.QTextBrowser(self.groupBoxLog)
        self.textLog.setGeometry(QtCore.QRect(10, 20, 690, 340))
        self.textLog.setObjectName("textLog")
        self.groupBoxResult = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxResult.setGeometry(QtCore.QRect(10, 20, 220, 370))
        self.groupBoxResult.setAutoFillBackground(True)
        self.groupBoxResult.setObjectName("groupBoxResult")
        self.labelResult = QtWidgets.QLabel(self.groupBoxResult)
        self.labelResult.setGeometry(QtCore.QRect(10, 20, 200, 340))
        self.labelResult.setAutoFillBackground(True)
        self.labelResult.setText("")
        self.labelResult.setPixmap(QtGui.QPixmap("src/result_dfault.png"))
        self.labelResult.setScaledContents(True)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoadLocalFile = QtWidgets.QMenu(self.menuFile)
        self.menuLoadLocalFile.setObjectName("menuLoadLocalFile")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        

        self.groupBoxButton = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxButton.setGeometry(QtCore.QRect(970, 750, 940, 200))
        self.groupBoxButton.setAutoFillBackground(True)
        self.groupBoxButton.setObjectName("groupBoxButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_1.setGeometry(QtCore.QRect(35, 10, 120, 120))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText("001") 

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_2.setGeometry(QtCore.QRect(185, 10, 120, 120))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("002")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_3.setGeometry(QtCore.QRect(335, 10, 120, 120))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("003")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_4.setGeometry(QtCore.QRect(485, 10, 120, 120))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("004")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_5.setGeometry(QtCore.QRect(635, 10, 120, 120))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("005")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_6.setGeometry(QtCore.QRect(785, 10, 120, 120))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("006")

        self.pushButton_c = QtWidgets.QPushButton(self.groupBoxButton)
        self.pushButton_c.setGeometry(QtCore.QRect(35, 140, 120, 50))
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_c.setText("Clear") 

        # self.pushButton.setGeometry(QtCore.QRect(10, 520, 20, 60))
        # self.pushButton.setText("Close")          #text
        # # self.pushButton.setIcon(QIcon("close.png")) #icon
        # self.pushButton.setShortcut('Ctrl+D')  #shortcut key
        # # self.pushButton.clicked.connect(self.close)
        # self.pushButton.setToolTip("Close the widget") #Tool tip
        # self.pushButton.move(100,100)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCloseCamera = QtWidgets.QAction(MainWindow)
        self.actionCloseCamera.setObjectName("actionCloseCamera")
        self.actionLoadImage = QtWidgets.QAction(MainWindow)
        self.actionLoadImage.setObjectName("actionLoadImage")
        self.actionLoadVideo = QtWidgets.QAction(MainWindow)
        self.actionLoadVideo.setObjectName("actionLoadVideo")

        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionLoop = QtWidgets.QAction(MainWindow)
        self.actionLoop.setObjectName("actionLoop")
        self.actionHandSize = QtWidgets.QAction(MainWindow)
        self.actionHandSize.setObjectName("actionHandSize")
        self.actionMaxNumHands = QtWidgets.QAction(MainWindow)
        self.actionMaxNumHands.setObjectName("actionMaxNumHands")
        self.actionMinDetectionConfidence = QtWidgets.QAction(MainWindow)
        self.actionMinDetectionConfidence.setObjectName("actionMinDetectionConfidence")
        self.actionMinTrackingConfidence = QtWidgets.QAction(MainWindow)
        self.actionMinTrackingConfidence.setObjectName("actionMinTrackingConfidence")
        self.actionModelFile = QtWidgets.QAction(MainWindow)
        self.actionModelFile.setObjectName("actionModelFile")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionCamera_0 = QtWidgets.QAction(MainWindow)
        self.actionCamera_0.setObjectName("actionCamera_0")
        self.actionCamera_1 = QtWidgets.QAction(MainWindow)
        self.actionCamera_1.setObjectName("actionCamera_1")
        self.actionOpenCamera_2 = QtWidgets.QAction(MainWindow)
        self.actionOpenCamera_2.setObjectName("actionOpenCamera_2")
        self.actionOpenCamera = QtWidgets.QAction(MainWindow)
        self.actionOpenCamera.setObjectName("actionOpenCamera")
        self.actionSelectedCamera = QtWidgets.QAction(MainWindow)
        self.actionSelectedCamera.setObjectName("actionSelectedCamera")
        self.actionVideoFPS = QtWidgets.QAction(MainWindow)
        self.actionVideoFPS.setObjectName("actionVideoFPS")

        self.menuLoadLocalFile.addAction(self.actionLoadImage)
        self.menuLoadLocalFile.addAction(self.actionLoadVideo)
        self.menuFile.addAction(self.menuLoadLocalFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuCamera.addAction(self.actionOpenCamera)
        self.menuCamera.addAction(self.actionCloseCamera)
        self.menuView.addAction(self.actionHandSize)
        self.menuView.addAction(self.actionMinDetectionConfidence)
        self.menuView.addAction(self.actionMinTrackingConfidence)
        self.menuView.addAction(self.actionModelFile)
        self.menuActions.addAction(self.actionStart)
        self.menuActions.addAction(self.actionPredict)
        self.menuSettings.addAction(self.actionSelectedCamera)
        self.menuSettings.addAction(self.actionVideoFPS)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxImageOrVideo.setTitle(_translate("MainWindow", "Video_Stream"))
        self.groupBoxVideoSample.setTitle(_translate("MainWindow", "Video_Sample"))
        self.groupBoxLog.setTitle(_translate("MainWindow", "Log"))
        self.groupBoxResult.setTitle(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoadLocalFile.setTitle(_translate("MainWindow", "LoadLocalFile"))
        self.menuCamera.setTitle(_translate("MainWindow", "Camera"))
        self.menuView.setTitle(_translate("MainWindow", "Parameters"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCloseCamera.setText(_translate("MainWindow", "CloseCamera"))
        self.actionLoadImage.setText(_translate("MainWindow", "LoadImage"))
        self.actionLoadVideo.setText(_translate("MainWindow", "LoadVideo"))
        self.actionStart.setText(_translate("MainWindow", "StartDetect"))
        self.actionStop.setText(_translate("MainWindow", "StopDetect"))
        self.actionLoop.setText(_translate("MainWindow", "Loop(ON)"))
        self.actionHandSize.setText(_translate("MainWindow", "HandSize"))
        self.actionMaxNumHands.setText(_translate("MainWindow", "MaxNumHands"))
        self.actionMinDetectionConfidence.setText(_translate("MainWindow", "MinDetectionConfidence"))
        self.actionMinTrackingConfidence.setText(_translate("MainWindow", "MinTrackingConfidence"))
        self.actionModelFile.setText(_translate("MainWindow", "ModelFile"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionCamera_0.setText(_translate("MainWindow", "Camera 0"))
        self.actionCamera_1.setText(_translate("MainWindow", "Camera 1"))
        self.actionOpenCamera_2.setText(_translate("MainWindow", "OpenCamera"))
        self.actionOpenCamera.setText(_translate("MainWindow", "OpenCamera"))
        self.actionSelectedCamera.setText(_translate("MainWindow", "SelectedCamera0"))
        self.actionVideoFPS.setText(_translate("MainWindow", "VideoFPS"))