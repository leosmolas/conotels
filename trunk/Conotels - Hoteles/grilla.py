# -*- coding: iso-8859-1 -*-
from PyQt4 import QtCore,QtGui
from ui.grilla import Ui_Grilla

from connection.model import Model
from tableitem import TableItem
from reserva import ReservaDialog

from models.reserva import Reserva
from models.unidad import Unidad

# Tipos de items:
# 0 - Pre reserva
# 1 - Reserva confirmada
# 2 - Reserva en curso

class GrillaDialog(QtGui.QWidget):
	def __init__(self, conn, parent = None, mainWin = None):
		super(GrillaDialog, self).__init__(parent)

		self.ui = Ui_Grilla()
		self.ui.setupUi(self)
		
		self.uiMain = mainWin
		
		self.conn = conn

		self.ui.anioSpin.setValue(QtCore.QDate.currentDate().year())
		self.ui.mesCombo.setCurrentIndex(QtCore.QDate.currentDate().month()-1)

		self.model = Reserva(conn)

		self.unidades = Unidad(conn)
		self.unidades.loadDisponibles()
		self.cantUnidades = self.unidades.model.rowCount()

		self.uDict = dict()
		self.names = QtCore.QStringList()
		
		# Armamos las filas segun las unidades
		j = 0
		for i in range(0, self.cantUnidades):
			# Armo un dict porque no siempre los ids son seguidos
			self.uDict.update({self.unidades.model.getItem("idUnidad", i).toInt()[0]: i})
