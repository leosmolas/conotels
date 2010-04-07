from abstractmodel import AbstractModel

class Tipo(AbstractModel):
	def __init__(self):
		super(Tipo, self).__init__()

		self.tableName = "tipo"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def __del__(self):
		super(Tipo, self).__del__()

	def save(self, id=-1, nombre="", costoTemporadaAlta=0, costoTemporadaBaja=0, descripcion=""):
		if id != -1:
			print "update"
			self.conn.query("update "+self.tableName+
				"set nombre='"+nombre+"', "+
					"costoTemporadaAlta="+str(costoTemporadaAlta)+","+
					"costoTemporadaBaja="+str(costoTemporadaBaja)+","+
					"descripcion='"+descripcion+
				"' where idTipo="+str(id))
		else:
			print "save"
			self.conn.query("insert into "+self.tableName+
				"(nombre,costoTemporadaAlta,costoTemporadaBaja,descripcion) "+
				"values ('"+nombre+"',"+str(costoTemporadaAlta)+","+str(costoTemporadaBaja)+","+descripcion+")")
