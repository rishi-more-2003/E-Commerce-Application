-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basket`
--

DROP TABLE IF EXISTS `basket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basket` (
  `orno` int DEFAULT NULL,
  `it_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  KEY `orno` (`orno`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `basket_ibfk_1` FOREIGN KEY (`orno`) REFERENCES `orders` (`o_no`),
  CONSTRAINT `basket_ibfk_2` FOREIGN KEY (`it_id`) REFERENCES `items` (`itid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basket`
--

LOCK TABLES `basket` WRITE;
/*!40000 ALTER TABLE `basket` DISABLE KEYS */;
INSERT INTO `basket` VALUES (0,1,3),(0,2,2),(0,6,1),(1,1,2),(1,2,3),(2,2,2),(2,6,2),(3,1,1),(3,2,2),(4,1,2),(4,2,2),(4,50,3),(5,1,2),(5,2,1);
/*!40000 ALTER TABLE `basket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `compid` int NOT NULL,
  `compname` varchar(20) DEFAULT NULL,
  `cpass` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`compid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'Apple','Password'),(2,'Samsung','Password'),(3,'Xiaomi','Password'),(4,'Nokia','Password'),(5,'OnePlus','Password'),(6,'RealMe','Password'),(7,'Micromax','Password'),(8,'Adidas','Password'),(9,'Nike','Password'),(10,'Vans','Password'),(11,'Reebok','Password'),(12,'Sparx','Password'),(13,'Jordans','Password'),(14,'Levis','Password'),(15,'Gucci','Password'),(16,'Louis Vuitton','Password'),(17,'H&M','Password'),(18,'Zara','Password'),(19,'Casio','Password'),(20,'Rolex','Password'),(21,'Titan','Password'),(22,'Zenith','Password'),(23,'Test','Test');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL,
  `cust_name` varchar(20) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `cmail` varchar(20) DEFAULT NULL,
  `cno` int DEFAULT NULL,
  `phno` int DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Rishi','Bhandup,Mumbai','rishi@gmail.com',123456789,123456789,'Password'),(2,'Amit','Dadar,Mumbai','amit@gmail.com',987654321,987654321,'Password'),(3,'Chirag','Wadala,Mumbai','chirag@gmail.com',234567891,234567891,'Password'),(4,'Deep','Vidyavihar,Mumbai','deep@gmail.com',345678912,345678912,'Password'),(5,'Mayank','Jammu','mayank@gmail.com',456789012,456789012,'Password'),(6,'Sarang','Ghatkopar','sarang@gmail.com',456789013,456789013,'Password'),(7,'Anshul','Borivali,Mumbai','anshul@gmail.com',196878945,894237935,'Password');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `itid` int NOT NULL,
  `price` double(10,2) DEFAULT NULL,
  `companyid` int DEFAULT NULL,
  `it_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`itid`),
  KEY `companyid` (`companyid`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`compid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,60990.00,1,'iPhone 12'),(2,49000.00,1,'iPhone 11'),(3,43000.00,1,'iPhone XR'),(4,12000.00,1,'Airpods'),(5,20900.00,1,'Airpods Pro'),(6,37000.00,2,'Galaxy S20'),(7,55000.00,2,'Galaxy S21'),(8,110000.00,2,'Galaxy S22'),(9,39000.00,2,'Crystal 4K Pro TV'),(10,54000.00,2,'Crystal 4K UHD TV'),(11,40000.00,3,'11T Pro 5G'),(12,3500.00,3,'Mi SmartBand 6'),(13,2500.00,3,'Mi SmartBand 5'),(14,16000.00,3,'Redmi HD TV'),(15,43000.00,3,'Redmi 4K TV'),(16,6225.00,4,'C01 Plus 4G'),(17,14880.00,4,'T20 Tablet'),(18,11499.00,4,'G10'),(19,12999.00,4,'5.4'),(20,7999.00,4,'C20 Plus TA-1366'),(21,24999.00,5,'OnePlus Nord CE 2 5G'),(22,30000.00,5,'OnePlus Nord 2 5G '),(23,42999.00,5,'OnePlus 9RT 5G '),(24,49999.00,5,'OnePlus 9 5G '),(25,4999.00,5,'OnePlus Buds Z2 '),(26,11499.00,6,'Realme Narzo 50A'),(27,14266.00,6,'Realme 8'),(28,599.00,6,'Realme Buds 2'),(29,13290.00,6,'Realme 8i'),(30,1499.00,6,'Realme Buds Wireless'),(31,11249.00,7,'Micromax IN 1'),(32,11900.00,7,'Micromax IN 2B '),(33,16864.00,8,'Adidas Tennis Shoes'),(34,3028.00,8,'Adidas Running Shoes'),(35,399.00,8,'Adidas Slide Sandal'),(36,7000.00,8,'Adidas Hiking Shoes'),(37,5999.00,8,'Adidas Casual Shoes'),(38,7999.00,9,'Nike Blazer Vintage'),(39,15999.00,9,'Nike Air Max'),(40,8695.00,9,'Nike Blazer Premium'),(41,7495.00,9,'Nike GT Premium'),(42,2695.00,9,'Nike Casual Shirt'),(43,2799.00,10,'SoftStride Sandals'),(44,5199.00,10,'Tazon Running Shoes'),(45,2999.00,10,'Kent 2.0'),(46,3999.00,10,'Puma 1948 Mid L'),(47,2469.00,10,'Puma Men\'s Jacket'),(48,1800.00,10,'Puma Sweatshirt'),(49,3499.00,10,'Puma FlipFlops'),(50,40000.00,1,'iPhone 10'),(51,70000.00,1,'iPhone 13');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `o_no` int NOT NULL,
  `amount` int DEFAULT NULL,
  `cuno` int DEFAULT NULL,
  PRIMARY KEY (`o_no`),
  KEY `cuno` (`cuno`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`cuno`) REFERENCES `customer` (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (0,317970,1),(1,268980,1),(2,172000,1),(3,158990,2),(4,339980,1),(5,170980,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderspayment`
--

DROP TABLE IF EXISTS `orderspayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderspayment` (
  `ornum` int DEFAULT NULL,
  `num` int DEFAULT NULL,
  `paystat` int DEFAULT NULL,
  KEY `ornum` (`ornum`),
  KEY `num` (`num`),
  CONSTRAINT `orderspayment_ibfk_1` FOREIGN KEY (`ornum`) REFERENCES `orders` (`o_no`),
  CONSTRAINT `orderspayment_ibfk_2` FOREIGN KEY (`num`) REFERENCES `customer` (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderspayment`
--

LOCK TABLES `orderspayment` WRITE;
/*!40000 ALTER TABLE `orderspayment` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderspayment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01 16:34:20
