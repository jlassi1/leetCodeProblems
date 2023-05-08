# Write your MySQL query statement below
select  EmployeeUNI.unique_id, Employees.name from Employees
LEFT JOIN EMPLOYEEUNI 
ON EmployeeUNI.id = Employees.id;

