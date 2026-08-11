select a.machine_id, round(avg(b.timestamp - a.timestamp),3) processing_time
from activity as a join activity as b on a.machine_id = b.machine_id
where a.activity_type = 'start' and b.activity_type = 'end'
group by 1