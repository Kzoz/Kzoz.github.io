select Ft.name as 'Employee'
from Employee as Ft, Employee as St
where Ft.managerId = St.id and Ft.salary > St.salary;
