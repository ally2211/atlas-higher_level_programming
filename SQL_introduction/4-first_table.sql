-- this checks if there is a table called first_table before creating it

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
