SELECT 
DATE_FORMAT(trans_date, "%Y-%m") as month, country, COUNT(state) as trans_count, COUNT(CASE WHEN state="approved" THEN state END) as approved_count, SUM(amount) AS trans_total_amount  , SUM(CASE WHEN state="approved" THEN amount ELSE 0 END) AS approved_total_amount 
FROM transactions
GROUP BY month, country