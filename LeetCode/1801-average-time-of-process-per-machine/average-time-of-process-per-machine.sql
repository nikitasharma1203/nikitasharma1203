select a.machine_id, round(avg(b.timestamp - a.timestamp),3) as processing_time
from activity as a join activity as b on a.machine_id = b.machine_id
where b.activity_type = 'end' and a.activity_type = 'start'
group by 1