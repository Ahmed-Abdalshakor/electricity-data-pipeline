-- Create database
CREATE DATABASE ElectricityDB;
GO

-- Use the database
USE ElectricityDB;
GO

-- Create electricity demand table
CREATE TABLE electricity_demand (
    entity VARCHAR(100) NOT NULL,
    entity_code VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    demand_twh DECIMAL(10, 2) NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,

    CONSTRAINT PK_electricity_demand_date
        PRIMARY KEY (date)
);
GO