-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2016 at 01:31 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `id_q` int(11) NOT NULL,
  `id_ans` int(11) NOT NULL,
  `text_ans` varchar(200) DEFAULT NULL,
  `energy_change` int(11) DEFAULT NULL,
  `bodytemp_change` int(11) DEFAULT NULL,
  `next_q` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_q`,`id_ans`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id_q`, `id_ans`, `text_ans`, `energy_change`, `bodytemp_change`, `next_q`) VALUES
(1, 1, 'You leave the car immediately, trying to look for help.', -25, -20, 2),
(1, 2, 'Better to sleep and wait inside.', -10, 0, 3),
(1, 3, 'You try to fix the car.', -30, -15, 4),
(2, 1, 'Run!!! ', -45, 10, 5),
(2, 2, 'You notice you have cookies in your pocket so you give them to the bear.', -20, 0, 6),
(2, 3, 'You grab a stick and fight!!!', -1000, -1000, 12),
(3, 1, 'You are not made of sugar! Go look for help.', -30, -30, 7),
(3, 2, 'You stay in the car, of course, nothing else to do besides eating the leftovers you had in your car.', 30, 10, 8),
(3, 3, 'You try your best to fix the car', -30, -40, 9),
(4, 1, 'Start praying for some tools to appear. You believe in miracles.', -10, -30, 8),
(4, 2, 'Get some sticks in the wood and try to do your best using them as tools', -30, -40, 7),
(4, 3, 'Give up and go look for help.', -25, -40, 7),
(5, 1, 'Knock on the door looking for someone to help.', -5, 0, 10),
(5, 2, 'Scream loud until someone appears.', -10, -10, 10),
(5, 3, 'It''s an abandoned house!!! better keep running.', -30, -30, 8),
(6, 1, 'Go with him, and help him with the tools', -1000, 0, 9),
(6, 2, 'Wait in the car to make sure nothing happened', -10, -10, 12),
(6, 3, 'Don''t accept his help because bears don''t know how to fix cars', -40, -20, 12),
(7, 1, 'You dont care that he is angry and go ask him for help', -10, -10, 13),
(7, 2, 'Better not to disturb him... he has a really big gun', -1000, -1000, 8),
(7, 3, 'You ask to help him hunt, because you were really good when you were younger.', -10, 0, 11),
(8, 1, 'You lose', NULL, NULL, 0),
(8, 2, 'You lose', NULL, NULL, 0),
(8, 3, 'You lose', NULL, NULL, 0),
(9, 1, 'You lose', NULL, NULL, 0),
(9, 2, 'You lose', NULL, NULL, 0),
(9, 3, 'You lose', NULL, NULL, 0),
(10, 1, 'You win!', NULL, NULL, NULL),
(10, 2, 'You win!', NULL, NULL, NULL),
(10, 3, 'You win!', NULL, NULL, NULL),
(11, 1, 'You win!', NULL, NULL, NULL),
(11, 2, 'You win!', NULL, NULL, NULL),
(11, 3, 'You win!', NULL, NULL, NULL),
(12, 1, 'You lose', NULL, NULL, NULL),
(12, 2, 'You lose', NULL, NULL, NULL),
(12, 3, 'You lose', NULL, NULL, NULL),
(13, 1, 'You lose', NULL, NULL, NULL),
(13, 2, 'You lose', NULL, NULL, NULL),
(13, 3, 'You lose', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE IF NOT EXISTS `questions` (
  `id_q` int(11) NOT NULL DEFAULT '0',
  `text_q` varchar(200) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_q`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id_q`, `text_q`, `image`) VALUES
(0, '', ''),
(1, 'You were driving to meet your family for a weekend in the mountains. Since you worked late today, you''re stuck driving in the middle of the night. Suddenly, your car breaks down. What do you do?', 'mountains.jpg'),
(2, 'Uh oh! You run into a bear in the woods! How do you react?', 'bear.jpg'),
(3, 'Bad luck! It started raining! What do you do?', 'rain.jpg'),
(4, 'Crap you have no luck fixing your car.', 'car.jpg'),
(5, 'You run as far as you can until you see an abandoned house. What do you do now?', 'house.jpg'),
(6, 'You are now best friends with the bear and he decides to help you fix the car!!! He is going to get the tools with you...', 'tools.jpg'),
(7, 'Proactivity is good! You clearly really want to fix the car. You start to walk and find a really angry hunter in your way', 'hunter.jpg'),
(8, 'You end up running out of time and dying', 'time.jpg'),
(9, 'You run out of energy from working so hard on the car', 'energybar.jpg'),
(10, 'The owner of the house takes you in and helps you', 'host.jpg'),
(11, 'You help the hunter and so he helps you get out of the woods and to safety', 'bff.jpg'),
(12, 'The bear kills you', 'angrybear.jpg'),
(13, 'The hunter kills you', 'angryhunter.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id_users` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `energy_total` int(11) DEFAULT NULL,
  `bodytemp_total` int(11) DEFAULT NULL,
  `id_q` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_users`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_users_questions_idx` (`id_q`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_users`, `name`, `energy_total`, `bodytemp_total`, `id_q`) VALUES
(1, 'Ilana', 100, 100, 1),
(2, 'Camila', 100, 100, 1),
(3, 'Benji', 100, 100, 1),
(9, 'Liron', 100, 100, 1),
(12, 'Yippy', 100, 100, 1),
(21, 'None', 100, 100, 1),
(22, 'aaa', 100, 100, 1),
(23, 'abc', 100, 100, 1),
(24, 're', 100, 100, 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `fk_answers_questions1` FOREIGN KEY (`id_q`) REFERENCES `questions` (`id_q`) ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_questions` FOREIGN KEY (`id_q`) REFERENCES `questions` (`id_q`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
