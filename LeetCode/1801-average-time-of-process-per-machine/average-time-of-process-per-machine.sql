select a.machine_id, round(sum(b.timestamp - a.timestamp)/ count(a.process_id),3) as processing_time
from activity as a 
join activity as b
on a.machine_id = b.machine_id and a.process_id = b.process_id
where a.activity_type ='start' and b.activity_type ='end'
group by 1