# -*- coding: utf-8 -*-
from connection.model import Model
from connection.error import Error
from PyQt4 import QtCore,QtSql
import re
from connection.connection import Connection

class AbstractModel(object):
	def __init__(self, conn):
		self.model = None
		self.conn = conn

		self.tableName = ""
		self.id = ""
		#self.params = ""
		self.campos = []
	
	def load(self, id):
		self.model = self.conn.query("select * from "+self.tableName+" where "+self.id+"="+unicode(id))
	
	def loadAll(self):
		self.model = self.conn.query("select * from "+self.tableName)
	
	def delete(self, id):
		self.conn.update("delete from "+self.tableName+" where "+self.id+"="+unicode(id))
	
	def getModel(self):
		if self.model == None:
			raise Error("El model no ha sido asignado todavia", "Error de acceso a query model")
		return self.model
	
	def get(self, column):
		return self.getModel().getItem(column)
	
	#def filterModel(self, filter):
		#print "select * from "+self.tableName+" where match "+self.params+" against ('*"+filter+"*' in boolean mode)"
		#self.model = self.conn.query("select * from "+self.tableName+" where match "+self.params+" against ('*"+filter+"*' in boolean mode)")
	
	##
	#este es el metodo que resuelve la busqueda con likes. Solo esta usada en este momento por gastos.
	#agregu� un nuevo detalle para que haga una b�squeda m�s parecida a la fulltext search (para que el guru no refunfu�e)
	def filterModel(self, filter):
		list = filter.split(' ')
		for i in range(len(list)):
			list[i] = self.escape(unicode(list[i]))
		print list
		s = "select * from " + self.tableName + " where "
		for i in range(len(self.campos)):
			for j in range(len(list)):
				#esta parte es media parchosa... el split me genera strings vacios, asi que con esto los ignoro
				if  list[j]!='':
					s += self.campos[i] + " like '%" + list[j] + "%' "
					s += "OR "
		#siempre pongo un 'or ' al final, asi que con lo sig lo saco
		s = s[0:-3]
		print "consulta: " + s
		self.model = self.conn.query(s)

	def escape(self, str):
		ns = str
		return ns.replace('"', '\\"').replace("'", "\\'")
