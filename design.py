# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.create_bd = QAction(MainWindow)
        self.create_bd.setObjectName(u"create_bd")
        self.load_bd = QAction(MainWindow)
        self.load_bd.setObjectName(u"load_bd")
        self.save_bd = QAction(MainWindow)
        self.save_bd.setObjectName(u"save_bd")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
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
        self.categoryBox.setGeometry(QRect(20, 30, 161, 22))
        self.label = QLabel(self.BDtab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 10, 161, 20))
        self.label_2 = QLabel(self.BDtab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(21, 60, 161, 20))
        self.countryBox = QComboBox(self.BDtab)
        self.countryBox.addItem("")
        self.countryBox.setObjectName(u"countryBox")
        self.countryBox.setGeometry(QRect(20, 80, 161, 22))
        self.listWidget = QListWidget(self.BDtab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 120, 161, 411))
        self.label_3 = QLabel(self.BDtab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(221, 10, 91, 16))
        self.BDBox = QComboBox(self.BDtab)
        self.BDBox.addItem("")
        self.BDBox.setObjectName(u"BDBox")
        self.BDBox.setEnabled(False)
        self.BDBox.setGeometry(QRect(220, 30, 161, 21))
        self.baseInfo = QTableWidget(self.BDtab)
        if (self.baseInfo.columnCount() < 3):
            self.baseInfo.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.baseInfo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.baseInfo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.baseInfo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.baseInfo.setObjectName(u"baseInfo")
        self.baseInfo.setGeometry(QRect(220, 120, 541, 411))
        self.baseInfo.setLineWidth(1)
        self.baseInfo.setSelectionMode(QAbstractItemView.SingleSelection)
        self.baseInfo.setRowCount(0)
        self.baseInfo.setColumnCount(3)
        self.baseInfo.horizontalHeader().setDefaultSectionSize(163)
        self.groupBox = QGroupBox(self.BDtab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(540, 0, 161, 111))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addItemBtn = QPushButton(self.groupBox)
        self.addItemBtn.setObjectName(u"addItemBtn")
        self.addItemBtn.setEnabled(False)

        self.verticalLayout.addWidget(self.addItemBtn)

        self.changeItemBtn = QPushButton(self.groupBox)
        self.changeItemBtn.setObjectName(u"changeItemBtn")
        self.changeItemBtn.setEnabled(False)

        self.verticalLayout.addWidget(self.changeItemBtn)

        self.deleteItemBtn = QPushButton(self.groupBox)
        self.deleteItemBtn.setObjectName(u"deleteItemBtn")
        self.deleteItemBtn.setEnabled(False)

        self.verticalLayout.addWidget(self.deleteItemBtn)

        self.langBox = QGroupBox(self.BDtab)
        self.langBox.setObjectName(u"langBox")
        self.langBox.setEnabled(False)
        self.langBox.setGeometry(QRect(700, 0, 61, 111))
        self.verticalLayout_2 = QVBoxLayout(self.langBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ru_lang = QRadioButton(self.langBox)
        self.ru_lang.setObjectName(u"ru_lang")
        self.ru_lang.setChecked(True)

        self.verticalLayout_2.addWidget(self.ru_lang)

        self.en_lang = QRadioButton(self.langBox)
        self.en_lang.setObjectName(u"en_lang")

        self.verticalLayout_2.addWidget(self.en_lang)

        self.groupBox_3 = QGroupBox(self.BDtab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(400, 0, 141, 111))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.deleteBaseBtn = QPushButton(self.groupBox_3)
        self.deleteBaseBtn.setObjectName(u"deleteBaseBtn")
        self.deleteBaseBtn.setEnabled(False)

        self.gridLayout_2.addWidget(self.deleteBaseBtn, 2, 0, 1, 1)

        self.changeBaseBtn = QPushButton(self.groupBox_3)
        self.changeBaseBtn.setObjectName(u"changeBaseBtn")
        self.changeBaseBtn.setEnabled(False)

        self.gridLayout_2.addWidget(self.changeBaseBtn, 1, 0, 1, 1)

        self.addXlsBtn = QPushButton(self.groupBox_3)
        self.addXlsBtn.setObjectName(u"addXlsBtn")

        self.gridLayout_2.addWidget(self.addXlsBtn, 0, 0, 1, 1)

        self.tabWidget.addTab(self.BDtab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.resultTable = QTableWidget(self.tab_2)
        if (self.resultTable.columnCount() < 4):
            self.resultTable.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.resultTable.setObjectName(u"resultTable")
        self.resultTable.setGeometry(QRect(10, 10, 511, 451))
        self.resultTable.setColumnCount(4)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 480, 91, 16))
        font = QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.result_label = QLabel(self.tab_2)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(360, 480, 161, 16))
        self.result_label.setFont(font)
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(540, 10, 231, 111))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.positions = QSpinBox(self.groupBox_2)
        self.positions.setObjectName(u"positions")
        self.positions.setMinimum(1)
        self.positions.setMaximum(20)

        self.gridLayout_3.addWidget(self.positions, 0, 1, 2, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 2, 1)

        self.maxValue = QDoubleSpinBox(self.groupBox_2)
        self.maxValue.setObjectName(u"maxValue")
        self.maxValue.setMinimum(1.000000000000000)
        self.maxValue.setMaximum(9999999.990000000223517)
        self.maxValue.setSingleStep(100.000000000000000)

        self.gridLayout_3.addWidget(self.maxValue, 2, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(540, 160, 231, 151))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.workBtn = QPushButton(self.groupBox_4)
        self.workBtn.setObjectName(u"workBtn")
        self.workBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.workBtn)

        self.printBtn = QPushButton(self.groupBox_4)
        self.printBtn.setObjectName(u"printBtn")
        self.printBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.printBtn)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.create_bd)
        self.menu.addAction(self.load_bd)
        self.menu.addAction(self.save_bd)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0438\u0439\u0446\u0430 1\u0421, \u0432\u0435\u0440\u0441\u0438\u044f 0.01 Pre-Alpha", None))
        self.create_bd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0411\u0414...", None))
        self.load_bd.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0411\u0414...", None))
        self.save_bd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0411\u0414 \u043a\u0430\u043a...", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.categoryBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.countryBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 xlsx", None))
        self.BDBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0430\u0437\u0443...", None))

        ___qtablewidgetitem = self.baseInfo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f", None));
        ___qtablewidgetitem1 = self.baseInfo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem2 = self.baseInfo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430, $/\u0448\u0442.", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b", None))
        self.addItemBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.changeItemBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.deleteItemBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.langBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f", None))
        self.ru_lang.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443", None))
        self.en_lang.setText(QCoreApplication.translate("MainWindow", u"Eng", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u044b", None))
        self.deleteBaseBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.changeBaseBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.addXlsBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BDtab), QCoreApplication.translate("MainWindow", u"\u0411\u0414", None))
        ___qtablewidgetitem3 = self.resultTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem4 = self.resultTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e", None));
        ___qtablewidgetitem5 = self.resultTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem6 = self.resultTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430:", None))
        self.result_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u0431\u043e\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043f\u043e\u0437\u0438\u0446\u0438\u0439:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0438\u0433\u0430\u0435\u043c\u0430\u044f \u0441\u0443\u043c\u043c\u0430:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.workBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.printBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 .doc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

