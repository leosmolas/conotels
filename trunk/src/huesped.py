# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.huesped import Ui_huespedDialog
from models.huesped import Huesped

class HuespedDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_huespedDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)
		self.backBut = self.ui.buttonBox.addButton("Volver", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)
		QtCore.QObject.connect(self.backBut, QtCore.SIGNAL("clicked()"),
				self.on_backBut_clicked)

		#dni, apellido, nombre, telefono
	def __init__(self, conn, id = -1, dni = "", apellido = "", nombre = "", telefono = "", mainWin = None, parent = None):
		super(HuespedDialog, self).__init__(parent)
		self.setup()
		
		self.conn = conn
		self.model = Huesped(conn)
		self.modif = (id != -1)
		self.id = id
#        self.dni = dni
#        self.apellido = apellido
#        self.nombre = nombre
#        self.telefono = telefono
		
		if self.modif:
			self.ui.dniLine.setText(dni)
			self.ui.apellidoLine.setText(apellido)
			self.ui.nombreLine.setText(nombre)
			self.ui.telLine.setText(telefono)
			
		self.uiMain = mainWin #modif por Jona

	def save(self):
		if self.ui.dniLine.text() != "" and self.ui.nombreLine.text() != "" and self.ui.apellidoLine.text() != "": 
			self.model.save(id=self.id,dni=self.ui.dniLine.text(),
				nombre=self.ui.nombreLine.text(),
				apellido=self.ui.apellidoLine.text(),
				telefono=self.ui.telLine.text())
			QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
		else:
			QtGui.QMessageBox.information(self, "Advertencia", "Los campos DNI,Apellido y Nombre no pueden ser vacios!")
		
	def clear(self):
		self.ui.dniLine.setText("")
		self.ui.apellidoLine.setText("")
		self.ui.nombreLine.setText("")
		self.ui.telLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
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
