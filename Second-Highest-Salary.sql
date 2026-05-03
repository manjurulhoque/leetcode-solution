1SELECT (
2  SELECT DISTINCT salary
3  FROM Employee
4  ORDER BY salary DESC
5  LIMIT 1 OFFSET 1
6) AS SecondHighestSalary;