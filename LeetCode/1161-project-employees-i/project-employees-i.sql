-- Write your PostgreSQL query statement below
select project.project_id, round(sum(employee.experience_years)*1.0/count(project.employee_id),2) as average_years
from project join employee on project.employee_id = employee.employee_id
group by 1