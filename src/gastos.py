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
		self.reservaActual = -1
		self.model = Gastos(conn)


	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut= self.ui.buttonBox.addButton("Guardar", QtGui.QDialogButtonBox.ActionRole)		
		self.modificarBut = self.ui.buttonBox.addButton("Modificar", QtGui.QDialogButtonBox.ActionRole)
		self.okBut.setEnabled(False)
		self.modificarBut.setEnabled(False)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.modificarBut, QtCore.SIGNAL("clicked()"),
				self.on_okModificar_clicked)
		QtCore.QObject.connect(self.ui.buscarLineEdit, QtCore.SIGNAL("textChanged(QString)"),
				self.buscarReserva)
		QtCore.QObject.connect(self.ui.reservastableView, QtCore.SIGNAL("activated(QModelIndex)"),
				self.cargarGastos)
		QtCore.QObject.connect(self.ui.gastosTableView, QtCore.SIGNAL("activated(QModelIndex)"),
				self.activarModificar)

		self.reservasView = ReservasView(self.conn)
		self.reservasView.loadAll()
		self.ui.reservastableView.setModel(self.reservasView.model)
		self.ui.reservastableView.resizeColumnsToContents()


	def save(self,id = -1):
		print "new gastos"
		self.model.save(id,descripcion=self.ui.descripcionLine.text(),
				costo=self.ui.gastoSpin.value(),
				reserva=self.reservaActual)

	def clear(self):
		self.ui.gastoSpin.setValue(0)
		self.ui.descripcionLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
		self.clear()
		QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
		self.cargarGastos(self.ui.reservastableView.selectedIndexes()[0])
		
	@QtCore.pyqtSlot()
	def on_okModificar_clicked(self):
		if self.ui.gastosTableView.selectedIndexes()!=[]:
			#es media troska esta llamada
			#lo que hago es pedir los indices seleccionados, que devuelve una lista con pares ordenados del tipo QModelIndex
			#por eso selecciono la primera con el [0]
			#despues, a ese le saco el row. Con el row y el column en 0, pido con getitem el elemento al model. el elemento es un 
			#Qvariant, que lo paso a int. el metodo toInt es re manco: te pasa dos cosas, el entero, y un boolean que te dice si pudo o 
			#no (esto es por como esta implementado pyqt. Por esto, le pido el primer elemento al final, con un [0]
			
			self.save(QtCore.QVariant.toInt(self.model.model.getItem(0,self.ui.gastosTableView.selectedIndexes()[0].row()))[0])
			self.clear()
			QtGui.QMessageBox.information(self, "Guardado con exito", "Los datos se han guardado con exito!")
			self.cargarGastos(self.ui.reservastableView.selectedIndexes()[0])
		else:
			QtGui.QMessageBox.warning(self, "Cuidado!", "No ha seleccionado ningun gasto para modificar.")
		

	@QtCore.pyqtSlot()
	def buscarReserva(self,s):
		
		filtro = re.escape(str(s.replace(' ', '% ')))
		#print filtro	
		self.reservasView.filterModel(filtro)
		self.ui.reservastableView.setModel(self.reservasView.model)
		self.ui.reservastableView.resizeColumnsToContents()
		
		
	def cargarGastos(self,modelIndex):
		index = QtCore.QVariant.toInt(self.reservasView.model.getItem(modelIndex.row(),0))
		self.reservaActual = index[0]
		self.model.buscarPorReserva(self.reservaActual)
		self.ui.gastosTableView.setModel(self.model.model)
		self.ui.gastosTableView.hideColumn(3)
		self.ui.gastosTableView.resizeColumnsToContents()
		self.okBut.setEnabled(True)
		
	@QtCore.pyqtSlot()
	def activarModificar(self,modelIndexList):
		self.modificarBut.setEnabled(modelIndexList!=[])