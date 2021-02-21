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
  PRIMARY KEY(eID));

create table Company(
  pID int NOT NULL,
  position varchar(45) NOT NULL,
  positionTaken char(3),
  directive text,
  PRIMARY KEY(pID));

create table PersonalInfo(eID int NOT NULL,
  pID int NOT NULL,
  yearlySalary int,
  email varchar(100),
  review text,
  FOREIGN KEY(eID) REFERENCES Employee(eID),
  FOREIGN KEY(pID) REFERENCES Company(pID));

/* insert data into Employee table*/
insert into Employee values(1000, 'Christian Escobarete', '07:00:00', '15:00:00');
insert into Employee values(1001, 'Jillian Smith', '06:00:00', '14:00:00');
insert into Employee values(1002, 'Darcy Martinez', '07:00:00', '15:00:00');
insert into Employee values(1003, 'Luis Vazquez', '08:00:00', '16:00:00');
insert into Employee values(1004, 'Ada Lovelace', '08:00:00', '16:00:00');

/* insert table into Company table*/
insert into Company values(1, 'Developer', 'yes','Create a project that will change the world');
insert into Company values(2, 'Developer', 'yes','Create a porject that will change the world');
insert into Company values(3, 'Help Desk', 'yes','Answer the phone');
insert into Company values(4, 'Senior Devloper', 'yes','Create a porject that will chnage the world');
insert into Company values(5, 'Manager', 'yes','Manage the employees and make sure things get done');
insert into Company values(6, 'Developer', 'no', NULL);
insert into Company values(7, 'Information Technology', 'no', NULL);

/* insert table data PersonalInfo into table*/
insert into PersonalInfo values(1000, 1, 50000, 'cescobarete@business.com', 'A terrible employee');
insert into PersonalInfo values(1001, 5, 70000, 'jsmith@business.com', 'Exemplory employee');
insert into PersonalInfo values(1002, 3, 30000, 'dmartinez@business.com', 'Does not work well with others');
insert into PersonalInfo values(1003, 4, 80000, 'lvazquez@business.com', 'Smiles all the time');
insert into PersonalInfo values(1004, 2, 50000, 'alovelace@business.com', 'Sketchy');

/* retrieve data very quickly by indexing*/
CREATE INDEX Employee
ON Employee(name, startTime, endTime);

/* Create user and privilges*/
CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost;
