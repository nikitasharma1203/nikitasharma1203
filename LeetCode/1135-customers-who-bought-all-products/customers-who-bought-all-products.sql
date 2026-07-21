select c.customer_id 
from customer as c 
join product as p on c.product_key = p.product_key
group by 1
having count(distinct c.product_key) = (select count(product_key) from product)