from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
# import convert

class InfoSearchTab(object):

    def setupUi(self, tabWidget):
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(300, 80, 823, 629))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 0, 2, 1, 2)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 1, 0, 1, 1)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.gridLayout.addWidget(self.graphicsView_5, 1, 1, 1, 1)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout.addWidget(self.graphicsView_6, 1, 3, 1, 1)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout.addWidget(self.graphicsView_7, 2, 0, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout.addWidget(self.graphicsView_8, 2, 1, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout.addWidget(self.graphicsView_9, 2, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setObjectName("widget1")
        self.gridLayout.addWidget(self.widget1, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 3, 3, 1, 1)
        tabWidget.addTab(self.widget, "")


        self.retranslateUi(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setTabText(tabWidget.indexOf(self.widget), _translate("MainWindow", "图像检索"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "上一页"))
        self.pushButton_3.setText(_translate("MainWindow", "下一页"))
        self.output_container_lst = [self.graphicsView_2, self.graphicsView_3, self.graphicsView_4, self.graphicsView_5,
                                     self.graphicsView_6, self.graphicsView_7, self.graphicsView_8, self.graphicsView_9]



class ImageRetrieval:
    input_path = './' + 'anomalyDetection'
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        # self.input_image_container_empty = True  # 图片状态
        self.input_image_name = None
        self.output_container_lst = self.MainWindow.infoSearchTab.output_container_lst
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
            self.MainWindow,"选择图片", ImageRetrieval.input_path, "Image Files(*.jpg *.png)")  # 若路径错，请在MainWindow.loadImage寻找根路径修改
        if len(imageName) == 0:
            self.MainWindow.statusbar.showMessage("未选择图片")
            return
        else:
            self.MainWindow.statusbar.showMessage("选择了" + imageName)
            # 选择图片显示的容器
            container = self.MainWindow.infoSearchTab.graphicsView
            # self.input_image_container_empty = False
            self.showImage_base(imageName, container)
            self.output_image_lst = self.MainWindow.image_retrieval_func(self.input_image_name)
            self.show_output()
            self.change_page()

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
            self.MainWindow.statusbar.showMessage("当前页数：{}，\t总页数：{}，\t 总输出图像数:{}。".format(self.output_page_index, int(
                len(self.output_image_lst) / self.output_container_num), len(self.output_image_lst)))

    def show_output(self):
        for i in range(self.output_container_num):
            self.showImage_base(self.output_image_lst[i], self.output_container_lst[i])
        self.output_page_index += 1
        self.MainWindow.statusbar.showMessage("当前页数：{}，\t总页数：{}，\t 总输出图像数:{}。".format(self.output_page_index, int(len(self.output_image_lst) / self.output_container_num), len(self.output_image_lst)))