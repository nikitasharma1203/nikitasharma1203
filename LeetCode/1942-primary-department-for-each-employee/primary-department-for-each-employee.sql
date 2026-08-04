select employee_id, department_id
from employee
where primary_flag = 'Y' or employee_id in (select employee_id
from employee
group by 1
having count(*) = 1)