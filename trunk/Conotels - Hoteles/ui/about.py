# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Mon Jun 28 10:33:36 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_aboutThis(object):
    def setupUi(self, aboutThis):
        aboutThis.setObjectName("aboutThis")
        aboutThis.resize(253, 176)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutThis.sizePolicy().hasHeightForWidth())
        aboutThis.setSizePolicy(sizePolicy)
        self.line = QtGui.QFrame(aboutThis)
        self.line.setGeometry(QtCore.QRect(0, 103, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bntAceptar = QtGui.QPushButton(aboutThis)
        self.bntAceptar.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.bntAceptar.setObjectName("bntAceptar")
        self.label = QtGui.QLabel(aboutThis)
        self.label.setGeometry(QtCore.QRect(0, 0, 251, 111))
        self.label.setStyleSheet("background-color: white;\n"
"\n"
"")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(aboutThis)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 81, 71))
        self.label_2.setStyleSheet("font-size: 48px;")
        self.label_2.setPixmap(QtGui.QPixmap(":/conosoft"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtGui.QLabel(aboutThis)
        self.label_5.setGeometry(QtCore.QRect(6, 111, 161, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(aboutThis)
        self.label_6.setGeometry(QtCore.QRect(26, 133, 32, 32))
        self.label_6.setPixmap(QtGui.QPixmap(":/windows-logo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(aboutThis)
        self.label_7.setGeometry(QtCore.QRect(76, 131, 32, 32))
        self.label_7.setPixmap(QtGui.QPixmap(":/apple-logo.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(aboutThis)
        self.label_8.setGeometry(QtCore.QRect(120, 133, 32, 32))
        self.label_8.setPixmap(QtGui.QPixmap(":/linux-logo.png"))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(aboutThis)
        QtCore.QObject.connect(self.bntAceptar, QtCore.SIGNAL("clicked()"), aboutThis.close)
        QtCore.QMetaObject.connectSlotsByName(aboutThis)

    def retranslateUi(self, aboutThis):
        aboutThis.setWindowTitle(QtGui.QApplication.translate("aboutThis", "Acerca de Conotels", None, QtGui.QApplication.UnicodeUTF8))
        self.bntAceptar.setText(QtGui.QApplication.translate("aboutThis", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("aboutThis", "Software multiplataforma:", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
import icons_rc
import icons_rc
