-- List all cities contained in the database, displayinf the id name and state
-- database: hbtn_0d_usa, table name: cities
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
