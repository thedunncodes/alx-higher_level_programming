-- This lists all the names and scores in the second_table
-- where score is greater than or equal to 10.
-- Results are sorted by score in descending order.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC
