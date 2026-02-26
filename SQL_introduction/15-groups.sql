-- here is script that prints the score and the number of students with that score, 
-- sorted by score from the highest to the lowest
SELECT score, COUNT(score) AS count
FROM second_table
GROUP BY score
ORDER BY score DESC;
