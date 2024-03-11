SELECT name, per_pupil_expenditure, graduated
FROM districts
JOIN expenditures ON districts.id=expenditures.district_id
JOIN schools ON districts.id=schools.district_id
JOIN graduation_rates ON graduation_rates.school_id =schools.id
ORDER BY per_pupil_expenditure DESC, schools.name;
