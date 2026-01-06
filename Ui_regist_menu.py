# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regist_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(484, 522)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0 #6a11cb, /* \u7d2b\u8272 */\n"
"        stop: 1 #2bd7d7 /* \u84dd\u8272 */\n"
"    );\n"
"    border: none;\n"
"}")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 200, 271, 31))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 270, 271, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(140, 340, 271, 31))
        self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 210, 54, 16))
        font = QFont()
        font.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font.setPointSize(14)
        font.setWeight(QFont.Medium)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 280, 54, 16))
        font1 = QFont()
        font1.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 350, 71, 16))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 90, 311, 61))
        font2 = QFont()
        font2.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font2.setPointSize(48)
        font2.setWeight(QFont.Medium)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 410, 161, 31))
        font3 = QFont()
        font3.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white; /* \u6587\u5b57\u989c\u8272 */\n"
"    background-color: rgba(255, 255, 255, 0.3); /* \u80cc\u666f\u989c\u8272\uff0c\u5e26\u6709\u4e00\u5b9a\u7684\u900f\u660e\u5ea6 */\n"
"    border: 2px solid rgba(255, 255, 255, 0.5); /* \u8fb9\u6846\u989c\u8272\u53ca\u5bbd\u5ea6\uff0c\u540c\u6837\u5e26\u6709\u900f\u660e\u5ea6 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u7a0b\u5ea6 */\n"
"    padding: 8px 16px; /* \u5185\u8fb9\u8ddd */\n"
"    font-size: 16px; /* \u5b57\u4f53\u5927\u5c0f */\n"
"    backdrop-filter: blur(4px); /* \u6a21\u7cca\u80cc\u666f\uff0c\u521b\u9020\u73bb\u7483\u6548\u679c\uff0c\u6ce8\u610f\uff1a\u6b64\u5c5e\u6027\u5728\u67d0\u4e9b\u5e73\u53f0\u6216\u7248\u672c\u53ef\u80fd\u4e0d\u5b8c\u5168\u652f\u6301 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.5); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.7); /* \u6309\u4e0b\u6309"
                        "\u94ae\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"    border-color: rgba(255, 255, 255, 0.8); /* \u6309\u4e0b\u6309\u94ae\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6ce8\u518c\u9875\u9762", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8d26\u6237", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c\u8d26\u6237", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
    # retranslateUi

