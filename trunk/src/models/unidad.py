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

	def save(self, id = -1, nombre="", tipo=0, capacidad=0, descripcion="", estado="Libre"):
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set nombre='"+nombre+
				"',tipo="+unicode(tipo)+
				",capacidad="+unicode(capacidad)+
				",descripcion='"+descripcion+
				"',estado='"+estado+ 
				"' where idUnidad="+unicode(id))
		else:
			self.conn.update("insert into "+self.tableName+
				"(nombre, tipo, capacidad, descripcion, estado)"+
				" values ('"+nombre+"',"+unicode(tipo)+","+unicode(capacidad)+",'"+descripcion+"','"+estado+"')")

	def loadAll(self):
		self.model = self.conn.query("select unidad.idUnidad,unidad.nombre,tipo.nombre,unidad.capacidad,unidad.descripcion,unidad.estado,unidad.tipo from unidad,tipo where unidad.tipo = tipo.idTipo")
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, u"Número")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Tipo")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, u"Descripción")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Capacidad")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Estado")
		self.model.setHeaderData(6, QtCore.Qt.Horizontal, "unidad.Tipo") #no visible en el QtTableWidget

	def count(self):
		self.loadAll()
		return self.model.rowCount()
		
	def checkname(self, nombre=""):
		self.model = self.conn.query("select * from unidad where nombre = '" + nombre + "'")
		return self.model.rowCount()

	def checkelim(self, id=0):
		model = self.conn.query("select * from reserva where unidad = " + unicode(id))
		return model.rowCount()
