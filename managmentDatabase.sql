--Christian Escobarete & Moe
/* Creates employee database*/
CREATE DATABASE IF NOT EXISTS ManageEmp;

/* Selects employee database within the system*/
USE ManageEmp;

/* Drops the tables if doesnt exist*/
drop table if exists Employee;
drop table if exists PersonalInfo;
drop table if exists Company;

/* creates tables for each variable*/
create table Employee(eID int, name varchar(25), startTime time, endTime time);
create table Company(pID int, position varchar(25), postionTaken char(3));
create table PersonalInfo(eID int, pID int, yearlySalary int, email varchar(100), review text);

/* insert data into Employee table*/
insert into Employee values(1000, 'Christian Escobarete', '07:00:00', '15:00:00');
insert into Employee values(1001, 'Jillian Smith', '06:00:00', '14:00:00');
insert into Employee values(1002, 'Darcy Martinez', '07:00:00', '15:00:00');
insert into Employee values(1003, 'Luis Vazquez', '08:00:00', '16:00:00');
insert into Employee values(1004, 'Ada Lovelace', '08:00:00', '16:00:00');

/* insert table into Company table*/
insert into Company values(1, 'Developer', 'yes');
insert into Company values(2, 'Developer', 'yes');
insert into Company values(3, 'Help Desk', 'yes');
insert into Company values(4, 'Senior Devloper', 'yes');
insert into Company values(5, 'Manager', 'yes');
insert into Company values(6, 'Developer', 'no');
insert into Company values(7, 'Information Technology', 'no');

/* insert table data PersonalInfo into table*/
insert into PersonalInfo values(1000, 1, 50000, 'cescobarete@business.com', 'A terrible employee');
insert into PersonalInfo values(1001, 5, 70000, 'jsmith@business.com', 'Exemplory employee');
insert into PersonalInfo values(1002, 3, 30000, 'dmartinez@business.com', 'Does not work well with others');
insert into PersonalInfo values(1003, 4, 80000, 'lvazquez@business.com', 'Smiles all the time');
insert into PersonalInfo values(1004, 2, 50000, 'alovelace@business.com', 'Sketchy');

/* Create user and privilges*/
CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost;
