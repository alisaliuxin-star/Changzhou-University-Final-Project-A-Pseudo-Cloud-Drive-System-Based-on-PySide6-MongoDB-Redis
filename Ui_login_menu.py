# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 613)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0,        /* \u8d77\u70b9\uff1a\u5de6\u4e0a\u89d2 */\n"
"        x2:1, y2:1,        /* \u7ec8\u70b9\uff1a\u53f3\u4e0b\u89d2 */\n"
"        stop:0 #7744FF ,    /* \u6e10\u53d8\u8d77\u59cb\u989c\u8272 */\n"
"        stop:1 #00FFFF     /* \u6e10\u53d8\u7ed3\u675f\u989c\u8272 */\n"
"    );\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 150, 341, 61))
        font = QFont()
        font.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 pink, stop:1 purple);\n"
"    text-shadow: -1px -1px 0 black,\n"
"                  1px -1px 0 black,\n"
"                 -1px  1px 0 black,\n"
"                  1px  1px 0 black;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 310, 38, 25))
        font1 = QFont()
        font1.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 380, 141, 31))
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 440, 141, 31))
        self.pushButton_2.setFont(font1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(290, 240, 251, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(290, 309, 251, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(220, 240, 40, 31))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u76d8\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
    # retranslateUi

