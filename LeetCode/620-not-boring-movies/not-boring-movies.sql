select id, movie, description, rating
from cinema as c
where description != 'boring' and id%2 !=0
order by 4 desc
