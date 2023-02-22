-- Script that creates a database usa and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY NOT NULL AUTO_INCRIMENT,
    name VARCHAR(256) NOT NULL
);