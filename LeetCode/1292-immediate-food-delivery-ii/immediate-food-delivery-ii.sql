select round(count(case when order_date = customer_pref_delivery_date then 1 end)*100/count(customer_id),2) as immediate_percentage
from (select customer_id, min(order_date) as order_date, min(customer_pref_delivery_date) as customer_pref_delivery_date
from delivery
group by customer_id) as temp