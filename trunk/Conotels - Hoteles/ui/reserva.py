# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reserva.ui'
#
# Created: Fri Jul 16 19:52:06 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_reservaDialog(object):
    def setupUi(self, reservaDialog):
        reservaDialog.setObjectName("reservaDialog")
        reservaDialog.resize(1280, 701)
        self.gridLayout = QtGui.QGridLayout(reservaDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(reservaDialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.unidadCombo = QtGui.QComboBox(reservaDialog)
        self.unidadCombo.setObjectName("unidadCombo")
        self.gridLayout_2.addWidget(self.unidadCombo, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(reservaDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.huespedLine = QtGui.QLineEdit(reservaDialog)
        self.huespedLine.setObjectName("huespedLine")
        self.gridLayout_2.addWidget(self.huespedLine, 1, 1, 1, 9)
        self.huespedView = QtGui.QTableView(reservaDialog)
        self.huespedView.setObjectName("huespedView")
        self.gridLayout_2.addWidget(self.huespedView, 2, 1, 3, 9)
        self.label_3 = QtGui.QLabel(reservaDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)
        self.inicioPreDate = QtGui.QDateEdit(reservaDialog)
        self.inicioPreDate.setCalendarPopup(True)
        self.inicioPreDate.setObjectName("inicioPreDate")
        self.gridLayout_2.addWidget(self.inicioPreDate, 8, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 8, 9, 1, 1)
        self.label_11 = QtGui.QLabel(reservaDialog)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.nuevoBut = QtGui.QPushButton(reservaDialog)
        self.nuevoBut.setObjectName("nuevoBut")
        self.gridLayout_2.addWidget(self.nuevoBut, 5, 1, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(reservaDialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 20, 0, 1, 1)
        self.seniaSpin = QtGui.QDoubleSpinBox(reservaDialog)
        self.seniaSpin.setMaximum(9999.99)
        self.seniaSpin.setObjectName("seniaSpin")
        self.gridLayout_2.addWidget(self.seniaSpin, 20, 1, 1, 1)
        self.finDate = QtGui.QDateEdit(reservaDialog)
        self.finDate.setCalendarPopup(True)
        self.finDate.setObjectName("finDate")
        self.gridLayout_2.addWidget(self.finDate, 13, 4, 1, 1)
        self.label_6 = QtGui.QLabel(reservaDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 13, 3, 1, 1)
        self.label_7 = QtGui.QLabel(reservaDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 5, 1, 1)
        self.inTime = QtGui.QTimeEdit(reservaDialog)
        self.inTime.setObjectName("inTime")
        self.gridLayout_2.addWidget(self.inTime, 8, 6, 1, 1)
        self.outTime = QtGui.QTimeEdit(reservaDialog)
        self.outTime.setObjectName("outTime")
        self.gridLayout_2.addWidget(self.outTime, 13, 6, 1, 1)
        self.label_8 = QtGui.QLabel(reservaDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 13, 5, 1, 1)
        self.label_9 = QtGui.QLabel(reservaDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 7, 1, 1)
        self.estadoCombo = QtGui.QComboBox(reservaDialog)
        self.estadoCombo.setObjectName("estadoCombo")
        self.estadoCombo.addItem("")
        self.estadoCombo.addItem("")
        self.estadoCombo.addItem("")
        self.estadoCombo.addItem("")
        self.estadoCombo.addItem("")
        self.gridLayout_2.addWidget(self.estadoCombo, 8, 8, 1, 1)
        self.label_10 = QtGui.QLabel(reservaDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 13, 7, 1, 1)
        self.temporadaCombo = QtGui.QComboBox(reservaDialog)
        self.temporadaCombo.setObjectName("temporadaCombo")
        self.temporadaCombo.addItem("")
        self.temporadaCombo.addItem("")
        self.gridLayout_2.addWidget(self.temporadaCombo, 13, 8, 1, 1)
        self.label_4 = QtGui.QLabel(reservaDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 13, 0, 1, 1)
        self.finPreDate = QtGui.QDateEdit(reservaDialog)
        self.finPreDate.setCalendarPopup(True)
        self.finPreDate.setObjectName("finPreDate")
        self.gridLayout_2.addWidget(self.finPreDate, 13, 1, 1, 1)
        self.label_5 = QtGui.QLabel(reservaDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 8, 3, 1, 1)
        self.inicioDate = QtGui.QDateEdit(reservaDialog)
        self.inicioDate.setCalendarPopup(True)
        self.inicioDate.setObjectName("inicioDate")
        self.gridLayout_2.addWidget(self.inicioDate, 8, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(reservaDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(reservaDialog)
        QtCore.QMetaObject.connectSlotsByName(reservaDialog)
        reservaDialog.setTabOrder(self.unidadCombo, self.huespedLine)
        reservaDialog.setTabOrder(self.huespedLine, self.huespedView)
        reservaDialog.setTabOrder(self.huespedView, self.nuevoBut)
        reservaDialog.setTabOrder(self.nuevoBut, self.inicioPreDate)

    def retranslateUi(self, reservaDialog):
        reservaDialog.setWindowTitle(QtGui.QApplication.translate("reservaDialog", "Nueva reserva", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("reservaDialog", "Unidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("reservaDialog", "Filtrar huéspedes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("reservaDialog", "Inicio Prereserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("reservaDialog", "Huésped:", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoBut.setText(QtGui.QApplication.translate("reservaDialog", "Crear nuevo huésped", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("reservaDialog", "Seña:", None, QtGui.QApplication.UnicodeUTF8))
        self.seniaSpin.setPrefix(QtGui.QApplication.translate("reservaDialog", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("reservaDialog", "Fin Reserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("reservaDialog", "Hora CheckIn:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("reservaDialog", "Hora CheckOut:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("reservaDialog", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.estadoCombo.setItemText(0, QtGui.QApplication.translate("reservaDialog", "Pre Reservado", None, QtGui.QApplication.UnicodeUTF8))
        self.estadoCombo.setItemText(1, QtGui.QApplication.translate("reservaDialog", "Reservado", None, QtGui.QApplication.UnicodeUTF8))
        self.estadoCombo.setItemText(2, QtGui.QApplication.translate("reservaDialog", "Reserva en curso", None, QtGui.QApplication.UnicodeUTF8))
        self.estadoCombo.setItemText(3, QtGui.QApplication.translate("reservaDialog", "Reserva terminada", None, QtGui.QApplication.UnicodeUTF8))
        self.estadoCombo.setItemText(4, QtGui.QApplication.translate("reservaDialog", "Reserva cancelada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("reservaDialog", "Temporada:", None, QtGui.QApplication.UnicodeUTF8))
        self.temporadaCombo.setItemText(0, QtGui.QApplication.translate("reservaDialog", "Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.temporadaCombo.setItemText(1, QtGui.QApplication.translate("reservaDialog", "Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("reservaDialog", "Fin Prereserva:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("reservaDialog", "Inicio Reserva:", None, QtGui.QApplication.UnicodeUTF8))

