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
	descripcion text,
	
	primary key (idTipo)

) ENGINE=innoDB;


create table unidad (

	idUnidad int unsigned not null auto_increment,
	nombre varchar(45) not null,
	tipo int unsigned not null,
	capacidad int unsigned not null,
	descripcion text,
	estado enum('Libre', 'Ocupada','No Disponible') not null,
	
	primary key (idUnidad),
	
	key FK_unidad_tipo (tipo),
	constraint FK_unidad_tipo foreign key (tipo) references tipo (idTipo)

) ENGINE=innoDB;


create table huesped (

	idHuesped int unsigned not null auto_increment,
	dni varchar(45) not null,
	apellido varchar(45) not null,
	nombre varchar(45) not null,
	telefonoFijo varchar(45),
	telefonoCelular varchar(45),
	direccion varchar(45),
	Localidad varchar(45),
	email varchar(45),
	autoPatente varchar(20),
	autoModelo varchar(45),
	autoColor varchar(45),
		
	primary key (idHuesped)

) ENGINE=innoDB;


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
	temporada enum('Alta', 'Baja'),
	gastos float unsigned default 0,
	
	primary key (idReserva),

	key FK_reserva_unidad (unidad),
	constraint FK_reserva_unidad foreign key (unidad) references unidad (idUnidad),
	
	
	key FK_reserva_huesped (huesped),
	constraint FK_reserva_huesped foreign key (huesped) references huesped (idHuesped)
	
) ENGINE=innoDB;


create table gasto (

	idGasto int unsigned not null auto_increment,
	descripcion text not null,
	costo float unsigned not null,
	reserva int unsigned not null,
	pendiente boolean,
	
	primary key (idGasto),
	
	key FK_gasto_reserva (reserva),
	constraint FK_gasto_reserva foreign key (reserva) references reserva (idReserva)

) ENGINE=innoDB;	

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


delimiter //
create trigger insert_gasto after insert on gasto
	for each row begin
		declare valor float;
		
		if new.pendiente = 1 then
			set valor = new.costo;
			update reserva set gastos = gastos + valor where idReserva = new.reserva;
		end if;
	end//
delimiter ;


delimiter //
create trigger update_gasto before update on gasto
	for each row begin
		declare valor float;
		
		-- Si el gasto ya estaba pago y solamente modifica el valor no me afecta, no hago nada (solo guardo el total de los gastos que restan por pagar)
		if new.pendiente = 1 or old.pendiente = 1 then
			set valor = new.costo - old.costo;			
					
			-- Si cambio el estado y se paso a pendiente tengo que agregar el valor del gasto total al total en la reserva
			if new.pendiente = 1 and old.pendiente = 0 then
				update reserva set gastos = gastos + new.costo;
			
			-- Si cambio el estado y se paso a no pendiente (pago) tengo que restar el valor del gasto al total en la reserva. (Si el costo del gasto no cambio valor = 0)
			elseif new.pendiente = 0 and old.pendiente = 1 then
				update reserva set gastos = gastos + valor - new.costo where idReserva = new.reserva;
			
			-- Si el estado se mantiene en pendiente tengo que actualizar el valor total con el valor que se modifico
			elseif new.pendiente = 1 and old.pendiente = 1 then
				update reserva set gastos = gastos + valor where idReserva = new.reserva;
			
			end if;
		end if;
	end//
delimiter ;


delimiter //
create trigger delete_gasto after delete on gasto
	for each row begin
		if old.pendiente = 1 then
			update reserva set gastos = gastos - old.costo;
		end if;
	end//
delimiter ;

-- una vista para la tabla de reservas en Gastos
CREATE VIEW reservasView AS 
	SELECT idReserva, apellido, dni, u.nombre, inicioPrereserva,finPrereserva, inicioReserva, finReserva, horaCheckIn, horaCheckOut, r.estado
	FROM  reserva AS r, huesped AS h, unidad AS u
	WHERE r.huesped = idHuesped AND idUnidad = unidad;