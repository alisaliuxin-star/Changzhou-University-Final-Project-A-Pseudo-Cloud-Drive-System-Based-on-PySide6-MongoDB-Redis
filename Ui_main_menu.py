# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 665)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0,        /* \u8d77\u70b9\uff1a\u5de6\u4e0a\u89d2 */\n"
"        x2:1, y2:1,        /* \u7ec8\u70b9\uff1a\u53f3\u4e0b\u89d2 */\n"
"        stop:0 #e450bb,    /* \u6e10\u53d8\u8d77\u59cb\u989c\u8272\uff08\u7ea2\u8272\uff09 */\n"
"        stop:1 #29b0f7     /* \u6e10\u53d8\u7ed3\u675f\u989c\u8272\uff08\u7eff\u8272\uff09 */\n"
"    );\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 101, 31))
        font = QFont()
        font.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 20, 101, 31))
        self.pushButton_2.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 20, 101, 31))
        self.pushButton_3.setFont(font)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.pushButton_3.setIcon(icon2)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 110, 861, 471))
        self.tableView.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.tableView.setTabletTracking(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(350, 20, 101, 31))
        self.pushButton_5.setFont(font)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButton_5.setIcon(icon3)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 70, 321, 31))
        self.plainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(260, 70, 81, 31))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setMouseTracking(False)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.pushButton_6.setIcon(icon4)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(680, 20, 201, 31))
        font1 = QFont()
        font1.setFamilies([u"\u53ef\u7231\u5c0f\u732b\u7684\u604b\u7231\u8b66\u62a5"])
        font1.setPointSize(14)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.tableView.raise_()
        self.pushButton_5.raise_()
        self.plainTextEdit.raise_()
        self.pushButton_6.raise_()
        self.label.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u5217\u8868", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6587\u4ef6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.label.setText("")
    # retranslateUi

