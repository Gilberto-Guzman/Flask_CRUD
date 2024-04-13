-- Create database --
CREATE DATABASE IF NOT EXISTS flask_crud;

-- Select database --
USE flask_crud;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
