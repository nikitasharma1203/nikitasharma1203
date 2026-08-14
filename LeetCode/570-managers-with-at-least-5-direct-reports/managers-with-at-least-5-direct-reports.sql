select e1.name 
from employee as e join employee as e1 on e.managerId = e1.id
group by 1, e1.id
having count(e.id) >= 5