select p.project_id, round(avg(e.experience_years),2) as average_years
from project as p
join employee as e on e.employee_id = p.employee_id
GROUP BY project_id