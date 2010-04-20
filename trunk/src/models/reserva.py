# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Reserva(AbstractModel):
	def __init__(self, conn):
		super(Reserva, self).__init__(conn)

		self.tableName = "reserva"
		self.id = "idReserva"
		
		
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id = -1, unidad="",huesped="",inicioPrereserva="",finPrereserva="",inicioReserva="",finReserva="",horaCheckIn="",horaCheckOut="",estado=""): # if id != -1: update; else: save;
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set unidad="+str(unidad)+
				",huesped='"+str(huesped)+
				"',inicioPrereserva='"+inicioPrereserva+
				"',finPrereserva='"+finPrereserva+
				"',inicioReserva='"+inicioReserva+
				"',finReserva='"+finReserva+
				"',horaCheckIn='"+horaCheckIn+
				"',horaCheckOut='"+horaCheckOut+
				"',estado='"+estado+ 
				"' where idReserva="+str(id))
		else:
			self.conn.update("insert into "+self.tableName+
			"(unidad,huesped,inicioPrereserva,finPrereserva,inicioReserva,finReserva,horaCheckIn,horaCheckOut,estado)"+
			" values ("+str(unidad)+",'"+str(huesped)+"','"+inicioPrereserva+"','"+finPrereserva+"','"+inicioReserva+"','"+finReserva+"','"+horaCheckIn+"','"+horaCheckOut+"','"+estado+"')")

	def loadAll(self):
		super(Reserva, self).loadAll()
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Unidad")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Huesped")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Inicio de prereserva")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Fin de prereserva")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Inicio de reserva")
		self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Fin de reserva")
		self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Hora de checkIn")
		self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Hora de checkOut")
		self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Estado")
