-- Script that lists all cities in california
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = "California"
ORDER BY cities.id ASC;