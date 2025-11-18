use OurDB
--Constraint, not null,
--primary key: not null and must be unique,
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50)
)

-- F5 to refresh and execute command
-- Ctrl+R to remove the view result
-- * means 'all'
select * from Emp
insert into Emp values (1,'Sam','Dicosta')
insert into Emp (Id,Fname) values (2,'Rameez')
select * from Emp
insert into Emp (Id,Lname) values (3,'Khan')
--Cannot insert the value NULL into column 'Fname', table 'OurDB.dbo.Emp'; column does not allow nulls. INSERT fails.
insert into Emp (Id,Fname) values (2,'Deep')
--Violation of PRIMARY KEY constraint 'PK__Emp__3214EC07C208C1F1'. Cannot insert duplicate key in object 'dbo.Emp'. The duplicate key value is (2)

--delete data
delete from Emp

--drop data
drop table Emp

---default value
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default('Kuala Lumpur')
)

insert into Emp values (1,'Sam','John','Brisbane')
insert into Emp values (2,'Rina','Kumari','Delhi')
---default value auto replace missing data in that particular value
insert into Emp (Id,Fname,Lname) values(3,'Alina','Khan')
select * from Emp

--check the values(Salary within range)
drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default('Kuala Lumpur'),
Salary float not null check(Salary>=10000 and Salary<=50000)
)
insert into Emp (Id,Fname,Lname,Salary) values(3,'Alina','Khan',12000)
insert into Emp values (2,'Rina','Kumari','Delhi',69000)  --terkurang drp range
--The INSERT statement conflicted with the CHECK constraint "CK__Emp__Salary__45F365D3". The conflict occurred in database "OurDB", table "dbo.Emp", column 'Salary'
insert into Emp values (2,'Rina','Kumari','Delhi',39000)
select * from Emp


--check specific values(only numbers for phone number)
drop table Emp
create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) check (Mobile like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
insert into Emp values (1,'Maan','0186427838')
insert into Emp values (2,'Saan','018642783a')
--The INSERT statement conflicted with the CHECK constraint "CK__Emp__Mobile__48CFD27E". 
--The conflict occurred in database "OurDB", table "dbo.Emp", column 'Mobile'.
insert into Emp values (3,'Taan','018642')
--The INSERT statement conflicted with the CHECK constraint "CK__Emp__Mobile__48CFD27E". 
--The conflict occurred in database "OurDB", table "dbo.Emp", column 'Mobile'.


--unique : not duplicate, allows null but not duplicate
drop table Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
insert into Emp values (1,'Sam','9876543210','sam@yahoo.com')
insert into Emp values (2,'Ravi','9876543210','ravi@yahoo.com')
--Violation of UNIQUE KEY constraint 'UQ__Emp__6FAE0782BBC7D4FA'. 
--Cannot insert duplicate key in object 'dbo.Emp'. The duplicate key value is (9876543210).
select * from Emp
insert into Emp values (2,'Ravi','9875553210','ravi@yahoo.com')

--to add one new column for table Emp
alter table Emp add City nvarchar(50) not null
select * from Emp
alter table Emp drop column City 
select * from Emp

--identity(seed,increment)
create table Students
(SId int identity,
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Ravi',5000.50)
insert into Students(SName,SFee) values ('Anil',3000.50)
insert into Students(SName,SFee) values ('Ravi',4500.20)
select * from Students
insert into Students(SName,SFee) values ('Riya',5500.20)
select * from Students

--------------------------------
drop table Students
--------------------------------
create table Students
(SId int identity(100,5),
SName nvarchar(50) not null,
SFee float)

insert into Students(SName,SFee) values ('Ravi',5000.50)
 insert into Students(SName,SFee) values ('Anil',3000.50)
  insert into Students(SName,SFee) values ('Ravi',4500.20)
   select * from Students
    insert into Students(SName,SFee) values ('Riya',5500.20)
     select * from Students
--alter table Emp drop row (5)???
       insert into Students(SName,SFee) values('Riya',4500.20)


---------------------------------
create table Salary
(Grade varchar(1) primary key,
BasicSalary float,
HRA as BasicSalary*0.10 persisted,
TA as BasicSalary*0.15 persisted,
DA as BasicSalary*0.20 persisted
)

insert into Salary values ('A',10000)
select * from Salary
insert into Salary values ('B',5000)

select Grade,BasicSalary,HRA,DA,TA, BasicSalary+TA+DA+HRA as 'Net Salary' from Salary
 insert into Salary values ('C',2000)
 insert into Salary values ('D',1000)
 select max(BasicSalary) as 'Max Basic' from Salary
 select min(BasicSalary) as 'Min Basic' from Salary
 select avg(BasicSalary) as 'Avg Basic' from Salary
 ----------
 exec sp_tables


-------------------------------------------------------
-- foreign key
-------------------------------------------------------
create table Category
(CatId int primary key,
CategoryName nvarchar(50) not null unique
)
insert into Category values (1,'Electronics'),(2,'Clothing'),(3,'Home Decoration'),(4,'Mobile')
select * from Category order by CatId

create table Product
(PId int primary key identity,
 PName nvarchar(50) not null,
 PPrice float not null,
 ProductCategory int foreign key references Category
 )
 select * from Product
 insert into Product values ('IPhone-17',5000,4)
 insert into Product values ('Nothing-3',2000,4)
 insert into Product values ('Washing Machine',4000,1)

 insert into Product values ('Shirt',200,2)
 insert into Product values ('T-Shirt',199,2)
 insert into Product values ('Jeans',159,2)
 select * from Product
 insert into Product values ('Tudung',259,7)
 select * from Product
 select * from Category

 ---------------------------------------------
 select * from Product join Category
 on Product.ProductCategory=Category.CatId
 --or--
 select * from Product p join Category c
 on p.ProductCategory=c.CatId

 select p.PId,p.PName,p.PPrice,p.ProductCategory,c.CategoryName
    from Product p join Category c
    on p.ProductCategory=c.CatId

select p.PId 'Product ID',p.PName 'Product Name',p.PPrice 'Product Price',p.ProductCategory'Product Category',c.CategoryName 'Category Name'
    from Product p join Category c
    on p.ProductCategory=c.CatId
