-- Script that creates a database usa and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);