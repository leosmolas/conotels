from connection.model import Model
from connection.error import Error

from connected import conn as connInstance

from PyQt4 import QtCore

class AbstractModel(object):
	def __init__(self):
		self.model = None
		self.conn = connInstance

		self.tableName = ""
		self.id = ""
	
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
