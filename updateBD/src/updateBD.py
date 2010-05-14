# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateBD.ui'
#
# Created: Thu May 13 23:10:14 2010
#      by: PyQt4 UI code generator 4.7.1
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateBD.ui'
#
# Created: Thu May 13 23:10:41 2010
#      by: PyQt4 UI code generator 4.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 212)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 151, 341, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButtonUpdate = QtGui.QPushButton(Dialog)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(160, 70, 113, 32))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.pushButtonUpdate, QtCore.SIGNAL("clicked()"), Dialog.updateBD)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("Dialog", "Actualizar", None, QtGui.QApplication.UnicodeUTF8))


