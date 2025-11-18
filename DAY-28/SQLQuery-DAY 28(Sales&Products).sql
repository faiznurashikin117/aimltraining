create database SalesDb

use SalesDb

create table Products
(ProductID int primary key,
ProductName nvarchar(100),
Category nvarchar(50),
UnitPrice(RM) decimal(10,2)
)
alter table Products rename column UnitPrice,"UnitPrice(RM)" decimal(10,2)
--ALTER TABLE Products RENAME COLUMN UnitPrice TO "UnitPrice(RM)"

insert into Products values (1,'Laptop Xiaomi','Electronics',1200)
select * from Products
insert into Products values
(2,'Wireless Keyboard','Electronics',100),
(3,'Wireless Mouse','Electronics',50),
(4,'Table','Furniture',1300),
(5,'PenBox','Stationaries',15),
(6,'Chair','Furniture',300),
(7,'Notebook','Stationaries',10.50)
select * from Products

create table Sales
(SalesID int primary key identity,
ProductID int foreign key references Products(ProductId),
Region nvarchar(50) check (Region in ('East','West','North','South')),
Quantity int,
SalesDate date
)
--YY-MM-DD
insert into Sales(ProductId,Region,Quantity,SalesDate) values (1,'East',5,'2024-02-23')
select * from Sales
insert into Sales(ProductId,Region,Quantity,SalesDate)
values (3,'West',15,'2024-02-23'),
(2,'West',10,'2024-02-23'),
(3,'West',5,'2024-02-23'),
(4,'West',6,'2024-02-23'),
(4,'West',10,'2024-02-23'),
(5,'West',12,'2024-02-23'),
(6,'West',4,'2024-02-23')

select * from Products
select * from Sales