-- this checks the cities with the state of California
SELECT cities.id, cities.name FROM cities
WHERE cities.state_id
IN (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;