SELECT h.hacker_id, H.name, sum(score) AS total_score
FROM Hackers AS h INNER JOIN(
    SELECT hacker_id,  max(score) AS score 
    FROM submissions 
    GROUP BY challenge_id, hacker_id
) AS Max_score
ON h.hacker_id = Max_score.hacker_id
GROUP BY h.hacker_id, name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id ASC;