DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);

INSERT INTO users
(username, password)
VALUES
('brian', 'waduhek'),
('diana', 'taylorswift'),
('vrishak', 'minecraft'),
('kiran', 'crypto'),
('sebastian', 'aigrader'),
('dheetya', '!@#$%^&*()'),
('katie', 'avocado');