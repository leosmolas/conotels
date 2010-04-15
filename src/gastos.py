# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore, QtGui

from ui.gastos import Ui_GastosDialog
from models.gastos import Gastos
from models.reserva import Reserva

class GastosDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut = self.ui.buttonBox.addButton("Guardar", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		
		QtCore.QObject.connect(self.ui.buscarLineEdit, QtCore.SIGNAL("textChanged(QString)"),
				self.buscarReserva)

		self.reserva = Reserva(self.conn)
		self.reserva.loadAll()
		self.ui.reservastableView.setModel(self.reserva.model)


	def __init__(self, conn, parent = None):
		super(GastosDialog, self).__init__(parent)

		self.conn = conn
		self.setup()

		self.model = Gastos(conn)

	def save(self):
		print "new gastos"
		
		'''self.model.save(descripcion=self.ui.descripcionLine.text(),
				costo=self.ui.gastoSpin.value(),
				reserva=self.ui.unidadCombo.itemText(self.ui.unidadCombo.currentIndex()))
	'''
	def clear(self):
		self.ui.gastoSpin.setValue(0)
		self.ui.descripcionLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
		self.clear()
		QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")


	def buscarReserva(self):
		print "cambio el texto"
		