COPY traffic_data(track_id, type,traveled_d, avg_speed, lat, lon, speed, lon_acc, lat_acc, time)
FROM '/data/d1_0830_0900.csv'
DELIMITER ','
CSV HEADER;