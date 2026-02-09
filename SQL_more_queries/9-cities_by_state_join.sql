-- mysql comment
-- Şəhərləri və onlara uyğun ştat adlarını birlikdə göstərir
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
