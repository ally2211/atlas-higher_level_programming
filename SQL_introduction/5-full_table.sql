-- Retrieve table information from the INFORMATION_SCHEMA database

SET @table_name = 'first_table';

-- Generate CREATE TABLE statement for the specified table
SELECT @table_name AS 'Table',
CONCAT('CREATE TABLE `first_table` (\n',
GROUP_CONCAT(CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE, IF(IS_NULLABLE = 'YES', ' DEFAULT NULL', ''), '\n')),
') ENGINE=InnoDB DEFAULT CcHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci') AS 'Create Table'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = @table_name