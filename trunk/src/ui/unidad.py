# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unidad.ui'
#
# Created: Wed Mar 24 11:28:25 2010
#      by: PyQt4 UI code generator snapshot-4.7.1-02f7e71246f9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_unidadDialog(object):
    def setupUi(self, unidadDialog):
        unidadDialog.setObjectName("unidadDialog")
        unidadDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(unidadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(unidadDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(unidadDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(unidadDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(unidadDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.numeroLine = QtGui.QLineEdit(unidadDialog)
        self.numeroLine.setObjectName("numeroLine")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.numeroLine)
        self.descripcionText = QtGui.QPlainTextEdit(unidadDialog)
        self.descripcionText.setObjectName("descripcionText")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.descripcionText)
        self.tipoCombo = QtGui.QComboBox(unidadDialog)
        self.tipoCombo.setObjectName("tipoCombo")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.tipoCombo)
        self.capacidadSpin = QtGui.QSpinBox(unidadDialog)
        self.capacidadSpin.setObjectName("capacidadSpin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.capacidadSpin)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(unidadDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(unidadDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), unidadDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), unidadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(unidadDialog)

    def retranslateUi(self, unidadDialog):
        unidadDialog.setWindowTitle(QtGui.QApplication.translate("unidadDialog", "Nueva unidad", None, QtGui.QApplication.UnicodeUTF8))
