-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: agenda-academica
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Dono`
--

DROP TABLE IF EXISTS `Dono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dono`
--

LOCK TABLES `Dono` WRITE;
/*!40000 ALTER TABLE `Dono` DISABLE KEYS */;
INSERT INTO `Dono` VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12);
/*!40000 ALTER TABLE `Dono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Grupo`
--

DROP TABLE IF EXISTS `Grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grupo` (
  `nome` varchar(20) NOT NULL,
  `dono_id` int(11) NOT NULL,
  PRIMARY KEY (`dono_id`),
  KEY `fk_Grupo_Dono1_idx` (`dono_id`),
  CONSTRAINT `fk_Grupo_Dono1Grupo` FOREIGN KEY (`dono_id`) REFERENCES `Dono` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Grupo`
--

LOCK TABLES `Grupo` WRITE;
/*!40000 ALTER TABLE `Grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Grupo_has_Usuario`
--

DROP TABLE IF EXISTS `Grupo_has_Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grupo_has_Usuario` (
  `eh_admin` tinyint(1) NOT NULL,
  `grupo_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`grupo_id`,`usuario_id`),
  KEY `fk_Grupo_has_Usuario_Usuario1_idx` (`usuario_id`),
  CONSTRAINT `fk_Grupo_has_Usuario_Grupo1` FOREIGN KEY (`grupo_id`) REFERENCES `Grupo` (`dono_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Grupo_has_Usuario_Usuario1` FOREIGN KEY (`usuario_id`) REFERENCES `Usuario` (`dono_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Grupo_has_Usuario`
--

LOCK TABLES `Grupo_has_Usuario` WRITE;
/*!40000 ALTER TABLE `Grupo_has_Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Grupo_has_Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tarefa`
--

DROP TABLE IF EXISTS `Tarefa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tarefa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `horario` time DEFAULT NULL,
  `titulo` varchar(30) NOT NULL,
  `descricao` varchar(80) DEFAULT NULL,
  `dono_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Tarefa_Dono1_idx` (`dono_id`),
  CONSTRAINT `fk_Tarefa_Dono1` FOREIGN KEY (`dono_id`) REFERENCES `Dono` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tarefa`
--

LOCK TABLES `Tarefa` WRITE;
/*!40000 ALTER TABLE `Tarefa` DISABLE KEYS */;
INSERT INTO `Tarefa` VALUES (1,'2018-11-11','12:12:00','Bater no thuza','uau!',11),(2,'2018-11-11','12:12:00','Batejjjr no thuza','uau!',11),(3,'2018-12-17','20:20:00','musica','sshsjs\n',11),(4,'2018-12-13','20:20:00','sjaja','hh',11),(5,'2018-11-14','20:20:00','dj','zhsh\n',11),(6,'2018-11-12','20:20:00','tjt','dvd\n',11),(7,'2018-12-06','20:20:00','okdh','hhhjhh\n',11),(8,'2019-01-03','12:00:00','bater no thuza','aproveitar e roubar uns pão de queijo da Dona Raquel.\n',11),(9,'2018-12-20','20:20:00','shsus','ok\n',11),(10,'2018-12-23','12:00:00','muuuuuu','ok',11),(11,'2018-12-24','20:20:00','nossaaaa','ikijui',11),(12,'2018-12-31','00:00:00','okok','ok',11),(13,'2018-12-25','12:30:00','natal','ok\n\n',11);
/*!40000 ALTER TABLE `Tarefa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `nome` varchar(45) NOT NULL,
  `login` varchar(45) NOT NULL,
  `senha` varchar(45) NOT NULL,
  `dono_id` int(11) NOT NULL,
  PRIMARY KEY (`dono_id`),
  UNIQUE KEY `login` (`login`),
  KEY `fk_Usuario_Dono1_idx` (`dono_id`),
  CONSTRAINT `fk_Usuario_Dono1` FOREIGN KEY (`dono_id`) REFERENCES `Dono` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES ('bxbx','x x ','dff',6),('Pedro','tutu','hoho',7),('oooo','ooo','hoho',8),('oooo22','ooo22','hoho',9),('ooo33o22','oo33o22','hoho',10),('hmmm','ok','hoho',11);
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-02 17:48:38
