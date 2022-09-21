ALTER ROLE postgres;
COPY objects('track_id', 'type','traveled_d', 'avg_speed', 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time')
FROM 'd1_0830_0900.csv'
DELIMITER ','
CSV HEADER;