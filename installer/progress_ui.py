# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created: Sat Jul  3 21:18:39 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProgressWidget(object):
    def setupUi(self, ProgressWidget):
        ProgressWidget.setObjectName("ProgressWidget")
        ProgressWidget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(ProgressWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtGui.QProgressBar(ProgressWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.label = QtGui.QLabel(ProgressWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(ProgressWidget)

    def retranslateUi(self, ProgressWidget):
        ProgressWidget.setWindowTitle(QtGui.QApplication.translate("ProgressWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProgressWidget", "Instalando, por favor espere...", None, QtGui.QApplication.UnicodeUTF8))

