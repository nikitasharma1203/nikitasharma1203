select max(distinct salary) as SecondHighestSalary
from Employee 
where salary < (select max(distinct salary)
from Employee)