create database yoo;
use yoo;

CREATE TABLE customers (
  customer_id     INT PRIMARY KEY,
  name            VARCHAR(50) NOT NULL,
  email           VARCHAR(120),
  city            VARCHAR(60),
  signup_at_utc   DATETIME
);

CREATE TABLE orders (
  order_id        INT PRIMARY KEY,
  customer_id     INT,
  order_code      VARCHAR(10) NOT NULL,
  status          VARCHAR(20) NOT NULL,
  total_amount    DECIMAL(10,2) NOT NULL,
  placed_at_utc   DATETIME NOT NULL,
  INDEX idx_orders_customer_id (customer_id)
);

INSERT INTO customers (customer_id, name, email, city, signup_at_utc) VALUES
(101, 'Aisha',  'aisha@demo.com',  'Delhi',     '2026-01-01 10:00:00'),
(102, 'Rohan',  'rohan@demo.com',  'Mumbai',    '2026-01-02 11:00:00'),
(103, 'Meera',  'meera@demo.com',  NULL,        '2026-01-03 12:00:00'),
(104, 'Arjun',  'arjun@demo.com',  'Delhi',     '2026-01-04 13:00:00'),
(106, 'Neha',   'neha@demo.com',   'Pune',      '2026-01-05 09:30:00'),
(107, 'Ishaan', 'ishaan@demo.com', 'Bengaluru', '2026-01-06 18:10:00'),
(108, 'Riya',   NULL,              'Delhi',     '2026-01-07 07:45:00'),
(109, 'Aisha',  'aisha2@demo.com', 'Jaipur',    '2026-01-08 20:00:00');

INSERT INTO orders (order_id, customer_id, order_code, status, total_amount, placed_at_utc) VALUES
(1, 101, 'A', 'PAID',      499.00, '2026-01-10 10:00:00'),
(2, 102, 'B', 'PAID',      299.00, '2026-01-10 11:00:00'),
(3, 105, 'C', 'PAID',      199.00, '2026-01-10 12:00:00'),
(4, 101, 'D', 'CANCELLED', 999.00, '2026-01-11 09:00:00'),
(5, 106, 'E', 'PAID',      799.00, '2026-01-11 10:30:00'),
(6, 106, 'F', 'PENDING',   149.00, '2026-01-12 08:20:00'),
(7, NULL,'G', 'PAID',      249.00, '2026-01-12 09:10:00'),
(8, 999, 'H', 'PAID',      129.00, '2026-01-12 15:40:00');

-- all details with left join	
select * from customers as c
left join orders as o
on c.customer_id=o.customer_id;

-- right join
select c.city from customers as c
right join orders as o
on c.customer_id=o.customer_id;

-- inly PAID as status
select * from customers as c
left join orders as o
on c.customer_id=o.customer_id
where o.status='PAID';

-- only the details of the orders in delhi
select * from customers as c
join orders as o
on c.customer_id=o.customer_id and c.city='Delhi';

-- Show every order we received, and attach customer name if we know it.
select name,o.order_id,o.customer_id,o.order_code,o.status,o.total_amount ,o.placed_at_utc from customers as c
right join orders as o
on c.customer_id=o.customer_id;

-- FULL JOIN
select * from customers as c
left join orders as o
on c.customer_id=o.customer_id
union 
select * from customers as c 
right join orders as o
on c.customer_id=o.customer_id;




create table student
(
id int primary key,
name varchar(50)
);

insert into student
values
(1,'ASHA'),
(2,'RAVI'),
(3,'NEHA'),
(4,'RAJ');

create table payments
(
id int primary key,
amt varchar(50)
);

insert into payments
values
(1,500),
(2,700),
(4,800);	

select s.id,s.name,p.amt from student as s
left join payments as p
on s.id=p.id;

select s.id,s.name,p.amt from student as s
right join payments as p
on s.id=p.id;

select s.id,s.name,p.amt from student as s
left join payments as p
on s.id=p.id
union 
select s.id,s.name,p.amt from student as s
right join payments as p
on s.id=p.id;

-- CROSS JOIN(4*3=12)
-- ALL THE VALUES (LIKE EXTRAS)
select count(*) from student 
cross join payments;

select * from student as s
cross join payments;

-- IMPLICIT JOIN (use , and where)
-- ONLY THE MATCHED VALUES
select * from student as s , payments as p
where s.id=p.id;

-- SELF JOIN
CREATE TABLE employeess (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employeess(emp_id)
);

INSERT INTO employeess 
VALUES
(1, 'Kriti', NULL),
(2, 'Siddhant', 1),
(3, 'Anamika', 1),
(4, 'Utkarsh', 2),
(5, 'Ronit', 2),
(6, 'Shivi', 3);

-- take the same table with aliases as E and MNG
select e.emp_name, mng.emp_name as manager_name from employeess as e
join employeess as mng
on e.manager_id=mng.emp_id;

-- count of the direct managers
select e.emp_name ,count(mng.manager_id) from employeess as e
join employeess as mng
on e.emp_id=mng.manager_id
-- cause we need to count
group by e.emp_name;
