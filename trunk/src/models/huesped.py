# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Huesped(AbstractModel):
	def __init__(self, conn):
		super(Huesped, self).__init__(conn)

		self.tableName = "huesped"
		self.id = "idHuesped"

		#self.params = "(dni,nombre,apellido,telefono)"
		self.campos = ["dni","nombre","apellido","telefonoFijo","telefonoCelular","direccion","Localidad"]
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self,id=-1, dni="", nombre="", apellido="", telefono="",celular="",direccion="",localidad=""):
		if id != -1:
			self.conn.update("update "+self.tableName+ 
				" set nombre='"+nombre+
				"',apellido='"+apellido+
				"',telefonoFijo='"+telefono+ 
				"',dni='"+dni+ 
				"',telefonoCelular='"+celular+
				"',direccion='"+direccion+
				"',Localidad='"+localidad+
				 "' where idHuesped="+unicode(id))
		else:
			#print "insert into "+self.tableName+" (dni, nombre, apellido, telefonoFijo,telefonoCelular,direccion,Localidad) "+ "values ('"+dni+"','"+nombre+"','"+apellido+"','"+telefono+"','"+celular+"','"+direccion+"','"+localidad+"')"
			
			self.conn.update("insert into "+self.tableName+
				" (dni, nombre, apellido, telefonoFijo,telefonoCelular,direccion,Localidad) "+ 
				"values ('"+dni+"','"+nombre+"','"+apellido+"','"+telefono+"','"+celular+"','"+direccion+"','"+localidad+"')")

	def loadAll(self):
		super(Huesped, self).loadAll()
		self.setHeaders()

	def setHeaders(self):
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "DNI")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Apellido")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Nombre")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Teléfono")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Celular")
		self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Dirección")
		self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Localidad")

	def filterModel(self,filtro):
		super(Huesped,self).filterModel(filtro)
		self.setHeaders()
		
	def checkdni(self, dni=""):
		self.model = self.conn.query("select * from huesped where dni = '" + dni + "'")
		return self.model.rowCount()

	def checkelim(self, id=0):
		model = self.conn.query("select * from reserva where huesped = " + unicode(id))
		return model.rowCount()
