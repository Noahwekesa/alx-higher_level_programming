
-- Script to Create the unique_id Table
CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256),
  PRIMARY KEY (id),
  UNIQUE KEY (id)
) ENGINE=InnoDB;