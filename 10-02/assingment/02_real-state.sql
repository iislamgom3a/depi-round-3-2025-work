create database RealState;

USE RealState; 


create table Employee (
emp_id int auto_increment primary key, 
emp_name varchar(40),
office_id int 
);

create table SalesOffice (
office_id int auto_increment primary key, 
location varchar(40),
manager_id int 
);

create table Porperty(
porperty_id int auto_increment primary key, 
city varchar(40),
state varchar(40),
zip varchar(40),
manager_id int, 
office_id int 
);


alter table Employee 
add constraint office_employee_fk foreign key (office_id) references SalesOffice(office_id);

alter table  SalesOffice
add constraint manager_fk foreign key (manager_id) references Employee(emp_id);

alter table Porperty
add constraint office_property_fk  foreign key (office_id) references SalesOffice(office_id);


create table Owner(
owner_id int auto_increment primary key, 
owner_name varchar(40)
);

create table PropertyOwner(
prob_id int, 
owner_id int, 
percent_owned int check(percent_owned between 0 and 100)
);

alter table PropertyOwner
add constraint many_property_fk  foreign key (prob_id) references Porperty (porperty_id);

alter table PropertyOwner
add constraint many_owner_fk  foreign key (owner_id) references Owner(owner_id);

---------------------------------------
-- Insert dummies 
---------------------------------------

-- Insert into SalesOffice table
USE RealState;

INSERT INTO SalesOffice (location) 
VALUES 
('New York'), 
('Chicago'), 
('Austin');

INSERT INTO Employee (emp_name, office_id) 
VALUES 
('Alice Smith', 1),
('Bob Johnson', 2),
('Charlie Lee', 3),
('David Brown', 1),
('Eva Green', 2);

UPDATE SalesOffice SET manager_id = 1 WHERE office_id = 1;
UPDATE SalesOffice SET manager_id = 2 WHERE office_id = 2;
UPDATE SalesOffice SET manager_id = 3 WHERE office_id = 3;

INSERT INTO Owner (owner_name) 
VALUES 
('Mike Davis'),
('Sarah Wilson'),
('Tom King'),
('Laura White');

INSERT INTO Porperty (city, state, zip, office_id) 
VALUES 
('New York', 'NY', '10001', 1),
('Brooklyn', 'NY', '11201', 1),
('Chicago', 'IL', '60601', 2),
('Austin', 'TX', '78701', 3),
('Dallas', 'TX', '75201', 3);

INSERT INTO PropertyOwner (prob_id, owner_id, percent_owned) 
VALUES 
(1, 1, 60),
(1, 2, 40),
(2, 2, 100),
(3, 3, 100),
(4, 4, 100),
(5, 1, 100);

---------------------------------------
-- Query Examples
---------------------------------------

-- Basic SELECT 


SELECT emp_name
FROM `Employee`
WHERE office_id = (
    SELECT office_id
    From `SalesOffice`
    WHERE location = 'New York'
);

SELECT * FROM `Porperty` 
WHERE city = 'Chicago'; 

-- JOINS 

-- Show properties and their managing office location.
SELECT p.*, s.location as "Managing Office Loaction"
FROM `Porperty` as p  
JOIN `SalesOffice` as s 
ON p.office_id = s.office_id ; 

--  List owners with the properties they own.

SELECT o.*, p.*, po.percent_owned 
FROM `PropertyOwner` as po
INNER JOIN `Porperty` as p
ON p.porperty_id = po.prob_id
INNER JOIN `Owner` as o 
ON o.owner_id = po.owner_id;  


--- Aggregations

-- Count how many employees are in each office
SELECT 
    s.office_id,
    s.location, 
    COUNT (e.emp_id) as "Employee Count"
FROM `Employee` as e  
JOIN `SalesOffice` as s ON s.office_id = e.office_id
GROUP BY s.location, s.office_id; 


-- Find average number of properties per office.
SELECT 
    (SELECT COUNT(*) FROM `Porperty`) / (SELECT COUNT(*) FROM `SalesOffice`);


-- Constrians 

-- o Make sure every property is linked to exactly one office.
SELECT * FROM Porperty 
WHERE office_id IS NULL;

-- o Show employees not assigned as managers.
SELECT e.*, s.manager_id 
FROM `SalesOffice` as s
RIGHT JOIN `Employee` as e
ON s.manager_id = e.emp_id
WHERE s.manager_id IS NULL; 


-- Subqueries

-- Find offices that have more properties than the average office.

SELECT office_id, COUNT(office_id) > (
    SELECT COUNT(*) FROM `Porperty`) / (SELECT COUNT(*) FROM `SalesOffice`
) as 'Above AVG'
FROM `Porperty` GROUP BY office_id ;


-- o Find owners who own more than one property.
SELECT owner_id, owner_name
FROM Owner
WHERE owner_id IN (
    SELECT owner_id
    FROM `PropertyOwner` 
    GROUP BY owner_id
    HAVING COUNT(owner_id) > 1
);


-- Views

-- Create a view office_summary showing office_id, city, num_employees, num_properties.

CREATE VIEW office_summary  
AS 
SELECT 
    s.office_id, 
    s.location, 
    COUNT(DISTINCT e.emp_id) AS "Employee Count",
    COUNT(DISTINCT p.porperty_id) AS "Property Count"
FROM
    `SalesOffice` as s
LEFT JOIN 
    `Employee` as e ON s.office_id = e.office_id
LEFT JOIN 
    `Porperty` as p On s.office_id = p.office_id
GROUP BY
    s.office_id, s.location; 


-- Indexes
-- Add an index on Property(city) for faster searching. 

CREATE INDEX idx_property_ciy ON Porperty (city); 

-- Transaction

-- Simulate selling a property:
-- START TRANSACTION → delete ownership rows for a property → insert new
-- owner → COMMIT.

START TRANSACTION; 
UPDATE `PropertyOwner` SET owner_id = 2 
WHERE owner_id = 1 && prob_id = 1;
COMMIT; 
