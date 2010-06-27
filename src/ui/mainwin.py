# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created: Sun Jun 27 20:49:32 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 650)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame#buttonsFrame{\n"
"    background-color: rgb(200, 200, 200);\n"
"    border-radius: 5px;\n"
"};")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtGui.QGroupBox(self.centralwidget)
        self.title.setObjectName("title")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.title)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgets = QtGui.QStackedWidget(self.title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgets.sizePolicy().hasHeightForWidth())
        self.widgets.setSizePolicy(sizePolicy)
        self.widgets.setObjectName("widgets")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.page)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widgets.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.widgets.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.widgets)
        self.gridLayout.addWidget(self.title, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.buttonsFrame = QtGui.QFrame(self.centralwidget)
        self.buttonsFrame.setStyleSheet("QToolButton{    \n"
"    border: 2px;\n"
"    border-radius: 3px;    \n"
"    icon-size:64px ;\n"
"    text-align:center;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgb(220, 220, 220);\n"
"\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"    background-color: rgba(130, 130, 130, 100);\n"
"}\n"
"\n"
"")
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.buttonsLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.gridLayout_2.addWidget(self.buttonsFrame, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 570, 18))
        self.menuBar.setObjectName("menuBar")
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuHerramientas = QtGui.QMenu(self.menuBar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNueva_unidad = QtGui.QAction(MainWindow)
        self.actionNueva_unidad.setObjectName("actionNueva_unidad")
        self.actionNuevo_Tipo = QtGui.QAction(MainWindow)
        self.actionNuevo_Tipo.setObjectName("actionNuevo_Tipo")
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionAyuda = QtGui.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuAyuda_2 = QtGui.QAction(MainWindow)
        self.menuAyuda_2.setObjectName("menuAyuda_2")
        self.menuAcercade = QtGui.QAction(MainWindow)
        self.menuAcercade.setObjectName("menuAcercade")
        self.actionPrereservas = QtGui.QAction(MainWindow)
        self.actionPrereservas.setObjectName("actionPrereservas")
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.menuAcercade)
        self.menuHerramientas.addAction(self.actionPrereservas)
        self.menuBar.addAction(self.menuAyuda.menuAction())
        self.menuBar.addAction(self.menuHerramientas.menuAction())

        self.retranslateUi(MainWindow)
        self.widgets.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Conotels 1.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", " Bienvenido!", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHerramientas.setTitle(QtGui.QApplication.translate("MainWindow", "Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_unidad.setText(QtGui.QApplication.translate("MainWindow", "Nueva unidad", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevo_Tipo.setText(QtGui.QApplication.translate("MainWindow", "Nuevo Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setText(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda_2.setText(QtGui.QApplication.translate("MainWindow", "Ayuda Conotels", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAcercade.setText(QtGui.QApplication.translate("MainWindow", "Acerca de", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrereservas.setText(QtGui.QApplication.translate("MainWindow", "Prereservas expiradas", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
