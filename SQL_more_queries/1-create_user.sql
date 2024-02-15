-- Create the user (if it doesn't exist) and set the password
CREATE USER 'user_0d_1'@'localhost' IF NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on the entire server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

--SELECT IFNULL(COUNT(*), 0) as user_exists
--FROM mysql.user
--WHERE User = 'user_0d_1';
