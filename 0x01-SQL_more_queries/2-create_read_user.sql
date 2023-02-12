-- Create the database 'hbtn_0d_2' and the MySQL server user 'user_0d_2'
-- Had to make password 'User_0d_2_pwd' in server to satisfy system
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
