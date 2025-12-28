WITH PlayerActivity AS (
    SELECT 
        player_id,
        event_date,
        LEAD(event_date) OVER (
            PARTITION BY player_id 
            ORDER BY event_date
        ) AS next_date,
        MIN(event_date) OVER (
            PARTITION BY player_id
        ) AS first_date
    FROM Activity
),
NextDayPlayers AS (
    SELECT DISTINCT player_id
    FROM PlayerActivity
    WHERE next_date = DATE_ADD(first_date, INTERVAL 1 DAY)
)
SELECT 
    ROUND(
        COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM NextDayPlayers;
