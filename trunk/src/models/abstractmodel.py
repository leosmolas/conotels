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
		self.model = self.conn.query("select * from "+self.tableName+" where match "+self.params+" against ('"+filter+"*' in boolean mode)")
