select customer_id
from customer as c 
join product as p on p.product_key = c.product_key
group by 1
having count(distinct c.product_key) = (select count(*) from product)