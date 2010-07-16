use conotels;

drop user userHoteles;

drop trigger if exists update_unidad;
drop trigger if exists update_gasto;
drop trigger if exists delete_gasto;
drop trigger if exists insert_reserva_bf;
drop trigger if exists insert_reserva;
drop trigger if exists insert_gasto;

drop database if exists conotels;