create database carga_m_A;
use carga_m_A;
Create Table usuarios(
id int not null auto_increment,
name varchar(50) not null,
company varchar(50) not null,
job varchar(50) not null,
email varchar(50) not null,
phone varchar(50) not null,
mac_address varchar(50) not null,
primary key(id)
);

select * from usuarios;
insert into usuarios(name, company, job, email, phone, mac_address) values('Alberto Montes', 'Hernández-Pedraza', 
'Técnico en ciencias físicas y químicas','juangalindo@example.com', '328 014 34 08','dc:a2:7d:5c:86:03');
