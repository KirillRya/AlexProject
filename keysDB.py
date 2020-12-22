# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keysDB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListControl(object):
    def setupUi(self, ListControl):
        if not ListControl.objectName():
            ListControl.setObjectName(u"ListControl")
        ListControl.resize(292, 480)
        self.verticalLayout = QVBoxLayout(ListControl)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ListControl)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.keysInputEdit = QLineEdit(ListControl)
        self.keysInputEdit.setObjectName(u"keysInputEdit")

        self.horizontalLayout.addWidget(self.keysInputEdit)

        self.keysAddBtn = QPushButton(ListControl)
        self.keysAddBtn.setObjectName(u"keysAddBtn")

        self.horizontalLayout.addWidget(self.keysAddBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.keysList = QListWidget(ListControl)
        self.keysList.setObjectName(u"keysList")

        self.verticalLayout.addWidget(self.keysList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.keysDeleteBtn = QPushButton(ListControl)
        self.keysDeleteBtn.setObjectName(u"keysDeleteBtn")

        self.horizontalLayout_2.addWidget(self.keysDeleteBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ListControl)

        QMetaObject.connectSlotsByName(ListControl)
    # setupUi

    def retranslateUi(self, ListControl):
        ListControl.setWindowTitle(QCoreApplication.translate("ListControl", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ListControl", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.keysAddBtn.setText(QCoreApplication.translate("ListControl", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.keysDeleteBtn.setText(QCoreApplication.translate("ListControl", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

