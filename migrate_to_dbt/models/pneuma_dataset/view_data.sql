-- select distinct(traffic_data." type"), SUM(traffic_data." avg_speed"), AVG(traffic_data." traveled_d"), count(traffic_data." type")
-- from public.traffic_data
-- GROUP BY traffic_data." type"
select * from traffic_data