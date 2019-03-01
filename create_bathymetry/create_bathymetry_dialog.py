# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_bathymetry_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BathCreatorDialogBase(object):
    def setupUi(self, BathCreatorDialogBase):
        BathCreatorDialogBase.setObjectName("BathCreatorDialogBase")
        BathCreatorDialogBase.resize(400, 446)
        self.widget = QtWidgets.QWidget(BathCreatorDialogBase)
        self.widget.setGeometry(QtCore.QRect(20, 33, 281, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.delta = QtWidgets.QLineEdit(self.widget)
        self.delta.setObjectName("delta")
        self.verticalLayout.addWidget(self.delta)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.polygone = QtWidgets.QLineEdit(self.widget)
        self.polygone.setObjectName("polygone")
        self.verticalLayout.addWidget(self.polygone)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line = QtWidgets.QLineEdit(self.widget)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.dem = QtWidgets.QLineEdit(self.widget)
        self.dem.setObjectName("dem")
        self.verticalLayout.addWidget(self.dem)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.csv = QtWidgets.QLineEdit(self.widget)
        self.csv.setObjectName("csv")
        self.verticalLayout.addWidget(self.csv)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.button_box = QtWidgets.QDialogButtonBox(self.widget)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)

        self.retranslateUi(BathCreatorDialogBase)
        self.button_box.accepted.connect(BathCreatorDialogBase.accept)
        self.button_box.rejected.connect(BathCreatorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(BathCreatorDialogBase)

    def retranslateUi(self, BathCreatorDialogBase):
        _translate = QtCore.QCoreApplication.translate
        BathCreatorDialogBase.setWindowTitle(_translate("BathCreatorDialogBase", "CE-QUAL-W2_Bathymetry "))
        self.label.setText(_translate("BathCreatorDialogBase", "Delta Z:"))
        self.label_2.setText(_translate("BathCreatorDialogBase", "Poligones layer name:"))
        self.label_3.setText(_translate("BathCreatorDialogBase", "Lines layer name:"))
        self.label_4.setText(_translate("BathCreatorDialogBase", "DEM layer name:"))
        self.label_5.setText(_translate("BathCreatorDialogBase", "Output CSV file:"))

