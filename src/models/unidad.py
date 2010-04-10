# -*- coding: iso-8859-1 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Unidad(AbstractModel):
	def __init__(self, conn):
		super(Unidad, self).__init__(conn)

		self.tableName = "unidad"
		self.id = "idUnidad"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id = -1, nombre="", tipo=0, capacidad=0, descripcion="", estado="libre"):
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set nombre='"+nombre+
				"',tipo="+str(tipo)+
				",capacidad="+str(capacidad)+
				",descripcion='"+descripcion+
				"',estado='"+estado+ 
				"' where idUnidad="+str(id))
		else:
			self.conn.update("insert into "+self.tableName+
				"(nombre, tipo, capacidad, descripcion, estado)"+
				" values ('"+nombre+"',"+str(tipo)+","+str(capacidad)+",'"+descripcion+"','"+estado+"')")

	def loadAll(self):
		super(Unidad, self).loadAll()
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Numero")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Tipo")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Descripcion")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Capacidad")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Estado")
