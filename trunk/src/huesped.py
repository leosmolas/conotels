# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.huesped import Ui_huespedDialog
# from db.tipo import SARASA
from models.huesped import Huesped

class HuespedDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_huespedDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)

		#dni, apellido, nombre, telefono
	def __init__(self, id = -1, dni = "", apellido = "", nombre = "", telefono = "", parent = None):
		super(HuespedDialog, self).__init__(parent)
		self.setup()
		
		self.model = Huesped()
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

	def save(self):
		self.model.save(id=self.id,dni=self.ui.dniLine.text(),
				nombre=self.ui.nombreLine.text(),
				apellido=self.ui.apellidoLine.text(),
				telefono=self.ui.telLine.text())
	
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

#import sys

#app = QtGui.QApplication(sys.argv)
#main = huespedDialog()
#main = huespedDialog("dni","apellido","nombre","telefono",1)
#main.show()
#sys.exit(app.exec_())
