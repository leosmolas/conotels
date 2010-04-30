# -*- coding: utf-8 -*-
import re
from PyQt4 import QtCore, QtGui

from ui.reserva import Ui_reservaDialog

from models.huesped import Huesped
from models.unidad import Unidad
from models.reserva import Reserva

class ReservaDialog(QtGui.QDialog):
	def setup(self):
		self.ui = Ui_reservaDialog()
		self.ui.setupUi(self)
		
		self.okBut = self.ui.buttonBox.addButton("&Guardar", QtGui.QDialogButtonBox.ActionRole)
		self.cancelBut = self.ui.buttonBox.addButton("&Cancelar", QtGui.QDialogButtonBox.ActionRole)

		self.okBut.setIcon(QtGui.QIcon(":/save.png"))
		self.cancelBut.setIcon(QtGui.QIcon(":/cancel.png"))

		QtCore.QObject.connect(self.okBut, QtCore.SIGNAL("clicked()"),
				self.on_okBut_clicked)
		QtCore.QObject.connect(self.cancelBut, QtCore.SIGNAL("clicked()"),
				self.on_cancelBut_clicked)

		if self.uiMain != None:
			self.backBut = self.ui.buttonBox.addButton("&Volver", QtGui.QDialogButtonBox.ActionRole)
			self.backBut.setIcon(QtGui.QIcon(":/back.png"))
			QtCore.QObject.connect(self.backBut, QtCore.SIGNAL("clicked()"),
					self.on_backBut_clicked)
		#hacer consultas para buscar huespedes y unidades libres para reserva?

		self.ui.huespedView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		QtCore.QObject.connect(self.ui.huespedLine, QtCore.SIGNAL("textChanged(const QString &)"),
			self.update)
		
	def __init__(self, conn, id = -1, unidad = 0, huesped = 0, inicioPrereserva = "", finPrereserva = "", inicioReserva = "", finReserva = "", horaCheckIn = "", horaCheckOut = "", estado = "", mod = 0, mainWin = None, parent = None):
		super(ReservaDialog, self).__init__(parent)

		self.conn = conn
		self.id = id
		self.model = Reserva(self.conn)

		self.uiMain = mainWin #modif por Jona

		self.modif = (id != -1)
		self.setup()
		
		self.huesped = Huesped(self.conn)
		self.huesped.loadAll()
		self.ui.huespedView.setModel(self.huesped.model)

		self.unidad = Unidad(self.conn)
		self.unidad.loadAll()
		self.ui.unidadCombo.setModel(self.unidad.model)
		self.ui.unidadCombo.setModelColumn(1)
		
		if not self.modif:				
			self.clear()
		else:			
			unidadComboModel = self.ui.unidadCombo.model()			
			found = False
			i = 0
			while not found and i<unidadComboModel.rowCount():
				if unidadComboModel.data(unidadComboModel.index(i,0)).toInt()[0] == unidad:
					found = True
				else:
					i+=1
			self.ui.unidadCombo.setCurrentIndex(i)
			
			self.ui.huespedLine.setText("")			
			
			huespedViewModel = self.ui.huespedView.model()			
			found = False
			i = 0
			while not found and i<huespedViewModel.rowCount():
				if huespedViewModel.data(huespedViewModel.index(i,0)).toInt()[0] == huesped:
					found = True
				else:
					i+=1
			self.ui.huespedView.selectRow(i)			
			
			self.ui.huespedLine.setText("")

