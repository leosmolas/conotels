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

) ENGINE=InnoDB;


create table unidad (

	idUnidad int unsigned not null auto_increment,
	nombre varchar(45) not null,
	tipo int unsigned not null,
	capacidad int unsigned not null,
	descripcion varchar(45),
	estado enum('libre', 'ocupada',"noDisponible") not null,
	
	primary key (idUnidad),
	
	key FK_unidad_tipo (tipo),
	constraint FK_unidad_tipo foreign key (tipo) references tipo (idTipo)

) ENGINE=InnoDB;


create table huesped (

	#idHuesped int unsigned not null auto_increment,
	dni varchar(45) not null,
	apellido varchar(45) not null,
	nombre varchar(45) not null,
	
	telefono varchar(45) not null,
	
	primary key (dni)

) ENGINE=InnoDB;


create table reserva (

	idReserva int unsigned not null auto_increment,
	unidad int unsigned not null,
	#huesped int unisgned not null,
	huesped varchar (45) not null,
	inicioPrereserva date not null,
	finPrereserva date,
	inicioReserva date,
	finReserva date,
	horaCheckIn time,
	horaCheckOut time,
	estado enum('preReservado', 'reservado', 'enCurso', 'terminada', 'cancelada'),
	
	primary key (idReserva),

	#key FK_reserva_huesped (huesped),
	#constraint FK_reserva_huesped foreign key (huesped) references huesped (idHuesped)
	
	key FK_reserva_huesped (huesped),
	constraint FK_reserva_huesped foreign key (huesped) references huesped (dni)
	
) ENGINE=InnoDB;


create table gasto (

	idGasto int unsigned not null auto_increment,
	descripcion varchar(45) not null,
	costo int unsigned not null,
	reserva int unsigned not null,
	
	primary key (idGasto),
	
	key FK_gasto_reserva (reserva),
	constraint FK_gasto_reserva foreign key (reserva) references reserva (idReserva)

) ENGINE=InnoDB;