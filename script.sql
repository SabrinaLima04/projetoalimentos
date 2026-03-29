CREATE DATABASE IF NOT EXISTS db_alimentos;
USE db_alimentos;

CREATE TABLE IF NOT EXISTS alimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod VARCHAR(8) UNIQUE NOT NULL,
    sec INT(4) ZEROFILL NOT NULL,
    grupo_id VARCHAR(1) NOT NULL,
    tipo_alimento CHAR(1) NOT NULL,
    pais VARCHAR(2) NOT NULL
);

SELECT*FROM alimentos;



