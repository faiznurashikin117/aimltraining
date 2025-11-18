CREATE DATABASE ExerciseOne
USE ExerciseOne;
create table StudentMarks (
    StudentID int,
    StudentName nvarchar(50),
    Math int,
    Science int,
    English int,
    History int
)

--insert few records
insert into StudentMarks values
(1,'Sam',95,85,90,88)
select * from StudentMarks

insert into StudentMarks values
(2,'Mas',90,75,90,78),
(3,'Ams',70,85,90,87),
(4,'Cha',90,85,90,88),
(5,'Ang',80,75,60,83),
(6,'Chang',78,95,90,85)

drop table StudentMarks
