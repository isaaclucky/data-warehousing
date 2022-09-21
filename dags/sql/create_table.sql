-- CREATE DATABASE IF NOT EXISTS `city_traffic`;
CREATE TABLE IF NOT EXISTS  'objects' (
   'track_id' INT Primary KEY,
   'type' varchar(20),
   'traveled_d' FLOAT,
   'avg_speed' FLOAT,
   'lat' FLOAT,
   'lon' FLOAT,
   'speed' FLOAT, 
   'lon_acc' FLOAT,
   'lat_acc' FLOAT,
   'time' FLOAT,
);