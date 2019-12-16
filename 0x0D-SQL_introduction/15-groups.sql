-- lists the number of records with the same score in the table
-- table: second_table, order by score, database: hbtn_0c_0
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
