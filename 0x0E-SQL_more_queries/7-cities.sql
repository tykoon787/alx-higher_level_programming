-- Script that creates the cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(state_id)
);