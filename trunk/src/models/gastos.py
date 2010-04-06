from abstractmodel import AbstractModel

class Gastos(AbstractModel):
	def __init__(self):
		super(Gastos, self).__init__()

		self.tableName = "gastos"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id = -1, descripcion="",costo=0,reserva=0): # if id != -1: update; else: save;
		if id != -1:
			self.conn.query("update "+self.tableName+" 
			set descripcion="+descripcion+",
				costo="+costo+",
				reserva="+reserva +" 
			where idGasto="+str(id))
		else:
			self.conn.query("insert into "+self.tableName+"
			(descripcion,costo,reserva) 
			values ("+descripcion+","+costo+","+reserva+")")
