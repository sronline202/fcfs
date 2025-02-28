/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.4.21-MariaDB : Database - agriculturedatabse
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`agriculturedatabse` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `agriculturedatabse`;

/*Table structure for table `croptype` */

DROP TABLE IF EXISTS `croptype`;

CREATE TABLE `croptype` (
  `SlNo` int(11) NOT NULL AUTO_INCREMENT,
  `CropName` varchar(200) NOT NULL,
  `CropCost` varchar(200) NOT NULL,
  PRIMARY KEY (`SlNo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `croptype` */

insert  into `croptype`(`SlNo`,`CropName`,`CropCost`) values (1,'Rice','1000'),(2,'Wheat','1500'),(3,'Greengram','1800'),(4,'Paddy','2000');

/*Table structure for table `customerreg` */

DROP TABLE IF EXISTS `customerreg`;

CREATE TABLE `customerreg` (
  `ID` int(200) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) DEFAULT NULL,
  `Email` varchar(200) DEFAULT NULL,
  `Age` varchar(200) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL,
  `Contact` varchar(100) DEFAULT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `customerreg` */

insert  into `customerreg`(`ID`,`Name`,`Email`,`Age`,`Password`,`Contact`,`Address`,`status`) values (1,'customer','customer@gmail.com','45','1234','987-123-1595','kalakada','pending'),(2,'customer','customer1@gmail.com','21','1234','124-758-1546','Tirupathi','pending'),(3,'admin','admin@gmail.com','40','1234','984-852-6524','Nandyala','pending'),(4,'mouli','mouli@gmail.com','25','1596','789-456-1235','puttor(dist)','pending');

/*Table structure for table `dealerreg` */

DROP TABLE IF EXISTS `dealerreg`;

CREATE TABLE `dealerreg` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Age` varchar(200) NOT NULL,
  `Contact` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `dealerreg` */

insert  into `dealerreg`(`Id`,`Name`,`Email`,`Password`,`Age`,`Contact`,`Address`) values (1,'dealer','dealer@gmail.com','1234','45','125-584-4521','chittor dist(kotthapalli )');

/*Table structure for table `farmerencdata` */

DROP TABLE IF EXISTS `farmerencdata`;

CREATE TABLE `farmerencdata` (
  `Id` int(100) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) DEFAULT NULL,
  `Contact` varchar(200) DEFAULT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `filename` varchar(200) DEFAULT NULL,
  `Dataone` longblob DEFAULT NULL,
  `Datatwo` longblob DEFAULT NULL,
  `Hashone` varchar(200) DEFAULT NULL,
  `Hashtwo` varchar(200) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `farmerencdata` */

insert  into `farmerencdata`(`Id`,`Name`,`Contact`,`Address`,`filename`,`Dataone`,`Datatwo`,`Hashone`,`Hashtwo`,`status`,`Email`) values (1,'farmer','458-124-1236','chittor dist(kotthapalli )','file.txt',' ÞÈ„ÚÚÉ_†«Îõ¥','ç*ÇÂtÔSÅ1Ïë¡„f\\','966c2e80fbdeb5dfe8673392085cb149f7640fc7953a42265cabd911a940153e','56c24dced1ba23dae14cf47f3c1bf57f9524e637f7e79d70e794c58771428335','accepted','farmer@gmail.com');

/*Table structure for table `farmerreg` */

DROP TABLE IF EXISTS `farmerreg`;

CREATE TABLE `farmerreg` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Age` varchar(200) NOT NULL,
  `Contact` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `farmerreg` */

insert  into `farmerreg`(`Id`,`Name`,`Email`,`Password`,`Age`,`Contact`,`Address`) values (1,'farmer','farmer@gmail.com','1234','50','458-124-1236','chittor dist(kotthapalli )');

/*Table structure for table `subdealercroptype` */

DROP TABLE IF EXISTS `subdealercroptype`;

CREATE TABLE `subdealercroptype` (
  `SlNo` int(11) NOT NULL AUTO_INCREMENT,
  `CropName` varchar(200) NOT NULL,
  `CropCost` varchar(200) NOT NULL,
  PRIMARY KEY (`SlNo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subdealercroptype` */

insert  into `subdealercroptype`(`SlNo`,`CropName`,`CropCost`) values (1,'Rice','2000'),(2,'Wheat','2400'),(3,'paddy','2800'),(4,'Greengram','3000');

/*Table structure for table `subdealerrequests` */

DROP TABLE IF EXISTS `subdealerrequests`;

CREATE TABLE `subdealerrequests` (
  `Id` int(200) NOT NULL AUTO_INCREMENT,
  `Cropname` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `Subdealeremail` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subdealerrequests` */

insert  into `subdealerrequests`(`Id`,`Cropname`,`quantity`,`Subdealeremail`,`status`) values (1,'wheat','4 quintals','subdealer@gmail.com','pending'),(2,'Gram','500 kgs','subdealer@gmail.com','pending'),(3,'wheat','10kgs','subdealer@gmail.com','accepted'),(4,'wheat','1 quintal','subdealer@gmail.com','accepted');

/*Table structure for table `subdealers` */

DROP TABLE IF EXISTS `subdealers`;

CREATE TABLE `subdealers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `status` varchar(100) DEFAULT 'pending',
  `Contact` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subdealers` */

insert  into `subdealers`(`id`,`Name`,`Email`,`Password`,`Address`,`status`,`Contact`) values (1,'subdealer','subdealer@gmail.com','1234','narsapoor(3rd street)drno:099','sent','987-123-1595');

/*Table structure for table `subdelaercustomerrequest` */

DROP TABLE IF EXISTS `subdelaercustomerrequest`;

CREATE TABLE `subdelaercustomerrequest` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `Slno` int(200) DEFAULT NULL,
  `Name` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `status` varchar(100) DEFAULT 'pending',
  `Contact` varchar(100) DEFAULT NULL,
  `CustomerEmail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subdelaercustomerrequest` */

insert  into `subdelaercustomerrequest`(`id`,`Slno`,`Name`,`Email`,`Address`,`status`,`Contact`,`CustomerEmail`) values (1,1,'subdealer','subdealer@gmail.com','narsapoor(3rd street)drno:099','accepted','987-123-1595','customer1@gmail.com'),(2,1,'subdealer','subdealer@gmail.com','narsapoor(3rd street)drno:099','sent','987-123-1595','mouli@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
