-- Write your PostgreSQL query statement below
select e2.name
from employee as e1
join employee as e2 on e1.managerId = e2.id
group by e2.id, 1
having count(e1.id) >= 5