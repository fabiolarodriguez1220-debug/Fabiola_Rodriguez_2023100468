-- Archivo: create_table_mysql.sql
CREATE TABLE contactos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  correo VARCHAR(255) NOT NULL,
  celular VARCHAR(50),
  horario VARCHAR(100)
);
