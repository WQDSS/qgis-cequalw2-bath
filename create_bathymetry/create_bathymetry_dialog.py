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
        BathCreatorDialogBase.resize(373, 446)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(BathCreatorDialogBase)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(BathCreatorDialogBase)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.delta = QtWidgets.QLineEdit(BathCreatorDialogBase)
        self.delta.setObjectName("delta")
        self.verticalLayout.addWidget(self.delta)
        self.label_2 = QtWidgets.QLabel(BathCreatorDialogBase)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.polygone = gui.QgsMapLayerComboBox(BathCreatorDialogBase)
        self.polygone.setObjectName("polygone")
        self.verticalLayout.addWidget(self.polygone)
        self.label_3 = QtWidgets.QLabel(BathCreatorDialogBase)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line = gui.QgsMapLayerComboBox(BathCreatorDialogBase)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(BathCreatorDialogBase)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.dem = gui.QgsMapLayerComboBox(BathCreatorDialogBase)
        self.dem.setObjectName("dem")
        self.verticalLayout.addWidget(self.dem)
        self.label_5 = QtWidgets.QLabel(BathCreatorDialogBase)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.csv = QtWidgets.QLineEdit(BathCreatorDialogBase)
        self.csv.setObjectName("csv")
        self.horizontalLayout.addWidget(self.csv)
        self.browsebttn = QtWidgets.QPushButton(BathCreatorDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browsebttn.sizePolicy().hasHeightForWidth())
        self.browsebttn.setSizePolicy(sizePolicy)
        self.browsebttn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browsebttn.setObjectName("browsebttn")
        self.horizontalLayout.addWidget(self.browsebttn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.button_box = QtWidgets.QDialogButtonBox(BathCreatorDialogBase)
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
        self.browsebttn.setText(_translate("BathCreatorDialogBase", "..."))

from qgis import gui
