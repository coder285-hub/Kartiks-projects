SELECT districts.name, expenditures.per_pupil_expenditure,staff_evaluations.exemplary FROM districts
JOIN expenditures ON district.id = expenditures.district_id
JOIN staff_evaluations ON staff_evaluation.district_id = district_id
WHERE districts.type ="Public School District" 
