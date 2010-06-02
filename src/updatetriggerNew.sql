use conotels;

alter table reserva add gastos float unsigned default 0;

update reserva set gastos = 0 where gastos is null;

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