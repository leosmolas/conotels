# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Tipo(AbstractModel):
	def __init__(self, conn):
		super(Tipo, self).__init__(conn)

		self.tableName = "tipo"
		self.id = "idTipo"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id=-1, nombre="", costoTemporadaAlta=0, costoTemporadaBaja=0, descripcion=""):
		if id != -1:
			print "update "+self.tableName+" set nombre='"+nombre+"', "+"costoTemporadaAlta="+unicode(costoTemporadaAlta)+", "+	"costoTemporadaBaja="+unicode(costoTemporadaBaja)+", "+	"descripcion='"+descripcion+"' "+				" where idTipo="+unicode(id)
			self.conn.update("update "+self.tableName+
				" set nombre='"+nombre+"', "+
					"costoTemporadaAlta="+unicode(costoTemporadaAlta)+", "+
					"costoTemporadaBaja="+unicode(costoTemporadaBaja)+", "+
					"descripcion='"+descripcion+"' "+
				" where idTipo="+unicode(id))
		else:
			self.conn.update("insert into "+self.tableName+
				"(nombre,costoTemporadaAlta,costoTemporadaBaja,descripcion) "+
				"values ('"+nombre+"',"+unicode(costoTemporadaAlta)+","+unicode(costoTemporadaBaja)+",'"+descripcion+"')")

	def loadAll(self):
		super(Tipo, self).loadAll()
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, u"ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, u"Nombre")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, u"Costo en Temporada Alta")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, u"Costo en Temporada Baja")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, u"Descripción")
		
	def checkname(self, nombre=""):
		#print "select * from tipo where nombre = '" + nombre + "'"
		self.model = self.conn.query("select * from tipo where nombre = '" + nombre + "'")
		return self.model.rowCount()
		
	def checkelim(self, id=""):
		model = self.conn.query("select * from unidad where tipo = " + unicode(id))
		return model.rowCount()
