select e2.employee_id, e2.name, count(distinct e1.employee_id) as reports_count, round(avg(e1.age)) as average_age
from employees as e1 
join employees as e2 on e1.reports_to = e2.employee_id
group by 1,2
having count(e1.employee_id) >=1
order by 1