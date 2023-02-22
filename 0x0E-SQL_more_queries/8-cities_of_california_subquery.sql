-- Script that lists all cities in california
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.id = states.id
ORDER BY cities.id ASC;