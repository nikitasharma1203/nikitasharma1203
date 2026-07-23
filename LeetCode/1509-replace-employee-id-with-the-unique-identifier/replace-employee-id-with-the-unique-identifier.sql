select unique_id, name
from employees as e
left join employeeuni as eu on eu.id = e.id