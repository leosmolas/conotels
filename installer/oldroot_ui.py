# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oldroot.ui'
#
# Created: Sat Jul  3 21:18:30 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OldRootWidget(object):
    def setupUi(self, OldRootWidget):
        OldRootWidget.setObjectName("OldRootWidget")
        OldRootWidget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(OldRootWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.existsLabel = QtGui.QLabel(OldRootWidget)
        self.existsLabel.setWordWrap(True)
        self.existsLabel.setObjectName("existsLabel")
        self.gridLayout.addWidget(self.existsLabel, 3, 0, 1, 1)
        self.passLine = QtGui.QLineEdit(OldRootWidget)
        self.passLine.setAutoFillBackground(False)
        self.passLine.setInputMask("")
        self.passLine.setText("")
        self.passLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passLine.setObjectName("passLine")
        self.gridLayout.addWidget(self.passLine, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.basicLabel = QtGui.QLabel(OldRootWidget)
        self.basicLabel.setObjectName("basicLabel")
        self.gridLayout.addWidget(self.basicLabel, 2, 0, 1, 1)
        self.errorLabel = QtGui.QLabel(OldRootWidget)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(OldRootWidget)
        QtCore.QMetaObject.connectSlotsByName(OldRootWidget)

    def retranslateUi(self, OldRootWidget):
        OldRootWidget.setWindowTitle(QtGui.QApplication.translate("OldRootWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.existsLabel.setText(QtGui.QApplication.translate("OldRootWidget", "Ya existe una instalacion de MySQL.\n"
"Por favor, escriba el password de root para poder instalar Conotels:", None, QtGui.QApplication.UnicodeUTF8))
        self.basicLabel.setText(QtGui.QApplication.translate("OldRootWidget", "Por favor, ingrese el password para la base de datos:", None, QtGui.QApplication.UnicodeUTF8))
        self.errorLabel.setText(QtGui.QApplication.translate("OldRootWidget", "Ha ocurrido un error.\n"
"Por favor, vuelva a ingresar el password de la base de datos:", None, QtGui.QApplication.UnicodeUTF8))

