# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.unidad import Ui_unidadDialog
# from db.unidad import SARASA
from models.unidad import Unidad

class UnidadDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_unidadDialog()
		self.ui.setupUi(self)

		self.okBut = self.ui.buttonBox.addButton("Ok", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("Cancel", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)
		# Llenar el comboBox de Tipo

	def __init__(self, numero = 0, tipo = 0, capacidad = 0, 
	descripcion = 0, estado = 0, parent = None):
		super(UnidadDialog, self).__init__(parent)

		self.model = Unidad()
		self.modif = (tipo != 0)
		self.numero = numero
		self.tipo = tipo
		self.capacidad = capacidad
		self.descripcion = descripcion
		self.estado = estado

		self.setup()

	def __del__(self):
		pass

	def save(self):
		if self.modif:
			# db.save
			print "hola"
		else:
			# db.addNew
			print "new unidad"
			self.model.save(nombre=self.ui.numeroLine.text(),tipo=self.ui.tipoCombo.itemText(self.ui.tipoCombo.currentIndex()),
				capacidad=self.ui.capacidadSpin.value(),
				descripcion=self.ui.descripcionText.toPlainText())
	
	def clear(self):
		self.ui.numeroLine.setText("")
		self.ui.tipoCombo.setCurrentIndex(0)
		self.ui.capacidadSpin.setValue(0)
		self.ui.descripcionText.setPlainText("")

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
#main = unidadDialog()
#main = unidadDialog(1,1,1,1,1)
#main.show()
#sys.exit(app.exec_())
