#1
create database Social_media;

#2
Select * from students_social_media_addiction;

#3
SELECT 
    Addicted_Score, ROUND(AVG(avg_daily_usage_hours), 2) AS avg_hours
FROM
    students_social_media_addiction
GROUP BY Addicted_Score
ORDER BY avg_hours DESC;

#4
SELECT 
    COUNT(Student_ID) AS No_of_Students_academic_performance_affected 
FROM
    students_social_media_addiction
WHERE
    Affects_Academic_Performance = 'Yes';
    
#5
SELECT 
    Addicted_Score,
    Affects_Academic_Performance,
    COUNT(*) AS total_students
FROM
    students_social_media_addiction
GROUP BY Addicted_Score , Affects_Academic_Performance
ORDER BY Addicted_Score;

#6
SELECT 
    Most_Used_Platform, COUNT(*) AS Students_Count
FROM
    students_social_media_addiction
GROUP BY Most_Used_Platform
ORDER BY user_count DESC;

#7
SELECT 
    Addicted_Score,
    ROUND(AVG(Sleep_Hours_Per_night), 2) AS avg_sleep
FROM
    students_social_media_addiction
GROUP BY Addicted_Score
ORDER BY Addicted_Score DESC;

#8
SELECT 
    CASE 
        WHEN Avg_Daily_Usage_Hours < 3 THEN 'Low Usage (0-3h)'
        WHEN Avg_Daily_Usage_Hours BETWEEN 3 AND 6 THEN 'Moderate Usage (3-6h)'
        ELSE 'High Usage (6h+)'
    END AS Usage_Tier,
    COUNT(*) AS Total_Students,
    ROUND(AVG(CASE WHEN Affects_Academic_Performance = 'Yes' THEN 1.0 ELSE 0.0 END) * 100,1) AS Percent_Affected_Academically,
    ROUND(AVG(Sleep_Hours_Per_Night), 2) AS Avg_Sleep
FROM students_social_media_addiction
GROUP BY 1
ORDER BY Avg_Sleep DESC;

#9
SELECT 
    Addicted_Score,
    ROUND(AVG(Mental_Health_Score)) AS Mental_health_level
FROM
    students_social_media_addiction
GROUP BY Addicted_Score
ORDER BY Addicted_Score DESC;

#10
SELECT 
    Student_ID,
    Avg_Daily_Usage_Hours,
    Addicted_Score,
    CASE
        WHEN Avg_Daily_Usage_Hours >= 6 THEN 'High Risk'
        WHEN Avg_Daily_Usage_Hours BETWEEN 3 AND 5.9 THEN 'Moderate Risk'
        ELSE 'Low Risk'
    END AS usage_risk_category
FROM
    students_social_media_addiction;

#11
SELECT usage_risk_category, COUNT(*) AS total_students
FROM (
    SELECT
        CASE
            WHEN  Avg_Daily_Usage_Hours >= 6 THEN 'High Risk'
            WHEN  Avg_Daily_Usage_Hours BETWEEN 3 AND 5.9 THEN 'Moderate Risk'
            ELSE 'Low Risk'
        END AS usage_risk_category
    FROM students_social_media_addiction
) temp_table
GROUP BY usage_risk_category;