#This was My Attempt
-- SELECT user_id, ROUND(sum_c/(sum_c+sum_t),2)  IN (

-- SELECT s.user_id, SUM(action="timeout") as sum_t, SUM(action="confirmed") as sum_c   FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id GROUP BY s.user_id ) 
SELECT s.user_id, IFNULL(ROUND(SUM(action='confirmed')/COUNT(*),2),0) as confirmation_rate 
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id=c.user_id
GROUP BY s.user_id
