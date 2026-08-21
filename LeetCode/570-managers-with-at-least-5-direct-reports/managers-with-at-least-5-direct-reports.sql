select m.name
from employee as e join employee as m on e.managerid = m.id
group by 1, m.id
having count(e.id) >= 5