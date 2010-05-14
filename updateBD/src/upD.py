from PyQt4 import QtCore, QtGui
from updateBD import Ui_Dialog
from connection import Connection

def readFile(fileName):
	fileDrop = open(fileName,'r')
	res=""
	for line in fileDrop.readlines():
		res=res+line
	return res


class CustomDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

	@QtCore.pyqtSlot()
	def updateBD(self):
		
		file = open("conf.dat")
		user = file.readline()
		password = file.readline()
		conn=Connection(dbName="conotels", dbUser=user.replace('\n', ''), dbPass=password.replace('\n', ''))
		conn.open()
		conn.update("drop table IF EXISTS gasto;")
		conn.update("drop table IF EXISTS reserva;")
		conn.update("drop table IF EXISTS huesped;")
		conn.update("drop table IF EXISTS unidad;")
		conn.update("drop table IF EXISTS tipo;")
		conn.update("drop trigger IF EXISTS update_unidad;")
		conn.update("DROP VIEW IF EXISTS reservasView;")
		conn.update("create table tipo (idTipo int unsigned not null auto_increment,nombre varchar(45) not null,costoTemporadaAlta int unsigned not null,costoTemporadaBaja int unsigned not null,descripcion text,primary key (idTipo)) ENGINE=innoDB;")
		conn.update("create table unidad (idUnidad int unsigned not null auto_increment,nombre varchar(45) not null,tipo int unsigned not null,capacidad int unsigned not null,descripcion text,estado enum('Libre', 'Ocupada','No Disponible') not null,primary key (idUnidad),key FK_unidad_tipo (tipo),constraint FK_unidad_tipo foreign key (tipo) references tipo (idTipo)) ENGINE=innoDB;")
		conn.update("create table huesped (idHuesped int unsigned not null auto_increment,dni varchar(45) not null,apellido varchar(45) not null,nombre varchar(45) not null,telefonoFijo varchar(45),telefonoCelular varchar(45),direccion varchar(45),Localidad varchar(45),primary key (idHuesped)) ENGINE=innoDB;")
		conn.update("create table reserva (idReserva int unsigned not null auto_increment,unidad int unsigned not null,huesped int unsigned not null,inicioPrereserva date not null,finPrereserva date,inicioReserva date,finReserva date,horaCheckIn time,horaCheckOut time,estado enum('Pre Reservado', 'Reservado', 'Reserva en curso', 'Reserva terminada', 'Reserva cancelada'),temporada enum('Alta', 'Baja'),primary key (idReserva),key FK_reserva_unidad (unidad),constraint FK_reserva_unidad foreign key (unidad) references unidad (idUnidad),key FK_reserva_huesped (huesped),constraint FK_reserva_huesped foreign key (huesped) references huesped (idHuesped)) ENGINE=innoDB;");
		conn.update("create table gasto (idGasto int unsigned not null auto_increment,descripcion text not null,costo float unsigned not null,reserva int unsigned not null,pendiente boolean,primary key (idGasto),key FK_gasto_reserva (reserva),constraint FK_gasto_reserva foreign key (reserva) references reserva (idReserva)) ENGINE=innoDB;");
		conn.update("create trigger update_unidad before update on reserva for each row begin \n declare uni int;set uni = new.unidad;if new.estado = 'Reserva en curso' then update unidad set estado = 'Ocupada' where unidad.idUnidad = uni;elseif old.estado = 'Reserva en curso' and new.estado <> 'Reserva en curso' then update unidad set estado = 'Libre' where unidad.idUnidad = uni;end if;end")
		conn.update("CREATE VIEW reservasView AS SELECT idReserva, apellido, dni, u.nombre, inicioPrereserva,finPrereserva, inicioReserva, finReserva, horaCheckIn, horaCheckOut, r.estado FROM  reserva AS r, huesped AS h, unidad AS u WHERE r.huesped = idHuesped AND idUnidad = unidad;")
		conn.close()
		reply = QtGui.QMessageBox.question(self, 'Update',"Base de Datos Actualizada con exito", QtGui.QMessageBox.Ok)
		
		
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ui = CustomDialog()
	ui.show()
	sys.exit(app.exec_())