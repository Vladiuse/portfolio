{%load code%}
{%lang 'sql'%}
DROP TABLE IF EXISTS product;

CREATE TABLE product
(id SERIAL PRIMARY KEY,
name CHAR(10) NOT NULL,
price INT NOT NULL DEFAULT 0);

INSERT INTO product (name, price)
VALUES ('one', 10),('two', 100),('three', 20),('four', 670),('five', 55);

SELECT 
CASE
    WHEN price > 60 THEN 'high_price'
    WHEN price > 50 THEN 'midle_price'
    ELSE 'low_price'
END AS price_grade
,COUNT(name) as count
FROM product GROUP BY price_grade;
{%end%}
<pre>
 price_grade | count 
-------------+-------
 high_price  |     2
 low_price   |     2
 midle_price |     1
</pre>