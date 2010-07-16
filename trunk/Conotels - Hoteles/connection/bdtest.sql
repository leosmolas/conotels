create database bdtest;
create user 'bdtest'@'localhost' identified by 'bdtest';
grant super on *.* to 'bdtest'@'localhost';
grant all privileges on *.* to 'bdtest'@'localhost' with grant option;

USE bdtest;

create table empresa (

	id_empresa int unsigned not null auto_increment,
	nombre varchar(45) not null,
	primary key (id_empresa)
) ENGINE=InnoDB;

create table persona (
	cuil varchar(13) not null,
	nombre varchar(45) not null,
	apellido varchar(45) not null,
	direccion varchar(45),
	primary key (cuil)
) ENGINE=InnoDB;

USE bdtest;
insert into empresa(nombre) values ('Conosoft');
insert into empresa(nombre) values ('Club del Pelo S.A.');
insert into empresa(nombre) values ('Peronismo Today');
insert into empresa(nombre) values ('Puto el que lee ltd.');
insert into empresa(nombre) values ('Cacos');
insert into empresa(nombre) values ('Troskos');
insert into empresa(nombre) values ('Manco & Manco S.A:');

insert into persona(cuil,nombre,apellido,direccion) values (1,'Ego','Molas','Troskolandia 122');
insert into persona(cuil,nombre,apellido,direccion) values (2,'Tommy','El guru','Cueva de Oso 400');
insert into persona(cuil,nombre,apellido,direccion) values (3,'Jona','Impresentable Vainstein','Israel 25');
insert into persona(cuil,nombre,apellido,direccion) values (4,'Fer','limado Sisul','WOW 11');
insert into persona(cuil,nombre,apellido,direccion) values (5,'Manu','Quantum Torres','Pueblito de mala muerte 800');
