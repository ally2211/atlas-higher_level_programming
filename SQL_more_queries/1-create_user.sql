SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- Create the user if it does not exist
SET @create_user_query = IF(@user_exists = 0, 'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';', 'SELECT \'User already exists\' status;');
PREPARE stmt FROM @create_user_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant privileges only if the user was just created
SET @grant_privileges_query = IF(@user_exists = 0, 'GRANT ALL PRIVILEGES ON *.* TO \'user_0d_1\'@\'localhost\' WITH GRANT OPTION;', 'SELECT \'User already exists, no privileges granted\' status;');
PREPARE stmt FROM @grant_privileges_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Reload the privileges
-- FLUSH PRIVILEGES;
