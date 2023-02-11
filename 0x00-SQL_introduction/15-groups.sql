-- List number of records with same 'score' in table 'second_table'
SELECT score 'score', COUNT(score) 'number' FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
-- '' label the records
