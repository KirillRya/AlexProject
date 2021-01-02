# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeDB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(436, 233)
        self.chngAccept = QPushButton(Dialog)
        self.chngAccept.setObjectName(u"chngAccept")
        self.chngAccept.setGeometry(QRect(230, 180, 75, 23))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 91, 16))
        self.chngName = QLineEdit(Dialog)
        self.chngName.setObjectName(u"chngName")
        self.chngName.setEnabled(False)
        self.chngName.setGeometry(QRect(150, 30, 201, 20))
        self.chngCategoryBtn = QPushButton(Dialog)
        self.chngCategoryBtn.setObjectName(u"chngCategoryBtn")
        self.chngCategoryBtn.setGeometry(QRect(320, 80, 75, 23))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 47, 13))
        self.chngReject = QPushButton(Dialog)
        self.chngReject.setObjectName(u"chngReject")
        self.chngReject.setGeometry(QRect(320, 180, 75, 23))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 71, 16))
        self.chngCategory = QComboBox(Dialog)
        self.chngCategory.setObjectName(u"chngCategory")
        self.chngCategory.setGeometry(QRect(150, 80, 131, 22))
        self.chngCountryBtn = QPushButton(Dialog)
        self.chngCountryBtn.setObjectName(u"chngCountryBtn")
        self.chngCountryBtn.setGeometry(QRect(320, 120, 75, 23))
        self.chngCountry = QComboBox(Dialog)
        self.chngCountry.setObjectName(u"chngCountry")
        self.chngCountry.setGeometry(QRect(150, 120, 131, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0431\u0430\u0437\u044b", None))
        self.chngAccept.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0411\u0414", None))
        self.chngCategoryBtn.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.chngReject.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.chngCountryBtn.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

