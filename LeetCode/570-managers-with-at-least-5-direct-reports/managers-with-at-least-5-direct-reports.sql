SELECT e2.name
FROM employee AS e1
JOIN employee AS e2
  ON e2.id = e1.managerId
GROUP BY e2.id
HAVING COUNT(e1.id) >= 5;