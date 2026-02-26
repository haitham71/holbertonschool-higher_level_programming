-- here is script that prints the score and the name of all students,
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;