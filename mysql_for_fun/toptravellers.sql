select name, IFNULL(sum(distance),0) as travelled_distance
from users
left join Rides
on Users.id = Rides.user_id
group by 1
order by 2 desc, 1;