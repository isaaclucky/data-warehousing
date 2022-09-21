select distinct(type1), SUM(avg_speed), AVG(traveled_d), count(type1)
from public.objects
GROUP BY type1