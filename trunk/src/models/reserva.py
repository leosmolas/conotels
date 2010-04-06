from abstractmodel import AbstractModel

class Reserva(AbstractModel):
	def __init__(self):
		super(Reserva, self).__init__()

		self.tableName = "Reserva"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id = -1, unidad,huesped,inicioPrereserva,finPrereserva,inicioReserva,finReserva,horaCheckIn,horaCheckOut,estado): # if id != -1: update; else: save;
		if id != -1:
			self.conn.query("update "+self.tableName+" 
			set unidad="+unidad+",
				huesped"+huesped+",
				inicioPrereserva="+inicioPrereserva+",
				finPrereserva="+finPrereserva+",
				inicioReserva="+inicioReserva+",
				finReserva="+finReserva+",
				horaCheckIn="+horaCheckIn+",
				horaCheckOut="+horaCheckOut+",
				estado="+estado+ "
			where idReserva="+str(id))
		else:
			self.conn.query("insert into "+self.tableName+"
			(unidad,huesped,inicioPrereserva,finPrereserva,inicioReserva,finReserva,horaCheckIn,horaCheckOut,estado) 
			values ("+unidad+","+huesped+","+inicioPrereserva+","+finPrereserva+","+inicioReserva+","+finReserva+","+horaCheckIn+","+horaCheckOut+","+estado+")")
