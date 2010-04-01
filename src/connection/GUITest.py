# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUITest.ui'
#
# Created: Thu Apr  1 16:33:46 2010
#      by: PyQt4 UI code generator 4.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 466)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 390, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 200, 661, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 101, 17))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtGui.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 171, 80))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 61, 17))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(223, 60, 201, 80))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(530, 60, 111, 26))
        self.comboBox.setObjectName("comboBox")
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(440, 120, 61, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(540, 120, 91, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(440, 70, 81, 17))
        self.label_4.setObjectName("label_4")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 661, 191))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 61, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(280, 30, 71, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(510, 30, 91, 17))
        self.label_7.setObjectName("label_7")
        self.listView = QtGui.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(20, 60, 191, 121))
        self.listView.setObjectName("listView")
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(240, 60, 191, 121))
        self.tableView.setObjectName("tableView")
        self.columnView = QtGui.QColumnView(self.groupBox)
        self.columnView.setGeometry(QtCore.QRect(460, 60, 191, 121))
        self.columnView.setObjectName("columnView")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Conteiners:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Plain Text Edit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "TextEdit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "LineEdit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "ComboBox:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Views:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "List View:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "TableView:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "ColumnView:", None, QtGui.QApplication.UnicodeUTF8))

