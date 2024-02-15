-- this checks if there is a table called force_name  before creating it

CREATE TABLE IF NOT EXISTS unique_id (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256)
);