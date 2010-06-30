 # -*- coding: latin-1 -*-
from PyQt4 import QtCore, QtGui
import re

from ui.huesped import Ui_huespedDialog
from models.huesped import Huesped

class HuespedDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_huespedDialog()
		self.ui.setupUi(self)
		
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/house.png")))
		
		self.okBut = self.ui.buttonBox.addButton("&Guardar", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("&Cancelar", QtGui.QDialogButtonBox.ActionRole)

		self.okBut.setIcon(QtGui.QIcon(":/save.png"))
		self.cancelBut.setIcon(QtGui.QIcon(":/cancel.png"))

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)

		if self.uiMain != None:
			self.backBut = self.ui.buttonBox.addButton("&Volver", QtGui.QDialogButtonBox.ActionRole)
			self.backBut.setIcon(QtGui.QIcon(":/back.png"))
			QtCore.QObject.connect(self.backBut, QtCore.SIGNAL("clicked()"),
				self.on_backBut_clicked)

		#dni varchar(45) not null,
		#apellido varchar(45) not null,
		#nombre varchar(45) not null,
		#telefonoFijo varchar(45),
		#telefonoCelular varchar(45),
		#direccion varchar(100),
		#localidad varchar(45),
		#email varchar(45),
		#autoPatente varchar(20),
		#autoModelo varchar(45),
		#autoColor varchar(45),
	def __init__(self, conn, id = -1, dni = "", apellido = "", nombre = "", telefono = "",celular="",direccion="",localidad="", email="", patente="", modelo="", color="", mainWin = None, parent = None):
		super(HuespedDialog, self).__init__(parent)
		
		self.conn = conn
		self.model = Huesped(conn)
		self.modif = (id != -1)
		self.dni = dni
		self.id = id
		self.uiMain = mainWin #modif por Jona
		
		self.setup()
		
		if self.modif:
			self.ui.dniLine.setText(dni)
			self.ui.apellidoLine.setText(apellido)
			self.ui.nombreLine.setText(nombre)
			self.ui.telLine.setText(telefono)
			self.ui.celLine.setText(celular)
			self.ui.direccionLine.setText(direccion)
			self.ui.localidadLine.setText(localidad)	
			self.ui.emailLine.setText(email)
			self.ui.patenteLine.setText(patente)
			self.ui.modeloLine.setText(modelo)
			self.ui.colorLine.setText(color)
		
		self.installEventFilter(self)

	def save(self):
		if self.ui.dniLine.text() != "" and self.ui.nombreLine.text() != "" and self.ui.apellidoLine.text() != "": 
			if (self.modif and self.ui.dniLine.text() == self.dni) or self.model.checkdni(self.ui.dniLine.text()) == 0:
				self.model.save(id=self.id,dni=re.escape(unicode(self.ui.dniLine.text())),
					nombre      = re.escape(unicode(self.ui.nombreLine.text())),
					apellido    = re.escape(unicode(self.ui.apellidoLine.text())),
					telefono    = re.escape(unicode(self.ui.telLine.text())),
					celular     = re.escape(unicode(self.ui.celLine.text())),
					direccion   = re.escape(unicode(self.ui.direccionLine.text())),
					localidad   = re.escape(unicode(self.ui.localidadLine.text())),
					email       = re.escape(unicode(self.ui.emailLine.text())),
					autoPatente = re.escape(unicode(self.ui.patenteLine.text())),
					autoModelo  = re.escape(unicode(self.ui.modeloLine.text())),
					autoColor   = re.escape(unicode(self.ui.colorLine.text()))
					)
				#QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
				if self.uiMain != None:
					self.uiMain.statusBar.showMessage(u"Los datos se han guardado con éxito!",3000)
				return True
			else:
				QtGui.QMessageBox.information(self, "Error", "El DNI ingresado ya existe!")
				#self.uiMain.statusBar.showMessage("Los campos DNI, Apellido y Nombre no pueden ser vacios!",3000)
				return False
		else:
			QtGui.QMessageBox.information(self, "Error", u"Los campos DNI, Apellido y Nombre no pueden estar vacíos!")
			#self.uiMain.statusBar.showMessage("Los campos DNI, Apellido y Nombre no pueden ser vacios!",3000)
			return False
		
	def clear(self):
		self.ui.dniLine.setText("")
		self.ui.apellidoLine.setText("")
		self.ui.nombreLine.setText("")
		self.ui.telLine.setText("")
		self.ui.celLine.setText("")
		self.ui.direccionLine.setText("")
		self.ui.localidadLine.setText("")
		self.ui.emailLine.setText("")
		self.ui.patenteLine.setText("")
		self.ui.modeloLine.setText("")
		self.ui.colorLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		save = self.save()
		if save == True:
			self.clear()
			if self.modif or self.uiMain == None:
				self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		#self.clear()
		#if self.modif or self.uiMain == None:
		#	self.close()
		if self.modif or self.uiMain == None:
			self.close()
		else:
			self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
			self.uiMain.title.setTitle(u"Huéspedes")
			self.uiMain.widgets.setCurrentIndex(1)
			self.uiMain.widgets.widget(1).loadAll()

	def on_backBut_clicked(self):
		if self.modif or self.uiMain == None:
			self.close()
		else:
			self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
			self.uiMain.title.setTitle(u"Huéspedes")
			self.uiMain.widgets.setCurrentIndex(1)
			self.uiMain.widgets.widget(1).loadAll()
		#self.clear()
		#if self.modif or self.uiMain == None:
		#	self.close()

	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress) and ((keyEvent.key() == QtCore.Qt.Key_Return) or (keyEvent.key() == QtCore.Qt.Key_Enter)):
			self.focusNextChild()
			return
		elif keyEvent.key() == QtCore.Qt.Key_Escape:
			print "ESC!!!!"
			keyEvent.accept()
			return
		return super(HuespedDialog, self).keyPressEvent(keyEvent)
