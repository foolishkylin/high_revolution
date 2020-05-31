# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '目标检测.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ObjectDetection(object):
    def setupUi(self, tabWidget):
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(90, 110, 258, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        tabWidget.addTab(self.widget, "")
        self.retranslateUi(tabWidget)

    # def setupUi(self, tabWidget):
    #     self.widget = QtWidgets.QWidget()
    #     self.widget.setGeometry(QtCore.QRect(260, 110, 258, 229))
    #     self.widget.setObjectName("widget")
    #     self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
    #     self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    #     self.verticalLayout.setObjectName("verticalLayout")
    #     self.graphicsView = QtWidgets.QGraphicsView(self.widget)
    #     self.graphicsView.setObjectName("graphicsView")
    #     self.verticalLayout.addWidget(self.graphicsView)
    #     self.pushButton = QtWidgets.QPushButton(self.widget)
    #     # self.pushButton.setMaximumSize(QtCore.QSize(100, 32))
    #     self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
    #     self.pushButton.setObjectName("pushButton")
    #     tabWidget.addTab(self.widget, "")
    #     self.retranslateUi(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setTabText(tabWidget.indexOf(self.widget), _translate("MainWindow", "目标检测"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "目标检测"))
