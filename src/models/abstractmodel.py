# -*- coding: utf-8 -*-
from connection.model import Model
from connection.error import Error

from connection.connection import Connection

class AbstractModel(object):
	def __init__(self, conn):
		self.model = None
		self.conn = conn

		self.tableName = ""
		self.id = ""
		self.params = ""
		self.campos = []
	
	def load(self, id):
		self.model = self.conn.query("select * from "+self.tableName+" where id="+str(id))
	
	def loadAll(self):
		self.model = self.conn.query("select * from "+self.tableName)
	
	def delete(self, id):
		self.conn.update("delete from "+self.tableName+" where "+self.id+"="+str(id))
	
	def getModel(self):
		if self.model == None:
			raise Error("El model no ha sido asignado todavia", "Error de acceso a query model")
		return self.model
	
	def get(self, column):
		return self.getModel().getItem(column)
	
	def filterModel(self, filter):
		print "select * from "+self.tableName+" where match "+self.params+" against ('*"+filter+"*' in boolean mode)"
		self.model = self.conn.query("select * from "+self.tableName+" where match "+self.params+" against ('*"+filter+"*' in boolean mode)")

	#este es el metodo que resuelve la busqueda con likes. Solo esta usada en este momento por gastos.
	def filterModel2(self, filter):
		s = "select * from " + self.tableName + " where "
		for i in range(len(self.campos)):
			s += self.campos[i] + " like '%" + filter + "%' "
			if (i<len(self.campos)-1):
				s += "OR "
		print s
		self.model = self.conn.query(s)
