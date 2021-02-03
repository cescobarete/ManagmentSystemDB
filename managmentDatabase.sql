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
create table Employee(eID int, name varchar(25), position varchar(25), startTime time, endTime time);
create table Company(pID int, position varchar(25), postionTaken char(3));
create table PersonalInfo(eID int, pID int, payroll int, email varchar(100), review text);

insert into Employee values(1000, 'Christian Escobarete', 'Developer', '07:00:00', '15:00:00');

insert into Company values(1, 'Developer', 'yes');

insert into PersonalInfo values(1000, 1, 50, 'christianaescobare@lewisu.edu', 'A terrible employee');
