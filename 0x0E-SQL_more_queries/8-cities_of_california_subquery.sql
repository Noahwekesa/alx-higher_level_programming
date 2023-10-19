-- Script to List Cities of California in the hbtn_0d_usa Database

SELECT cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;