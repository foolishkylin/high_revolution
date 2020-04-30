# -*- coding: UTF-8 -*-

# Author: 曾鹏慷、朱锦涛
# Time:   2019/8/10
# Name:   软件部分

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QMessageBox, QProgressDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt, QThread,pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout
from segnet_predict import predict
from PCAKmeans import find_PCAKmeans
import convert
import os
from RcTest import test_rc_map
import darkChannel
import keras
keras.backend.clear_session()
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

class MyThread(QThread):#线程类
     def __init__(self,path):
         super(MyThread, self).__init__()
         self.ui = MyMainWindow()
         self.path = path
     def run(self): #线程执行函数
         try:
            filepath = predict(self.path)
            self.showRealResultImage(filepath)
            print('no')
         except Exception as e:
             print(e)
         self.sleep(1)#释放自定义的信号
             #通过自定义信号把传递给槽函数



class MyMainWindow(QMainWindow, Ui_MainWindow):
    # 图片容器是否为空
    # 变化检测
    isCDOriginImageContainer1Empty = True
    isCDOriginImageContainer2Empty = True
    isCDResultImageContainerEmpty = True
    # 原图名字
    CDOriginImageName1 = ''
    CDOriginImageName2 = ''

    # 语义分割
    isSSOriginImageContainerEmpty = True
    isSSResultImageContainerEmpty = True
    # 原图名字
    SSOriginImageName = ''

    # 异常检测
    isADOriginImageContainerEmpty = True
    #isADOriginImageContainer2Empty = True
    isADResultImageContainerEmpty = True
    # 原图名字
    ADOriginImageName = ''
    #IFOriginImageName2 = ''

    # 去云雾
    isRemovalOriginImageContainerEmpty = True
    isRemovalResultImageContainerEmpty = True
    # 原图名字
    removalOriginImageName = ''

    # 原图
    CDOriginImageName = ''
    SSOriginImageName = ''
    ADOriginImageName = ''
    removalOriginImageName = ''

    originImageName = ''
    container = None

    # 原图与结果图片的对应关系
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    # 显示进度条
    def showLoadingBar(self):
        self.progress = QProgressDialog(self)
        self.progress.setWindowTitle("请稍等")
        self.progress.setLabelText("正在处理，请稍等...")
        self.progress.setCancelButtonText("取消")
        self.progress.setMinimum(0)
        self.progress.setMaximum(0)
        self.progress.setWindowModality(Qt.WindowModal)
        self.progress.show()

    # 隐藏进度条
    def closeLoadingBar(self):
        self.progress.close()

    def showImage(self, pixmap, container):
        # 显示图片
        container.scene = QGraphicsScene()
        container.item = QGraphicsPixmapItem(pixmap)
        container.scene.addItem(container.item)
        container.setScene(container.scene)
        container.fitInView(container.item)

    # 显示已经准备好的处理结果
    def showResultImage(self):
        self.testTimer.stop()
        self.closeLoadingBar()

        sender = self.sender()
        print(sender)

        paths = self.originImageName.split('/')

        originImgName = paths[len(paths) - 1]
        resultImageName = self.files[originImgName]
        normalImageName = '.' + resultImageName.split(".")[1] + '.jpg'

        print('paths: ', paths)
        print('originImgName: ', originImgName)
        print('resultImageName: ', resultImageName)
        print('normalImageName: ', normalImageName)

        image = QPixmap()
        hasImage = image.load(normalImageName)
        if not hasImage:
            convert.convertBit(resultImageName, 8)
            image.load(normalImageName)
        self.showImage(image, self.container)

        # 显示操作内容
        if self.container == self.CDResultContainer:
            self.isCDResultImageContainerEmpty = False
            self.statusbar.showMessage("完成变化检测处理")
        elif self.container == self.ADResultContainer:
            self.isADResultImageContainerEmpty = False
            self.statusbar.showMessage("完成异常检测处理")


    # 显示真正处理过的结果
    def showRealResultImage(self, imageName):
        image = QPixmap()
        hasImage = image.load(imageName)
        if not hasImage:
            self.statusbar.showMessage("处理失败")
            return
        self.showImage(image, self.container)

        if self.container == self.CDResultContainer:
            self.isCDResultImageContainerEmpty = False
            self.statusbar.showMessage("完成变化检测处理")
        elif self.container == self.SSResultContainer:
            self.isSSResultImageContainerEmpty = False
            self.statusbar.showMessage("完成语义分割处理")
        elif self.container == self.ADResultContainer:
            self.isADResultImageContainerEmpty = False
            self.statusbar.showMessage("完成异常检测处理")
        elif self.container == self.removalResultContainer:
            self.isRemovalResultImageContainerEmpty = False
            self.statusbar.showMessage("完成去云雾处理")

    # 加载图片
    def loadImage(self):
        # 信号源
        sender = self.sender()
        # 选择图片显示的容器
        dirRoot = './'
        if sender == self.CDChoseImageBtn1:
            dirRoot += 'changeDetection'
        elif sender == self.CDChoseImageBtn2:
            dirRoot += 'changeDetection'
        elif sender == self.SSChoseImageBtn:
            # dirRoot += 'anomalyDetection'
            dirRoot += 'Segmentation'
        elif sender == self.ADChoseImageBtn:
            dirRoot += 'anomalyDetection'
        elif sender == self.removalChoseImageBtn:
            dirRoot += 'removal'

        imageName, imageType = QFileDialog.getOpenFileName(self, "选择图片", dirRoot, "Image Files(*.jpg *.png)")
        if len(imageName) == 0:
            self.statusbar.showMessage("未选择图片")
            return
        else:
            self.statusbar.showMessage("选择了" + imageName)
            # 选择图片显示的容器
            container = None
            if sender == self.CDChoseImageBtn1:
                container = self.CDOriginImageContainer1
                self.isCDOriginImageContainer1Empty = False
                self.CDOriginImageName1 = imageName

            elif sender == self.CDChoseImageBtn2:
                container = self.CDOriginImageContainer2
                self.isCDOriginImageContainer2Empty = False
                self.CDOriginImageName2 = imageName

            elif sender == self.ADChoseImageBtn:
                container = self.ADOriginImageContainer
                self.isADOriginImageContainerEmpty = False
                self.ADOriginImageName = imageName

            elif sender == self.SSChoseImageBtn:
                container = self.SSOriginImageContainer
                self.isSSOriginImageContainerEmpty = False
                self.SSOriginImageName = imageName

            elif sender == self.removalChoseImageBtn:
                container = self.removalOriginImageContainer
                self.isRemovalOriginImageContainerEmpty = False
                self.removalOriginImageName = imageName

            normalImageName = imageName.split(".")[0] + '.jpg'
            image = QPixmap()
            hasImage = image.load(normalImageName)
            print('has:' + hasImage.__str__())

            if not hasImage:
                convert.convertBit(imageName, 8)
                # convert.convertBit(imageName, 8, "0")
                image.load(normalImageName)

            self.showImage(image, container)

    # 变化检测
    def changeDetection(self):
        if self.isCDOriginImageContainer1Empty or self.isCDOriginImageContainer2Empty:
            QMessageBox.warning(self, "提示", "请选择图片")
        else:
            self.statusbar.showMessage("正在处理")
            self.showLoadingBar()

            # 清除结果容器的图片
            if not self.isCDResultImageContainerEmpty:
                self.CDResultContainer.scene.clear()
                self.isCDResultImageContainerEmpty = True

            self.originImageName = self.CDOriginImageName1
            self.container = self.CDResultContainer

            # self.testTimer = QTimer()  # 创建定时器
            # self.testTimer.timeout.connect(self.showResultImage)  # 定时超时事件绑定showResultImage函数
            # self.testTimer.start(3000)  # 定时器每一秒执行一次

            filename = find_PCAKmeans(self.CDOriginImageName1, self.CDOriginImageName2)
            print(self.CDOriginImageName1)
            print(self.CDOriginImageName2)
            print(filename)
            self.showRealResultImage(filename)
            self.closeLoadingBar()

    # 清除变化检测容器内的图片
    def resetCDContainer(self):
        if self.isCDOriginImageContainer1Empty and self.isCDOriginImageContainer2Empty and self.isCDResultImageContainerEmpty:
            return

        if not self.isCDOriginImageContainer1Empty:
            self.CDOriginImageContainer1.scene.clear()
            self.isCDOriginImageContainer1Empty = True

        if not self.isCDOriginImageContainer2Empty:
            self.CDOriginImageContainer2.scene.clear()
            self.isCDOriginImageContainer2Empty = True

        if not self.isCDResultImageContainerEmpty:
            self.CDResultContainer.scene.clear()
            self.isCDResultImageContainerEmpty = True

        self.statusbar.showMessage("重置成功")

    def showpicture(self,filepath):
        self.showRealResultImage(filepath)


    # 语义分割
    def Segmentation(self):
        self.statusbar.showMessage("正在处理")

        if self.isSSOriginImageContainerEmpty:
            QMessageBox.warning(self, "提示", "请选择图片")
        else:
            self.showLoadingBar()

            # 清除结果容器的图片
            if not self.isSSResultImageContainerEmpty:
                self.SSResultContainer.scene.clear()
                self.isSSResultImageContainerEmpty = True

            self.originImageName = self.SSOriginImageName
            self.container = self.SSResultContainer

            # self.testTimer = QTimer()  # 创建定时器
            # self.testTimer.timeout.connect(self.showResultImage)  # 定时超时事件绑定show_time这个函数
            # self.testTimer.start(3000)  # 定时器每一秒执行一次

            try:
                path = self.SSOriginImageName
                print(path)
                # self.thread = MyThread(path)
                # QApplication.processEvents()
                # self.thread.start()
                filepath = predict(path)
                self.showRealResultImage(filepath)
                self.closeLoadingBar()
            except Exception as e:
                print(e)



    # 清除语义分割容器内的图片
    def resetSSContainer(self):
        if self.isSSOriginImageContainerEmpty and self.isSSResultImageContainerEmpty:
            return

        if not self.isSSOriginImageContainerEmpty:
            self.SSOriginImageContainer.scene.clear()
            self.isSSOriginImageContainerEmpty = True
            if not self.isSSResultImageContainerEmpty:
                self.SSResultContainer.scene.clear()
                self.isSSResultImageContainerEmpty = True

        self.statusbar.showMessage("重置成功")


    # real异常检测
    def anomalyDetection(self):

        if self.isADOriginImageContainerEmpty:
            QMessageBox.warning(self, "提示", "avbc")
            # QMessageBox.about(None, "提示", "未选择原图！")
        else:
            self.statusbar.showMessage("正在处理")
            self.showLoadingBar()

            self.originImageName = self.ADOriginImageName
            self.container = self.ADResultContainer

            #self.testTimer = QTimer()  # 创建定时器
            #self.testTimer.timeout.connect(self.showResultImage)  # 定时超时事件绑定show_time这个函数
            #self.testTimer.start(1500)  # 定时器每一秒执行一次


            # 清除结果容器的图片
            if not self.isADResultImageContainerEmpty:
                self.ADResultContainer.scene.clear()
                self.isADResultImageContainerEmpty = True
            #显示处理图片
            try:
                filename = test_rc_map(self.ADOriginImageName)
                self.showRealResultImage(filename)
                self.closeLoadingBar()
            except Exception as e:
                print(e)
    # 清除异常检测容器内的图片
    def resetADContainer(self):
        if self.isADOriginImageContainerEmpty and self.isADResultImageContainerEmpty:
            return

        if not self.isADOriginImageContainerEmpty:
            self.ADOriginImageContainer.scene.clear()
            self.isADOriginImageContainerEmpty = True
        if not self.isADResultImageContainerEmpty:
            self.ADResultContainer.scene.clear()
            self.isADResultImageContainerEmpty = True

        self.statusbar.showMessage("重置成功")

    #去云雾
    def Removal(self):

        if self.isRemovalOriginImageContainerEmpty:
            QMessageBox.warning(self, "提示", "未选择原图")
        else:
            self.statusbar.showMessage("正在处理")
            self.showLoadingBar()

            self.originImageName = self.removalOriginImageName
            self.container = self.removalResultContainer

            # self.testTimer = QTimer()  # 创建定时器
            # self.testTimer.timeout.connect(self.showResultImage)  # 定时超时事件绑定show_time这个函数
            # self.testTimer.start(1500)  # 定时器每一秒执行一次

            # 清除结果容器的图片
            if not self.isRemovalResultImageContainerEmpty:
                self.removalResultContainer.scene.clear()
                self.isRemovalResultImageContainerEmpty = True
            # 显示处理图片
            try:
                filename = darkChannel.getDefog(self.removalOriginImageName)
                print(filename)
                self.showRealResultImage(filename)
            except Exception as e:
                print(e)
            self.closeLoadingBar()

    # 清除去云雾容器内的图片
    def resetRemovalContainer(self):
        if self.isRemovalOriginImageContainerEmpty and self.isRemovalResultImageContainerEmpty:
            return

        if not self.isRemovalOriginImageContainerEmpty:
            self.removalOriginImageContainer.scene.clear()
            self.isRemovalOriginImageContainerEmpty = True
        if not self.isRemovalResultImageContainerEmpty:
            self.removalResultContainer.scene.clear()
            self.isRemovalResultImageContainerEmpty = True

        self.statusbar.showMessage("重置成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())