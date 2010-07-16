use conotels;

CREATE VIEW reservasView AS 
	SELECT idReserva, apellido, dni, u.nombre, inicioPrereserva,finPrereserva, inicioReserva, finReserva, horaCheckIn, horaCheckOut, r.estado
	FROM  reserva AS r, huesped AS h, unidad AS u
	WHERE r.huesped = idHuesped AND idUnidad = unidad;
