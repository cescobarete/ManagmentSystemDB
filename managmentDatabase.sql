CREATE DATABASE IF NOT EXISTS ManageEmp;

USE ManageEmp;

drop table if exists PersonalInfo;
drop table if exists Company;
drop table if exists Employee;

create table Employee(
  eID int NOT NULL,
  name varchar(45) NOT NULL,
  startTime time,
  endTime time,
  schedule_create date,
  mon char(2),
  tue char(2),
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
  pswd VARCHAR(255) NOT NULL,
  positionTaken char(3),
  directive text,
  PRIMARY KEY(pID));

create table PersonalInfo(
  eID int NOT NULL,
  pID int NOT NULL,
  yearlySalary decimal(10,2),
  email varchar(100),
  phone VARCHAR(20) NOT NULL UNIQUE,
  ssn VARCHAR(20) NOT NULL UNIQUE,
  city varchar(100),
  adr varchar(100),
  zip BIGINT(10),
  review text,
  FOREIGN KEY(eID) REFERENCES Employee(eID),
  FOREIGN KEY(pID) REFERENCES Company(pID));

insert into Employee values(1000, 'Christian Escobarete', '07:00:00', '15:00:00', '2021-12-1','Y','N','Y','Y','Y','Y','N');
insert into Employee values(1001, 'Jillian Smith', '06:00:00', '14:00:00','2021-12-1','Y','Y','N','Y','Y','Y','N');
insert into Employee values(1002, 'Darcy Martinez', '07:00:00', '15:00:00','2021-12-1','Y','N','N','N','Y','Y','N');
insert into Employee values(1003, 'Luis Vazquez', '08:00:00', '16:00:00','2021-12-1','Y','Y','Y','Y','Y','Y','N');
insert into Employee values(1004, 'Ada Lovelace', '08:00:00', '16:00:00','2021-12-1','Y','Y','Y','Y','Y','Y','N');

insert into Company values(1, 'Developer','denied','abc123','yes','Create a project that will change the world');
insert into Company values(2, 'Developer','denied','abc123','yes','Create a project that will change the world');
insert into Company values(3, 'Help Desk','denied','abc1234','yes','Answer the phone');
insert into Company values(4, 'Senior Developer','denied','abc1234','yes','Create a project that will change the world');
insert into Company values(5, 'Manager','granted','abc12','yes','Manage the employees and make sure things get done');
insert into Company values(6, 'Developer','denied','abc45','no', 'None yet');
insert into Company values(7, 'Information Technology','denied','abc123','no', 'Not yet');

insert into PersonalInfo values(1000, 1, 50000.00, 'cescobarete@business.com', '990-988-4567', '345-54-3422', 'Romeoville', '567 Street dr', 60446, 'A terrible employee');
insert into PersonalInfo values(1001, 5, 70000.00, 'jsmith@business.com', '990-988-4569', '345-54-3423', 'Romeoville', '567 Street dr', 60446, 'Exemplary employee');
insert into PersonalInfo values(1002, 3, 30000.00, 'dmartinez@business.com', '990-988-4565', '345-54-4424', 'Romeoville', '567 Street dr', 60446, 'Does not work well with others');
insert into PersonalInfo values(1003, 4, 80000.00, 'lvazquez@business.com', '990-988-4560', '345-54-3425', 'Romeoville', '567 Street dr', 60446, 'Smiles all the time');
insert into PersonalInfo values(1004, 2, 50000.00, 'alovelace@business.com', '990-988-4561', '345-54-3426', 'Romeoville', '567 Street dr', 60446, 'Sketchy');

CREATE INDEX Employee
ON Employee(name, startTime, endTime);

CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost;
