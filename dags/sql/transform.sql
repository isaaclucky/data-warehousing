select distinct(type), SUM(avg_speed), AVG(traveled_d), count(type)
from public.traffic_data
GROUP BY type;