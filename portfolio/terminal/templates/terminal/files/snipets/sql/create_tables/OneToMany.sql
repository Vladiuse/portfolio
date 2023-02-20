{%load code%}

{%lang 'sql'%}
DROP TABLE IF EXISTS position;
DROP TABLE IF EXISTS employee;

CREATE TABLE position (id SERIAL PRIMARY KEY,
name CHAR(20) UNIQUE NOT NULL);

CREATE TABLE employee (id SERIAL PRIMARY KEY,
name CHAR(20) NOT NULL,
position INT REFERENCES position(id));
{%end%}

