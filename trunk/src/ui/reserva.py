# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reserva.ui'
#
# Created: Fri Apr  2 21:03:43 2010
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
        self.huespedLine = QtGui.QLineEdit(reservaDialog)
        self.huespedLine.setObjectName("huespedLine")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.huespedLine)
        self.label_3 = QtGui.QLabel(reservaDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(reservaDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.unidadLine = QtGui.QLineEdit(reservaDialog)
        self.unidadLine.setObjectName("unidadLine")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.unidadLine)
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
        self.estadoCombo = QtGui.QComboBox(reservaDialog)
        self.estadoCombo.setObjectName("estadoCombo")
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.estadoCombo)
        self.inTime = QtGui.QTimeEdit(reservaDialog)
        self.inTime.setObjectName("inTime")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.inTime)
        self.outTime = QtGui.QTimeEdit(reservaDialog)
        self.outTime.setObjectName("outTime")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.outTime)
        self.finDate = QtGui.QDateEdit(reservaDialog)
        self.finDate.setCalendarPopup(True)
        self.finDate.setObjectName("finDate")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.finDate)
        self.inicioDate = QtGui.QDateEdit(reservaDialog)
        self.inicioDate.setCalendarPopup(True)
        self.inicioDate.setObjectName("inicioDate")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.inicioDate)
        self.inicioPreDate = QtGui.QDateEdit(reservaDialog)
        self.inicioPreDate.setCalendarPopup(True)
        self.inicioPreDate.setObjectName("inicioPreDate")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.inicioPreDate)
        self.finPreDate = QtGui.QDateEdit(reservaDialog)
        self.finPreDate.setCalendarPopup(True)
        self.finPreDate.setObjectName("finPreDate")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.finPreDate)
        self.unidadBut = QtGui.QPushButton(reservaDialog)
        self.unidadBut.setObjectName("unidadBut")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.unidadBut)
        self.huespedBut = QtGui.QPushButton(reservaDialog)
        self.huespedBut.setObjectName("huespedBut")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.huespedBut)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(reservaDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), reservaDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), reservaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(reservaDialog)
        reservaDialog.setTabOrder(self.unidadLine, self.huespedLine)
        reservaDialog.setTabOrder(self.huespedLine, self.buttonBox)

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
        self.unidadBut.setText(QtGui.QApplication.translate("reservaDialog", "Buscar Unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.huespedBut.setText(QtGui.QApplication.translate("reservaDialog", "Buscar Huesped", None, QtGui.QApplication.UnicodeUTF8))