#            print self.unidades.model.getItem("nombre",i).toString()
			self.names.append(unicode(self.unidades.model.getItem("nombre",i).toString()))
			self.ui.tableWidget.insertRow(i)
			j += 1

		print self.uDict

		self.ui.tableWidget.setRowCount(j)
		self.ui.tableWidget.setVerticalHeaderLabels(self.names)

		self.update(0)

		QtCore.QObject.connect(self.ui.mesCombo, QtCore.SIGNAL("currentIndexChanged(int)"),
				self.update)
		QtCore.QObject.connect(self.ui.anioSpin, QtCore.SIGNAL("valueChanged(int)"),
				self.update)
		QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("cellDoubleClicked(int,int)"),
				self.doubleClicked)
		
		QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("cellClicked(int,int)"),
				self.clicked)
		
		QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), 
			self.on_context_menu)

		self.ui.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # Popup Menu
		self.popMenu = QtGui.QMenu(self)
		self.popMenu.addAction("Crear/Editar", self.edit)
		self.popMenu.addSeparator()
		self.popMenu.addAction("Eliminar", self.delete)
	
		#-Agregado para hacer la eliminacion de reservas-#
		self.idReservaActual = -1 #Sirve para mantener el id de la reserva que esta seleccionada.
		#self.reserva = Reserva(self.conn)
		#---------------------------#
		
	@QtCore.pyqtSlot()
	def edit(self):
		print "edit"
		print self.currentItem
		self.doubleClicked(self.currentItem.row(), self.currentItem.column())

	@QtCore.pyqtSlot()
	def delete(self):
		print "del"
		print self.currentItem
		#self.clicked(self.currentItem.row(), self.currentItem.column())
		self.elimReserva()


	@QtCore.pyqtSlot()
	def on_context_menu(self, p):
		print "context"
		self.currentItem = self.ui.tableWidget.itemAt(p)
		self.popMenu.exec_(self.ui.tableWidget.mapToGlobal(p))

	@QtCore.pyqtSlot()
	def update(self, index):
		print "updating"
		self.ui.tableWidget.setColumnCount(0)
		mes = self.ui.mesCombo.currentIndex()+1
		anio = self.ui.anioSpin.value()

		self.model.loadMesAnio(mes,anio)
		q = self.model.model

		date = QtCore.QDate(self.ui.anioSpin.value(),self.ui.mesCombo.currentIndex()+1,1)

		# Armamos las columnas segun los dias del mes seleccionado
		days = 0
		nameDays = QtCore.QStringList()
		while date.month() == mes:
			days+=1
			
			nameDays.append(str(unicode(date.shortDayName(date.dayOfWeek())).encode("latin-1"))+" "+str(days))
			date = date.addDays(1)

		self.ui.tableWidget.setColumnCount(days)
		self.ui.tableWidget.setHorizontalHeaderLabels(nameDays)
		self.ui.tableWidget.resizeColumnsToContents()

		for i in range(0, self.cantUnidades):
			for j in range(0, days):
				self.ui.tableWidget.setItem(i, j, TableItem(self.conn))

		# Aca empieza la magia
		for i in range(0,q.rowCount()):
			initDate = QtCore.QDate.fromString(q.getItem("inicioReserva",i).toString(), "yyyy-MM-dd")
			endDate = QtCore.QDate.fromString(q.getItem("finReserva",i).toString(), "yyyy-MM-dd")

			unidad = q.getItem("unidad",i).toInt()[0]
			res = q.getItem("idReserva",i).toInt()[0]

			print "Reserva!"
			print res

			initDay = 1
			endDay = days

			est = unicode(q.getItem("estado",i).toString())
			print est

			estado = 2

			if est == "Reservado":
				print "la reserva "+str(res)+" tiene estado 1"
				estado = 1
			elif est == "Reserva en curso":
				print "la reserva "+str(res)+" tiene estado 3"
				estado = 3
			elif est == "Pre Reservado":
				print "la reserva "+str(res)+" tiene estado 2"
				estado = 2

			if initDate.month() == endDate.month():
				initDay = initDate.day()
				endDay = endDate.day()
			elif initDate.month() != mes:
				endDay = endDate.day() # si el init es del mes anterior, entonces end si o si es de este mes
			elif endDate.month() != mes:
				initDay = initDate.day() # si el end es del mes siguiente, entonces init si o si es de este mes

			print "initDay: %d" % initDay
			print "endDay: %d" % endDay

			for i in range(initDay-1, endDay):
				self.ui.tableWidget.setItem(self.uDict[unidad], i, TableItem(self.conn, reserva=res, tipo=estado,init=(i==(initDay-1))))


	@QtCore.pyqtSlot()
	def doubleClicked(self, row, column):
		print "double!"

		res = self.ui.tableWidget.item(row,column).reserva
		self.idReservaActual = res #Mantengo en una variable global el id de la reserva seleccionada
		
		print "double clic" + str(res)
		if res == -1:

			idunidad = [k for k, v in self.uDict.iteritems() if v == row][0]
			today = QtCore.QDate.fromString("%d-%02d-%02d" % (self.ui.anioSpin.value(),self.ui.mesCombo.currentIndex()+1,column+1),"yyyy-MM-dd").toString("yyyy-MM-dd")

			endReservaDefault = QtCore.QDate.currentDate().addDays(7).toString("yyyy-MM-dd")

			diag = ReservaDialog(self.conn, inicioReserva=today, finReserva=endReservaDefault, unidad=idunidad)
			
		else:
			resMod = Reserva(self.conn)
			resMod.load(res)
			m = resMod.model
			print m.getItem("unidad").toInt()[0]
			diag = ReservaDialog(self.conn, id=res, unidad=m.getItem("unidad").toInt()[0], 
				huesped=m.getItem("huesped").toInt()[0], inicioPrereserva=unicode(m.getItem("inicioPrereserva").toString()), 
				finPrereserva=unicode(m.getItem("finPrereserva").toString()), inicioReserva=unicode(m.getItem("inicioReserva").toString()), 
				finReserva=unicode(m.getItem("finReserva").toString()), horaCheckIn=unicode(m.getItem("horaCheckIn").toString()), 
				horaCheckOut=unicode(m.getItem("horaCheckOut").toString()), estado=unicode(m.getItem("estado").toString()), temporada=unicode(m.getItem("temporada").toString()),
				senia = m.getItem("senia").toFloat()[0],
				mainWin = self.uiMain, parent = self)

		diag.exec_()
		self.update(0)

	@QtCore.pyqtSlot()
	def clicked(self, row, column):
		self.idReservaActual = self.ui.tableWidget.item(row,column).reserva
		print "un click " + str(self.idReservaActual)
	
	@QtCore.pyqtSlot()
	def keyPressEvent(self, event):
		keyEvent = QtGui.QKeyEvent(event)
		if(event.type()==QtCore.QEvent.KeyPress) and (keyEvent.key() == QtCore.Qt.Key_Delete):
			self.elimReserva()
		return super(GrillaDialog, self).keyPressEvent(keyEvent)
		
	def elimReserva(self):
		if (self.idReservaActual != -1):
			if (not self.model.checkelim(unicode(self.idReservaActual)) == 0):
				QtGui.QMessageBox.information(self, u"Error", u"La reserva está asociada a un gasto!")
			else:
				ret = QtGui.QMessageBox.question(self, "Advertencia", u"Está seguro de que desea realizar la eliminación?",
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
				if ret == QtGui.QMessageBox.Ok:
					print "Eliminando"
					self.model.delete(unicode(self.idReservaActual))
					self.update(0)
					self.idReservaActual = -1 #por las dudas que quede con un valor de id valido y se provoque un error
