-- Creating a database and an user that only have the SELECT privilege in the database
-- user name: user_0d_2; passwd: user_0d_2_pwd; database: hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
