use conotels;

INSERT INTO tipo ( nombre        , costoTemporadaAlta , costoTemporadaBaja , descripcion ) 
VALUES 		 ("cabaña re top", 150		      , 100		   , "asd");

INSERT INTO unidad ( nombre , tipo , capacidad , descripcion    , estado ) 
VALUES 		   ("A"     , 1    , 3         , "linda cabaña" , "Libre");

INSERT INTO huesped ( dni , apellido , nombre , telefono ) 
VALUES 		    ( 1   , "Canepa" , "Toga" , 123123   );

INSERT INTO reserva ( unidad , huesped , inicioPrereserva , finPrereserva , inicioReserva , finReserva  , horaCheckIn , horaCheckOut , estado ) 
VALUES 		    ( 1      , 1       , '2010-01-01'     , null          , '2010-01-01'  , '2010-01-02', null        , null         , 'Reserva cancelada');

INSERT INTO gasto ( descripcion             , costo , reserva ) 
VALUES 		  ( "Servicio de habitación", 50    , 1       );
