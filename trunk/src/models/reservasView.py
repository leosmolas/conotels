# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class ReservasView(AbstractModel):
	def __init__(self, conn):
		super(ReservasView, self).__init__(conn)

		self.tableName = "reservasView"
		self.id = "idReserva"
		
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def loadAll(self):
		super(ReservasView, self).loadAll()
		self.model.setHeaderData(0,  QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1,  QtCore.Qt.Horizontal, "Apellido")
		self.model.setHeaderData(2,  QtCore.Qt.Horizontal, "DNI")
		self.model.setHeaderData(3,  QtCore.Qt.Horizontal, "Unidad")
		self.model.setHeaderData(4,  QtCore.Qt.Horizontal, "Inicio de prereserva")
		self.model.setHeaderData(5,  QtCore.Qt.Horizontal, "Fin de prereserva")
		self.model.setHeaderData(6,  QtCore.Qt.Horizontal, "Inicio de reserva")
		self.model.setHeaderData(7,  QtCore.Qt.Horizontal, "Fin de reserva")
		self.model.setHeaderData(8,  QtCore.Qt.Horizontal, "Hora de checkIn")
		self.model.setHeaderData(9,  QtCore.Qt.Horizontal, "Hora de checkOut")
		self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Estado")

	def filterModel(self,filter,campo):
		print "select * from "+self.tableName+" where " + campo + " like '%" + filter + "%'"
		self.model = self.conn.query("select * from "+self.tableName+" where " + campo + " like '%" + filter + "%'")