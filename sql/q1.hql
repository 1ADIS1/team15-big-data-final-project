USE team15_projectdb;


-- q1
SELECT 
US_state,
COUNT(entry_ID) as total_vehicles
FROM car_vehicles_ext_part_bucket
GROUP BY US_state
ORDER BY total_vehicles avsc
LIMIT 15;