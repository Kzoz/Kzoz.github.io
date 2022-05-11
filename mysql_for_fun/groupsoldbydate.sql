select sell_date, count(distinct product) as 'num_sold',
group_concat(distinct product order by product asc separator ',') 
as 'products'
from Activities
group by 1
order by 1;