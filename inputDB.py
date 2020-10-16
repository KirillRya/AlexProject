# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputDB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InputDB_Form(object):
    def setupUi(self, InputDB_Form):
        if not InputDB_Form.objectName():
            InputDB_Form.setObjectName(u"InputDB_Form")
        InputDB_Form.resize(571, 312)
        self.label_4 = QLabel(InputDB_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 170, 47, 13))
        self.inpName = QLineEdit(InputDB_Form)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setEnabled(False)
        self.inpName.setGeometry(QRect(160, 80, 201, 20))
        self.inpPathBtn = QPushButton(InputDB_Form)
        self.inpPathBtn.setObjectName(u"inpPathBtn")
        self.inpPathBtn.setGeometry(QRect(380, 30, 21, 23))
        self.label_3 = QLabel(InputDB_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 130, 71, 16))
        self.inpCountryBtn = QPushButton(InputDB_Form)
        self.inpCountryBtn.setObjectName(u"inpCountryBtn")
        self.inpCountryBtn.setGeometry(QRect(330, 170, 75, 23))
        self.inpCategoryBtn = QPushButton(InputDB_Form)
        self.inpCategoryBtn.setObjectName(u"inpCategoryBtn")
        self.inpCategoryBtn.setGeometry(QRect(330, 130, 75, 23))
        self.inpPath = QLineEdit(InputDB_Form)
        self.inpPath.setObjectName(u"inpPath")
        self.inpPath.setEnabled(False)
        self.inpPath.setGeometry(QRect(160, 30, 201, 20))
        self.inpCategory = QComboBox(InputDB_Form)
        self.inpCategory.setObjectName(u"inpCategory")
        self.inpCategory.setGeometry(QRect(160, 130, 131, 22))
        self.label_2 = QLabel(InputDB_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 91, 16))
        self.inpCountry = QComboBox(InputDB_Form)
        self.inpCountry.setObjectName(u"inpCountry")
        self.inpCountry.setGeometry(QRect(160, 170, 131, 22))
        self.label = QLabel(InputDB_Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 121, 16))
        self.inpAccept = QPushButton(InputDB_Form)
        self.inpAccept.setObjectName(u"inpAccept")
        self.inpAccept.setGeometry(QRect(390, 270, 75, 23))
        self.inpReject = QPushButton(InputDB_Form)
        self.inpReject.setObjectName(u"inpReject")
        self.inpReject.setGeometry(QRect(480, 270, 75, 23))

        self.retranslateUi(InputDB_Form)

        QMetaObject.connectSlotsByName(InputDB_Form)
    # setupUi

    def retranslateUi(self, InputDB_Form):
        InputDB_Form.setWindowTitle(QCoreApplication.translate("InputDB_Form", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("InputDB_Form", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.inpPathBtn.setText(QCoreApplication.translate("InputDB_Form", u":", None))
        self.label_3.setText(QCoreApplication.translate("InputDB_Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.inpCountryBtn.setText(QCoreApplication.translate("InputDB_Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.inpCategoryBtn.setText(QCoreApplication.translate("InputDB_Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("InputDB_Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0411\u0414", None))
        self.label.setText(QCoreApplication.translate("InputDB_Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
        self.inpAccept.setText(QCoreApplication.translate("InputDB_Form", u"OK", None))
        self.inpReject.setText(QCoreApplication.translate("InputDB_Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

