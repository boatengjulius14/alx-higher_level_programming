-- Write a script that lists all recores of the table second_table
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
