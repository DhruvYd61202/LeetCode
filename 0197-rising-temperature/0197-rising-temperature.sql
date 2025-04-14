SELECT w1.id as Id FROM Weather w1, Weather w2
WHERE (dateDiff(w1.recordDate, w2.recordDate) = 1) and w1.temperature > w2.temperature