select m.employee_id, m.name, count(distinct e.employee_id) as reports_count,round(avg(e.age)) as average_age
from employees as e
join employees as m on e.reports_to = m.employee_id
group by 1, 2
order by 1