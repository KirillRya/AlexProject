# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addElement.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddElement_Form(object):
    def setupUi(self, AddElement_Form):
        if not AddElement_Form.objectName():
            AddElement_Form.setObjectName(u"AddElement_Form")
        AddElement_Form.resize(373, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddElement_Form.sizePolicy().hasHeightForWidth())
        AddElement_Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(AddElement_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(AddElement_Form)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 3)

        self.label = QLabel(AddElement_Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.nameRu = QLineEdit(AddElement_Form)
        self.nameRu.setObjectName(u"nameRu")

        self.gridLayout.addWidget(self.nameRu, 1, 1, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)

        self.label_2 = QLabel(AddElement_Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.nameEn = QLineEdit(AddElement_Form)
        self.nameEn.setObjectName(u"nameEn")

        self.gridLayout.addWidget(self.nameEn, 3, 1, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout.addLayout(self.verticalLayout_3, 4, 1, 1, 1)

        self.label_3 = QLabel(AddElement_Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.num = QSpinBox(AddElement_Form)
        self.num.setObjectName(u"num")
        self.num.setMaximum(9999999)

        self.gridLayout.addWidget(self.num, 5, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout.addLayout(self.verticalLayout_4, 6, 1, 1, 1)

        self.label_4 = QLabel(AddElement_Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.price = QDoubleSpinBox(AddElement_Form)
        self.price.setObjectName(u"price")
        self.price.setMaximum(999999.989999999990687)

        self.gridLayout.addWidget(self.price, 7, 1, 1, 1)

        self.OKBtn = QPushButton(AddElement_Form)
        self.OKBtn.setObjectName(u"OKBtn")

        self.gridLayout.addWidget(self.OKBtn, 8, 2, 1, 1)

        self.cancelBtn = QPushButton(AddElement_Form)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.gridLayout.addWidget(self.cancelBtn, 8, 3, 1, 1)


        self.retranslateUi(AddElement_Form)

        QMetaObject.connectSlotsByName(AddElement_Form)
    # setupUi

    def retranslateUi(self, AddElement_Form):
        AddElement_Form.setWindowTitle(QCoreApplication.translate("AddElement_Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("AddElement_Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430:", None))
        self.label.setText(QCoreApplication.translate("AddElement_Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("AddElement_Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("AddElement_Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("AddElement_Form", u"\u0426\u0435\u043d\u0430", None))
        self.OKBtn.setText(QCoreApplication.translate("AddElement_Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelBtn.setText(QCoreApplication.translate("AddElement_Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

