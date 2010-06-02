# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipo.ui'
#
# Created: Wed Jun 02 17:26:46 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_tipoDialog(object):
    def setupUi(self, tipoDialog):
        tipoDialog.setObjectName("tipoDialog")
        tipoDialog.resize(485, 203)
        self.gridLayout = QtGui.QGridLayout(tipoDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(tipoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(tipoDialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.nombreLine = QtGui.QLineEdit(tipoDialog)
        self.nombreLine.setObjectName("nombreLine")
        self.gridLayout_2.addWidget(self.nombreLine, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(tipoDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(tipoDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(tipoDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.descEdit = QtGui.QPlainTextEdit(tipoDialog)
        self.descEdit.setObjectName("descEdit")
        self.gridLayout_2.addWidget(self.descEdit, 3, 1, 2, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.costoTempBajaSpin = QtGui.QDoubleSpinBox(tipoDialog)
        self.costoTempBajaSpin.setObjectName("costoTempBajaSpin")
        self.gridLayout_2.addWidget(self.costoTempBajaSpin, 1, 1, 1, 1)
        self.costoTempAltaSpin = QtGui.QDoubleSpinBox(tipoDialog)
        self.costoTempAltaSpin.setMinimumSize(QtCore.QSize(70, 0))
        self.costoTempAltaSpin.setObjectName("costoTempAltaSpin")
        self.gridLayout_2.addWidget(self.costoTempAltaSpin, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tipoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), tipoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), tipoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(tipoDialog)
        tipoDialog.setTabOrder(self.nombreLine, self.costoTempBajaSpin)
        tipoDialog.setTabOrder(self.costoTempBajaSpin, self.costoTempAltaSpin)
        tipoDialog.setTabOrder(self.costoTempAltaSpin, self.descEdit)
        tipoDialog.setTabOrder(self.descEdit, self.buttonBox)

    def retranslateUi(self, tipoDialog):
        tipoDialog.setWindowTitle(QtGui.QApplication.translate("tipoDialog", "Agregando nuevo tipo de unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("tipoDialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("tipoDialog", "Costo en temporada baja:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("tipoDialog", "Costo en temporada alta:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("tipoDialog", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.costoTempBajaSpin.setPrefix(QtGui.QApplication.translate("tipoDialog", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.costoTempAltaSpin.setPrefix(QtGui.QApplication.translate("tipoDialog", "$ ", None, QtGui.QApplication.UnicodeUTF8))

