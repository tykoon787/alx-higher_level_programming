-- Script that creates a database and grants select privilege to the user
CREATE DATABASE IF NOT EXISTS hbtn_02;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_02.*
TO 'user_0d_2'@'localhost';