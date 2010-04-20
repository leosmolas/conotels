# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipo.ui'
#
# Created: Tue Apr 20 00:56:45 2010
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_tipoDialog(object):
    def setupUi(self, tipoDialog):
        tipoDialog.setObjectName("tipoDialog")
        tipoDialog.resize(485, 203)
        self.gridLayout = QtGui.QGridLayout(tipoDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(tipoDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(tipoDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(tipoDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.nombreLine = QtGui.QLineEdit(tipoDialog)
        self.nombreLine.setObjectName("nombreLine")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreLine)
        self.costoTempBajaSpin = QtGui.QSpinBox(tipoDialog)
        self.costoTempBajaSpin.setMaximum(9999999)
        self.costoTempBajaSpin.setObjectName("costoTempBajaSpin")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.costoTempBajaSpin)
        self.costoTempAltaSpin = QtGui.QSpinBox(tipoDialog)
        self.costoTempAltaSpin.setMaximum(999999)
        self.costoTempAltaSpin.setObjectName("costoTempAltaSpin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.costoTempAltaSpin)
        self.label_4 = QtGui.QLabel(tipoDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.descEdit = QtGui.QPlainTextEdit(tipoDialog)
        self.descEdit.setObjectName("descEdit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.descEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(tipoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(tipoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), tipoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), tipoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(tipoDialog)
        tipoDialog.setTabOrder(self.nombreLine, self.costoTempBajaSpin)
        tipoDialog.setTabOrder(self.costoTempBajaSpin, self.costoTempAltaSpin)
        tipoDialog.setTabOrder(self.costoTempAltaSpin, self.buttonBox)

    def retranslateUi(self, tipoDialog):
        tipoDialog.setWindowTitle(QtGui.QApplication.translate("tipoDialog", "Agregando nuevo tipo de unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("tipoDialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("tipoDialog", "Costo en temporada baja:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("tipoDialog", "Costo en temporada alta:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("tipoDialog", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))

