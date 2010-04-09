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
	def __init__(self, dni = "", apellido = "", nombre = "", telefono = "", mod = 0, parent = None):
		super(HuespedDialog, self).__init__(parent)
		self.setup()
		
		self.model = Huesped()
		self.modif = (mod != 0)
		self.dni = dni
		self.apellido = apellido
		self.nombre = nombre
		self.telefono = telefono
		
	def __del__(self):
		pass

	def save(self):
		if self.modif:
			# db.save
			print "modify"
		else:
			# db.addNew
			print "new Reserva"

			self.model.save(dni=self.ui.dniLine.text(),
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
