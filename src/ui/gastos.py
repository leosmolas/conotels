# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gastos.ui'
#
# Created: Thu Apr 15 16:11:37 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GastosDialog(object):
    def setupUi(self, GastosDialog):
        GastosDialog.setObjectName("GastosDialog")
        GastosDialog.resize(545, 371)
        self.gridLayout_2 = QtGui.QGridLayout(GastosDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.unidadCombo = QtGui.QComboBox(GastosDialog)
        self.unidadCombo.setObjectName("unidadCombo")
        self.gridLayout.addWidget(self.unidadCombo, 0, 1, 1, 3)
        self.tableView = QtGui.QTableView(GastosDialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 4)
        self.label_5 = QtGui.QLabel(GastosDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 3, 1, 1)
        self.descripcionLine = QtGui.QLineEdit(GastosDialog)
        self.descripcionLine.setObjectName("descripcionLine")
        self.gridLayout.addWidget(self.descripcionLine, 9, 0, 1, 2)
        self.label_6 = QtGui.QLabel(GastosDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 2, 1, 1)
        self.gastoSpin = QtGui.QSpinBox(GastosDialog)
        self.gastoSpin.setObjectName("gastoSpin")
        self.gridLayout.addWidget(self.gastoSpin, 9, 3, 1, 1)
        self.label = QtGui.QLabel(GastosDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(GastosDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(GastosDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(GastosDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GastosDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 4)
        self.line = QtGui.QFrame(GastosDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 4)
        self.label_7 = QtGui.QLabel(GastosDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(GastosDialog)
        QtCore.QMetaObject.connectSlotsByName(GastosDialog)

    def retranslateUi(self, GastosDialog):
        GastosDialog.setWindowTitle(QtGui.QApplication.translate("GastosDialog", "Gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("GastosDialog", "Gasto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GastosDialog", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GastosDialog", "Unidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GastosDialog", "Gastos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GastosDialog", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GastosDialog", "Nuevo gasto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("GastosDialog", "Total:", None, QtGui.QApplication.UnicodeUTF8))

