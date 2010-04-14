# -*- coding: iso-8859-1 -*-
from abstractmodel import AbstractModel

class Gastos(AbstractModel):
	def __init__(self, conn):
		super(Gastos, self).__init__(conn)

		self.tableName = "gasto"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def __del__(self):
		super(Tipo, self).__del__()

	def save(self, id = -1, descripcion="",costo=0,reserva=0): # if id != -1: update; else: save;
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set descripcion='"+descripcion+
				"',costo="+str(costo)+
				",reserva="+str(reserva) + 
			" where idGasto="+str(id))
		else:
			self.conn.update("insert into "+self.tableName+
			"(descripcion,costo,reserva)"+ 
			" values ('"+descripcion+"',"+str(costo)+","+str(reserva)+")")
