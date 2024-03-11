SELECT name, per_pupil_expenditure
FROM districts
JOIN expenditures ON expenditures.district_id=districts.id
WHERE type LIKE "%Public School%"
ORDER BY per_pupil_expenditure DESC;
