DROP DATABASE trackxpense;
CREATE DATABASE IF NOT EXISTS trackxpense;
CREATE USER IF NOT EXISTS `root`@'localhost' IDENTIFIED BY 'aloh';
GRANT ALL PRIVILEGES ON `trackxpense`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;