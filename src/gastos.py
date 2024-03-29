# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import re
from ui.gastos import Ui_GastosDialog
from models.gastos import Gastos
from models.reservasView import ReservasView
from connection.model import Model

class GastosDialog(QtGui.QWidget):

	def __init__(self, conn, parent = None):
		super(GastosDialog, self).__init__(parent)
		self.uiMain = parent
		self.conn = conn
		self.setup()
		self.reservaActual = -1
		self.model = Gastos(conn)


	def setup(self):
		self.ui = Ui_GastosDialog()
		self.ui.setupUi(self)

		self.okBut        = self.ui.buttonBox.addButton("Guardar &Nuevo", QtGui.QDialogButtonBox.ActionRole)		
		self.modificarBut = self.ui.buttonBox.addButton( u"Guardar &Modificación", QtGui.QDialogButtonBox.ActionRole)
		self.cancelarPendientesBut = self.ui.buttonBox.addButton("Cancelar &Pendientes", QtGui.QDialogButtonBox.ActionRole)
		self.eliminarBut = self.ui.buttonBox.addButton("&Eliminar", QtGui.QDialogButtonBox.ActionRole)
		self.okBut.setEnabled       (False)
		self.modificarBut.setEnabled(False)
		self.cancelarPendientesBut.setEnabled(False)
		self.eliminarBut.setEnabled(False)

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.modificarBut, QtCore.SIGNAL("clicked()"),
				self.on_okModificar_clicked)
		QtCore.QObject.connect(self.cancelarPendientesBut, QtCore.SIGNAL("clicked()"),
				self.cancelarPendientes)
		QtCore.QObject.connect(self.eliminarBut, QtCore.SIGNAL("clicked()"),
				self.eliminarGasto)
		QtCore.QObject.connect(self.ui.buscarLineEdit, QtCore.SIGNAL("textChanged(QString)"),
				self.buscarReserva)
		QtCore.QObject.connect(self.ui.reservastableView, QtCore.SIGNAL("clicked(QModelIndex)"),
				self.cargarGastos)
		QtCore.QObject.connect(self.ui.gastosTableView, QtCore.SIGNAL("clicked(QModelIndex)"),
				self.activarModificar)

		self.reservasView = ReservasView(self.conn)
		self.reservasView.loadAll()
		
		self.ui.reservastableView.setModel(self.reservasView.model)
		self.ui.reservastableView.setColumnHidden(0,True)
		self.ui.reservastableView.resizeColumnsToContents()
		self.ui.reservastableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.ui.gastosTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)


	def save(self,id = -1):
		print "new gastos"
		self.model.save(id,descripcion=self.escape(unicode(self.ui.descripcionLine.text())),
				costo=self.ui.gastoSpin.value(),
				reserva=self.reservaActual,
				pendiente=self.ui.pendienteCheckBox.isChecked())

	def clear(self):
		self.ui.gastoSpin.setValue(0)
		self.ui.descripcionLine.setText("")

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		self.save()
		self.clear()
		self.uiMain.statusBar.showMessage(u"Los datos se han guardado con éxito!",3000)
		# print "self.ui.reservastableView.selectedIndexes()[0]" + str(self.ui.reservastableView.selectedIndexes()[0])
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
			self.uiMain.statusBar.showMessage(u"Los datos se han guardado con éxito!",3000)
			self.cargarGastos(self.ui.reservastableView.selectedIndexes()[0])
		else:
			self.uiMain.statusBar.showMessage("No ha seleccionado ningun gasto para modificar.",3000)
		

	@QtCore.pyqtSlot()
	def buscarReserva(self,s):
		#filtro = re.escape(str(s.replace(' ', '% ')))
		#print filtro	
		self.reservasView.filterModel(s)
		self.ui.reservastableView.setModel(self.reservasView.model)
		self.ui.reservastableView.resizeColumnsToContents()
		
	@QtCore.pyqtSlot()
	def cargarGastos(self,modelIndex):
		index = QtCore.QVariant.toInt(self.reservasView.model.getItem(0,modelIndex.row()))
		self.reservaActual = index[0]
		self.model.buscarPorReserva(self.reservaActual)
		
		self.ui.gastosTableView.setModel(self.model.model)
		self.ui.gastosTableView.setColumnHidden(0,True)
		
