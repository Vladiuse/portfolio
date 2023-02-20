
{%load code%}
{%lang 'sql'%}
-- 2 tables
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS abs_user;

CREATE TABLE abs_user(user_id SERIAL PRIMARY KEY,
login CHAR(30) NOT NULL UNIQUE,
email CHAR(30) NOT NULL UNIQUE);

CREATE TABLE employee(user_id INT REFERENCES abs_user(user_id) NOT NULL UNIQUE,
name CHAR(30) NOT NULL,
CHECK (name != ''));

INSERT INTO abs_user
(login, email) VALUES ('vladiuse', 'vladiuse@gmail.com');

INSERT INTO employee
(user_id,name) VALUES 
((SELECT user_id FROM abs_user WHERE login = 'vladiuse'),'Vlad');

-- one table

DROP TABLE IF EXISTS employee;
CREATE TABLE employee
(id SERIAL PRIMARY KEY,
name CHAR(20),
manager INT REFERENCES employee(id));
{%end%}




