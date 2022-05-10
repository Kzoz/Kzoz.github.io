SELECT user_id, 
CONCAT(UPPER(SUBSTRING(name,1,1)),
LOWER(SUBSTRING(name,2))) AS Name 
FROM Users
order by 1;