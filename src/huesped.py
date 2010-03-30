from PyQt4 import QtCore, QtGui

from ui.huesped import Ui_huespedDialog
# from db.tipo import SARASA

class huespedDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_huespedDialog()
		self.ui.setupUi(self)
		
		#dni, apellido, nombre, telefono
	def __init__(self, dni = "", apellido = "", nombre = "", telefono = "", mod = 0, parent = None):
		super(huespedDialog, self).__init__(parent)
		self.setup()

		self.modif = (mod == 0)
		self.dni = dni
		self.apellido = apellido
		self.nombre = nombre
		self.telefono = telefono
		
	def save(self):
		if self.modif:
			# db.save
			print "modify"
		else:
			# db.addNew
			print "new"
	
	@QtCore.pyqtSlot()
	def on_buttonBox_accepted(self):
		self.save()
	
	@QtCore.pyqtSlot()
	def on_buttonBox_rejected(self):
		self.close()

import sys

app = QtGui.QApplication(sys.argv)
main = huespedDialog()
main = huespedDialog("dni","apellido","nombre","telefono",1)
main.show()
sys.exit(app.exec_())
