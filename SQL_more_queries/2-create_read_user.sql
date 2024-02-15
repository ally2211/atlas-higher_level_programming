-- create a new database
-- cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user='user_0d_2' AND host='localhost');

IF NOT EXISTS(SELECT 1 FROM mysql.user WHERE user='user_0d_2' AND host='localhost') THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
END IF;
GRANT SELECT ON hbtn_0c_2.* TO 'user_0d_2'@'localhost';