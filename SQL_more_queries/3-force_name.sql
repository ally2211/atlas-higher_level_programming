-- this checks if there is a table called force_name  before creating it

CREATE TABLE IF NOT EXISTS force_name  (
  id INT,
  name VARCHAR(256)
);