# Write your MySQL query statement below
select machine_id,
ROUND(AVG(end_time - start_time),3) AS processing_time
from (
    select machine_id,process_id,
    MAX(CASE WHEN activity_type = 'end' then timestamp end) as end_time,
    MAX(CASE WHEN activity_type = 'start' then timestamp end ) as start_time
    from Activity
    GROUP BY machine_id,process_id
)
as process_times
group by machine_id;