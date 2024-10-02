# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QToolButton, QVBoxLayout, QWidget)
# import resouces_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1690, 1156)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 900))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacerLeft)

        self.preBtn = QPushButton(self.layoutWidget)
        self.preBtn.setObjectName(u"preBtn")
        sizePolicy.setHeightForWidth(self.preBtn.sizePolicy().hasHeightForWidth())
        self.preBtn.setSizePolicy(sizePolicy)
        self.preBtn.setMinimumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.preBtn)

        self.nextBtn = QPushButton(self.layoutWidget)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setMinimumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.nextBtn)

        self.undoBtn = QPushButton(self.layoutWidget)
        self.undoBtn.setObjectName(u"undoBtn")
        sizePolicy.setHeightForWidth(self.undoBtn.sizePolicy().hasHeightForWidth())
        self.undoBtn.setSizePolicy(sizePolicy)
        self.undoBtn.setMinimumSize(QSize(200, 60))

        self.horizontalLayout.addWidget(self.undoBtn)

        self.addRadio = QRadioButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.addRadio)
        self.addRadio.setObjectName(u"addRadio")

        self.horizontalLayout.addWidget(self.addRadio)

        self.removeRadio = QRadioButton(self.layoutWidget)
        self.buttonGroup.addButton(self.removeRadio)
        self.removeRadio.setObjectName(u"removeRadio")
        self.removeRadio.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.removeRadio)

        self.configBtn = QToolButton(self.layoutWidget)
        self.configBtn.setObjectName(u"configBtn")

        self.horizontalLayout.addWidget(self.configBtn)

        self.hSpacerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacerRight)

        self.splitter.addWidget(self.layoutWidget)
        self.imageLabel = QLabel(self.splitter)
        # self.imageLabel.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(600, 900))
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.imageLabel)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.preBtn.setText(QCoreApplication.translate("Form", u"Previous", None))
        self.nextBtn.setText(QCoreApplication.translate("Form", u"Next", None))
        self.undoBtn.setText(QCoreApplication.translate("Form", u"Undo", None))
        self.addRadio.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.removeRadio.setText(QCoreApplication.translate("Form", u"REMOVE", None))
        self.configBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.imageLabel.setText("")
    # retranslateUi

