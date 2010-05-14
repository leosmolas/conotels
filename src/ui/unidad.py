# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unidad.ui'
#
# Created: Fri May 14 14:49:55 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_unidadDialog(object):
    def setupUi(self, unidadDialog):
        unidadDialog.setObjectName("unidadDialog")
        unidadDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(unidadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(unidadDialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.numeroLine = QtGui.QLineEdit(unidadDialog)
        self.numeroLine.setObjectName("numeroLine")
        self.gridLayout_2.addWidget(self.numeroLine, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(unidadDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.tipoCombo = QtGui.QComboBox(unidadDialog)
        self.tipoCombo.setObjectName("tipoCombo")
        self.gridLayout_2.addWidget(self.tipoCombo, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(unidadDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.capacidadSpin = QtGui.QSpinBox(unidadDialog)
        self.capacidadSpin.setObjectName("capacidadSpin")
        self.gridLayout_2.addWidget(self.capacidadSpin, 2, 1, 1, 1)
        self.noDisponibleCheck = QtGui.QCheckBox(unidadDialog)
        self.noDisponibleCheck.setObjectName("noDisponibleCheck")
        self.gridLayout_2.addWidget(self.noDisponibleCheck, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(unidadDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.descripcionText = QtGui.QPlainTextEdit(unidadDialog)
        self.descripcionText.setObjectName("descripcionText")
        self.gridLayout_2.addWidget(self.descripcionText, 4, 1, 2, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(unidadDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(unidadDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), unidadDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), unidadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(unidadDialog)
        unidadDialog.setTabOrder(self.numeroLine, self.tipoCombo)
        unidadDialog.setTabOrder(self.tipoCombo, self.capacidadSpin)
        unidadDialog.setTabOrder(self.capacidadSpin, self.noDisponibleCheck)
        unidadDialog.setTabOrder(self.noDisponibleCheck, self.descripcionText)
        unidadDialog.setTabOrder(self.descripcionText, self.buttonBox)

    def retranslateUi(self, unidadDialog):
        unidadDialog.setWindowTitle(QtGui.QApplication.translate("unidadDialog", "Nueva unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("unidadDialog", "Número:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("unidadDialog", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("unidadDialog", "Capacidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.noDisponibleCheck.setText(QtGui.QApplication.translate("unidadDialog", "No disponible", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("unidadDialog", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))

