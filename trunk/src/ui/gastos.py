# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gastos.ui'
#
# Created: Tue May 11 19:58:19 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GastosDialog(object):
    def setupUi(self, GastosDialog):
        GastosDialog.setObjectName("GastosDialog")
        GastosDialog.resize(505, 526)
        self.gridLayout_2 = QtGui.QGridLayout(GastosDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gastosTableView = QtGui.QTableView(GastosDialog)
        self.gastosTableView.setMinimumSize(QtCore.QSize(0, 0))
        self.gastosTableView.setObjectName("gastosTableView")
        self.gridLayout.addWidget(self.gastosTableView, 3, 0, 1, 5)
        self.reservastableView = QtGui.QTableView(GastosDialog)
        self.reservastableView.setObjectName("reservastableView")
        self.gridLayout.addWidget(self.reservastableView, 1, 0, 1, 5)
        self.label_2 = QtGui.QLabel(GastosDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line = QtGui.QFrame(GastosDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 5)
        self.descripcionLine = QtGui.QLineEdit(GastosDialog)
        self.descripcionLine.setObjectName("descripcionLine")
        self.gridLayout.addWidget(self.descripcionLine, 9, 0, 1, 3)
        self.label_5 = QtGui.QLabel(GastosDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 4, 1, 1)
        self.label_4 = QtGui.QLabel(GastosDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(GastosDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_6 = QtGui.QLabel(GastosDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 3, 1, 1)
        self.frame = QtGui.QFrame(GastosDialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setBaseSize(QtCore.QSize(400, 0))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, -1, 5, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.buscarLineEdit = QtGui.QLineEdit(self.frame)
        self.buscarLineEdit.setObjectName("buscarLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.buscarLineEdit)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 5)
        self.buttonBox = QtGui.QDialogButtonBox(GastosDialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 5)
        self.pendienteFrame = QtGui.QFrame(GastosDialog)
        self.pendienteFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.pendienteFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pendienteFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.pendienteFrame.setObjectName("pendienteFrame")
        self.formLayout_3 = QtGui.QFormLayout(self.pendienteFrame)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(0, 2, 2, 2)
        self.formLayout_3.setHorizontalSpacing(8)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.pendienteLabel = QtGui.QLabel(self.pendienteFrame)
        self.pendienteLabel.setObjectName("pendienteLabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.pendienteLabel)
        self.pendienteCheckBox = QtGui.QCheckBox(self.pendienteFrame)
        self.pendienteCheckBox.setEnabled(False)
        self.pendienteCheckBox.setCheckable(True)
        self.pendienteCheckBox.setChecked(True)
        self.pendienteCheckBox.setObjectName("pendienteCheckBox")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.pendienteCheckBox)
        self.gridLayout.addWidget(self.pendienteFrame, 7, 0, 1, 1)
        self.totalFrame = QtGui.QFrame(GastosDialog)
        self.totalFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.totalFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.totalFrame.setObjectName("totalFrame")
        self.formLayout_2 = QtGui.QFormLayout(self.totalFrame)
        self.formLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl = QtGui.QLabel(self.totalFrame)
        self.lbl.setObjectName("lbl")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl)
        self.totalLabel = QtGui.QLabel(self.totalFrame)
        self.totalLabel.setObjectName("totalLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.totalLabel)
        self.gridLayout.addWidget(self.totalFrame, 4, 2, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.gastoSpin = QtGui.QDoubleSpinBox(GastosDialog)
        self.gastoSpin.setMinimumSize(QtCore.QSize(80, 0))
        self.gastoSpin.setObjectName("gastoSpin")
        self.gridLayout.addWidget(self.gastoSpin, 9, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(GastosDialog)
        QtCore.QMetaObject.connectSlotsByName(GastosDialog)
        GastosDialog.setTabOrder(self.buscarLineEdit, self.reservastableView)
        GastosDialog.setTabOrder(self.reservastableView, self.gastosTableView)
        GastosDialog.setTabOrder(self.gastosTableView, self.pendienteCheckBox)
        GastosDialog.setTabOrder(self.pendienteCheckBox, self.descripcionLine)
        GastosDialog.setTabOrder(self.descripcionLine, self.buttonBox)
        GastosDialog.setTabOrder(self.buttonBox, self.gastoSpin)

    def retranslateUi(self, GastosDialog):
        GastosDialog.setWindowTitle(QtGui.QApplication.translate("GastosDialog", "Gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GastosDialog", "Gastos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("GastosDialog", "Gasto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GastosDialog", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GastosDialog", "Nuevo gasto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GastosDialog", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GastosDialog", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pendienteLabel.setText(QtGui.QApplication.translate("GastosDialog", "Pendiente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("GastosDialog", "Total:", None, QtGui.QApplication.UnicodeUTF8))

