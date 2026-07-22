select r.contest_id, round(count(distinct r.user_id)*100/(select count(user_id) from users),2) as percentage
from users as u join register as r on u.user_id = r.user_id
group by 1
order by 2 desc, 1 asc