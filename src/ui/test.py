# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Apr 01 13:38:00 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_reservaDialog(object):
    def setupUi(self, reservaDialog):
        reservaDialog.setObjectName("reservaDialog")
        reservaDialog.resize(400, 375)
        self.gridLayout = QtGui.QGridLayout(reservaDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(reservaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(reservaDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(reservaDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(reservaDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(reservaDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.numeroLine_2 = QtGui.QLineEdit(reservaDialog)
        self.numeroLine_2.setObjectName("numeroLine_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.numeroLine_2)
        self.label_5 = QtGui.QLabel(reservaDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(reservaDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(reservaDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(reservaDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(reservaDialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_9)
        self.comboBox = QtGui.QComboBox(reservaDialog)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.timeEdit = QtGui.QTimeEdit(reservaDialog)
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.timeEdit)
        self.timeEdit_2 = QtGui.QTimeEdit(reservaDialog)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.timeEdit_2)
        self.dateEdit = QtGui.QDateEdit(reservaDialog)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.dateEdit)
        self.dateEdit_2 = QtGui.QDateEdit(reservaDialog)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.dateEdit_2)
        self.dateEdit_3 = QtGui.QDateEdit(reservaDialog)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dateEdit_3)
        self.dateEdit_4 = QtGui.QDateEdit(reservaDialog)
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.dateEdit_4)
        self.pushButton = QtGui.QPushButton(reservaDialog)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(reservaDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.checkBox = QtGui.QCheckBox(reservaDialog)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(reservaDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), reservaDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), reservaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(reservaDialog)
        reservaDialog.setTabOrder(self.numeroLine_2, self.buttonBox)

    def retranslateUi(self, reservaDialog):
        reservaDialog.setWindowTitle(QtGui.QApplication.translate("reservaDialog", "Nueva unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("reservaDialog", "Unidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("reservaDialog", "Huesped:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("reservaDialog", "Inicio Prereserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("reservaDialog", "Fin Prereserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("reservaDialog", "Inicio Reserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("reservaDialog", "Fin Reserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("reservaDialog", "Hora CheckIn:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("reservaDialog", "Hora CheckOut:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("reservaDialog", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("reservaDialog", "Buscar Unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("reservaDialog", "Buscar Huesped", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("reservaDialog", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
