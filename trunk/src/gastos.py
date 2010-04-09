# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.gastos import Ui_GastosDialog
# from db.unidad import SARASA
from models.gastos import Gastos
from models.unidad import Unidad

class GastosDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut = self.ui.buttonBox.addButton("Guardar", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)

		self.unidad = Unidad()
		self.unidad.loadAll()
		self.ui.unidadCombo.setModel(self.unidad.model)
		self.ui.unidadCombo.setModelColumn=1

	def __init__(self, parent = None):
		super(GastosDialog, self).__init__(parent)

		self.setup()
		self.model = Gastos()

	def __del__(self):
		pass

	def save(self):
		# db.save
		print "new gastos"
		
		self.model.save(descripcion=self.ui.descripcionLine.text(),
				costo=self.ui.gastoSpin.value(),
				reserva=self.unidadCombo.itemText(self.unidadCombo.currentIndex()))
	
	def clear(self):
		self.ui.gastoSpin.setValue(0)
		self.ui.descripcionLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
