# Write your MySQL query statement below
with TotalUsers as(
    select count(*) total_users from Users
)
select r.contest_id,
ROUND(COUNT(r.user_id)*100.0/tu.total_users,2) as percentage
from Register r
join TotalUsers tu
group by r.contest_id 
order by percentage desc ,contest_id asc;