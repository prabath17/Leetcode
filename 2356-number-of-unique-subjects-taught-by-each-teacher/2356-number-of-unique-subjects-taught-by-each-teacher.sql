# Write your MySQL query statement below

select teacher_id, count(DISTINCT subject_id) cnt
from Teacher
-- where teacher_id <> subject_id
group by teacher_id