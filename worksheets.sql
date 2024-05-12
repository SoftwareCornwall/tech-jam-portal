-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2024 at 08:33 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `worksheets`
--

-- --------------------------------------------------------

--
-- Table structure for table `worksheets`
--

CREATE TABLE `worksheets` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `difficulty` varchar(50) DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `worksheets`
--

INSERT INTO `worksheets` (`id`, `title`, `description`, `difficulty`, `language`, `file_path`) VALUES
(1, 'Introduction to Python', 'Learn the basics of Python programming', 'Beginner', 'Python', '/path/to/intro_python.pdf'),
(2, 'Advanced SQL Queries', 'Master complex SQL queries', 'Advanced', 'SQL', '/path/to/advanced_sql_queries.pdf'),
(3, 'Web Development Basics', 'Build a simple website using HTML and CSS', 'Intermediate', 'HTML/CSS', '/path/to/web_dev_basics.pdf'),
(4, 'Inputs and Outputs in Python', 'Learn how to take inputs and output data in Python', 'Beginner', 'Python', '/path/to/beginner_python_inputs.pdf');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `worksheets`
--
ALTER TABLE `worksheets`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `worksheets`
--
ALTER TABLE `worksheets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
