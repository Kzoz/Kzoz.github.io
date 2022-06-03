with counter as (select count(*) as count from Seat)

select 
case 
when Seat.id%2 = 0 then (Seat.id)-1
when Seat.id%2 = 1 and Seat.id =  counter.count then Seat.id
else (Seat.id)+1
end as id,
Seat.student 
from Seat, counter
order by id asc;