select s.user_id, ifnull(round(count(case when c.action = 'confirmed' then 1 end)/count(c.user_id),2),0) as confirmation_rate
from confirmations as c 
right join signups as s on c.user_id = s.user_id
group by 1