use conotels

alter table reserva add gastos float unsigned default 0;

update reserva set gastos = 0 where gastos is null;

delimiter //
create trigger insert_gasto after insert on gasto
	for each row begin
		declare valor float;
		set valor = new.costo;
		update reserva set gastos = gastos + valor where idReserva = new.reserva;
	end//
delimiter ;

delimiter //
create trigger update_gasto before update on gasto
	for each row begin
		declare valor float;
		set valor = new.costo - old.costo;
		update reserva set gastos = gastos + valor where idReserva = new.reserva;
	end//
delimiter ;

