from abstractmodel import AbstractModel

class Huesped(AbstractModel):
	def __init__(self):
		super(Huesped, self).__init__()

		self.tableName = "unidad"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def __del__(self):
		super(Tipo, self).__del__()

	def save(self, dni="", nombre="", apellido="", telefono=""):
		if dni != "":
			self.conn.update("update "+self.tableName+" 
				set nombre='"+nombre+"',
					apellido='"+apellido+"',
					telefono='"+telefono+ "' 
				where dni='"+str(dni)+"'")
		else:
			self.conn.update("insert into "+self.tableName+"
				(dni, nombre, apellido, telefono) 
				values ('"+dni+"','"+nombre+"','"+apellido+"','"+telefono+"')")
