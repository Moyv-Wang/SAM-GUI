from ui.Ui_1 import Ui_Form 
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, QMouseEvent, QPainter, QImage, QPen, QColor, QPolygon
from PySide6.QtCore import Qt, QPoint, QObject, QThread, Signal
import cv2
import os
import numpy as np

from SAM import segment, extract_embedding
from modal_window import ModalDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.addRadio.setChecked(True)
        self.ui.configBtn.clicked.connect(self.configFunc)
        self.ui.addRadio.toggled.connect(self.addRadioFunc)
        self.ui.removeRadio.toggled.connect(self.removeRadioFunc)
        self.ui.undoBtn.clicked.connect(self.undoPoint)
        
        self.i = 0
        # self.configed = False
        self.outputDirectory = ""
        self.pointFlag = 1
        self.pointPromptsForSeg = []
        self.pointPromptsForDraw = []
        self.promptsLabels = []
        self.image_path = ""
        self.predictor = None
        self.isScaled = False
        self.pixmap = None
        self.masks = None
        self.scale_factor = 1
        self.allPreviousMasks = []

    def init_params(self):
        self.i = 0
        self.pointFlag = 1
        self.pointPromptsForSeg = []
        self.pointPromptsForDraw = []
        self.promptsLabels = []
        self.image_path = ""
        self.predictor = None
        self.isScaled = False
        self.pixmap = None
        self.masks = None
        self.scale_factor = 1
        self.allPreviousMasks = []

    def undoPoint(self):
        self.pointPromptsForDraw.pop()
        self.pointPromptsForSeg.pop()
        self.promptsLabels.pop()
        self.allPreviousMasks.pop()
        if len(self.allPreviousMasks) == 0:
            self.ui.imageLabel.setPixmap(self.pixmap)
        else:
            self.show_mask_on_pixmap(self.allPreviousMasks[-1], self.scale_factor)

    def configFunc(self):
        self.init_params()
        self.image_path = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp)")[0]
        if self.image_path:
            # self.Originalpixmap = QPixmap(self.image_path)
            self.pixmap = QPixmap(self.image_path)
            print(f"pixmap尺寸: {self.pixmap.width(), self.pixmap.height()}")
            # self.ui.imageLabel.resize(self.pixmap.width(), self.pixmap.height())
            print(f"imageLabel尺寸: {self.ui.imageLabel.width(), self.ui.imageLabel.height()}")
            if(self.pixmap.width() > self.ui.imageLabel.width() or self.pixmap.height() > self.ui.imageLabel.height()):
                pixmap = self.pixmap.scaled(self.ui.imageLabel.width(), self.ui.imageLabel.height(), Qt.AspectRatioMode.KeepAspectRatio)
                # 计算缩放比例（确保按比例缩放）
                scale_x = pixmap.width() / self.pixmap.width()
                scale_y = pixmap.height() / self.pixmap.height()
                self.scale_factor = min(scale_x, scale_y)  # 确保比例一致
                self.isScaled = True
                self.pixmap = pixmap
            self.ui.imageLabel.setPixmap(self.pixmap)
            # 获取图片文件名作为输出文件夹名
            self.outputDirectory = os.path.join('./output/', os.path.basename(self.image_path).split(".")[0])
            os.makedirs(self.outputDirectory, exist_ok=True)
        self.dialog = ModalDialog(self)
        self.dialog.show()
        self.predictor = extract_embedding(self.image_path)
        self.dialog.close()
    def addRadioFunc(self):
        self.pointFlag = 1
    
    def removeRadioFunc(self):
        self.pointFlag = 0
    
    def mousePressEvent(self, event: QMouseEvent):
        print(f"imageLabel尺寸: {self.ui.imageLabel.width(), self.ui.imageLabel.height()}")
        print(f"pixmap尺寸: {self.pixmap.width(), self.pixmap.height()}")
        # self.ui.imageLabel.setStyleSheet("background-color: yellow; border: 1px solid black;")
        if event.button() == Qt.LeftButton:  # 判断是否为鼠标左键
            # 计算左上角的偏移量（假设居中对齐）
            if self.pixmap.width() < self.ui.imageLabel.width():
                x_offset = (self.ui.imageLabel.width() - self.pixmap.width()) / 2
            else:
                x_offset = 0
            if self.pixmap.height() < self.ui.imageLabel.height():
                y_offset = (self.ui.imageLabel.height() - self.pixmap.height()) / 2
            else:
                y_offset = 0
            print(f"偏移量：{x_offset, y_offset}")
            point = self.ui.imageLabel.mapFrom(self.window(), event.position().toPoint())
            # global_point = self.ui.imageLabel.mapFrom(self.window(), QPoint(0, 0))
            # print(f"全局坐标: {global_point.x(), global_point.y()}")
            x = point.x() - x_offset
            y = point.y() - y_offset
            print(f"点击坐标: ({x}, {y})")
            x_draw = x
            y_draw = y
            if self.isScaled:
                x_seg = x / self.scale_factor
                y_seg = y / self.scale_factor
            else:
                x_seg = x
                y_seg = y
            self.pointPromptsForSeg.append([x_seg, y_seg])
            self.pointPromptsForDraw.append([x_draw, y_draw])
            self.promptsLabels.append(self.pointFlag)
            # self.drawPrompt(self.pointPromptsForDraw)
            self.masks = segment(self.image_path, self.pointPromptsForSeg, self.promptsLabels, self.predictor)
            self.allPreviousMasks.append(self.masks[0])
            self.show_mask_on_pixmap(self.masks[0], self.scale_factor)
        if(event.button() == Qt.RightButton):
            self.write_masks_to_folder()
            
    # def drawPrompt(self, pointList, size=3):
    #     # 获取当前的 QPixmap
    #     # pixmap = self.Originalpixmap.copy()
    #     pixmap = self.pixmap.copy()

    #     # 创建 QPainter 在 Pixmap 上绘制
    #     painter = QPainter(pixmap)
    #     pen = QPen(QColor("red"))  # 设置画笔颜色为红色
    #     pen.setWidth(1)
    #     painter.setPen(pen)
    #     painter.setBrush(QColor("yellow"))  # 设置填充颜色为黄色
    #     for point in pointList:
    #         x, y = point
    #         painter.drawEllipse(QPoint(int(x), int(y)), size, size)
    #     painter.end()
    #     self.ui.imageLabel.setPixmap(pixmap)

    def show_mask_on_pixmap(self, mask, scale_factor=1, size=3):
        # 创建一个 QImage 来表示掩码
        mask_image = QImage(mask.shape[1], mask.shape[0], QImage.Format_ARGB32)
        mask_image.fill(Qt.transparent)

        # 遍历掩码，将 mask == 1 的位置填充为红色
        for y in range(mask.shape[0]):
            for x in range(mask.shape[1]):
                if mask[y, x] == 1:
                    mask_image.setPixel(x, y, QColor(50, 180, 170, 100).rgba())
        
        # 将掩码图像按比例缩放到与 QLabel 中的缩放图片相匹配
        mask_image = mask_image.scaled(int(mask_image.width() * scale_factor), int(mask_image.height() * scale_factor), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 将原始 pixmap 拷贝一份用于绘制
        pixmap_with_mask = self.pixmap.copy()

        # 使用 QPainter 在原始 pixmap 上绘制掩码
        painter = QPainter(pixmap_with_mask)
        painter.drawImage(0, 0, mask_image)

        pen = QPen(QColor("red"))  # 设置画笔颜色为红色
        pen.setWidth(1)
        painter.setPen(pen)
        painter.setBrush(QColor("yellow"))  # 设置填充颜色为黄色
        for point in self.pointPromptsForDraw:
            x, y = point
            painter.drawEllipse(QPoint(int(x), int(y)), size, size)
        painter.end()

        # 显示带有掩码的图片
        self.ui.imageLabel.setPixmap(pixmap_with_mask)

    
    def write_masks_to_folder(self):
        self.i += 1
        filename = f"{self.i}.png"
        cv2.imwrite(os.path.join(self.outputDirectory, filename), (self.allPreviousMasks[-1].astype(np.uint8)) * 255)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()