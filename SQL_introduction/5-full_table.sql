SET @db_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Generate CREATE TABLE statement for the specified table
SELECT CONCAT('CREATE TABLE `', @table_name, '` (\n',
  GROUP_CONCAT(
    CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE,
      IF(IS_NULLABLE = 'YES', ' DEFAULT NULL', ' NOT NULL'),
      IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT \'', COLUMN_DEFAULT, '\''), ''),
      IF(EXTRA != '', CONCAT(' ', EXTRA), ''),
      '\n'
    ) ORDER BY ORDINAL_POSITION ASC SEPARATOR ','),
  ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;') AS CreateTableStatement
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = @db_name AND TABLE_NAME = @table_name
GROUP BY TABLE_NAME;

