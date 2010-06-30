# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

import exceptions

class ReservaOverlapError(Exception):

	def __init__(self, msg,type):
		self.msg = msg
		self.type = type

	def getMsg(self):
		return self.msg
		
	def getType(self):
		return self.type

	"""
	Metodo para imprimir el mensaje de error de la excepcion.
	Se ejecuta automaticamante cuando la excepcion no es capturada, 
	antes de interrumpir la ejecucion del programa.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def __str__(self):
		print "",self.msg

		

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

	def save(self, id = -1, unidad="",huesped="",inicioPrereserva="",finPrereserva="",inicioReserva="",finReserva="",horaCheckIn="",horaCheckOut="",estado="", temporada="",senia=0): # if id != -1: update; else: save;
		
		self.q = "select distinct idreserva from reserva where (((inicioReserva >= '"+inicioReserva+"') and (inicioReserva <= '"+finReserva+"')) or ((finReserva >= '"+inicioReserva+"') and (finReserva <= '"+finReserva+"'))) and (unidad="+unicode(unidad)+")"
		
		print self.q
		
		self.queryOverlap = self.conn.query(self.q)
		
		print self.queryOverlap.rowCount()
		
		
		if id != -1: #Es una modificación
			# not(No se solapa o se solapa sólo con si misma) -> Error
			if not (self.queryOverlap.rowCount() == 0 or ((self.queryOverlap.rowCount() == 1) and (self.queryOverlap.getItem("idreserva") == id))):
				print "Pete aca"
				raise ReservaOverlapError("Ya existen reservas en ese periodo!", "Error al modificar la reserva")
			self.conn.update("update "+self.tableName+ 
				" set unidad="+unicode(unidad)+
				",huesped="+unicode(huesped)+
				",inicioPrereserva='"+inicioPrereserva+
				"',finPrereserva='"+finPrereserva+
				"',inicioReserva='"+inicioReserva+
				"',finReserva='"+finReserva+
				"',horaCheckIn='"+horaCheckIn+
				"',horaCheckOut='"+horaCheckOut+
				"',estado='"+estado+ 
				"',temporada='"+temporada+ 
				"',senia="+senia+
				" where idReserva="+unicode(id))
		else:
			if self.queryOverlap.rowCount() != 0:
				print "Pete alla"
				raise ReservaOverlapError("Ya existen reservas en ese periodo!", "Error al insertar la reserva")
			else:
				print "entre"
				self.conn.update("insert into "+self.tableName+
				"(unidad,huesped,inicioPrereserva,finPrereserva,inicioReserva,finReserva,horaCheckIn,horaCheckOut,estado,temporada,senia)"+
				" values ("+unicode(unidad)+","+unicode(huesped)+",'"+inicioPrereserva+"','"+finPrereserva+"','"+inicioReserva+"','"+finReserva+"','"+horaCheckIn+"','"+horaCheckOut+"','"+estado+"','"+temporada+"',"+unicode(senia)+")")

	def loadAll(self):
		self.model = self.conn.query(
		"""select reserva.idReserva,
unidad.nombre, 
huesped.apellido, 
reserva.inicioPrereserva, 
reserva.finPrereserva, 
reserva.inicioReserva, 
reserva.finReserva, 
reserva.horaCheckIn, 
reserva.horaCheckOut, 
reserva.estado, 
reserva.temporada, 
reserva.senia,
unidad.idUnidad, 
huesped.idHuesped 
from reserva,unidad,huesped 
where unidad.idUnidad = reserva.unidad and huesped.idHuesped = reserva.huesped""")
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Unidad")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, u"Huésped")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Inicio de pre-reserva")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Fin de pre-reserva")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Inicio de reserva")
		self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Fin de reserva")
		self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Hora de checkIn")
		self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Hora de checkOut")
		self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Estado")
		self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Temporada")
		self.model.setHeaderData(11, QtCore.Qt.Horizontal, u"Seña")
		self.model.setHeaderData(12, QtCore.Qt.Horizontal, "idUnidad")
		self.model.setHeaderData(13, QtCore.Qt.Horizontal, "idHuesped")

	def loadMesAnio(self, mes = 1, anio = 2000):
		self.model = self.conn.query("select * from reserva where (month(inicioReserva)=%(mes)d or month(finReserva)=%(mes)d) and (year(inicioReserva)=%(anio)d or year(finReserva)=%(anio)d) and estado!=\"Reserva cancelada\" and estado!=\"Reserva terminada\"" % {'mes': mes, 'anio': anio});

	def checkelim(self, id=""):
		model = self.conn.query("select * from gasto where reserva = " + unicode(id))
		return model.rowCount()
		
	def loadPreExpiradas(self):
		today = QtCore.QDate.currentDate().toString("yyyy-MM-dd")
		self.model = self.conn.query("SELECT reserva.idReserva, unidad.nombre, huesped.apellido, reserva.inicioPrereserva, reserva.finPrereserva, reserva.inicioReserva, reserva.finReserva, reserva.horaCheckIn, reserva.horaCheckOut, reserva.estado, reserva.temporada, reserva.senia, unidad.idUnidad, huesped.idHuesped FROM reserva, unidad, huesped WHERE reserva.estado = \'Pre reservado\' AND reserva.finPrereserva < \'" + today + "\' AND unidad.idUnidad = reserva.unidad AND huesped.idHuesped = reserva.huesped")
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Unidad")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, u"Huésped")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Inicio de pre-reserva")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Fin de pre-reserva")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Inicio de reserva")
		self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Fin de reserva")
		self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Hora de checkIn")
		self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Hora de checkOut")
		self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Estado")
		self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Temporada")
		self.model.setHeaderData(11, QtCore.Qt.Horizontal, u"Seña")
		self.model.setHeaderData(12, QtCore.Qt.Horizontal, "idUnidad")
		self.model.setHeaderData(13, QtCore.Qt.Horizontal, "idHuesped")
