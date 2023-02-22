-- Script that creates a table whose Id should not be null
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR (256)
);