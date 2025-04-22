# Write your MySQL query statement below
WITH RunningTotal AS(
    SELECT person_id, person_name, weight, turn, SUM(weight) OVER (ORDER BY turn) AS running_total_weight
    FROM queue
)
SELECT person_name
FROM `RunningTotal`
WHERE running_total_weight <= 1000
ORDER BY running_total_weight DESC LIMIT 1