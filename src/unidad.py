from PyQt4 import QtCore, QtGui

from ui.unidad import Ui_unidadDialog
# from db.unidad import SARASA

class unidadDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_unidadDialog()
		self.ui.setupUi(self)
		
		# Llenar el comboBox de Tipo

	def __init__(self, numero = 0, tipo = 0, capacidad = 0, 
	descripcion = 0, estado = 0, parent = None):
		super(unidadDialog, self).__init__(parent)
		self.setup()

		self.modif = (tipo == 0)
		self.numero = numero
		self.tipo = tipo
		self.capacidad = capacidad
		self.descripcion = descripcion
		self.estado = estado

	def save(self):
		if self.modif:
			# db.save
			print "hola"
		else:
			# db.addNew
			print "chau"
	
	@QtCore.pyqtSlot()
	def on_buttonBox_accepted(self):
		self.save()
	
	@QtCore.pyqtSlot()
	def on_buttonBox_rejected(self):
		self.close()

#import sys

#app = QtGui.QApplication(sys.argv)
#main = unidadDialog()
#main = unidadDialog(1,1,1,1,1)
#main.show()
#sys.exit(app.exec_())
