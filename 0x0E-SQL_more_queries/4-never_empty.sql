-- Creates a table with a description where a value can not be null
-- table name: id_not_null; description: id INT with default value 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1 NOT NULL, name VARCHAR(256));
