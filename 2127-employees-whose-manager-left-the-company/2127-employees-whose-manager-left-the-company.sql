SELECT employee_id FROM Employees as e1
WHERE manager_id not in (SELECT employee_id FROM employees) and salary < 30000
ORDER BY employee_id ASC