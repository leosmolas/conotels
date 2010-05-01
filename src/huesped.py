# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

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

		if not self.modif:
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
		self.id = id

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
			
		self.uiMain = mainWin #modif por Jona
		self.installEventFilter(self)

	def save(self):
		if self.ui.dniLine.text() != "" and self.ui.nombreLine.text() != "" and self.ui.apellidoLine.text() != "": 
			self.model.save(id=self.id,dni=self.ui.dniLine.text(),
				nombre=self.ui.nombreLine.text(),
				apellido=self.ui.apellidoLine.text(),
				telefono=self.ui.telLine.text(),
				celular=self.ui.celLine.text(),
				direccion=self.ui.direccionLine.text(),
				localidad=self.ui.localidadLine.text())
			#QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
			self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
			return True
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
			if self.modif:
				self.close()
	
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.modif:
			self.close()

	def on_backBut_clicked(self):
		self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
		self.uiMain.title.setTitle("Administrar huesped")
		self.uiMain.widgets.setCurrentIndex(1)
		self.uiMain.widgets.widget(1).loadAll()

	@QtCore.pyqtSlot()
	def eventFilter(self, object, event):
		if(event.type()==QtCore.QEvent.KeyPress):
			keyEvent = QtGui.QKeyEvent(event)
			if (keyEvent.key() == QtCore.Qt.Key_Return):
				keyEvent = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,QtCore.Qt.Key_Tab,QtCore.Qt.NoModifier)
		return False	
