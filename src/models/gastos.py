from abstractmodel import AbstractModel

class Unidad(AbstractModel):
	def __init__(self):
		super(Unidad, self).__init__()

		self.tableName = "unidad"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id = -1, ...): # if id != -1: update; else: save;
		if id != -1:
			self.conn.query("update "+self.tableName+" set ... where id="+str(id))
		else:
			self.conn.query("insert into "+self.tableName+"(...) values (...)")
