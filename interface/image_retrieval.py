from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
# import convert

class InfoSearchTab(object):
    def setupUi(self, tabWidget):
        self.layoutWidget = QtWidgets.QWidget()
        self.layoutWidget.setGeometry(QtCore.QRect(300, 80, 823, 629))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_8.addWidget(self.graphicsView_2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 3, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_9.addWidget(self.graphicsView_3)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 3, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_10.addWidget(self.graphicsView_4)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_10, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.verticalLayout_11.addWidget(self.graphicsView_5)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.verticalLayout_12.addWidget(self.graphicsView_6)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_12, 1, 3, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.verticalLayout_13.addWidget(self.graphicsView_7)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.verticalLayout_14.addWidget(self.graphicsView_8)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.gridLayout.addLayout(self.verticalLayout_14, 2, 1, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.verticalLayout_15.addWidget(self.graphicsView_9)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_15.addWidget(self.label_15)
        self.gridLayout.addLayout(self.verticalLayout_15, 2, 3, 1, 1)
        tabWidget.addTab(self.layoutWidget, "")

        self.retranslateUi(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setTabText(tabWidget.indexOf(self.layoutWidget), _translate("MainWindow", "图像检索"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "上一页"))
        self.pushButton_3.setText(_translate("MainWindow", "下一页"))
        self.label.setText(_translate("MainWindow", "输入图片"))
        self.label_8.setText(_translate("MainWindow", "输出"))
        self.label_9.setText(_translate("MainWindow", "输出"))
        self.label_10.setText(_translate("MainWindow", "输出"))
        self.label_11.setText(_translate("MainWindow", "输出"))
        self.label_12.setText(_translate("MainWindow", "输出"))
        self.label_13.setText(_translate("MainWindow", "输出"))
        self.label_14.setText(_translate("MainWindow", "输出"))
        self.label_15.setText(_translate("MainWindow", "输出"))
        self.output_container_lst = [self.graphicsView_2, self.graphicsView_3, self.graphicsView_4,
                                     self.graphicsView_5,
                                     self.graphicsView_6, self.graphicsView_7, self.graphicsView_8,
                                     self.graphicsView_9]
        self.output_label_lst = [self.label_8, self.label_9, self.label_10, self.label_11,
                                 self.label_12, self.label_13, self.label_14,self.label_15]

class ImageRetrieval:
    input_path = './' + 'anomalyDetection'
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        # self.input_image_container_empty = True  # 图片状态
        self.input_image_name = None
        self.output_container_lst = self.MainWindow.infoSearchTab.output_container_lst
        self.output_label_lst = self.MainWindow.infoSearchTab.output_label_lst
        self.output_container_num = len(self.output_container_lst)
        self.output_image_lst = None
        self.output_page_index = 0

    def showImage_base(self, imageName, container):
        normalImageName = imageName
        print(normalImageName)
        image = QPixmap()
        hasImage = image.load(normalImageName)
        print(hasImage)
        print('has:' + hasImage.__str__())

        if not hasImage:
            convert.convertBit(imageName, 8)
            # convert.convertBit(imageName, 8, "0")
            image.load(normalImageName)

        self.MainWindow.showImage(image, container)


    def loadImage(self):
        imageName, imageType = QFileDialog.getOpenFileName(
            self.MainWindow,"选择图片", ImageRetrieval.input_path, "Image Files(*.jpg *.png *.tif)")  # 若路径错，请在MainWindow.loadImage寻找根路径修改

        if len(imageName) == 0:
            self.MainWindow.statusbar.showMessage("未选择图片")
            # return
        else:
            self.MainWindow.statusbar.showMessage("选择了" + imageName)
            # 选择图片显示的容器
            container = self.MainWindow.infoSearchTab.graphicsView
            # self.input_image_container_empty = False
            self.showImage_base(imageName, container)
            self.output_image_lst = self.MainWindow.image_retrieval_func(self.input_image_name)
            self.show_output()

    def change_page(self):
        if self.output_image_lst is not None:
            sender = self.MainWindow.sender()
            if sender == self.MainWindow.infoSearchTab.pushButton_2:  # 上一页
                if self.output_page_index == 0:
                    return
                self.output_page_index -= 1
            elif sender == self.MainWindow.infoSearchTab.pushButton_3:
                if self.output_page_index >= int(len(self.output_image_lst) / self.output_container_num) - 1:
                    return
                self.output_page_index += 1

            num_base = self.output_page_index * self.output_container_num
            for i in range(self.output_container_num):
                self.showImage_base(self.output_image_lst[num_base + i], self.output_container_lst[i])
                self.output_label_lst[i].setText("输出索引{}".format(num_base + i + 1))
            self.MainWindow.statusbar.showMessage("当前页数：{}，\t总页数：{}，\t 总输出图像数:{}。".format(self.output_page_index + 1, int(
                len(self.output_image_lst) / self.output_container_num) + 1, len(self.output_image_lst)))

    def show_output(self):
        self.output_page_index = 0
        self.MainWindow.statusbar.showMessage("当前页数：{}，\t总页数：{}，\t 总输出图像数:{}。".format(1, int(
            len(self.output_image_lst) / self.output_container_num) + 1, len(self.output_image_lst)))
        for i in range(self.output_container_num):
            self.showImage_base(self.output_image_lst[i], self.output_container_lst[i])
            self.output_label_lst[i].setText("输出索引{}".format(i + 1))

