# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import re

from ui.huesped import Ui_huespedDialog
from models.huesped import Huesped

class HuespedDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_huespedDialog()
		self.ui.setupUi(self)
		
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

		#dni, apellido, nombre, telefono
	def __init__(self, conn, id = -1, dni = "", apellido = "", nombre = "", telefono = "",celular="",direccion="",localidad="", mainWin = None, parent = None):
		super(HuespedDialog, self).__init__(parent)
		
		self.conn = conn
		self.model = Huesped(conn)
		self.modif = (id != -1)
		self.dni = dni
		self.id = id
		self.uiMain = mainWin #modif por Jona
		
		self.setup()

#        self.dni = dni
#        self.apellido = apellido
#        self.nombre = nombre
#        self.telefono = telefono
		
		if self.modif:
			self.ui.dniLine.setText(dni)
			self.ui.apellidoLine.setText(apellido)
			self.ui.nombreLine.setText(nombre)
			self.ui.telLine.setText(telefono)
			self.ui.celLine.setText(celular)
			self.ui.direccionLine.setText(direccion)
			self.ui.localidadLine.setText(localidad)			
		
		self.installEventFilter(self)

	def save(self):
		if self.ui.dniLine.text() != "" and self.ui.nombreLine.text() != "" and self.ui.apellidoLine.text() != "": 
			if (self.modif and self.ui.dniLine.text() == self.dni) or self.model.checkdni(self.ui.dniLine.text()) == 0:
				self.model.save(id=self.id,dni=re.escape(str(self.ui.dniLine.text())),
					nombre=re.escape(str(self.ui.nombreLine.text())),
					apellido=re.escape(str(self.ui.apellidoLine.text())),
					telefono=re.escape(str(self.ui.telLine.text())),
					celular=re.escape(str(self.ui.celLine.text())),
					direccion=re.escape(str(self.ui.direccionLine.text())),
					localidad=re.escape(str(self.ui.localidadLine.text())))
				#QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
				if self.uiMain != None:
					self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
				return True
			else:
				QtGui.QMessageBox.information(self, "Advertencia", "El DNI Ingresado ya existe!")
				#self.uiMain.statusBar.showMessage("Los campos DNI, Apellido y Nombre no pueden ser vacios!",3000)
				return False
		else:
			QtGui.QMessageBox.information(self, "Advertencia", "Los campos DNI, Apellido y Nombre no pueden ser vacios!")
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

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		save = self.save()
		if save == True:
			self.clear()
			if self.modif or self.uiMain == None:
				self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.modif or self.uiMain == None:
			self.close()

	def on_backBut_clicked(self):
		self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
		self.uiMain.title.setTitle("Administrar huesped")
		self.uiMain.widgets.setCurrentIndex(1)
		self.uiMain.widgets.widget(1).loadAll()

	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress) and ((keyEvent.key() == QtCore.Qt.Key_Return) or (keyEvent.key() == QtCore.Qt.Key_Enter)):
			self.focusNextChild()
		return super(HuespedDialog, self).keyPressEvent(keyEvent)
