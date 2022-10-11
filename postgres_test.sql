
--- Creación de tablas

CREATE TABLE proveedor(
	id SERIAL, 
	nombre VARCHAR(1024) NOT NULL, 
	PRIMARY KEY(id)
);

CREATE TABLE categoria(
	id SERIAL, 
	nombre VARCHAR(1024) NOT NULL, 
	PRIMARY KEY(id)
);

CREATE TABLE producto(
	id SERIAL, 
	nombre VARCHAR(1024) NOT NULL, 
	cantidad INTEGER NOT NULL, 
	fecha_actualizacion DATE NOT NULL, 
	idProveedor INTEGER, 
	idCategoria INTEGER, 
	FOREIGN KEY(idProveedor) REFERENCES proveedor(id),
	FOREIGN KEY(idCategoria) REFERENCES categoria(id),
	PRIMARY KEY(id)
);

-- Insertar datos

INSERT INTO proveedor (nombre) VALUES ('Papelera SA de CV');
INSERT INTO proveedor (nombre) VALUES ('Tiendita de la esquina');
INSERT INTO proveedor (nombre) VALUES ('Compania de Electronica');


INSERT INTO categoria (nombre) VALUES ('oficina');
INSERT INTO categoria (nombre) VALUES ('viaticos');
INSERT INTO categoria (nombre) VALUES ('electronica');


INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('lapiz', 10, '2022-05-03', 1, 1);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('goma', 15, '2022-05-05', 1, 1);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('sacapuntas', 12, '2022-05-05', 1, 1);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('resistol', 5, '2022-09-20', 1, 1);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('agua', 7, '2022-07-07', 2, 2);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('papitas', 16, '2022-10-01', 2, 2);

INSERT INTO producto (nombre, cantidad, fecha_actualizacion, idProveedor, idCategoria)
VALUES ('cable', 1, '2022-06-14', 3, 3);

-- Consultas a la BD

-- Listar el nombre de los productos donde el nombre de categoria sea viaticos y la fecha de actualización del producto sea antes de septiembre.
SELECT P.nombre
FROM producto as P JOIN categoria as C ON P.idCategoria = C.id
WHERE C.nombre LIKE 'viaticos' AND EXTRACT(MONTH FROM P.fecha_actualizacion) <= '09';


-- Listar el nombre del producto y el nombre de categoría correspondiente al producto, que tengan más de 4 en cantidad, ordenados por cantidad
SELECT P.nombre, C.nombre AS "Categoria"
FROM producto AS P INNER JOIN categoria AS C ON P.idCategoria = C.id
WHERE P.cantidad > 4 ORDER BY P.cantidad;

-- Listar el nombre del proveedor donde la cantidad de productos sea mayor a 11, sin registros repetidos.
SELECT DISTINCT P.nombre, P.cantidad
FROM producto as P INNER JOIN categoria as C ON P.idCategoria = C.id
WHERE P.cantidad > 11;
