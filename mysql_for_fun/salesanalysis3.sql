select Product.product_id, product_name
from Product
left join Sales
on Product.product_id = Sales.product_id
group by Product.product_id
having min(Sales.sale_date) >= '2019-01-01'
and max(Sales.sale_date) <= '2019-03-31'