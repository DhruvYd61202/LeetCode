#using the IN operator
-- select name from employee where id in
-- (
-- select managerId
-- from employee
-- group by managerId
-- having count(*) >= 5

-- )

#Can Also be done using join function
#Need to understand this how this is working?

#Using the join operator
SELECT Name FROM Employee WHERE Id IN 

(SELECT ManagerId from employee GROUP BY ManagerId
HAVING (COUNT(DISTINCT Id) >=5 ))