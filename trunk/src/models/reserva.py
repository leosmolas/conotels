﻿# -*- coding: utf-8 -*-
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

	def save(self, id = -1, unidad="",huesped="",inicioPrereserva="",finPrereserva="",inicioReserva="",finReserva="",horaCheckIn="",horaCheckOut="",estado="", temporada=""): # if id != -1: update; else: save;
		
		self.q = "select idreserva from reserva where (((inicioReserva >= '"+inicioReserva+"') and (inicioReserva <= '"+finReserva+"')) or ((finReserva >= '"+inicioReserva+"') and (finReserva <= '"+finReserva+"'))) and (unidad="+str(unidad)+")"
		
		print self.q
		
		self.queryOverlap = self.conn.query(self.q)
		
		print self.queryOverlap.rowCount()
		
		
		if id != -1:
			if self.queryOverlap.rowCount() != 1:
				raise "Ya existen reservas en ese periodo!"
			self.conn.update("update "+self.tableName+ 
				" set unidad="+str(unidad)+
				",huesped="+str(huesped)+
				",inicioPrereserva='"+inicioPrereserva+
				"',finPrereserva='"+finPrereserva+
				"',inicioReserva='"+inicioReserva+
				"',finReserva='"+finReserva+
				"',horaCheckIn='"+horaCheckIn+
				"',horaCheckOut='"+horaCheckOut+
				"',estado='"+estado+ 
				"',temporada='"+temporada+ 
				"' where idReserva="+str(id))
		else:
			if self.queryOverlap.rowCount() != 0:
				raise "Ya existen reservas en ese periodo!"
			else:
				print "entre"
				self.conn.update("insert into "+self.tableName+
				"(unidad,huesped,inicioPrereserva,finPrereserva,inicioReserva,finReserva,horaCheckIn,horaCheckOut,estado,temporada)"+
				" values ("+str(unidad)+","+str(huesped)+",'"+inicioPrereserva+"','"+finPrereserva+"','"+inicioReserva+"','"+finReserva+"','"+horaCheckIn+"','"+horaCheckOut+"','"+estado+"','"+temporada+"')")

	def loadAll(self):
		self.model = self.conn.query("select reserva.idReserva,unidad.nombre,huesped.apellido,reserva.inicioPrereserva,reserva.finPrereserva,reserva.inicioReserva,reserva.finReserva,reserva.horaCheckIn,reserva.horaCheckOut,reserva.estado,reserva.temporada,unidad.idUnidad,huesped.idHuesped from reserva,unidad,huesped where unidad.idUnidad = reserva.unidad and huesped.idHuesped = reserva.huesped")
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
		self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Temporada")
		self.model.setHeaderData(11, QtCore.Qt.Horizontal, "idUnidad")
		self.model.setHeaderData(12, QtCore.Qt.Horizontal, "idHuesped")

	def loadMesAnio(self, mes = 1, anio = 2000):
		self.model = self.conn.query("select * from reserva where (month(inicioPrereserva)=%(mes)d or month(finPrereserva)=%(mes)d or month(inicioReserva)=%(mes)d or month(finReserva)=%(mes)d) and (year(inicioReserva)=%(anio)d or year(finReserva)=%(anio)d or year(inicioPrereserva)=%(anio)d or year(finPrereserva)=%(anio)d) and estado!=\"Reserva cancelada\"" % {'mes': mes, 'anio': anio});

	def checkelim(self, id=""):
		model = self.conn.query("select * from gasto where reserva = " + str(id))
		return model.rowCount()