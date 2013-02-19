-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.27 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL version:             7.0.0.4053
-- Date/time:                    2013-02-19 11:38:41
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;

-- Dumping database structure for search
CREATE DATABASE IF NOT EXISTS `search` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `search`;


-- Dumping structure for table search.sites
CREATE TABLE IF NOT EXISTS `sites` (
  `id` int(10) DEFAULT NULL,
  `site` text NOT NULL,
  `explored` int(10) DEFAULT NULL,
  PRIMARY KEY (`site`(300))
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- Dumping data for table search.sites: 715 rows
/*!40000 ALTER TABLE `sites` DISABLE KEYS */;
INSERT INTO `sites` (`id`, `site`, `explored`) VALUES
	(1, 'http://www.google.com', 0);
/*!40000 ALTER TABLE `sites` ENABLE KEYS */;
/*!40014 SET FOREIGN_KEY_CHECKS=1 */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
