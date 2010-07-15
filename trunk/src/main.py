# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui.mainwin import Ui_MainWindow

from unidad import UnidadDialog
from tipo import TipoDialog
from reserva import ReservaDialog
from huesped import HuespedDialog
from gastos import GastosDialog
from admin import Admin
from grilla import GrillaDialog
from about import AboutDialog
from models.reserva import Reserva
import os
import backup

from connection.connection import Connection

import icons_rc

class MainWindow(QtGui.QMainWindow):
	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/house.png")))
		self.statusBar = QtGui.QStatusBar(self)
		self.setStatusBar(self.statusBar)
		self.ui.statusBar = self.statusBar;
		
		self.buttonGroup = QtGui.QButtonGroup(self)
		
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.ui.buttonsLayout.addItem(spacerItem)
				
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/calendar.png"))
		button.setText("Grilla")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		button.setChecked(True)
		self.buttonGroup.addButton(button,1)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/diaryplain.png"))
		button.setText("Reservas")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,2)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/purse.png"))
		button.setText("Gastos")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,3)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/people.png"))
		button.setText(u"Huésped")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,4)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/property.png"))
		button.setText("Unidades")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,5)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/tools.png"))
		button.setText("Tipos de Unidad")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,6)
		self.ui.buttonsLayout.addWidget(button)
		
		button = QtGui.QToolButton(self.ui.buttonsFrame)
		button.setIcon(QtGui.QIcon(":/exit.png"))
		button.setText("Salir")
		button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		button.setCheckable(True)
		self.buttonGroup.addButton(button,7)
		self.ui.buttonsLayout.addWidget(button)
		
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.ui.buttonsLayout.addItem(spacerItem)
		
		QtCore.QObject.connect(self.buttonGroup, QtCore.SIGNAL("buttonClicked(int)"), self.butClicked)
				
		QtCore.QObject.connect(self.ui.menuAcercade,QtCore.SIGNAL("activated()"),self.abrirAcercade)
		
		QtCore.QObject.connect(self.ui.actionPrereservas,QtCore.SIGNAL("activated()"),self.checkPrereservas)
		
		QtCore.QObject.connect(self.ui.actionCrear_Backup,QtCore.SIGNAL("triggered()"),self.createBackup)
		
		QtCore.QObject.connect(self.ui.actionCargar_Backup,QtCore.SIGNAL("triggered()"),self.loadBackup)
		
		self.butClicked(1)
		
		#self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewTypeBut.setText("Grilla")
		#self.addNewTypeBut.setIcon(QtGui.QIcon(":/calendar.png"))
		#self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		
		#self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewUnitBut.setText("Administrar unidades")
		#self.addNewUnitBut.setIcon(QtGui.QIcon(":/property.png"))
		#self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		#self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewUnitBut.setText("Administrar reservas")
		#self.addNewUnitBut.setIcon(QtGui.QIcon(":/diaryplain.png"))
		#self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		#self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewUnitBut.setText("Administrar tipo")
		#self.addNewUnitBut.setIcon(QtGui.QIcon(":/tools.png"))
		#self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		#self.addNewUnitBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewUnitBut.setText("Administrar huesped")
		#self.addNewUnitBut.setIcon(QtGui.QIcon(":/people.png"))
		#self.addNewUnitBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewUnitBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		#self.addNewTypeBut = QtGui.QListWidgetItem(self.ui.options)
		#self.addNewTypeBut.setText("Administrar gastos")
		#self.addNewTypeBut.setIcon(QtGui.QIcon())
		#self.addNewTypeBut.setTextAlignment(QtCore.Qt.AlignHCenter)
		#self.addNewTypeBut.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)


		#QtCore.QObject.connect(self.ui.menuAdministracion, QtCore.SIGNAL("triggered(QAction *)"),
		#		self.changeToAction)
		
	def openConn(self):
		file = open("conf.dat")
		user = file.readline()
		password = file.readline()
		self.conn = Connection(dbName="conotels", dbUser=user.replace('\n', ''), dbPass=password.replace('\n', ''))
		self.conn.open()
		

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)

		'''file = open("conf.dat")
		user = file.readline()
		password = file.readline()
		self.conn = Connection(dbName="conotels", dbUser=user.replace('\n', ''), dbPass=password.replace('\n', ''))
		self.conn.open()'''
		self.openConn()

		self.setup()

		#self.ui.options.currentItemChanged.connect(self.changeView)
		#self.ui.options.setViewMode(QtGui.QListView.IconMode)
		#self.ui.options.setCurrentRow(0)

	#def changeToAction(self, action):
		#self.ui.widgets.removeWidget(self.ui.widgets.currentWidget())
		#if action.text() == "Nueva unidad":
			#self.ui.title.setTitle(action.text())
			#self.ui.widgets.insertWidget(1, UnidadDialog(self.conn))
		#elif action.text() == "Nuevo Tipo":
			#self.ui.title.setTitle(action.text())
			#self.ui.widgets.insertWidget(1, TipoDialog(self.conn))
		#self.ui.widgets.setCurrentIndex(1)

	def __del__(self):
		self.conn.close()

	def butClicked(self, selected, shortcut=False):
		if (selected == self.buttonGroup.checkedId() or shortcut):
			
			if selected != 7:
				self.ui.widgets.removeWidget(self.ui.widgets.currentWidget())
				if selected == 1:
					self.ui.title.setTitle(u"Grilla")
					self.ui.widgets.insertWidget(1, GrillaDialog(self.conn, mainWin = self.ui))
				elif selected == 2:
					self.ui.title.setTitle(u"Reservas")
					self.ui.widgets.insertWidget(1, Admin(self.conn, "Reserva",self.ui))
				elif selected == 3:
					self.ui.title.setTitle(u"Gastos")
					self.ui.widgets.insertWidget(1, GastosDialog(self.conn,self))
				elif selected == 4:
					self.ui.title.setTitle(u"Huéspedes")
					self.ui.widgets.insertWidget(1, Admin(self.conn, "Huesped",self.ui))
				elif selected == 5:
					self.ui.title.setTitle(u"Unidades")
					self.ui.widgets.insertWidget(1, Admin(self.conn, "Unidad",self.ui))
				elif selected == 6:
					self.ui.title.setTitle(u"Tipos de Unidad")
					self.ui.widgets.insertWidget(1, Admin(self.conn, "Tipo",self.ui))
				self.ui.widgets.setCurrentIndex(1)
				self.lastButtonClicked = selected #Para volver a llamar después de algún diálogo.
			else:	
				ret = QtGui.QMessageBox.question(self, "Advertencia", u"¿Está seguro que desea salir?",
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
				if ret == QtGui.QMessageBox.Ok:
					sys.exit(app.exec_())
				else:
					self.buttonGroup.button(self.lastButtonClicked).toggle()
	
	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress):
			if keyEvent.key() == QtCore.Qt.Key_F2:
				self.buttonGroup.button(1).click()
			elif keyEvent.key() == QtCore.Qt.Key_F3:
				self.buttonGroup.button(2).click()
			elif keyEvent.key() == QtCore.Qt.Key_F4:
				self.buttonGroup.button(3).click()
			elif keyEvent.key() == QtCore.Qt.Key_F5:
				self.buttonGroup.button(4).click()
			elif keyEvent.key() == QtCore.Qt.Key_F6:
				self.buttonGroup.button(5).click()
			elif keyEvent.key() == QtCore.Qt.Key_F7:
				self.buttonGroup.button(6).click()
			elif keyEvent.key() == QtCore.Qt.Key_F8:
				self.buttonGroup.button(7).click()
			elif keyEvent.key() == QtCore.Qt.Key_Escape:
				event.accept()
				return
		return super(MainWindow, self).keyPressEvent(keyEvent)
	
	def abrirAcercade(self):
		print "hola"
		diag = AboutDialog()
		diag.setWindowFlags(QtCore.Qt.Tool|QtCore.Qt.MSWindowsFixedSizeDialogHint)
		#diag.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
		diag.exec_()
		
	@QtCore.pyqtSlot()
	def createBackup(self):
		fileDialog=QtGui.QFileDialog.getSaveFileName(self, "Examinar", os.path.expandvars("%HOMEDRIVE%") + "\conotels_backup.sql")
		fileDialog=unicode(str(fileDialog))

		if(str(fileDialog)!=""):
			backup.backupDatabase("conotels","userHoteles","userHoteles",os.path.normcase(fileDialog))		

	@QtCore.pyqtSlot()
	def loadBackup(self):
		fileDialog=QtGui.QFileDialog.getOpenFileName(self, "Examinar", os.path.expandvars("%HOMEDRIVE%"))
		self.conn.close()
		self.openConn()
		fileDialog=unicode(str(fileDialog))
		
		if(fileDialog!=""):
			msgBox=QtGui.QMessageBox(self);
			msgBox.setText("Esta seguro de cargar los datos? Los datos anteriores se perderan.")
			msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			if(msgBox.exec_()==QtGui.QMessageBox.Yes):
				backup.loadDatabase("conotels","userHoteles","userHoteles",os.path.normcase(fileDialog))
			self.butClicked(self.lastButtonClicked) #Para hacer repaint y mantener consistencia con los cambios que hubo
 
	def checkPrereservas(self):
		preExpDialog = Admin(self.conn, "PreExpiradas", self.ui)
		preExpDialog.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/house.png")))
		preExpDialog.exec_()
		self.butClicked(self.lastButtonClicked) #Para hacer repaint y mantener consistencia con los cambios que hubo

import sys

app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QWindowsVistaStyle())
#app.setStyle("windowsvista")
main = MainWindow()
main.show()
sys.exit(app.exec_())
