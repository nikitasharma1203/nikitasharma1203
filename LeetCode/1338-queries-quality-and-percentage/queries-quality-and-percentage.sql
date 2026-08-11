select query_name, round(avg(rating/position),2) as quality, round(count(case when rating < 3 then 1 end)*100/count(query_name),2) as poor_query_percentage
from queries
group by 1