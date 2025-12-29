WITH ranked AS (
SELECT e.id, e.name AS Employee, e.salary, e.departmentId,
DENSE_RANK() OVER (PARTITION BY e.departmentId 
ORDER BY e.salary DESC
) AS rnk
FROM Employee e)

SELECT d.name AS Department, r.Employee, r.salary
FROM ranked as r
JOIN Department as d ON r.departmentId = d.id
WHERE r.rnk <= 3;
