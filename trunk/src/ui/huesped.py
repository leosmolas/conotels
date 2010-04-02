# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huesped.ui'
#
# Created: Fri Apr  2 21:03:42 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_huespedDialog(object):
    def setupUi(self, huespedDialog):
        huespedDialog.setObjectName("huespedDialog")
        huespedDialog.resize(400, 159)
        self.gridLayout = QtGui.QGridLayout(huespedDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(huespedDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(huespedDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(huespedDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.apellidoLine = QtGui.QLineEdit(huespedDialog)
        self.apellidoLine.setObjectName("apellidoLine")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.apellidoLine)
        self.label_3 = QtGui.QLabel(huespedDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.nombreLine = QtGui.QLineEdit(huespedDialog)
        self.nombreLine.setObjectName("nombreLine")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.nombreLine)
        self.label_4 = QtGui.QLabel(huespedDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.telLine = QtGui.QLineEdit(huespedDialog)
        self.telLine.setObjectName("telLine")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.telLine)
        self.dniLine = QtGui.QLineEdit(huespedDialog)
        self.dniLine.setObjectName("dniLine")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dniLine)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(huespedDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), huespedDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), huespedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(huespedDialog)
        huespedDialog.setTabOrder(self.dniLine, self.apellidoLine)
        huespedDialog.setTabOrder(self.apellidoLine, self.nombreLine)
        huespedDialog.setTabOrder(self.nombreLine, self.telLine)
        huespedDialog.setTabOrder(self.telLine, self.buttonBox)

    def retranslateUi(self, huespedDialog):
        huespedDialog.setWindowTitle(QtGui.QApplication.translate("huespedDialog", "Nueva unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("huespedDialog", "DNI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("huespedDialog", "Apellido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("huespedDialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("huespedDialog", "Telefono:", None, QtGui.QApplication.UnicodeUTF8))

