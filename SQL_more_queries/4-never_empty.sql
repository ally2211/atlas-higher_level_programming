-- this checks if there is a table called force_name  before creating it

CREATE TABLE IF NOT EXISTS id_not_null   (
  id INT DEFAULT 1,
  name VARCHAR(256)
);