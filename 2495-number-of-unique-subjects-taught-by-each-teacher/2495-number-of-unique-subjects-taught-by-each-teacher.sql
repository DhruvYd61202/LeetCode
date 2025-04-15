# Write your MySQL query statement below
select teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher GROUP BY teacher_id;

--     result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
--     result.rename(columns={'subject_id': 'cnt'}, inplace=True)
    