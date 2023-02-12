-- Create the MySQL server user 'user_0d_1'
-- Had to make password 'User_0d_1_pwd' in server to satisfy system
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
