create database conotels;
create user 'userHoteles' identified by 'userHoteles';
grant super on *.* to 'userHoteles';
grant all privileges on *.* to 'userHoteles' with grant option;


USE conotels;


create table tipo (

	idTipo int unsigned not null auto_increment,
	nombre varchar(45) not null,
	costoTemporadaAlta int unsigned not null,
	costoTemporadaBaja int unsigned not null,
	descripcion varchar(45),
	
	primary key (idTipo)

) ENGINE=MYISAM;


create table unidad (

	idUnidad int unsigned not null auto_increment,
	nombre varchar(45) not null,
	tipo int unsigned not null,
	capacidad int unsigned not null,
	descripcion varchar(45),
	estado enum('Libre', 'Ocupada','No Disponible') not null,
	
	primary key (idUnidad),
	
	key FK_unidad_tipo (tipo),
	constraint FK_unidad_tipo foreign key (tipo) references tipo (idTipo)

) ENGINE=MYISAM;


create table huesped (

	idHuesped int unsigned not null auto_increment,
	dni varchar(45) not null,
	apellido varchar(45) not null,
	nombre varchar(45) not null,
	
	telefono varchar(45) not null,
	
	primary key (idHuesped)

) ENGINE=MYISAM;


create table reserva (

	idReserva int unsigned not null auto_increment,
	unidad int unsigned not null,
	huesped int unsigned not null,
	inicioPrereserva date not null,
	finPrereserva date,
	inicioReserva date,
	finReserva date,
	horaCheckIn time,
	horaCheckOut time,
	estado enum('Pre Reservado', 'Reservado', 'Reserva en curso', 'Reserva terminada', 'Reserva cancelada'),
	
	primary key (idReserva),

	key FK_reserva_unidad (unidad),
	constraint FK_reserva_unidad foreign key (unidad) references unidad (idUnidad),
	
	
	key FK_reserva_huesped (huesped),
	constraint FK_reserva_huesped foreign key (huesped) references huesped (idHuesped)
	
) ENGINE=MYISAM;


create table gasto (

	idGasto int unsigned not null auto_increment,
	descripcion varchar(45) not null,
	costo int unsigned not null,
	reserva int unsigned not null,
	
	primary key (idGasto),
	
	key FK_gasto_reserva (reserva),
	constraint FK_gasto_reserva foreign key (reserva) references reserva (idReserva)

) ENGINE=MYISAM;	

use conotels;

delimiter //
create trigger update_unidad before update on reserva
	for each row begin
		declare uni int;
		set uni = new.unidad;
		if new.estado = 'Reserva en curso' then
			update unidad set estado = 'Ocupada' where unidad.idUnidad = uni;
		elseif old.estado = 'Reserva en curso' and new.estado <> 'Reserva en curso' then
			update unidad set estado = 'Libre' where unidad.idUnidad = uni;
		end if;
	end//
delimiter ;