-- CREATE DATABASE IF NOT EXISTS `city_traffic`;
CREATE TABLE IF NOT EXISTS  traffic_data (
   track_id INT PRIMARY KEY,
   type varchar(20),
   traveled_d FLOAT,
   avg_speed FLOAT,
   lat FLOAT,
   lon FLOAT,
   speed FLOAT, 
   lon_acc FLOAT,
   lat_acc FLOAT,
   time FLOAT
);