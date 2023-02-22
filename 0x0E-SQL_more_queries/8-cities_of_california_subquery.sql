-- Script that lists all cities in california
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.id = states.id
    AND states.name = 'California'
ORDER BY cities.id ASC;