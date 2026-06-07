select max(distinct salary) as SecondHighestSalary
from employee
where salary < (select max(distinct salary) from employee)