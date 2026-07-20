select max(num) as num
from (select num
from mynumbers
group by 1
having count(num) = 1)as wind