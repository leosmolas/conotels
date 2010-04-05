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

	def save(self, id = -1, nombre="", tipo=0, capacidad=0, descripcion="", estado="libre"):
		if id != -1:
			self.conn.query("update "+self.tableName+" 
				set nombre="+nombre+",
					tipo="+tipo+",
					capacidad="+capacidad+",
					descripcion="+descripcion+",
					estado="+estado+"
				where idUnidad="+str(id))
		else:
			self.conn.query("insert into "+self.tableName+"
				(nombre, tipo, capacidad, descripcion, estado) 
				values ("+nombre+","+tipo+","+capacidad+","+descripcion+","+estado+")")
