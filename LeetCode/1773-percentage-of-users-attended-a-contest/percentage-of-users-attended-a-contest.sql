select r.contest_id, round(count(r.user_id)*100/(select count(*) from users),2) percentage
from users as u join register as r on u.user_id = r.user_id
group by 1
order by 2 desc ,1 