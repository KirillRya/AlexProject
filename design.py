# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.BDtab = QWidget()
        self.BDtab.setObjectName(u"BDtab")
        self.categoryBox = QComboBox(self.BDtab)
        self.categoryBox.addItem("")
        self.categoryBox.setObjectName(u"categoryBox")
        self.categoryBox.setGeometry(QRect(20, 40, 121, 22))
        self.label = QLabel(self.BDtab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 16))
        self.label_2 = QLabel(self.BDtab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 20, 47, 13))
        self.countryBox = QComboBox(self.BDtab)
        self.countryBox.addItem("")
        self.countryBox.setObjectName(u"countryBox")
        self.countryBox.setGeometry(QRect(190, 40, 121, 22))
        self.listWidget = QListWidget(self.BDtab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 150, 301, 261))
        self.label_3 = QLabel(self.BDtab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 20, 91, 16))
        self.BDBox = QComboBox(self.BDtab)
        self.BDBox.addItem("")
        self.BDBox.setObjectName(u"BDBox")
        self.BDBox.setEnabled(False)
        self.BDBox.setGeometry(QRect(360, 40, 111, 22))
        self.addXlsBtn = QPushButton(self.BDtab)
        self.addXlsBtn.setObjectName(u"addXlsBtn")
        self.addXlsBtn.setGeometry(QRect(390, 240, 181, 51))
        self.tabWidget.addTab(self.BDtab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u0431\u043e\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 228", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0411\u0414...", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0411\u0414...", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0411\u0414 \u043a\u0430\u043a...", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.categoryBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.countryBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 xlsx", None))
        self.BDBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.addXlsBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c xlsx", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BDtab), QCoreApplication.translate("MainWindow", u"\u0411\u0414", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

