SELECT "year", ROUND(AVG("salary"), 2) AS "average salaries" FROM "Salaries"
GROUP BY "year"
ORDER BY "year" DESC;
