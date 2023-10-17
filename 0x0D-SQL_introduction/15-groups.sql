--Script to List Number of Records with the Same Score
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;