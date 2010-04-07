from connection.model import Model
from connection.error import Error
from connection.connection import Connection

class AbstractModel(object):
	def __init__(self):
		self.model = None

		self.conn = Connection("conotels", dbUser="root", dbPass="")
		self.conn.open()
	
		self.tableName = ""
	
	def __del__(self):
		print "Desconectando"
		self.conn.close()
	
	def load(self, id):
		self.model = self.conn.query("select * from "+self.tableName+" where id="+str(id))
	
	def loadAll(self):
		self.model = self.conn.query("select * from "+self.tableName)
	
	def delete(self, id):
		self.conn.update("delete from "+self.tableName+" where id="+str(id))
	
	def getModel(self):
		if self.model == None:
			raise Error("El model no ha sido asignado todavia", "Error de acceso a query model")
		return self.model
	
	def get(self, column):
		return self.getModel().getItem(column)
