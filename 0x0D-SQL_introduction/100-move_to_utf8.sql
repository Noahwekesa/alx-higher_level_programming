-- Script to Convert hbtn_0c_0 Database to UTF8
SHOW CREATE DATABASE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW CREATE TABLE hbtn_0c_0.first_table;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW FULL COLUMNS FROM hbtn_0c_0.first_table LIKE 'name';
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
