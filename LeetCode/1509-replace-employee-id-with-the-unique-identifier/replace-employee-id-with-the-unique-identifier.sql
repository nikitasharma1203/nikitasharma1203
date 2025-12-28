select unique_id, name 
from Employees as E 
LEFT Join EmployeeUNI as EU on E.id = EU.id
