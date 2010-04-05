from connection.model import Model
from connection.error import Error
from connection.connection import Connection

class AbstractModel():
	def __init__(self):
		super(AbstractModel, self).__init__()

		self.model = None

		self.conn = Connection("conotels", dbUser="userHoteles", dbPass="userHoteles")
		self.conn.open()
	
		self.tableName = ""
	
	def __del__(self):
		self.conn.close()
	
	def load(self, id):
		self.model = self.conn.query("select * from "+self.tableName+" where id="+str(id))
	
	def loadAll(self):
		self.model = self.conn.query("select * from "+self.tableName)
	
	def delete(self, id):
		self.conn.query("drop from "+self.tableName+" where id="+str(id))
	
	#def save(self, id = -1, ...): # if id != -1: update; else: save;
	
	def getModel(self):
		if self.model == None:
			raise Error("El model no ha sido asignado todavia", "Error de acceso a query model")
		return self.model
	
	def get(self, column):
		return self.getModel().getItem(column)