# si quieren no le den bola a esto

		# delegate = QtGui.QStyledItemDelegate(self.ui.gastosTableView)
		# editorFactory = QtGui.QItemEditorFactory()
		# delegate.setItemEditorFactory(editorFactory)
		#delegate.createEditor(self.ui.gastosTableView,QtGui.QStyleOptionViewItem.Left
		# self.ui.gastosTableView.setItemDelegateForColumn(2,delegate)
		#for i in range(self.model.model.rowCount()):
			# if QtCore.QVariant.toInt(self.model.model.getItem(3,i))[0] == 1:
				# self.model.model.setData(self.model.model.createIndex(i,2),QtGui.QBrush(QtGui.QColor(255,60,60)), QtCore.Qt.BackgroundRole)
				# delegate = QtGui(self.ui.gastosTableView)
				# delegate.setItemEditorFactory()
				# self.ui.gastosTableView.setItemDelegateForRow(i,
			# else:
				# self.model.model.setData(self.model.model.createIndex(i,2),QtGui.QColor(60,255,60), QtCore.Qt.BackgroundColorRole)
		
		self.ui.gastosTableView.hideColumn(3)
		self.ui.gastosTableView.resizeColumnsToContents()
		self.okBut.setEnabled(True)
		self.cancelarPendientesBut.setEnabled(True)
		self.ui.pendienteCheckBox.setEnabled(True)
		self.ui.pendienteCheckBox.setChecked(True)
		self.calcularTotal()
		self.ui.restaLabel.setText("$ %.2f" % self.model.getRestaPagar(self.reservaActual))

		
	def calcularTotal(self):
		total = 0
		for i in range(self.model.model.rowCount()):
			total +=  QtCore.QVariant.toDouble(self.model.model.getItem(2,i))[0]
		#esta fumanchadez se refiere a lo siguiente: el ".2" es la precisión, y la f que es un floating point decimal común
		#igual si no se necesita la presición, se puede cambiar por una %d 
		self.ui.totalLabel.setText("$ %.2f" % total)

	@QtCore.pyqtSlot()
	def activarModificar(self,modelIndexList):
		activar = modelIndexList!=[]
		self.modificarBut.setEnabled(activar)
		self.eliminarBut.setEnabled(activar)
		self.ui.gastoSpin.setValue(self.model.model.getItem(2,self.ui.gastosTableView.selectedIndexes()[0].row()).toFloat()[0]) #aca se hacia toInt, pero era un pete.
		self.ui.descripcionLine.setText(self.model.model.getItem(1,self.ui.gastosTableView.selectedIndexes()[0].row()).toString())
		#llamada media troska... le tengo que pasar un booleano a setChecked.
		# Lo consigo comparando el valor de pendiente con 1. Si da igual, es que tengo que activar el checkBox pendiente.
		# La llamada es como siempre, pido los indices seleccionados. Supongo que es uno y pido el primero. Le pido el row. Obtengo el valor con la operación que tenemos getItem. Esto es un Qvariant, asi que lo convierto a int. Como esa operación devuelve un vector con dos elementos, le pido el que me interesa
		self.ui.pendienteCheckBox.setChecked(QtCore.QVariant.toString(self.model.model.getItem(4,self.ui.gastosTableView.selectedIndexes()[0].row()))==QtCore.QString("Si"))
		
	@QtCore.pyqtSlot()
	def cancelarPendientes(self):
		self.model.cancelarPendientes(self.reservaActual)
		self.cargarGastos(self.ui.reservastableView.selectedIndexes()[0])
		self.uiMain.statusBar.showMessage("Se han cancelado todos los gastos de la reserva.",3000)
		
	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress) and ((keyEvent.key() == QtCore.Qt.Key_Return) or (keyEvent.key() == QtCore.Qt.Key_Enter)):
			self.focusNextChild()
		return super(GastosDialog, self).keyPressEvent(keyEvent)
	
	@QtCore.pyqtSlot()
	def eliminarGasto(self):
		if self.ui.gastosTableView.selectedIndexes()!=[]:
			ret = QtGui.QMessageBox.question(self, "Advertencia", u"Está seguro de que desea realizar la eliminación?",
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			
			if ret == QtGui.QMessageBox.Ok:
				self.model.eliminar(QtCore.QVariant.toInt(self.model.model.getItem(0,self.ui.gastosTableView.selectedIndexes()[0].row()))[0])
				self.clear()
				self.cargarGastos(self.ui.reservastableView.selectedIndexes()[0])
				self.uiMain.statusBar.showMessage("El gasto ha sido eliminado exitosamente.",3000)
		else:
			self.uiMain.statusBar.showMessage("No ha seleccionado ningun gasto para ser eliminado.",3000)

	def escape(self, str):
		ns = str
		return ns.replace('"', '\\"').replace("'", "\\'")
