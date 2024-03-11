SELECT districts.name, expenditures.per_pupil_expenditure,staff_evaluations.exemplary FROM districts
JOIN expenditures ON district.id
