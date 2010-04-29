# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grilla.ui'
#
# Created: Mon Apr 26 11:26:50 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Grilla(object):
    def setupUi(self, Grilla):
        Grilla.setObjectName("Grilla")
        Grilla.resize(621, 495)
        self.gridLayout_2 = QtGui.QGridLayout(Grilla)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mesCombo = QtGui.QComboBox(Grilla)
        self.mesCombo.setObjectName("mesCombo")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.mesCombo.addItem("")
        self.gridLayout.addWidget(self.mesCombo, 0, 2, 1, 1)
        self.anioSpin = QtGui.QSpinBox(Grilla)
        self.anioSpin.setMinimum(2000)
        self.anioSpin.setMaximum(3000)
        self.anioSpin.setObjectName("anioSpin")
        self.gridLayout.addWidget(self.anioSpin, 0, 4, 1, 1)
        self.label = QtGui.QLabel(Grilla)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Grilla)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.tableWidget = QtGui.QTableWidget(Grilla)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 6)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Grilla)
        QtCore.QMetaObject.connectSlotsByName(Grilla)

    def retranslateUi(self, Grilla):
        Grilla.setWindowTitle(QtGui.QApplication.translate("Grilla", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(0, QtGui.QApplication.translate("Grilla", "Enero", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(1, QtGui.QApplication.translate("Grilla", "Febrero", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(2, QtGui.QApplication.translate("Grilla", "Marzo", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(3, QtGui.QApplication.translate("Grilla", "Abril", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(4, QtGui.QApplication.translate("Grilla", "Mayo", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(5, QtGui.QApplication.translate("Grilla", "Junio", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(6, QtGui.QApplication.translate("Grilla", "Julio", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(7, QtGui.QApplication.translate("Grilla", "Agosto", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(8, QtGui.QApplication.translate("Grilla", "Septiembre", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(9, QtGui.QApplication.translate("Grilla", "Octubre", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(10, QtGui.QApplication.translate("Grilla", "Noviembre", None, QtGui.QApplication.UnicodeUTF8))
        self.mesCombo.setItemText(11, QtGui.QApplication.translate("Grilla", "Diciembre", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Grilla", "Mes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Grilla", "Año:", None, QtGui.QApplication.UnicodeUTF8))

