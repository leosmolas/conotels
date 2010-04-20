# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel
from PyQt4 import QtCore

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
			#print "update "+ self.tableName + " set descripcion='"+descripcion+"',costo="+str(costo)+",reserva="+str(reserva) + " where idGasto="+str(id)
			self.conn.update("update "+self.tableName+ 
				" set descripcion='"+descripcion+
				"',costo="+str(costo)+
				",reserva="+str(reserva) + 
				" where idGasto="+str(id))
		else:
			#print "insert into "+self.tableName+"(descripcion,costo,reserva)"+ " values ('"+descripcion+"',"+str(costo)+","+str(reserva)+")"
			self.conn.update("insert into "+self.tableName+
				"(descripcion,costo,reserva)"+ 
				" values ('"+descripcion+"',"+str(costo)+"," + str(reserva) + ")")
	
	#en vez de hacer una busqueda con likes re cacos, hace una busqueda con un where :)
	def buscarPorReserva(self,reserva):
		#print "select * from " + self.tableName + " where reserva = " + str(reserva)
		self.model = self.conn.query("select * from " + self.tableName + " where reserva = " +str(reserva))
		self.setHeaders()

	def setHeaders(self):
		self.model.setHeaderData(0,  QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1,  QtCore.Qt.Horizontal, "Descripcion") #si pongo descripción sale feo
		self.model.setHeaderData(2,  QtCore.Qt.Horizontal, "Costo")