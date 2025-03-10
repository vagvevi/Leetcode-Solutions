# Write your MySQL query statement below
delete p
from Person p,Person q
where p.id>q.id
and q.Email = p.Email