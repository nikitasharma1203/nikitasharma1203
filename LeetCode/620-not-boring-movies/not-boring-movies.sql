-- Write your PostgreSQL query statement below
select id, movie, description, rating
from cinema
where description != 'boring' and id%2 = 1
order by 4 desc