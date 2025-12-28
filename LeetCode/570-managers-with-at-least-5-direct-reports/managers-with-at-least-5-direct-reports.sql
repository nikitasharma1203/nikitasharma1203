SELECT e.name
FROM employee AS e
JOIN employee AS r
  ON e.id = r.managerId
GROUP BY e.id
HAVING COUNT(r.id) >= 5;
