update Salary
set sex = 
CASE
  WHEN sex = "m" THEN "f"
  ELSE "m"
 END;

 

UPDATE Salary
SET sex = IF(sex = "m", "f", "m");