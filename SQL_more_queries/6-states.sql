-- this checks if there is a table called force_name  before creating it

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL
);