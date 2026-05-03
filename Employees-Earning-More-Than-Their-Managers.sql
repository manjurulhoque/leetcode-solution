1SELECT e.name AS Employee
2FROM Employee e
3JOIN Employee m ON e.managerId = m.id
4WHERE e.salary > m.salary;
5