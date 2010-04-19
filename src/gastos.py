# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import re
from ui.gastos import Ui_GastosDialog
from models.gastos import Gastos
from models.reservasView import ReservasView

class GastosDialog(QtGui.QDialog):

	def __init__(self, conn, parent = None):
		super(GastosDialog, self).__init__(parent)

		self.conn = conn
		self.setup()

		self.model = Gastos(conn)


	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut = self.ui.buttonBox.addButton("Guardar", QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		
		QtCore.QObject.connect(self.ui.buscarLineEdit, QtCore.SIGNAL("textChanged(QString)"),
				self.buscarReserva)


		self.reservasView = ReservasView(self.conn)
		self.reservasView.loadAll()
		self.ui.reservastableView.setModel(self.reservasView.model)


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

	@QtCore.pyqtSlot()
	def buscarReserva(self,s):
		
		filtro = re.escape(str(s.replace(' ', '* ')))
		#print filtro	
		self.reservasView.filterModel2(filtro)
		self.ui.reservastableView.setModel(self.reservasView.model)
		
		