with t1 as (
select Employees.employee_id, Employees.name, Salaries.salary
    from Employees
    left join Salaries
    on Employees.employee_id = Salaries.employee_id
        union all
        select Salaries.employee_id, Employees.name, Salaries.salary
        from Employees
        right join Salaries
        on Employees.employee_id = Salaries.employee_id
        where Employees.name is null
    
)
select employee_id from t1
where name is null 
or salary is null
order by 1 asc;

/* ---------------------   An alternative ↓  ---------------------*/

select employee_id from Employees 
where employee_id 
not in (select employee_id from salaries)
UNION 
select employee_id from salaries 
where employee_id 
not in (select employee_id from employees)
order by employee_id asc