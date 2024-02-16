SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- Create the user if it does not exist
-- User already exists
SET @create_user_query = IF(@user_exists = 0, 'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';', 'SELECT status;');
PREPARE stmt FROM @create_user_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant privileges only if the user was just created
-- User already exists, no privileges granted
SET @grant_privileges_query = IF(@user_exists = 0, 'GRANT ALL PRIVILEGES ON *.* TO \'user_0d_1\'@\'localhost\';', 'SELECT status;');
PREPARE stmt FROM @grant_privileges_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Reload the privileges
-- FLUSH PRIVILEGES;
