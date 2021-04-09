--Christian Escobarete & Moe
/* Creates employee database*/
CREATE DATABASE IF NOT EXISTS ManageEmp;

/* Selects employee database within the system*/
USE ManageEmp;

/* Drops the tables if doesnt exist*/
drop table if exists PersonalInfo;
drop table if exists Company;
drop table if exists Employee;

/* creates tables for each variable*/
create table Employee(
  eID int NOT NULL,
  name varchar(45) NOT NULL,
  startTime time,
  endTime time,
  schedule_create date,
  mon char(2),
  tu char(2),
  wed char(2),
  thur char(2),
  fri char(2),
  sat char(2),
  sun char(2),
  PRIMARY KEY(eID));

create table Company(
  pID int NOT NULL,
  position varchar(45) NOT NULL,
  privilege varchar(25) NOT NULL,
  positionTaken char(3),
  directive text,
  PRIMARY KEY(pID));

create table PersonalInfo(
  eID int NOT NULL,
  pID int NOT NULL,
  yearlySalary decimal(10,2),
  email varchar(100),
  phone BIGINT(20) NOT NULL UNIQUE,
  ssn BIGINT(20) NOT NULL UNIQUE,
  city varchar(20),
  adr varchar(30),
  zip BIGINT(10),
  review text,
  FOREIGN KEY(eID) REFERENCES Employee(eID),
  FOREIGN KEY(pID) REFERENCES Company(pID));

/* insert data into Employee table*/
insert into Employee values(1000, 'Christian Escobarete', '07:00:00', '15:00:00', '2021-12-1','Y','N','Y','Y','Y','Y','N');
insert into Employee values(1001, 'Jillian Smith', '06:00:00', '14:00:00','2021-12-1','Y','Y','N','Y','Y','Y','N');
insert into Employee values(1002, 'Darcy Martinez', '07:00:00', '15:00:00','2021-12-1','Y','N','N','N','Y','Y','N');
insert into Employee values(1003, 'Luis Vazquez', '08:00:00', '16:00:00','2021-12-1','Y','Y','Y','Y','Y','Y','N');
insert into Employee values(1004, 'Ada Lovelace', '08:00:00', '16:00:00','2021-12-1','Y','Y','Y','Y','Y','Y','N');

/* insert table into Company table*/
insert into Company values(1, 'Developer','denied','yes','Create a project that will change the world');
insert into Company values(2, 'Developer','denied','yes','Create a project that will change the world');
insert into Company values(3, 'Help Desk','denied','yes','Answer the phone');
insert into Company values(4, 'Senior Developer','denied','yes','Create a project that will change the world');
insert into Company values(5, 'Manager','granted','yes','Manage the employees and make sure things get done');
insert into Company values(6, 'Developer','denied','no', 'None yet');
insert into Company values(7, 'Information Technology','denied','no', 'Not yet');

/* insert table data PersonalInfo into table*/
insert into PersonalInfo values(1000, 1, 50000.00, 'cescobarete@business.com', 9909884567, 345543422, 'Romeoville', '567 Street dr', 60446, 'A terrible employee');
insert into PersonalInfo values(1001, 5, 70000.00, 'jsmith@business.com', 9909884569, 345543423, 'Romeoville', '567 Street dr', 60446, 'Exemplary employee');
insert into PersonalInfo values(1002, 3, 30000.00, 'dmartinez@business.com', 9909884565, 345544424, 'Romeoville', '567 Street dr', 60446, 'Does not work well with others');
insert into PersonalInfo values(1003, 4, 80000.00, 'lvazquez@business.com', 9909884560, 345543425, 'Romeoville', '567 Street dr', 60446, 'Smiles all the time');
insert into PersonalInfo values(1004, 2, 50000.00, 'alovelace@business.com', 9909884561, 345543426, 'Romeoville', '567 Street dr', 60446, 'Sketchy');

/* retrieve data very quickly by indexing*/
CREATE INDEX Employee
ON Employee(name, startTime, endTime);

/* Create user and privilges*/
CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost;
