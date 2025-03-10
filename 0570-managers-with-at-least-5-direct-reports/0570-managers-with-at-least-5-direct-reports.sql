# Write your MySQL query statement below
select a.name
from Employee a
join Employee b
where a.id = b.managerId
group by b.managerId
having count(*) >= 5