#            self.ui.inicioPreDate.setDate(QtCore.QDate(inicioPrereserva.left(4).toInt()[0], inicioPrereserva.mid(5,2).toInt()[0], inicioPrereserva.right(2).toInt()[0]))
#            self.ui.finPreDate.setDate(QtCore.QDate(finPrereserva.left(4).toInt()[0], finPrereserva.mid(5,2).toInt()[0], finPrereserva.right(2).toInt()[0]))
#            self.ui.inicioDate.setDate(QtCore.QDate(inicioReserva.left(4).toInt()[0], inicioReserva.mid(5,2).toInt()[0], inicioReserva.right(2).toInt()[0]))
#            self.ui.finDate.setDate(QtCore.QDate(finReserva.left(4).toInt()[0], finReserva.mid(5,2).toInt()[0], finReserva.right(2).toInt()[0]))
#            self.ui.inTime.setTime(QtCore.QTime(horaCheckIn.left(2).toInt()[0], horaCheckIn.mid(3,2).toInt()[0], horaCheckIn.right(2).toInt()[0]))
#            self.ui.outTime.setTime(QtCore.QTime(horaCheckOut.left(2).toInt()[0], horaCheckOut.mid(3,2).toInt()[0], horaCheckOut.right(2).toInt()[0]))

			self.ui.inicioPreDate.setDate(QtCore.QDate.fromString(inicioPrereserva, "yyyy-MM-dd"))
			self.ui.finPreDate.setDate(QtCore.QDate.fromString(finPrereserva, "yyyy-MM-dd"))
			self.ui.inicioDate.setDate(QtCore.QDate.fromString(inicioReserva, "yyyy-MM-dd"))
			self.ui.finDate.setDate(QtCore.QDate.fromString(finReserva, "yyyy-MM-dd"))
			self.ui.inTime.setTime(QtCore.QTime.fromString(horaCheckIn, "hh:mm:ss"))
			self.ui.outTime.setTime(QtCore.QTime.fromString(horaCheckOut, "hh:mm:ss"))
			
			estadoComboModel = self.ui.estadoCombo.model()
			found = False
			i = 0
			while not found and i<estadoComboModel.rowCount():
				if estadoComboModel.data(estadoComboModel.index(i,0)) == estado:
					found = True
				else:
					i+=1
			self.ui.estadoCombo.setCurrentIndex(i)			
			self.ui.huespedView.resizeColumnsToContents()

		if not self.modif and self.uiMain == None:
			# Si se hace una reserva a traves de la grilla, se ponen datos mas puntuales
			today = QtCore.QDate.currentDate()
			inicio = QtCore.QDate.fromString(inicioReserva, "yyyy-MM-dd")
			self.ui.inicioPreDate.setDate(today)
			self.ui.finPreDate.setDate(today.addDays(7))
			self.ui.inicioDate.setDate(inicio)
			self.ui.finDate.setDate(inicio.addDays(7))
	
	def update(self, s):
		self.huesped.filterModel(s)
		self.ui.huespedView.setModel(self.huesped.model)
		self.ui.huespedView.resizeColumnsToContents()

	def save(self):
		if self.ui.unidadCombo.count() > 0:
			if self.ui.huespedView.currentIndex().row() != -1:
				
				#save(self, id = -1, unidad="",huesped="",inicioPrereserva="",finPrereserva="",inicioReserva="",finReserva="",horaCheckIn="",horaCheckOut="",estado=""): # if id != -1: update; else: save;
				
#                    estado=self.ui.estadoCombo.model().data(self.ui.estadoCombo.model().index(self.ui.estadoCombo.currentIndex(),0)).toString()
				self.model.save(id=self.id, 
					unidad=self.ui.unidadCombo.model().data(self.ui.unidadCombo.model().index(self.ui.unidadCombo.currentIndex(),0)).toInt()[0],
					huesped=self.huesped.model.record(self.ui.huespedView.currentIndex().row()).value(0).toInt()[0],
					inicioPrereserva=self.ui.inicioPreDate.date().toString("yyyy-MM-dd"),
					finPrereserva=self.ui.finPreDate.date().toString("yyyy-MM-dd"),
					inicioReserva=self.ui.inicioDate.date().toString("yyyy-MM-dd"), 
					finReserva=self.ui.finDate.date().toString("yyyy-MM-dd"),
					horaCheckIn=self.ui.inTime.time().toString("HH:mm:ss"),
					horaCheckOut=self.ui.outTime.time().toString("HH:mm:ss"), 
					estado=self.ui.estadoCombo.currentText()
				)
				self.uiMain.statusBar.showMessage("Los datos se han guardado con exito!",3000)
				return True
			else:
				#self.uiMain.statusBar.showMessage("Debe seleccionar un Huesped para realizar la reserva!",3000)
				QtGui.QMessageBox.information(self, "Advertencia","Debe seleccionar un Huesped para realizar la reserva!")
				return False
		else:
			#self.uiMain.statusBar.showMessage("Debe seleccionar una Unidad para realizar la reserva!",3000)
			QtGui.QMessageBox.information(self, "Advertencia","Debe seleccionar una Unidad para realizar la reserva!")
			return False
		
	def clear(self):
		self.ui.unidadCombo.setCurrentIndex(0)
		self.ui.huespedLine.setText("")
		self.ui.inicioPreDate.setDate(QtCore.QDate.currentDate())
		self.ui.finPreDate.setDate(QtCore.QDate.currentDate())
		self.ui.inicioDate.setDate(QtCore.QDate.currentDate())
		self.ui.finDate.setDate(QtCore.QDate.currentDate())
		self.ui.inTime.setTime(QtCore.QTime.currentTime())
		self.ui.outTime.setTime(QtCore.QTime.currentTime())
		self.ui.estadoCombo.setCurrentIndex(0)

	@QtCore.pyqtSlot()
	def on_okBut_clicked(self):
		save = self.save()
		if save == True:
			self.clear()		
			if self.uiMain == None:
				self.close()
				
	@QtCore.pyqtSlot()
	def on_cancelBut_clicked(self):
		self.clear()
		if self.uiMain == None:
			self.close()

	@QtCore.pyqtSlot()
	def on_backBut_clicked(self):
		self.uiMain.widgets.removeWidget(self.uiMain.widgets.widget(2))
		self.uiMain.title.setTitle("Administrar reservas")
		self.uiMain.widgets.setCurrentIndex(1)
		self.uiMain.widgets.widget(1).loadAll()
