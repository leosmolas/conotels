# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemploSQL1.ui'
#
# Created: Wed Mar 24 12:41:59 2010
#      by: PyQt4 UI code generator 4.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 476)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 440, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 50, 201, 221))
        self.tableView.setObjectName("tableView")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(240, 50, 191, 221))
        self.listView.setObjectName("listView")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.columnView = QtGui.QColumnView(Dialog)
        self.columnView.setGeometry(QtCore.QRect(440, 50, 221, 221))
        self.columnView.setObjectName("columnView")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 20, 91, 16))
        self.label_3.setObjectName("label_3")
        self.treeView = QtGui.QTreeView(Dialog)
        self.treeView.setGeometry(QtCore.QRect(40, 280, 191, 141))
        self.treeView.setObjectName("treeView")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "TableView:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "ListView:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "ColumnView:", None, QtGui.QApplication.UnicodeUTF8))

