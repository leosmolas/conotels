# -*- coding: iso-8859-1 -*-
from abstractmodel import AbstractModel

class Reserva(AbstractModel):
	def __init__(self):
		super(Reserva, self).__init__()

		self.tableName = "reserva"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def __del__(self):
		super(Tipo, self).__del__()

	def save(self, id = -1, unidad="",huesped="",inicioPrereserva="",finPrereserva="",inicioReserva="",finReserva="",horaCheckIn="",horaCheckOut="",estado=""): # if id != -1: update; else: save;
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set unidad="+str(unidad)+
				",huesped='"+huesped+
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
			" values ("+str(unidad)+",'"+huesped+"','"+inicioPrereserva+"','"+finPrereserva+"','"+inicioReserva+"','"+finReserva+"','"+horaCheckIn+"','"+horaCheckOut+"','"+estado+"')")
