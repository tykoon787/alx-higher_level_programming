-- Script that creates a user
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS;
GRANT ALL
ON *.*
TO 'user_0d_1'@'localhost';