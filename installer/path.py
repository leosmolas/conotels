# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path.ui'
#
# Created: Mon Jul 05 20:48:57 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PathWidget(object):
    def setupUi(self, PathWidget):
        PathWidget.setObjectName("PathWidget")
        PathWidget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(PathWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pathLine = QtGui.QLineEdit(PathWidget)
        self.pathLine.setEnabled(False)
        self.pathLine.setText("")
        self.pathLine.setObjectName("pathLine")
        self.gridLayout.addWidget(self.pathLine, 2, 0, 1, 1)
        self.fileBut = QtGui.QPushButton(PathWidget)
        self.fileBut.setObjectName("fileBut")
        self.gridLayout.addWidget(self.fileBut, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.label = QtGui.QLabel(PathWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(PathWidget)
        QtCore.QMetaObject.connectSlotsByName(PathWidget)

    def retranslateUi(self, PathWidget):
        PathWidget.setWindowTitle(QtGui.QApplication.translate("PathWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBut.setText(QtGui.QApplication.translate("PathWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PathWidget", "Elija la ruta:", None, QtGui.QApplication.UnicodeUTF8))

