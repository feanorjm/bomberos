-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: cmingenieria.mysql.pythonanywhere-services.com    Database: cmingenieria$qasbomberos
-- ------------------------------------------------------
-- Server version	5.6.27-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'grupo_obac'),(2,'grupo_tenientes');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,34),(2,1,35),(3,1,36),(22,1,40),(23,1,41),(24,1,42),(25,2,20),(7,2,28),(8,2,29),(9,2,30),(10,2,34),(11,2,35),(12,2,36),(13,2,40),(14,2,41),(15,2,42),(16,2,43),(17,2,44),(18,2,45),(19,2,52),(20,2,53),(21,2,54),(4,2,73),(5,2,74),(6,2,75);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add maquina',7,'add_maquina'),(20,'Can change maquina',7,'change_maquina'),(21,'Can delete maquina',7,'delete_maquina'),(22,'Can add usuario comp',8,'add_usuariocomp'),(23,'Can change usuario comp',8,'change_usuariocomp'),(24,'Can delete usuario comp',8,'delete_usuariocomp'),(25,'Can add compania',9,'add_compania'),(26,'Can change compania',9,'change_compania'),(27,'Can delete compania',9,'delete_compania'),(28,'Can add detalle_ maquina',10,'add_detalle_maquina'),(29,'Can change detalle_ maquina',10,'change_detalle_maquina'),(30,'Can delete detalle_ maquina',10,'delete_detalle_maquina'),(31,'Can add clasificacion_maquina',11,'add_clasificacion_maquina'),(32,'Can change clasificacion_maquina',11,'change_clasificacion_maquina'),(33,'Can delete clasificacion_maquina',11,'delete_clasificacion_maquina'),(34,'Can add bitacora',12,'add_bitacora'),(35,'Can change bitacora',12,'change_bitacora'),(36,'Can delete bitacora',12,'delete_bitacora'),(37,'Can add clave',13,'add_clave'),(38,'Can change clave',13,'change_clave'),(39,'Can delete clave',13,'delete_clave'),(40,'Can add carguios_combustible',14,'add_carguios_combustible'),(41,'Can change carguios_combustible',14,'change_carguios_combustible'),(42,'Can delete carguios_combustible',14,'delete_carguios_combustible'),(43,'Can add mantencion',15,'add_mantencion'),(44,'Can change mantencion',15,'change_mantencion'),(45,'Can delete mantencion',15,'delete_mantencion'),(46,'Can add tipo mantencion',16,'add_tipomantencion'),(47,'Can change tipo mantencion',16,'change_tipomantencion'),(48,'Can delete tipo mantencion',16,'delete_tipomantencion'),(49,'Can add conductor',17,'add_conductor'),(50,'Can change conductor',17,'change_conductor'),(51,'Can delete conductor',17,'delete_conductor'),(52,'Can add repuesto detalle mantencion',18,'add_repuestodetallemantencion'),(53,'Can change repuesto detalle mantencion',18,'change_repuestodetallemantencion'),(54,'Can delete repuesto detalle mantencion',18,'delete_repuestodetallemantencion'),(55,'Can add taller',19,'add_taller'),(56,'Can change taller',19,'change_taller'),(57,'Can delete taller',19,'delete_taller'),(58,'Can add division',20,'add_division'),(59,'Can change division',20,'change_division'),(60,'Can delete division',20,'delete_division'),(61,'Can add componente',21,'add_componente'),(62,'Can change componente',21,'change_componente'),(63,'Can delete componente',21,'delete_componente'),(64,'Can add subdivision',22,'add_subdivision'),(65,'Can change subdivision',22,'change_subdivision'),(66,'Can delete subdivision',22,'delete_subdivision'),(67,'Can add servicentro',23,'add_servicentro'),(68,'Can change servicentro',23,'change_servicentro'),(69,'Can delete servicentro',23,'delete_servicentro'),(70,'Can add servicio mantencion',24,'add_serviciomantencion'),(71,'Can change servicio mantencion',24,'change_serviciomantencion'),(72,'Can delete servicio mantencion',24,'delete_serviciomantencion'),(73,'Can add detalle mantencion',25,'add_detallemantencion'),(74,'Can change detalle mantencion',25,'change_detallemantencion'),(75,'Can delete detalle mantencion',25,'delete_detallemantencion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$HCznWHOLAa6Z$tkeSxTT2mn6P6uat2OUsnhrdI8wqOaEIKMxVQsjbp0U=','2017-08-11 22:55:01.235406',1,'admin','','','claudio.munoz@cmingenieria.cl',1,1,'2017-07-26 22:59:39.089776'),(2,'pbkdf2_sha256$36000$WW6dv8ZvZLRs$tTGet7KFCrRHX21v72zZKR+T5WH3+48QxCnUyud4fT8=','2017-08-10 03:04:46.311355',1,'fponce','Felipe','Ponce','',1,1,'2017-07-27 19:47:15.000000'),(3,'pbkdf2_sha256$36000$eYNvhuhXXWC1$vxY0O0HZSdGkh0G3rKL955BRfGw+kT5bSsK6KO9/G1c=','2017-07-31 18:06:19.544860',1,'vinigo','Victor','Iñigo','',1,1,'2017-07-27 19:48:50.000000'),(4,'pbkdf2_sha256$36000$L0ykW2wV8bWd$xyNMnYnxJhxOu9StaU3teWN6nVMnDFRt9R0IN6OCdAY=','2017-08-12 22:49:01.623115',0,'2da','Obac 2da compañia','','',0,1,'2017-07-27 19:51:32.000000'),(5,'pbkdf2_sha256$36000$Ccqs2QHNWn78$9bnrFLvP4si30bykAFTz68jGQ/Mp4ga+BApONGdFeGg=','2017-08-11 05:53:39.275589',0,'tte2da','Tte 2da compañia','','',0,1,'2017-07-27 19:54:22.000000'),(6,'pbkdf2_sha256$36000$ByraFo5RWn2b$N0hSCqvwmyPbjdZo9ZNjfYtdtg2i+QrTRA0Y87rUCRg=','2017-08-08 21:50:59.788729',0,'3ra','Obac 3ra compañia','','',0,1,'2017-07-27 19:55:51.000000'),(7,'pbkdf2_sha256$36000$4zJE9EpVkF10$00tPANeQSi12ILrFWxdaiOwHoO0V7emLzqGuB3hs29k=','2017-08-03 04:32:04.084690',0,'tte3ra','Tte 3ra compañia','','',0,1,'2017-07-27 19:57:30.000000'),(8,'pbkdf2_sha256$36000$WKxcZ0qdBQkI$EwSZfPq1cFo4f+lCGig6xCvq8rKDcve4EuGNceWw0MA=','2017-08-08 14:41:48.438692',0,'6ta','Obac 6ta compañia','','',0,1,'2017-07-27 20:00:38.000000'),(9,'pbkdf2_sha256$36000$T5UZOdpmdzq1$ai959MuVy6ichGyGybO9WY43xHNlLy6Hpvh3B51GIPY=','2017-08-13 01:16:00.458842',0,'tte6ta','Tte sexta compañia','','',0,1,'2017-07-27 20:01:12.000000'),(10,'pbkdf2_sha256$36000$qH2ci39jstEK$jsSTKhEA+e2/99XNEhrj5CxC779i4evECxBbbaEx/ow=','2017-08-09 13:55:08.159852',0,'capitan6','','','',0,1,'2017-08-08 21:17:38.573356'),(11,'pbkdf2_sha256$36000$C1DCEj1ozL2H$+6fOaZWvbLCjvZXGR9zjOybQ2F+TU5GzlG+rDrDc+lQ=','2017-08-09 22:37:30.618597',0,'capitan2','','','',0,1,'2017-08-09 13:33:01.455103'),(12,'pbkdf2_sha256$36000$DEkMgQqkUZH6$oumHBvBHjTfZ0vhtLB4hXEG7ogjkHNORR3xNQ8wXzrs=','2017-08-09 21:00:18.509244',0,'capitan3','','','',0,1,'2017-08-09 20:54:22.746723');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,4,1),(4,5,2),(2,6,1),(5,7,2),(3,8,1),(6,9,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,2,11),(12,2,12),(13,2,13),(14,2,14),(15,2,15),(16,2,16),(17,2,17),(18,2,18),(19,2,19),(20,2,20),(21,2,21),(22,2,22),(23,2,23),(24,2,24),(25,2,25),(26,2,26),(27,2,27),(28,2,28),(29,2,29),(30,2,30),(31,2,31),(32,2,32),(33,2,33),(34,2,34),(35,2,35),(36,2,36),(37,2,37),(38,2,38),(39,2,39),(40,2,40),(41,2,41),(42,2,42),(43,2,43),(44,2,44),(45,2,45),(46,2,46),(47,2,47),(48,2,48),(49,2,49),(50,2,50),(51,2,51),(52,2,52),(53,2,53),(54,2,54),(55,2,55),(56,2,56),(57,2,57),(58,2,58),(59,2,59),(60,2,60),(61,2,61),(62,2,62),(63,2,63),(64,2,64),(65,2,65),(66,2,66),(67,2,67),(68,2,68),(69,2,69),(70,2,70),(71,2,71),(72,2,72),(73,2,73),(74,2,74),(75,2,75);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-07-27 19:47:15.346105','2','fponce',1,'[{\"added\": {}}]',4,1),(2,'2017-07-27 19:48:05.508430','2','fponce',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(3,'2017-07-27 19:48:31.570354','2','fponce',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(4,'2017-07-27 19:48:50.394710','3','vinigo',1,'[{\"added\": {}}]',4,1),(5,'2017-07-27 19:49:12.080085','3','vinigo',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"is_staff\", \"is_superuser\"]}}]',4,1),(6,'2017-07-27 19:49:21.338188','2','fponce',2,'[{\"changed\": {\"fields\": [\"is_superuser\"]}}]',4,1),(7,'2017-07-27 19:51:32.870070','4','2da',1,'[{\"added\": {}}]',4,1),(8,'2017-07-27 19:51:57.394786','4','2da',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(9,'2017-07-27 19:54:22.449245','5','tte3da',1,'[{\"added\": {}}]',4,1),(10,'2017-07-27 19:54:49.508260','5','tte3da',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(11,'2017-07-27 19:55:19.300088','5','tte2da',2,'[{\"changed\": {\"fields\": [\"username\"]}}]',4,1),(12,'2017-07-27 19:55:51.597271','6','3ra',1,'[{\"added\": {}}]',4,1),(13,'2017-07-27 19:56:10.718713','6','3ra',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(14,'2017-07-27 19:56:26.428715','4','2da',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(15,'2017-07-27 19:56:46.950178','5','tte2da',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(16,'2017-07-27 19:57:30.166712','7','tte3ra',1,'[{\"added\": {}}]',4,1),(17,'2017-07-27 20:00:05.554543','7','tte3ra',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(18,'2017-07-27 20:00:38.649010','8','6ta',1,'[{\"added\": {}}]',4,1),(19,'2017-07-27 20:00:50.917081','8','6ta',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(20,'2017-07-27 20:01:13.089590','9','tte6ta',1,'[{\"added\": {}}]',4,1),(21,'2017-07-27 20:01:50.099638','9','tte6ta',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,1),(22,'2017-07-27 20:02:32.151625','1','fponce',1,'[{\"added\": {}}]',8,1),(23,'2017-07-27 20:02:44.407478','2','vinigo',1,'[{\"added\": {}}]',8,1),(24,'2017-07-27 20:02:53.814624','3','2da',1,'[{\"added\": {}}]',8,1),(25,'2017-07-27 20:03:00.959899','4','3ra',1,'[{\"added\": {}}]',8,1),(26,'2017-07-27 20:03:07.576349','5','6ta',1,'[{\"added\": {}}]',8,1),(27,'2017-07-27 20:03:18.744094','6','tte2da',1,'[{\"added\": {}}]',8,1),(28,'2017-07-27 20:03:30.438061','7','tte3ra',1,'[{\"added\": {}}]',8,1),(29,'2017-07-27 20:03:40.719758','8','tte6ta',1,'[{\"added\": {}}]',8,1),(30,'2017-07-27 20:04:09.230889','9','admin',1,'[{\"added\": {}}]',8,1),(31,'2017-07-27 20:15:32.942781','1','grupo_obac',1,'[{\"added\": {}}]',2,1),(32,'2017-07-27 20:15:53.601246','4','2da',2,'[]',4,1),(33,'2017-07-27 20:16:04.823011','6','3ra',2,'[]',4,1),(34,'2017-07-27 20:16:21.159038','8','6ta',2,'[]',4,1),(35,'2017-07-27 20:43:28.202665','2','grupo_tenientes',1,'[{\"added\": {}}]',2,1),(36,'2017-07-27 20:43:48.450960','1','grupo_obac',2,'[]',2,1),(37,'2017-07-27 20:44:15.807003','5','tte2da',2,'[]',4,1),(38,'2017-07-27 20:44:26.946328','7','tte3ra',2,'[]',4,1),(39,'2017-07-27 20:44:37.769583','9','tte6ta',2,'[]',4,1),(40,'2017-07-27 20:48:23.904026','2','grupo_tenientes',2,'[]',2,1),(41,'2017-07-28 16:29:07.334579','1','Estroboscopico',1,'[{\"added\": {}}]',24,1),(42,'2017-07-31 22:50:54.905954','32','sellos',1,'[{\"added\": {}}]',22,2),(43,'2017-07-31 22:51:09.731561','32','sellos',2,'[]',22,2),(44,'2017-07-31 22:51:19.743298','33','Gomas',1,'[{\"added\": {}}]',22,2),(45,'2017-07-31 22:51:28.863712','32','sellos',2,'[]',22,2),(46,'2017-07-31 22:54:13.591317','34','SELLOS',1,'[{\"added\": {}}]',22,2),(47,'2017-07-31 22:54:24.343349','34','SELLOS',2,'[]',22,2),(48,'2017-07-31 22:55:28.234127','34','SELLOS',3,'',22,2),(49,'2017-07-31 22:56:01.525435','35','Gomas',1,'[{\"added\": {}}]',22,2),(50,'2017-07-31 22:56:08.014043','35','Gomas',3,'',22,2),(51,'2017-07-31 23:05:07.430427','36','COMPARTIMIENTOS',1,'[{\"added\": {}}]',22,2),(52,'2017-07-31 23:05:50.826104','33','Gomas',3,'',22,2),(53,'2017-07-31 23:05:50.833993','32','sellos',3,'',22,2),(54,'2017-08-01 00:55:54.709449','37','SELLOS',1,'[{\"added\": {}}]',22,2),(55,'2017-08-01 00:56:13.308021','38','RODAMIENTOS BOMBA',1,'[{\"added\": {}}]',22,2),(56,'2017-08-01 00:56:35.359699','39','CARDAN BOMBA',1,'[{\"added\": {}}]',22,2),(57,'2017-08-01 00:56:35.377840','21','2da Compañía - B-2 - 2017-06-30 - 10--4 - RESCATE VEHICULAR',3,'',12,1),(58,'2017-08-01 00:56:35.385011','20','2da Compañía - B-2 - 2017-06-29 - 10--6 - EMANACION DE GASES',3,'',12,1),(59,'2017-08-01 00:56:35.391865','19','2da Compañía - B-2 - 2017-06-28 - 6--13 - OTRO SERVICIO',3,'',12,1),(60,'2017-08-01 00:56:35.407156','18','2da Compañía - B-2 - 2017-06-28 - 10--9 - LLAMADO OTRO SERVICIO',3,'',12,1),(61,'2017-08-01 00:56:35.457847','17','2da Compañía - B-2 - 2017-06-24 - 10--6 - EMANACION DE GASES',3,'',12,1),(62,'2017-08-01 00:56:35.466991','16','2da Compañía - B-2 - 2017-06-24 - 10--7 - LLAMADO ELECTRICO',3,'',12,1),(63,'2017-08-01 00:56:35.473828','15','2da Compañía - B-2 - 2017-06-22 - 10--4 - RESCATE VEHICULAR',3,'',12,1),(64,'2017-08-01 00:56:35.480429','14','2da Compañía - B-2 - 2017-06-17 - 10--5 - LLAMADO HAZ-MAT',3,'',12,1),(65,'2017-08-01 00:56:35.488648','13','2da Compañía - B-2 - 2017-06-09 - 6--13 - OTRO SERVICIO',3,'',12,1),(66,'2017-08-01 00:56:35.499493','12','2da Compañía - B-2 - 2017-06-09 - 10--5 - LLAMADO HAZ-MAT',3,'',12,1),(67,'2017-08-01 00:56:35.510427','11','2da Compañía - B-2 - 2017-06-08 - 10--0 - LLAMADO ESTRUCTURAL',3,'',12,1),(68,'2017-08-01 00:56:35.519303','10','2da Compañía - B-2 - 2017-06-06 - 6--13 - OTRO SERVICIO',3,'',12,1),(69,'2017-08-01 00:56:35.528612','9','2da Compañía - B-2 - 2017-06-04 - 10--4 - RESCATE VEHICULAR',3,'',12,1),(70,'2017-08-01 00:56:35.535088','8','2da Compañía - B-2 - 2017-06-03 - 6--13 - OTRO SERVICIO',3,'',12,1),(71,'2017-08-01 00:56:35.543589','7','2da Compañía - B-2 - 2017-06-03 - 10--14 - INCENDIO',3,'',12,1),(72,'2017-08-01 00:56:35.550937','6','2da Compañía - B-2 - 2017-06-01 - 6--17 - EJERCICIO DE COMPAÑÍA',3,'',12,1),(73,'2017-08-01 00:56:57.274861','7','B-3-33',3,'',15,1),(74,'2017-08-01 00:56:57.281497','6','M-4-ccc',3,'',15,1),(75,'2017-08-01 00:56:57.287599','5','B-1-7777',3,'',15,1),(76,'2017-08-01 04:17:33.773668','125','Camilo Carrasco',2,'[{\"changed\": {\"fields\": [\"nombre\", \"ap_paterno\", \"ap_materno\"]}}]',17,1),(77,'2017-08-01 04:19:21.766819','127','Carlos Barria',2,'[{\"changed\": {\"fields\": [\"nombre\", \"ap_paterno\", \"ap_materno\"]}}]',17,1),(78,'2017-08-01 04:19:51.012458','126','Rene Aviles',2,'[{\"changed\": {\"fields\": [\"nombre\", \"ap_paterno\", \"ap_materno\"]}}]',17,1),(79,'2017-08-01 04:20:09.874321','124','Ricardo Flores',2,'[{\"changed\": {\"fields\": [\"nombre\", \"ap_paterno\", \"ap_materno\"]}}]',17,1),(80,'2017-08-04 20:40:05.076594','40','CUERPO BOMBA',1,'[{\"added\": {}}]',22,1),(81,'2017-08-04 20:40:24.777096','2','ENGRASE BOMBA',1,'[{\"added\": {}}]',24,1),(82,'2017-08-04 20:48:55.417116','3','CAMBIO ACEITE',1,'[{\"added\": {}}]',24,1),(83,'2017-08-08 01:17:46.606065','36','K-2',3,'',7,1),(84,'2017-08-08 21:08:57.682862','2','MANIFOR',2,'[{\"changed\": {\"fields\": [\"nombre\"]}}]',22,2),(85,'2017-08-08 21:17:38.630986','10','capitan6',1,'[{\"added\": {}}]',4,2),(86,'2017-08-08 21:19:15.181191','10','capitan6',1,'[{\"added\": {}}]',8,2),(87,'2017-08-09 13:33:01.671098','11','capitan2',1,'[{\"added\": {}}]',4,2),(88,'2017-08-09 13:33:11.499440','11','capitan2',1,'[{\"added\": {}}]',8,2),(89,'2017-08-09 20:54:22.811236','12','capitan3',1,'[{\"added\": {}}]',4,2),(90,'2017-08-09 20:55:17.799594','12','capitan3',1,'[{\"added\": {}}]',8,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'maintenance','bitacora'),(14,'maintenance','carguios_combustible'),(11,'maintenance','clasificacion_maquina'),(13,'maintenance','clave'),(9,'maintenance','compania'),(21,'maintenance','componente'),(17,'maintenance','conductor'),(25,'maintenance','detallemantencion'),(10,'maintenance','detalle_maquina'),(20,'maintenance','division'),(15,'maintenance','mantencion'),(7,'maintenance','maquina'),(18,'maintenance','repuestodetallemantencion'),(23,'maintenance','servicentro'),(24,'maintenance','serviciomantencion'),(22,'maintenance','subdivision'),(19,'maintenance','taller'),(16,'maintenance','tipomantencion'),(8,'maintenance','usuariocomp'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-07-26 22:29:28.536333'),(2,'auth','0001_initial','2017-07-26 22:29:31.569419'),(3,'admin','0001_initial','2017-07-26 22:29:32.434138'),(4,'admin','0002_logentry_remove_auto_add','2017-07-26 22:29:32.464574'),(5,'contenttypes','0002_remove_content_type_name','2017-07-26 22:29:32.600596'),(6,'auth','0002_alter_permission_name_max_length','2017-07-26 22:29:32.659437'),(7,'auth','0003_alter_user_email_max_length','2017-07-26 22:29:32.717090'),(8,'auth','0004_alter_user_username_opts','2017-07-26 22:29:32.735282'),(9,'auth','0005_alter_user_last_login_null','2017-07-26 22:29:32.808433'),(10,'auth','0006_require_contenttypes_0002','2017-07-26 22:29:32.820799'),(11,'auth','0007_alter_validators_add_error_messages','2017-07-26 22:29:32.837443'),(12,'auth','0008_alter_user_username_max_length','2017-07-26 22:29:32.898506'),(13,'maintenance','0001_initial','2017-07-26 22:29:35.513057'),(14,'maintenance','0002_clasificacion_maquina_descripcion','2017-07-26 22:29:35.655778'),(15,'sessions','0001_initial','2017-07-26 22:29:35.990177'),(16,'maintenance','0003_auto_20170726_1832','2017-07-26 22:32:38.631503'),(17,'maintenance','0004_auto_20170728_0128','2017-07-28 05:29:06.408483'),(18,'maintenance','0005_auto_20170802_2218','2017-08-03 02:18:55.534627'),(19,'maintenance','0006_auto_20170808_0321','2017-08-08 07:21:26.303908'),(20,'maintenance','0007_auto_20170809_0030','2017-08-09 04:30:27.022750'),(21,'maintenance','0008_auto_20170809_0102','2017-08-09 05:02:36.344738');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('15kzsqau2syz8tj6i8i50w86j8ww6evr','MmRhNThjNGY4NWRiMTU2NDk4ZDQ1YThjMWNhNGQwZWE1ZmJkYTY5ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9oYXNoIjoiNjU1ODI4ZWQxMjcyMDk5NjQzZmIzNzU5MDg5MTdhNWJmZGRkYjMyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-26 22:49:02.212733'),('1mvd9u5ylyi236hauuuv05p717bhdclq','MTBhNGIxNWRhZTk0MzI0MDYxNDY0MDk3NmUyODg4ZWY4NjEwZTk2ODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjU1ODI4ZWQxMjcyMDk5NjQzZmIzNzU5MDg5MTdhNWJmZGRkYjMyOCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2017-08-17 22:31:29.688490'),('3d4jre1ambqhaa9r6gb1y5t2r02m9s6j','YjJhZWIwYjg4MzA3ZjQ4MWI0NmIzOWE1ZjgxODlkZTU2NTAzMTdjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU4MjhlZDEyNzIwOTk2NDNmYjM3NTkwODkxN2E1YmZkZGRiMzI4In0=','2017-08-14 14:07:27.981179'),('3nj8qe6372muufvkepap5wjh2l0gxxsg','MThhODU5M2RhODU4MDNhYzNjYjFhNDExM2I2NzljZTcxZGRjZjcwNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWI0MGJjZjBlZDViOWU2MmY5MjcwZDZhZGMzYjc4YzEyOTIxMGM0OSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-10 00:58:25.962831'),('3q40hi7u0ahtic5ct2uwkqxacfth6igf','NzIzZDQ5ZjdlNjVkODZmNjVhMDliYzFhNmQ3YTY0OWJhODFjZDg3MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-22 15:32:24.213140'),('4c17mtro1au6mtgzgobrd0ax31p24rmb','OGU5ZjM3ZmY1NWRlZmZjYWQ2ZjYxZmFlZTU5ZTM0ZmQzMWM5YTg1Njp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2E2ZjQzN2Q2MzgyZThjMjNmYWVkOTM4NzcyMmJiZDhmZjgxMTVkMiJ9','2017-08-23 22:37:30.626211'),('4edwz34rzy8dl9rkllm4ut6h86savkpl','YzE0NTBiNDI4MjY3MDFkMGFmMTVhYmY1MDVlOTU2MmJjZjM3ZWI1Nzp7Il9hdXRoX3VzZXJfaGFzaCI6ImExYjI2YTM1MDQwZTEzNDlmZDViMzlhN2M5MzRlN2I4N2Q1OWExZDAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI5In0=','2017-08-22 20:57:54.518133'),('4lax2l8baknpla582jgno9rpg5q6m9mf','ZmRjNzI1ZjI5ZTYzZDc5YWI1MzFlYTI2MDJiNWE0NGVjOGZjYTEyNjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTZlYWIyMDg3ZTJmYzE2YTNjYzc3MGQxNjg2NGU5ZjM2YTY3MzlkIn0=','2017-08-24 03:04:46.343559'),('5ewgvqn1w88a570qfs740pi6lvjaljq7','NzIzZDQ5ZjdlNjVkODZmNjVhMDliYzFhNmQ3YTY0OWJhODFjZDg3MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-22 17:14:51.184378'),('6x95e2fr1l4axfyu67lmb2ocyc0hi2ks','NzE3YjllZDRkNGRiY2JkMmQ3MWJlMTQ1Y2MyODA1ODAzNTcyMzcxMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNhNmVhYjIwODdlMmZjMTZhM2NjNzcwZDE2ODY0ZTlmMzZhNjczOWQiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-15 17:02:17.264562'),('92ufq6mf6ywuhoy9v58ekapj0gzfws6w','NTdkMjQ4Y2YyNTg3NTY1NTQwYzcxZjBjMjljMTgxNDY3OTNmMWM1Yjp7Il9hdXRoX3VzZXJfaGFzaCI6ImExYjI2YTM1MDQwZTEzNDlmZDViMzlhN2M5MzRlN2I4N2Q1OWExZDAiLCJfYXV0aF91c2VyX2lkIjoiOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-15 16:58:05.341636'),('a218ta935rotlv45o45kqv3b03h9r95f','YjJhZWIwYjg4MzA3ZjQ4MWI0NmIzOWE1ZjgxODlkZTU2NTAzMTdjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU4MjhlZDEyNzIwOTk2NDNmYjM3NTkwODkxN2E1YmZkZGRiMzI4In0=','2017-08-11 21:23:32.627367'),('b41per8ugckgp6cw8wnyiohlsg8xf5sv','MTJmNjZlZmEyZDViM2E2OTEyNWUzOTFiMmM1YTg3OGYwYWFlYzc4Nzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjkiLCJfYXV0aF91c2VyX2hhc2giOiJhMWIyNmEzNTA0MGUxMzQ5ZmQ1YjM5YTdjOTM0ZTdiODdkNTlhMWQwIn0=','2017-08-11 21:23:00.380186'),('b5bleokp199z7n84mibqqlpoq91oi9zs','MWI5NGJmMGUwMjBjNmFhNTNmY2FjYWRjZGIxYjgzZjQzMzM2NmY2OTp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-25 00:53:36.365129'),('dfj5hrv0ysik0ey8sk475ukwnzr76mfj','YjJhZWIwYjg4MzA3ZjQ4MWI0NmIzOWE1ZjgxODlkZTU2NTAzMTdjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU4MjhlZDEyNzIwOTk2NDNmYjM3NTkwODkxN2E1YmZkZGRiMzI4In0=','2017-08-14 21:29:20.964762'),('eme1bbg7wmwi8lb31tpxp4ycfz50dfwd','MWI5NGJmMGUwMjBjNmFhNTNmY2FjYWRjZGIxYjgzZjQzMzM2NmY2OTp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-25 21:54:18.612236'),('henhvn9lagni3xz3o2guah0zrom261vy','YjJhZWIwYjg4MzA3ZjQ4MWI0NmIzOWE1ZjgxODlkZTU2NTAzMTdjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU4MjhlZDEyNzIwOTk2NDNmYjM3NTkwODkxN2E1YmZkZGRiMzI4In0=','2017-08-11 21:24:33.459672'),('iy58du5fia5tmpg93nortn4z3j1h3gs3','MzVjODgyZGI1ZTBlZjcxMzM4OTIyZGZhMGQ4ZTUyMzA2MjQ5MjA2Yjp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9oYXNoIjoiYTFiMjZhMzUwNDBlMTM0OWZkNWIzOWE3YzkzNGU3Yjg3ZDU5YTFkMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-27 00:01:59.431879'),('j6kd6lfoiv7mvzxi6b9deuereahiersx','ZmRjNzI1ZjI5ZTYzZDc5YWI1MzFlYTI2MDJiNWE0NGVjOGZjYTEyNjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTZlYWIyMDg3ZTJmYzE2YTNjYzc3MGQxNjg2NGU5ZjM2YTY3MzlkIn0=','2017-08-23 20:55:33.862375'),('juc7sl4smukxoo8xhtxrjyujanrl0sh6','YjJhZWIwYjg4MzA3ZjQ4MWI0NmIzOWE1ZjgxODlkZTU2NTAzMTdjNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU4MjhlZDEyNzIwOTk2NDNmYjM3NTkwODkxN2E1YmZkZGRiMzI4In0=','2017-08-14 04:45:06.176087'),('lip4evmr4vpzrkhsro1dvg9aoftzj2u5','MTg1ZTJhNDU3YjA3YTNlYTRjNzA4MjE5NzcxY2VlMTUxZDQ1NDYxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjQwYmNmMGVkNWI5ZTYyZjkyNzBkNmFkYzNiNzhjMTI5MjEwYzQ5In0=','2017-08-09 23:11:18.074794'),('mdcfmi2en514wioo3nmci7zdiuhvbf63','MWI5NGJmMGUwMjBjNmFhNTNmY2FjYWRjZGIxYjgzZjQzMzM2NmY2OTp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-19 02:31:05.465050'),('mjonp0w9ca45bvneicz22ejjjyao201c','NzE3YjllZDRkNGRiY2JkMmQ3MWJlMTQ1Y2MyODA1ODAzNTcyMzcxMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNhNmVhYjIwODdlMmZjMTZhM2NjNzcwZDE2ODY0ZTlmMzZhNjczOWQiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-18 20:06:07.146049'),('n55gmpmqzthzsazbpyad97sz4f0t9s9j','MWI5NGJmMGUwMjBjNmFhNTNmY2FjYWRjZGIxYjgzZjQzMzM2NmY2OTp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-21 18:05:08.767682'),('ny8rsz5jgpcdjb0192vowzlsr92ebs4t','MDk3YmMwM2U2NWY2NTRjYmE5NDU3NjA5ZjYzOGE2N2E4MTgwMzkwNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiJlYjQwYmNmMGVkNWI5ZTYyZjkyNzBkNmFkYzNiNzhjMTI5MjEwYzQ5In0=','2017-08-22 04:47:52.525665'),('obc4hfjel6cpt4jhh4b00l0496tceu8i','ZDYwZGFlNTQ0YmRkOTI0NGRhNzI4NzkwZGU1M2RmOTVkNGNhMjJkOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjM1YmE2OTYyZDVlNTVkMDAzNzYwYWU4ZTJhNDhiYzA4YTcyODA2NjAiLCJfYXV0aF91c2VyX2lkIjoiNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-15 16:19:09.859415'),('ocvv893s9n89o0srmrt8bsqctdhze716','MTg1ZTJhNDU3YjA3YTNlYTRjNzA4MjE5NzcxY2VlMTUxZDQ1NDYxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjQwYmNmMGVkNWI5ZTYyZjkyNzBkNmFkYzNiNzhjMTI5MjEwYzQ5In0=','2017-08-09 23:10:29.376678'),('pdqc3aep6lfxqs35xgxedqntytvgede9','MThhODU5M2RhODU4MDNhYzNjYjFhNDExM2I2NzljZTcxZGRjZjcwNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWI0MGJjZjBlZDViOWU2MmY5MjcwZDZhZGMzYjc4YzEyOTIxMGM0OSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-10 13:15:39.095482'),('qp8d3mry3bwi482mks3h7uti6aclbo49','MDk3YmMwM2U2NWY2NTRjYmE5NDU3NjA5ZjYzOGE2N2E4MTgwMzkwNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiJlYjQwYmNmMGVkNWI5ZTYyZjkyNzBkNmFkYzNiNzhjMTI5MjEwYzQ5In0=','2017-08-22 04:50:38.775356'),('rquf1bcrmw2tjipcg57ukw2dzw13dymy','M2ZlZjRiMTNiNTY2N2MzN2M4MGVjZThlZjE4YzViYjhmNDgyM2MzYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjUiLCJfYXV0aF91c2VyX2hhc2giOiI1NTBmMjUxZjM4M2VjZTM4YjE5ZDE2ZWZiYzk2NjJkOWYzOTEyMDZhIn0=','2017-08-14 04:50:55.845436'),('rygdglt1xqzq2oco1mzdglk91znqwas3','MTg1ZTJhNDU3YjA3YTNlYTRjNzA4MjE5NzcxY2VlMTUxZDQ1NDYxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjQwYmNmMGVkNWI5ZTYyZjkyNzBkNmFkYzNiNzhjMTI5MjEwYzQ5In0=','2017-08-09 23:12:47.698122'),('vh7t6nk1awq6kbcyjzrii9qqh663f4z0','YmIwOTY2MWI3MTRhMjU3NDk2MjRiODcxN2ZiYzM4MjAxMGIxN2YxYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmFmMTA0OTIzYjdlYjZlYjdhMTI3YzkxOTA0YTEzZTM2NmYyODExMiIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2017-08-10 20:26:52.233340'),('vlwrws50hyzjlssuw3vajwla4vgvirqd','ODljN2E3YjUzYTAwNWE0ZjYzNjI1ZjAxNTQ0ZmIxZjIzNDAyMWVhMTp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODM5OTljYzkzZGIxNDE1Zjg0YjhlN2RhYzMyYTc3OTY2YzgyY2MwMiJ9','2017-08-23 21:00:18.516935'),('vu1nrdjj562ugp04ry7zwyre8v2ms8ec','NzE3YjllZDRkNGRiY2JkMmQ3MWJlMTQ1Y2MyODA1ODAzNTcyMzcxMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNhNmVhYjIwODdlMmZjMTZhM2NjNzcwZDE2ODY0ZTlmMzZhNjczOWQiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-20 22:19:02.468226'),('vy7nfoi0wq3b330dpnsm21dkwy9df8y9','ZjE4ZWE5ZTkxMWUwMWNkZTU0MzdhNzA2NzJkZmVhM2QzNDY4YzQzMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2hhc2giOiIyYWYxMDQ5MjNiN2ViNmViN2ExMjdjOTE5MDRhMTNlMzY2ZjI4MTEyIn0=','2017-08-14 18:06:19.553686'),('wms7rk0prc3xdtrhtz6ihrv4ceubk0ma','MWI5NGJmMGUwMjBjNmFhNTNmY2FjYWRjZGIxYjgzZjQzMzM2NmY2OTp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-25 22:55:01.247645'),('x8ip9m1tgmkjfg3p2a3jjz84l6kwptuy','NzIzZDQ5ZjdlNjVkODZmNjVhMDliYzFhNmQ3YTY0OWJhODFjZDg3MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImViNDBiY2YwZWQ1YjllNjJmOTI3MGQ2YWRjM2I3OGMxMjkyMTBjNDkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-22 17:24:10.836055'),('xuf5zftjzgpqz8ezvec2suid3ydgpqhg','ODI2NzJlZmRkMjkwOTRlY2Y5OWU3NzE4YjAzZTljMzU5MDVjY2VmMDp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMWIyNmEzNTA0MGUxMzQ5ZmQ1YjM5YTdjOTM0ZTdiODdkNTlhMWQwIn0=','2017-08-24 01:58:08.455817'),('zk8ioor4nu0hz4v65ghfm829tfz9hguq','M2ZlZjRiMTNiNTY2N2MzN2M4MGVjZThlZjE4YzViYjhmNDgyM2MzYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjUiLCJfYXV0aF91c2VyX2hhc2giOiI1NTBmMjUxZjM4M2VjZTM4YjE5ZDE2ZWZiYzk2NjJkOWYzOTEyMDZhIn0=','2017-08-14 05:10:36.012798'),('zq8jkk2hvjmmsgdu3knnz2ozs7j70dyu','MmRhNThjNGY4NWRiMTU2NDk4ZDQ1YThjMWNhNGQwZWE1ZmJkYTY5ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9oYXNoIjoiNjU1ODI4ZWQxMjcyMDk5NjQzZmIzNzU5MDg5MTdhNWJmZGRkYjMyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-08-16 19:25:38.078267');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_bitacora`
--

DROP TABLE IF EXISTS `maintenance_bitacora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_bitacora` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` varchar(100) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora_salida` time(6) DEFAULT NULL,
  `hora_llegada` time(6) DEFAULT NULL,
  `kilometraje_salida` decimal(10,1) DEFAULT NULL,
  `kilometraje_llegada` decimal(10,1) DEFAULT NULL,
  `hodometro_salida` decimal(10,1) DEFAULT NULL,
  `hodometro_llegada` decimal(10,1) DEFAULT NULL,
  `ho_bomba_salida` decimal(10,1) DEFAULT NULL,
  `ho_bomba_regreso` decimal(10,1) DEFAULT NULL,
  `observciones` longtext,
  `clave_id` int(11) DEFAULT NULL,
  `compania_id` int(11) NOT NULL,
  `conductor_id` int(11) DEFAULT NULL,
  `maquina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_bitacora_clave_id_dc52c7ba_fk_maintenance_clave_id` (`clave_id`),
  KEY `maintenance_bitacora_compania_id_489ec387_fk_maintenan` (`compania_id`),
  KEY `maintenance_bitacora_conductor_id_fecd3f7b` (`conductor_id`),
  KEY `maintenance_bitacora_maquina_id_c6ed232e` (`maquina_id`),
  CONSTRAINT `maintenance_bitacora_clave_id_dc52c7ba_fk_maintenance_clave_id` FOREIGN KEY (`clave_id`) REFERENCES `maintenance_clave` (`id`),
  CONSTRAINT `maintenance_bitacora_compania_id_489ec387_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`),
  CONSTRAINT `maintenance_bitacora_conductor_id_fecd3f7b_fk_maintenan` FOREIGN KEY (`conductor_id`) REFERENCES `maintenance_conductor` (`id`),
  CONSTRAINT `maintenance_bitacora_maquina_id_c6ed232e_fk_maintenan` FOREIGN KEY (`maquina_id`) REFERENCES `maintenance_maquina` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_bitacora`
--

LOCK TABLES `maintenance_bitacora` WRITE;
/*!40000 ALTER TABLE `maintenance_bitacora` DISABLE KEYS */;
INSERT INTO `maintenance_bitacora` VALUES (28,'ruta 215 km 10 cruce las lumas 357','2017-08-01','09:10:00.000000','10:30:00.000000',4669.0,4705.2,331.4,332.0,45.3,45.3,'sin observaciones',21,2,124,17),(29,'Ruta 215 KM 10 cruce Las Lumas 357','2017-08-01','09:10:00.000000','10:11:00.000000',8476.0,8527.6,343.0,345.0,44.0,44.0,'s/o',21,3,61,20),(30,'Ruta 215 KM 10 cruce Las Lumas 357','2017-08-01','09:10:00.000000','10:11:00.000000',22524.0,22558.0,0.0,0.0,NULL,NULL,'Neumáticos delanteros con daño en banda de rodado',21,3,67,21),(31,'San Mateo 1970','2017-08-01','11:51:00.000000','12:43:00.000000',38899.0,38905.0,1019.0,1020.3,991.0,991.6,'Sin observaciones',20,6,126,26),(32,'San Mateo 1970','2017-08-01','11:51:00.000000','12:43:00.000000',41876.0,41882.0,2584.0,2585.4,0.0,0.8,'Sin Observaciones',20,6,127,37),(33,'Diego de Almagro 1958','2017-08-01','14:55:00.000000','15:16:00.000000',8527.6,8533.7,345.0,346.0,44.0,44.0,'S/O',19,3,61,20),(34,'Centro de Mantenimieto CBO','2017-08-02','18:59:00.000000','19:19:00.000000',41882.0,41886.0,2585.4,2585.9,0.8,0.8,'Móvil fuera de servicio en Centro de Mantenimiento',1,6,126,37),(35,'Hanga Roa 826','2017-08-02','20:05:00.000000','20:51:00.000000',4705.2,4710.4,332.0,332.1,45.3,45.3,'SIN OBSERVACIONES',13,2,45,17),(36,'ANGAROA #826','2017-08-02','20:05:00.000000','20:51:00.000000',15594.5,15599.5,2571.9,2572.7,711.1,719.8,'SIN OBSERVACIONES',13,2,47,16),(37,'Antofagasta 464','2017-08-02','20:20:00.000000','21:10:00.000000',38905.0,38905.4,1020.3,1020.6,991.6,991.8,'Sin Novedad',5,6,127,26),(38,'Antofagasta 464','2017-08-02','20:20:00.000000','21:10:00.000000',33118.6,33118.6,3362.5,3363.1,649.5,649.6,'Sirena no funciona',5,6,128,27),(39,'Villa Los Aromos','2017-08-02','20:00:00.000000','22:15:00.000000',14257.1,14263.0,2623.0,2625.3,693.0,693.9,'S/O',5,3,63,19),(40,'Villa Los Aromos','2017-08-02','20:00:00.000000','22:15:00.000000',8533.7,8551.8,346.0,347.0,44.0,45.0,'S/O',5,3,68,20),(41,'Villa Los Aromos','2017-08-02','20:00:00.000000','22:15:00.000000',22558.0,22566.0,0.0,0.8,NULL,NULL,'S/O',5,3,65,21),(42,'Puerto Octay','2017-08-02','19:50:00.000000','04:20:00.000000',39083.8,39193.8,0.0,8.8,712.0,712.0,'Apoyo a 10-5 volcamiento de camión con 15 tambores de 208lt con Formalina al 37%\r\nSe incorporo horometro de horas motor al carro',18,2,41,18),(43,'COPEC - BULNES 522','2017-08-03','00:00:00.000000','00:00:00.000000',39193.8,39196.0,8.8,9.3,712.0,712.0,'Carga combustible de 54 litros, valor: $26838, obac: Cristian Riquelme, boucher TCT: 572154694',2,2,41,18),(44,'planta skretting panamericana sur 729','2017-08-03','14:50:00.000000','16:10:00.000000',39196.0,39205.0,9.3,10.6,712.0,719.6,'sin observaciones',1,2,124,18),(45,'Lastarria esquina Los Carrara','2017-08-03','21:22:00.000000','22:00:00.000000',39205.0,39209.9,10.6,11.1,719.6,719.6,'Colisión con derrame.',11,2,124,18),(46,'acapulco sin numero','2017-08-04','10:17:00.000000','11:07:00.000000',38905.4,38913.0,1020.6,1021.0,991.8,992.3,'sin observaciones',7,6,127,26),(47,'wuenumapu 2544','2017-08-04','11:31:00.000000','12:39:00.000000',38913.0,38921.0,1021.0,1021.8,992.3,993.1,'sin obeservacion',19,6,127,26),(48,'cuartel segunda compañia','2017-08-04','12:49:00.000000','13:04:00.000000',38921.0,38925.0,1021.8,1021.8,993.1,993.1,'sin obeservacion',1,6,127,26),(49,'Ohiggins 909','2017-08-04','17:51:00.000000','17:58:00.000000',4710.4,4710.4,332.1,332.2,45.3,45.3,'Mantenimiento y Funcionamiento',1,2,39,17),(50,'cochrane esq casanova','2017-08-04','19:45:00.000000','20:10:00.000000',39209.9,39212.2,11.1,11.5,719.6,719.6,'no',12,2,124,18),(51,'Sector 3','2017-08-04','19:15:00.000000','20:45:00.000000',8551.8,8563.0,347.0,349.0,45.0,45.0,'S/O',1,3,67,20),(52,'Arturo Prat','2017-08-04','20:30:00.000000','21:40:00.000000',15599.5,15601.5,2572.7,2573.6,719.8,719.9,'Cortina de agua voluntario insigne Enrique Luegmayer',5,2,125,16),(53,'Arturo Prat','2017-08-04','20:30:00.000000','21:40:00.000000',4710.4,4712.4,332.2,332.5,45.3,45.3,'Cortina de agua Vol. Insigne Enrique Luegmayer',5,2,52,17),(54,'Cesar Ercilla esquina Los Carrera','2017-08-05','14:59:00.000000','15:30:00.000000',39212.2,39218.4,11.5,11.9,719.6,719.7,'Rescate con derrame de combustible',11,2,52,18),(55,'costanera francke','2017-08-05','14:04:00.000000','15:10:00.000000',38925.0,38934.0,1021.8,1022.0,993.1,993.1,'sin observaciones',1,6,96,26),(56,'portal del mar, población lagos del sur','2017-08-05','17:20:00.000000','18:27:00.000000',38934.0,38942.0,1022.0,1022.3,993.1,993.6,'sin obeservaciones',7,6,95,26),(57,'Santa Paulina Ovejeria Alto','2017-08-05','19:50:00.000000','20:57:00.000000',15601.5,15606.1,2573.6,2574.5,719.9,720.5,'S/O',20,2,125,16),(58,'Santa Paulina Ovejeria Alto','2017-08-05','19:50:00.000000','20:58:00.000000',39218.4,39223.0,11.9,13.0,719.7,720.2,'S/O',20,2,51,18),(59,'Avda. Costanera Francke','2017-08-05','14:30:00.000000','20:10:00.000000',8563.0,8674.0,349.0,354.0,45.0,47.0,'S/O',6,3,68,20),(60,'Avda. Costanera Francke','2017-08-05','14:30:00.000000','20:10:00.000000',22566.0,22586.0,0.8,4.5,NULL,NULL,'S/O',6,3,129,21),(61,'COPEC - JUAN MACKENNA 2019','2017-08-05','00:00:00.000000','00:00:00.000000',8674.0,8676.0,354.0,354.0,47.0,47.0,'Carga combustible de 82.3 litros, valor: $41422, obac: Fernando Cardenas, boucher TCT: 572178067',2,3,68,20),(62,'Parque Chuyaca','2017-08-06','08:45:00.000000','14:30:00.000000',8676.0,8731.6,354.0,358.0,47.0,48.0,'Cuenta kilometros funciona al estar la bomba enganchada.',6,3,68,20),(63,'Parque Chuyaca','2017-08-06','08:45:00.000000','14:30:00.000000',22586.0,22596.0,4.5,7.4,NULL,NULL,'S/O',6,3,67,21),(64,'Avenida 18 Sep sector Chuyaca','2017-08-06','08:39:00.000000','15:36:00.000000',4712.4,4732.0,332.5,337.0,45.3,47.0,'Sin Observaciones',6,2,39,17),(66,'COPEC - RENE SORIANO 2335','2017-08-06','00:00:00.000000','00:00:00.000000',4729.0,4733.0,337.0,337.5,47.0,47.0,'Carga combustible de 60.0 litros, valor: $30240, obac: Camilo Carrasco, boucher TCT: 572188758',2,2,39,17),(67,'Rene Soriano 2132','2017-08-06','21:08:00.000000','21:38:00.000000',14263.0,14266.0,2625.3,2626.2,693.9,694.0,'S/O',7,3,67,19),(68,'costanera francke','2017-08-05','14:30:00.000000','19:30:00.000000',14718.0,14737.0,0.0,4.0,NULL,NULL,'sin observaciones',6,6,98,28),(69,'Parque chuyaca','2017-08-06','08:53:00.000000','14:27:00.000000',14737.0,14752.0,4.0,8.0,NULL,NULL,'sin observaciones',6,6,98,28),(70,'punta yatac 2718 portal osorno','2017-08-07','18:33:00.000000','19:30:00.000000',39223.0,39237.6,13.0,14.1,720.2,720.2,'no',13,2,124,18),(71,'ovejeria santa paulina','2017-08-05','19:50:00.000000','21:00:00.000000',33118.6,33136.0,3363.1,3366.8,649.6,652.0,'el movil de encontraba en sector francke en 6-18 de las 14.30 aprox y se despacho a alarma de incendio alrededor del las 19.50',20,6,126,27),(72,'COPEC - BULNES 522','2017-08-05','00:00:00.000000','00:00:00.000000',33139.0,33139.0,3368.0,3368.9,652.0,652.0,'Carga combustible de 38.0 litros, valor: $19115, obac: alfredo villalobos, boucher TCT: 1467905',2,6,126,27),(73,'Parque chuyaca','2017-08-06','08:53:00.000000','14:27:00.000000',33139.0,33152.0,3368.9,3373.0,652.0,655.0,'sin obeservaciones',6,6,94,27),(74,'COPEC - BULNES 522','2017-08-06','00:00:00.000000','00:00:00.000000',33152.0,33153.0,3373.0,3373.0,655.0,655.0,'Carga combustible de 36 litros, valor: $18110, obac: alfredo villalobos33153, boucher TCT: 572186001',2,6,94,27),(75,'ovejeria santa paulina','2017-08-05','19:50:00.000000','21:00:00.000000',38942.0,38948.0,1022.3,1022.6,993.6,993.9,'durante el trabaja el móvil sufrió problemas en la bomba por lo cual quedo 0-8, ademas se informa perdida de tapa de rueda derecha delantera',20,6,96,26),(77,'TALLER FEREXPO','2017-08-07','09:00:00.000000','16:30:00.000000',38948.0,38955.0,1022.5,1022.6,993.9,994.0,'Mantencion orden de trabajo: 01, observacion:Reparacion conexiones cuerpo de bomba del movil',1,6,126,26),(79,'COPEC - RENE SORIANO 2335','2017-08-07','00:00:00.000000','00:00:00.000000',38955.0,38963.0,1022.6,1022.7,994.0,994.0,'Carga combustible de 42 litros, valor: $21410, obac: Carlos Baria, boucher TCT: 16942523',2,6,127,26),(80,'Sector Forrahue','2017-08-07','17:44:00.000000','19:40:00.000000',33153.0,33193.0,3373.0,3375.0,655.0,655.0,'sin observaciones',21,6,126,27),(81,'Sector Forrahue','2017-08-07','17:44:00.000000','19:40:00.000000',14752.0,14797.0,8.0,9.0,NULL,NULL,'sin observaciones',21,6,98,28),(82,'COPEC - RENE SORIANO 2335','2017-08-07','00:00:00.000000','00:00:00.000000',33193.0,33202.0,3375.0,3376.0,655.0,655.0,'Carga combustible de 25 litros, valor: $13037, obac: Edgar Gutierrez, boucher TCT: 16942524',2,6,126,27),(83,'COPEC - RENE SORIANO 2335','2017-08-07','00:00:00.000000','00:00:00.000000',14797.0,14801.0,9.0,10.0,NULL,NULL,'Carga combustible de 59 litros, valor: $30000, obac: Ricardo Vergara, boucher TCT: 16942524',2,6,98,28),(84,'COPEC - RENE SORIANO 2335','2017-08-07','00:00:00.000000','00:00:00.000000',39237.6,39242.9,14.1,14.5,720.2,720.2,'Carga combustible de 31.2 litros, valor: $15761, obac: 0, boucher TCT: 14',2,2,43,18),(85,'av. real con pj. huisca','2017-08-08','09:35:00.000000','10:17:00.000000',39242.9,39250.6,14.5,15.3,720.2,720.2,'no',12,2,124,18),(86,'pj. vasquez','2017-08-08','12:31:00.000000','13:04:00.000000',15606.1,15609.3,2574.5,2575.1,720.5,720.5,'se soldo cuerpo bomba trabajo realizado por Carlos vera',19,2,124,16),(87,'Trebol norte acceso Osorno','2017-08-08','12:39:00.000000','15:26:00.000000',39250.6,39265.5,15.3,17.2,720.2,720.2,'Sin Observaciones',12,2,47,18),(88,'Trebol norte acceso Osorno','2017-08-08','12:39:00.000000','15:26:00.000000',4733.0,4747.0,337.5,340.3,47.0,47.5,'Sin observaciones',12,2,41,17),(91,'TALLER FEREXPO','2017-08-08','18:05:00.000000','18:10:00.000000',38963.0,38963.0,1022.7,1023.0,994.0,994.3,'Mantencion orden de trabajo: 02, observacion:engrase preventivo de bomba',1,6,126,26),(92,'TALLER FEREXPO','2017-08-08','18:00:00.000000','18:05:00.000000',33202.0,33202.2,3376.0,3376.0,655.0,655.0,'Mantencion orden de trabajo: 03, observacion:engrase bomba',1,6,126,27),(93,'concepcion esq antofagasta','2017-08-08','19:39:00.000000','20:20:00.000000',39265.5,39269.6,17.2,18.5,720.2,720.2,'no',12,2,124,18),(95,'Tarapaca 546','2017-08-09','07:54:00.000000','08:18:00.000000',38963.0,38965.0,1023.0,1023.0,994.3,994.3,'Sin observaciones',19,6,94,26),(96,'Heroes de la Concepcion Planta Soprole','2017-08-09','12:51:00.000000','13:57:00.000000',15609.4,15617.8,257.5,257.6,720.5,720.5,'Fuga de Gas  Natural en >Mantenimiento estanque de la Planta.-',13,2,39,16),(97,'heroues de la consepcion planta prolesur','2017-08-09','12:51:00.000000','13:57:00.000000',39269.6,39279.2,18.5,19.8,720.2,720.2,'no',13,2,124,18),(98,'MARACUYA 480','2017-08-09','21:45:00.000000','22:23:00.000000',15617.8,15627.1,2576.0,2576.7,720.5,720.6,'NO',7,2,124,16),(99,'Colegio Claudio Arrau','2017-08-10','10:10:00.000000','10:54:00.000000',38965.0,38966.8,1023.0,1023.0,994.3,994.3,'Sin observaciones',1,6,127,26),(100,'ASENTAMIENTO BAQUEDANO PARCELA 4','2017-08-10','15:41:00.000000','16:39:00.000000',4747.0,4755.8,340.3,342.5,47.5,47.5,'NO',7,2,124,17),(101,'Ovejeria','2017-08-10','15:39:00.000000','15:56:00.000000',38966.8,38970.0,1023.0,1023.0,994.3,994.3,'Al movil durante el trayecto la central de alarmas le dio 10-61 por no reportar salida, lo cual el movil no llego al lugar y se regreso al cuartel',7,6,127,26),(102,'Cuartel segunda cia','2017-08-11','14:31:00.000000','14:52:00.000000',38970.0,38974.0,1023.0,1023.0,994.3,994.3,'Sin observaciones',1,6,127,26),(103,'cochabamba 1776','2017-08-11','21:14:00.000000','22:02:00.000000',38974.0,38980.0,1023.0,1023.0,994.3,994.6,'sin observaciones',20,6,126,26),(104,'cochabamba 1776','2017-08-11','21:14:00.000000','22:02:00.000000',33202.2,33208.0,3376.0,3376.0,655.0,655.0,'sin observaciones',20,6,92,27),(105,'CUARTEL SEGUNDA','2017-08-12','17:30:00.000000','18:30:00.000000',15627.1,15627.3,2576.7,2577.6,720.6,721.3,'S/O',1,2,125,16),(106,'Los lagos 2306','2017-08-12','18:23:00.000000','19:27:00.000000',38980.0,38987.0,1023.0,1224.0,994.6,995.3,'Sin observaciones',7,6,92,26),(107,'buena vista numero 6','2017-08-12','18:28:00.000000','18:57:00.000000',33208.0,33213.0,3376.0,3378.0,655.0,655.7,'sin observaciones',15,6,126,27);
/*!40000 ALTER TABLE `maintenance_bitacora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_carguios_combustible`
--

DROP TABLE IF EXISTS `maintenance_carguios_combustible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_carguios_combustible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `litros` decimal(10,1) DEFAULT NULL,
  `km_salida` decimal(10,1) DEFAULT NULL,
  `hm_salida` decimal(10,1) DEFAULT NULL,
  `km_regreso` decimal(10,1) DEFAULT NULL,
  `hm_regreso` decimal(10,1) DEFAULT NULL,
  `valor` int(11) NOT NULL,
  `tarjeta_tct` int(11) NOT NULL,
  `obac` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `compania_id` int(11) DEFAULT NULL,
  `conductor_id` int(11) DEFAULT NULL,
  `maquina_id` int(11) NOT NULL,
  `servicentro_id` int(11) NOT NULL,
  `ho_bomba_regreso` decimal(10,1) DEFAULT NULL,
  `ho_bomba_salida` decimal(10,1) DEFAULT NULL,
  `servicio_id` int(11) DEFAULT NULL,
  `hora_llegada` time(6) DEFAULT NULL,
  `hora_salida` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_carguios_compania_id_efe0735c_fk_maintenan` (`compania_id`),
  KEY `maintenance_carguios_combustible_conductor_id_a382e6c5` (`conductor_id`),
  KEY `maintenance_carguios_combustible_maquina_id_bdbd8a1a` (`maquina_id`),
  KEY `maintenance_carguios_servicentro_id_fe205e5d_fk_maintenan` (`servicentro_id`),
  KEY `maintenance_carguios_servicio_id_c14df8f9_fk_maintenan` (`servicio_id`),
  CONSTRAINT `maintenance_carguios_compania_id_efe0735c_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`),
  CONSTRAINT `maintenance_carguios_conductor_id_a382e6c5_fk_maintenan` FOREIGN KEY (`conductor_id`) REFERENCES `maintenance_conductor` (`id`),
  CONSTRAINT `maintenance_carguios_maquina_id_bdbd8a1a_fk_maintenan` FOREIGN KEY (`maquina_id`) REFERENCES `maintenance_maquina` (`id`),
  CONSTRAINT `maintenance_carguios_servicentro_id_fe205e5d_fk_maintenan` FOREIGN KEY (`servicentro_id`) REFERENCES `maintenance_servicentro` (`id`),
  CONSTRAINT `maintenance_carguios_servicio_id_c14df8f9_fk_maintenan` FOREIGN KEY (`servicio_id`) REFERENCES `maintenance_bitacora` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_carguios_combustible`
--

LOCK TABLES `maintenance_carguios_combustible` WRITE;
/*!40000 ALTER TABLE `maintenance_carguios_combustible` DISABLE KEYS */;
INSERT INTO `maintenance_carguios_combustible` VALUES (3,54.0,39193.8,8.8,39196.0,9.3,26838,572154694,'Cristian Riquelme','2017-08-03',2,41,18,2,712.0,712.0,43,NULL,NULL),(4,82.3,8674.0,354.0,8676.0,354.0,41422,572178067,'Fernando Cardenas','2017-08-05',3,68,20,4,47.0,47.0,61,NULL,NULL),(5,60.0,4729.0,337.0,4733.0,337.5,30240,572188758,'Camilo Carrasco','2017-08-06',2,39,17,3,47.0,47.0,66,NULL,NULL),(6,38.0,33139.0,3368.0,33139.0,3368.9,19115,1467905,'alfredo villalobos','2017-08-05',6,126,27,2,652.0,652.0,72,NULL,NULL),(7,36.0,33152.0,3373.0,33153.0,3373.0,18110,572186001,'alfredo villalobos33153','2017-08-06',6,94,27,2,655.0,655.0,74,NULL,NULL),(8,42.0,38955.0,1022.6,38963.0,1022.7,21410,16942523,'Carlos Baria','2017-08-07',6,127,26,3,994.0,994.0,79,NULL,NULL),(9,25.0,33193.0,3375.0,33202.0,3376.0,13037,16942524,'Edgar Gutierrez','2017-08-07',6,126,27,3,655.0,655.0,82,NULL,NULL),(10,59.0,14797.0,9.0,14801.0,10.0,30000,16942524,'Ricardo Vergara','2017-08-07',6,98,28,3,NULL,NULL,83,NULL,NULL),(11,31.2,39237.6,14.1,39242.9,14.5,15761,14,'0','2017-08-07',2,43,18,3,720.2,720.2,84,NULL,NULL);
/*!40000 ALTER TABLE `maintenance_carguios_combustible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_clasificacion_maquina`
--

DROP TABLE IF EXISTS `maintenance_clasificacion_maquina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_clasificacion_maquina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_clasificacion_maquina`
--

LOCK TABLES `maintenance_clasificacion_maquina` WRITE;
/*!40000 ALTER TABLE `maintenance_clasificacion_maquina` DISABLE KEYS */;
INSERT INTO `maintenance_clasificacion_maquina` VALUES (1,'BOMBA','Maquina principal bomberos'),(2,'PORTA ESCALA','porta escala'),(3,'AMBULANCIA','ambulancia'),(4,'TRANSPORTE','transporte'),(5,'HAZ-MAT','haz-mat'),(6,'ALJIBE','aljibe'),(7,'MECANICA','mecanica'),(8,'RESCATE','rescate'),(9,'COMANDO','comando'),(10,'USAR','usar');
/*!40000 ALTER TABLE `maintenance_clasificacion_maquina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_clave`
--

DROP TABLE IF EXISTS `maintenance_clave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_clave` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_clave`
--

LOCK TABLES `maintenance_clave` WRITE;
/*!40000 ALTER TABLE `maintenance_clave` DISABLE KEYS */;
INSERT INTO `maintenance_clave` VALUES (1,'6--13','OTRO SERVICIO'),(2,'6--14','CARGA DE COMBUSTIBLE'),(3,'6--15','ASISTENCIA A CENTRO SALUD'),(4,'6--16','FALSA ALARMA'),(5,'6--17','EJERCICIO DE COMPAÑÍA'),(6,'6--18','EJERCICIO DE COMANDANCIA'),(7,'10--0','LLAMADO ESTRUCTURAL'),(8,'10--1','LLAMADO VEHICULO'),(9,'10--2','LLAMADO DE PASTIZALES'),(10,'10--3','RESCATE'),(11,'10--4','RESCATE VEHICULAR'),(12,'10--5','LLAMADO HAZ-MAT'),(13,'10--6','EMANACION DE GASES'),(14,'10--7','LLAMADO ELECTRICO'),(15,'10--8','LLAMADO NO CLASIFICADO'),(16,'10--9','LLAMADO OTRO SERVICIO'),(17,'10--10','LLAMADO ESCOMBROS'),(18,'10--12','APOYO OTRO CUERPO'),(19,'10--13','LLAMADO CHIMENEA'),(20,'10--14','INCENDIO'),(21,'10--15','LLAMADO RURAL');
/*!40000 ALTER TABLE `maintenance_clave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_compania`
--

DROP TABLE IF EXISTS `maintenance_compania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_compania` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_compania`
--

LOCK TABLES `maintenance_compania` WRITE;
/*!40000 ALTER TABLE `maintenance_compania` DISABLE KEYS */;
INSERT INTO `maintenance_compania` VALUES (1,1,'1ra compañía','Mackenna 2134'),(2,2,'2da Compañía','dir'),(3,3,'3ra Compañía','dir'),(4,4,'4ta Compañía','dir'),(5,5,'5ta Compañía','dir'),(6,6,'6ta Compañía','dir'),(7,7,'7ma Compañía','dir'),(8,8,'8va Compañía','dir'),(9,9,'Comandancia','direccion Comandancia');
/*!40000 ALTER TABLE `maintenance_compania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_componente`
--

DROP TABLE IF EXISTS `maintenance_componente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_componente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_componente`
--

LOCK TABLES `maintenance_componente` WRITE;
/*!40000 ALTER TABLE `maintenance_componente` DISABLE KEYS */;
INSERT INTO `maintenance_componente` VALUES (1,'Sistema de escape','Sistema de escape'),(2,'Motor','Motor'),(3,'Sistema de dirección','Sistema de dirección'),(4,'Sistema eléctrico','Sistema eléctrico'),(5,'Sistema de refrigeración','Sistema de refrigeración'),(6,'Sistema de frenos','Sistema de frenos'),(7,'Sistema de combustible','Sistema de combustible'),(8,'Bomba','se debe engrasar cada 5 horas');
/*!40000 ALTER TABLE `maintenance_componente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_conductor`
--

DROP TABLE IF EXISTS `maintenance_conductor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_conductor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `ap_paterno` varchar(45) DEFAULT NULL,
  `ap_materno` varchar(45) DEFAULT NULL,
  `num_licencia` varchar(12) DEFAULT NULL,
  `venc_lic` date DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `compania_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_conducto_compania_id_35029b85_fk_maintenan` (`compania_id`),
  CONSTRAINT `maintenance_conducto_compania_id_35029b85_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_conductor`
--

LOCK TABLES `maintenance_conductor` WRITE;
/*!40000 ALTER TABLE `maintenance_conductor` DISABLE KEYS */;
INSERT INTO `maintenance_conductor` VALUES (22,'7.397.240-K','Ariel','Delgado','Henríquez',NULL,'2018-01-06','',1),(23,'14.096.699-1','Alejandro Hernán','Corrales','Risco',NULL,'2018-09-07','',1),(24,'15.296.114-6','Armin Iván','Moraga','Licán',NULL,'2020-07-21','',1),(25,'13.118.895-1','Héctor Mauricio','Balcázar','Obando',NULL,'2019-03-18','',1),(26,'16.831.546-5','Jaime Felipe','Cárcamo','Torres',NULL,'2019-05-11','',1),(27,'11.708.791-3','Ricardo Mauricio','García','Pacheco',NULL,'2018-03-12','',1),(28,'10.743.577-8','Onofre','Pérez','Arriagada',NULL,'2023-04-28','',1),(30,'8.911.450-0','Marcelo Nicasio','Millar','Guzmán',NULL,'2018-05-29','',1),(31,'12.422.013-0','Christian Morice','Cárdenas','Gómez',NULL,'2019-03-21','',1),(32,'5.456.823-1','Sergio Omar','Ríos','Leal',NULL,'2018-03-10','',1),(33,'15.795.934-4','Daniel','Gatica','Bachmann',NULL,'2020-07-13','',1),(38,'12.751.872-6','Cristian Rodrigo','Carrasco','Figueroa',NULL,'2021-06-17','',1),(39,'5.736.059-3','Alejandro Patricio','Delannoy','Schilling',NULL,'2020-01-04','',2),(40,'7.826.421-7','Luis Francisco','Rigo-Righi','Aubel',NULL,'2020-12-25','',2),(41,'12.047.686-6','Mauricio Ernesto','Nannig ','Briceño',NULL,'2021-09-23','',2),(42,'10.909.375-0','Jorge Alejandro','Huamanga','Noriega',NULL,'2019-08-16','',2),(43,'9.932.327-2','Chedomir Andres','Luksic','Aranguiz',NULL,'2022-09-19','',2),(44,'13.847.895-5','Mario Andres','Mohr','Hechenleitner',NULL,'2021-11-08','',2),(45,'15.273.396-8','Roberto Ignacio','Heuser','Miller',NULL,'2019-12-13','',2),(46,'10.955.803-6','Juan Luis','Matamala','Ubilla',NULL,'2021-03-21','',2),(47,'15.896.408-2','Carlos Alberto','Vera','Ortiz',NULL,'2018-12-31','',2),(48,'16.831.253-9','Francisco Ricardo','Flores','Aguila',NULL,'2018-03-21','',2),(49,'16.584.078-k','Eduardo Andres','Minte','Hess',NULL,'2021-03-23','',2),(50,'15.274.147-2','Ignacio Andres','Saldivia ','Saravia',NULL,'2018-06-27','',2),(51,'18.577.438-4','Simon Antonio','Baessolo ','Brito',NULL,'2017-08-27','',2),(52,'19.862.601-5','Nicolas Benjamin','Loaiza','Passi',NULL,'2021-11-15','',2),(54,'15.273.488-3','Claudio Ivan','Risco ','Henriquez',NULL,'2018-01-17','',2),(55,'6.317.281-2','Jaime','Santamaria','Cisterna',NULL,'2022-11-24','',3),(56,'7.839.571-0','Luis','Ojeda','Rosas',NULL,'2018-06-21','',3),(57,'7.008.742-1','Juan Carlos','Castillo','Rosas',NULL,'2021-08-21','',3),(58,'8.703.513-1','Juan Carlos','Alt','Hayal',NULL,'2021-12-16','',3),(59,'8.728.239-2','Ignacio Javier','Saenz','Kemp',NULL,'2018-01-16','',3),(60,'13.118.260-0','Francisco Javier','Ojeda','Valderas',NULL,'2019-11-22','',3),(61,'10.249.285-4','Luis Amador Sebastian','Santibañez','Delgado',NULL,'2019-07-22','',3),(62,'10.921.465-5','Mario Andres','Iglesias','Gomez',NULL,'2020-05-22','',3),(63,'14.570.332-8','Pablo Cesar','Labbe','Segura',NULL,'2023-10-03','',3),(64,'14.096.841-2','Gustavo Dario','Paisil','Cartes',NULL,'2017-10-26','',3),(65,'12.826.000-5','Victor Andres','Iñigo','Herrera',NULL,'2020-03-24','',3),(66,'13.162.446-8','Cesar Eduardo','Aranguiz','Muñoz',NULL,'2017-12-30','',3),(67,'16.397.775-3','Danny Alexis','Cortes','Alvarez',NULL,'2017-12-04','',3),(68,'14.479.766-3','Eduardo Javier','Leighton','Valderas',NULL,'2020-07-31','',3),(69,'8.890.139-8','Ricardo Esteban','Gallardo','Velazques',NULL,'2019-02-06','',4),(70,'12.340.259-6','Hardy Esteban','Asenjo','Acuña',NULL,'2019-04-30','',4),(71,'12 593 529-K','Joel Gaspar','Rupertus','Torres',NULL,'2021-04-16','',4),(72,'13.119.812-4','Mauricio Javier','Muñoz','Colipai',NULL,'2017-09-11','',4),(73,'13.734.712-1','Luis Elias','Cardenas','Arriagada',NULL,'2023-05-14','',4),(74,'14.038.562-K','Marcelo Rodrigo','Muñoz','Colipai',NULL,'2018-03-18','',4),(75,'15.895.251-3','Dinitri Heriberto','Silva','Silva',NULL,'2021-05-16','',4),(76,'14.038.870-K','Cesar Alfonso','Briones','Perez',NULL,'2021-05-18','',4),(77,'15.792.925-9','Cristian Alejandro','Garces','Saez',NULL,'2020-04-01','',4),(78,'17.197.588-3','Alejandro Javier','Castro','Cid',NULL,'2018-03-26','',4),(79,'16.344.050-4','Robinson Fernando','Carrillo','Alvarez',NULL,'2017-10-15','',4),(80,'16.831.504-K','Victor Alejandro','Ruiz','Alarcon',NULL,'2017-11-15','',4),(81,'6.827.577-6','Manuel Agustin','Taborga','Pizzarro',NULL,'2018-05-29','',4),(82,NULL,'Hector Antonio','Torres','Miranda',NULL,NULL,'',5),(83,'9.847.608-3','Leonel Segundo','Silva','Torres',NULL,'2018-10-25','',5),(84,'15.295.003-9','Alvaro Juvenal','Nuñez','Molina',NULL,'2018-12-10','',5),(85,'17.125.032-3','David Eduardo','Pacheco','Cardenas',NULL,'2019-12-20','',5),(86,'11.708.625-9','Cesar Rodrigo','Cancino','Mancilla',NULL,'2018-08-16','',5),(87,'15.268.478-9','Manuel Antonio','Contreras','Henriquez',NULL,'2017-10-05','',5),(88,'15.274.483-8','Carlos Andres','Birke','Burgos',NULL,'2020-09-12','',5),(89,'15.688.784-6','Luis  Fernando','Garnica','Silva',NULL,'2017-10-05','',5),(90,NULL,'Victor Eduardo ','Alarcon','Oyarzun',NULL,NULL,NULL,5),(91,'11.428.332-0','Mauricio Alejandro','Becker','Añazco',NULL,'2022-11-29','',5),(92,'12.592.945-1','Carlos Rene','Baeza','Padilla',NULL,'2019-06-02','',6),(93,'9.290.431-8','Juan Carlos','Cardenas','Uribe',NULL,'2019-06-20','',6),(94,'18.368.126-5','Nicolas','Caro','Crisosto',NULL,'2019-02-23','',6),(95,'9.064.648-6','Raul Hernan','Carrasco','Mancilla',NULL,'2018-10-03','',6),(96,'8.105651-0','Hector Julio','Flandez','Hernandez',NULL,'2020-01-29','',6),(97,'14.039.691-5','Franklin Eduardo','Flandez','Gallardo',NULL,'2018-08-08','',6),(98,'8.606.778.1','Walterio Hardy','Gonzalez','Sandoval',NULL,'2018-01-06','',6),(99,'10.155.770-7','Marco Antonio','Matamala','Vargas',NULL,'2019-10-20','',6),(100,'16.159.684-6','Felipe Rodrigo','Oyarzun','Rudolfh',NULL,'2018-12-30','',6),(101,'15.274.449-8','Felipe Daniel','Ponce','Ovalle',NULL,'2018-09-14','',6),(102,'8.226.776-k','Patricio Daniel','Ponce','Martinez',NULL,'2018-02-16','',6),(103,'7.140.409-9','Mario Armando','Soto','Huentelican',NULL,'2018-12-20','',6),(104,'16.112.406-0','Alfredo Ernesto','Villalobos','Monsalve',NULL,'2022-08-02','',6),(105,NULL,'Luis Enrique','Gonzalez','Manzanares',NULL,NULL,NULL,7),(106,'10.776.178-0','Juan Armando','Gonzalez','Manzanares',NULL,'2019-10-21','',7),(107,'6.562.759-0','Jorge Erwin','Gutierrez','Albornoz',NULL,'2018-08-28','',7),(108,'10.506.341-5','Luis Alberto','Aros','Soto',NULL,'2019-09-13','',7),(109,'13.822.167-9','Humberto Patricio','Segovia','Catalan',NULL,'2020-05-30','',7),(110,'13.821.536-4','Ernesto Alejandro','Cardenas','Ojeda',NULL,'2020-05-05','',7),(111,'15.297.561-9','Mario Patricio','Sanchez','Ravanal',NULL,'2018-02-08','',7),(112,'15.688.456-1','Claudio Andres','Gonzalez','Huayque',NULL,'2018-09-11','',7),(113,'16.111.373-5','Jorge Andres','Perez','Coronado',NULL,'2022-02-25','',7),(114,'15.689.662-4','Miguel Angel','Reyes','Licandeo',NULL,'2021-03-08','',7),(115,NULL,'Pablo Alejandro','Oyarzo','Diaz',NULL,NULL,NULL,8),(116,NULL,'Juan Patricio','Cañulef','Cardenas',NULL,NULL,NULL,8),(117,NULL,'Edgar Gamalier','Paredes','Pascal',NULL,NULL,NULL,8),(118,NULL,'Christian Patricio','Cardenas','Romero',NULL,NULL,NULL,8),(119,NULL,'Andres Eduardo','Obando','Aguilar',NULL,NULL,NULL,8),(120,NULL,'Andres Eduardo','Castillo','Silva',NULL,NULL,NULL,8),(121,NULL,'Cristofer Alexis','Ojeda','Arancibia',NULL,NULL,NULL,8),(122,NULL,'Felipe Alexis','Nactoch','Parra',NULL,NULL,NULL,8),(123,NULL,'Miguel Angel','Perez','Tapia',NULL,NULL,NULL,8),(124,'11.198.240-6','Ricardo','Flores','Aguila',NULL,'2019-09-16','',2),(125,'17.743.302-0','Camilo','Carrasco','Alvares',NULL,'2022-11-05','',2),(126,'4.894.435-3','Rene','Aviles','Obando',NULL,'2018-08-08','',6),(127,'13.823.250-6','Carlos','Barria','del Rio',NULL,'2020-06-02','',6),(128,'15.296.389-0','Alexis','Soto','Soto',NULL,'2019-09-13','',6),(129,'10.565.089-2','Hector','Guala','Moraga',NULL,'2020-09-26','',3),(130,'16.112.438-9','Victor','Antriao','Molina',NULL,'2021-08-24','',1),(131,'18.962.850-1','Andres','Santibañez','Gonzalez',NULL,'2018-11-17','',1),(132,'16.338.185-0','Andres','Gonzalez','Gonzalez',NULL,'2021-05-07','',1);
/*!40000 ALTER TABLE `maintenance_conductor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_detallemantencion`
--

DROP TABLE IF EXISTS `maintenance_detallemantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_detallemantencion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `des_detalle` longtext,
  `hodometro_prox_man` decimal(10,1) DEFAULT NULL,
  `division_id` int(11) DEFAULT NULL,
  `mantencion_id` int(11) NOT NULL,
  `servicio_id` int(11) DEFAULT NULL,
  `subdivision_id` int(11) DEFAULT NULL,
  `tipo_mantencion_id` int(11),
  PRIMARY KEY (`id`),
  KEY `maintenance_detallem_division_id_cb8cc18e_fk_maintenan` (`division_id`),
  KEY `maintenance_detallem_mantencion_id_97707aa3_fk_maintenan` (`mantencion_id`),
  KEY `maintenance_detallemantencion_servicio_id_bcbba1a7` (`servicio_id`),
  KEY `maintenance_detallemantencion_subdivision_id_0ec250ed` (`subdivision_id`),
  KEY `maintenance_detallem_tipo_mantencion_id_eabc783f_fk_maintenan` (`tipo_mantencion_id`),
  CONSTRAINT `maintenance_detallem_division_id_cb8cc18e_fk_maintenan` FOREIGN KEY (`division_id`) REFERENCES `maintenance_division` (`id`),
  CONSTRAINT `maintenance_detallem_mantencion_id_97707aa3_fk_maintenan` FOREIGN KEY (`mantencion_id`) REFERENCES `maintenance_mantencion` (`id`),
  CONSTRAINT `maintenance_detallem_servicio_id_bcbba1a7_fk_maintenan` FOREIGN KEY (`servicio_id`) REFERENCES `maintenance_serviciomantencion` (`id`),
  CONSTRAINT `maintenance_detallem_subdivision_id_0ec250ed_fk_maintenan` FOREIGN KEY (`subdivision_id`) REFERENCES `maintenance_subdivision` (`id`),
  CONSTRAINT `maintenance_detallem_tipo_mantencion_id_eabc783f_fk_maintenan` FOREIGN KEY (`tipo_mantencion_id`) REFERENCES `maintenance_tipomantencion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_detallemantencion`
--

LOCK TABLES `maintenance_detallemantencion` WRITE;
/*!40000 ALTER TABLE `maintenance_detallemantencion` DISABLE KEYS */;
INSERT INTO `maintenance_detallemantencion` VALUES (5,'engrase bomba',660.0,1,15,2,40,2);
/*!40000 ALTER TABLE `maintenance_detallemantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_division`
--

DROP TABLE IF EXISTS `maintenance_division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_division` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_division`
--

LOCK TABLES `maintenance_division` WRITE;
/*!40000 ALTER TABLE `maintenance_division` DISABLE KEYS */;
INSERT INTO `maintenance_division` VALUES (1,'BOMBA'),(2,'MECANICA'),(3,'ELECTRICO'),(4,'DESABOLLADURA Y PINTURA'),(5,'CARROZADO'),(6,'ESTRUCTURA GENERAL');
/*!40000 ALTER TABLE `maintenance_division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_mantencion`
--

DROP TABLE IF EXISTS `maintenance_mantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_mantencion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `ki_salida` decimal(10,1) DEFAULT NULL,
  `ho_salida` decimal(10,1) DEFAULT NULL,
  `ki_regreso` decimal(10,1) DEFAULT NULL,
  `ho_regreso` decimal(10,1) DEFAULT NULL,
  `cod_man` varchar(45) NOT NULL,
  `observacion` longtext NOT NULL,
  `num_factura` int(11) NOT NULL,
  `valor` int(11) NOT NULL,
  `responsable_id` int(11) DEFAULT NULL,
  `compania_id` int(11) DEFAULT NULL,
  `maquina_id` int(11) NOT NULL,
  `taller_id` int(11) NOT NULL,
  `ho_bomba_regreso` decimal(10,1) DEFAULT NULL,
  `ho_bomba_salida` decimal(10,1) DEFAULT NULL,
  `servicio_id` int(11) DEFAULT NULL,
  `hora_llegada` time(6) DEFAULT NULL,
  `hora_salida` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_mantenci_compania_id_cad2430f_fk_maintenan` (`compania_id`),
  KEY `maintenance_mantencion_maquina_id_63c3647a` (`maquina_id`),
  KEY `maintenance_mantenci_taller_id_605e696f_fk_maintenan` (`taller_id`),
  KEY `maintenance_mantencion_responsable_id_26c36e74` (`responsable_id`),
  KEY `maintenance_mantenci_servicio_id_ab42d79f_fk_maintenan` (`servicio_id`),
  CONSTRAINT `maintenance_mantenci_compania_id_cad2430f_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`),
  CONSTRAINT `maintenance_mantenci_maquina_id_63c3647a_fk_maintenan` FOREIGN KEY (`maquina_id`) REFERENCES `maintenance_maquina` (`id`),
  CONSTRAINT `maintenance_mantenci_responsable_id_26c36e74_fk_maintenan` FOREIGN KEY (`responsable_id`) REFERENCES `maintenance_conductor` (`id`),
  CONSTRAINT `maintenance_mantenci_servicio_id_ab42d79f_fk_maintenan` FOREIGN KEY (`servicio_id`) REFERENCES `maintenance_bitacora` (`id`),
  CONSTRAINT `maintenance_mantenci_taller_id_605e696f_fk_maintenan` FOREIGN KEY (`taller_id`) REFERENCES `maintenance_taller` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_mantencion`
--

LOCK TABLES `maintenance_mantencion` WRITE;
/*!40000 ALTER TABLE `maintenance_mantencion` DISABLE KEYS */;
INSERT INTO `maintenance_mantencion` VALUES (14,'2017-08-08',38963.0,1022.7,38963.0,1023.0,'02','engrase preventivo de bomba',0,0,126,6,26,5,994.3,994.0,91,NULL,NULL),(15,'2017-08-08',33202.0,3376.0,33202.2,3376.0,'03','engrase bomba',0,0,126,6,27,5,655.0,655.0,92,NULL,NULL);
/*!40000 ALTER TABLE `maintenance_mantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_maquina`
--

DROP TABLE IF EXISTS `maintenance_maquina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_maquina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `numero_motor` varchar(45) DEFAULT NULL,
  `numero_chasis` varchar(45) DEFAULT NULL,
  `bin` varchar(45) DEFAULT NULL,
  `patente` varchar(10) DEFAULT NULL,
  `clasificacion_id` int(11) NOT NULL,
  `compania_id` int(11) NOT NULL,
  `ano` varchar(5),
  `costo_patente` int(11) DEFAULT NULL,
  `costo_rev_tec` int(11) DEFAULT NULL,
  `costo_seg_auto` int(11) DEFAULT NULL,
  `hodometro` decimal(10,1) DEFAULT NULL,
  `hodometro_bomba` decimal(10,1) DEFAULT NULL,
  `kilometraje` decimal(10,1) DEFAULT NULL,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `prueba` decimal(10,1) DEFAULT NULL,
  `soap_costo` int(11) DEFAULT NULL,
  `tiene_bomba` tinyint(1) NOT NULL,
  `venc_patente` date DEFAULT NULL,
  `venc_rev_tec` date DEFAULT NULL,
  `venc_seg_auto` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_maquina_clasificacion_id_b86bbd74_fk_maintenan` (`clasificacion_id`),
  KEY `maintenance_maquina_compania_id_9f87ccfd_fk_maintenan` (`compania_id`),
  CONSTRAINT `maintenance_maquina_clasificacion_id_b86bbd74_fk_maintenan` FOREIGN KEY (`clasificacion_id`) REFERENCES `maintenance_clasificacion_maquina` (`id`),
  CONSTRAINT `maintenance_maquina_compania_id_9f87ccfd_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_maquina`
--

LOCK TABLES `maintenance_maquina` WRITE;
/*!40000 ALTER TABLE `maintenance_maquina` DISABLE KEYS */;
INSERT INTO `maintenance_maquina` VALUES (12,'B-1','83M0693075','VF645ACA000008868','VF645ACA000008868','WG 7785-3',1,1,'2006',230000,45000,NULL,3.5,11.0,4.0,'RENAULT','MIDLUM 270',NULL,5600,1,NULL,'2017-09-22',NULL),(13,'BX-1','5600564503','VF6JS00A000009811','VF6JS00A000009811','PU 6009-0',1,1,'1996',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','M 210',NULL,NULL,1,NULL,'2017-11-17',NULL),(14,'S-1',NULL,'WDB9046121R905005','WDB9046121R905005','DRVZ 37-4',3,1,'2006',NULL,NULL,NULL,0.0,NULL,0.0,'MERCEDES BENZ','SPRINTER',NULL,NULL,0,NULL,'2017-09-17',NULL),(15,'J-1','F4019074','LJ166B3C2G1500509','LJ166B3C2G1500509','HFRV-14-3',4,9,'2015',NULL,NULL,NULL,0.0,0.0,0.0,'JAC','RUNNER HFC',NULL,NULL,0,NULL,'2018-01-18',NULL),(16,'B-2','83M0691532','VF645ACA000008770','VF645ACA000008770','WG 7784',1,2,'2006',NULL,NULL,NULL,2577.6,721.3,15627.3,'RENAULT','MIDLUM 270',NULL,NULL,1,'2017-03-31','2017-10-24','2017-03-31'),(17,'BX-2','22842865174285','WMAN38ZZ1GY337899','WMAN38ZZ1GY337899','JCHX 32-0',1,2,'2015',NULL,NULL,NULL,342.5,47.5,4755.8,'MAN','18,34',NULL,NULL,1,'2017-03-31','2017-09-02','2017-03-31'),(18,'H-2','35154060243311','WMA5039068M058345','WMA5039068M058345','CBPW 62',5,2,'1987',NULL,NULL,NULL,19.8,720.2,39279.2,'MAN','LF-24',NULL,NULL,1,'2017-03-31','2017-09-01','2017-03-31'),(19,'B-3','83M0691339','VF645ACA000008759','VF645ACA000008759','WG 7783',1,3,'2006',NULL,NULL,NULL,2626.2,694.0,14266.0,'RENAULT','MIDLUM 270',NULL,NULL,1,NULL,'2017-10-12',NULL),(20,'BX-3','74012987','4S7CU2D93GC081296','4S7CU2D93GC081296','JFTJ92',1,3,'2016',NULL,NULL,NULL,358.0,48.0,8731.6,'SPARTAN','METRO STAR',NULL,NULL,1,NULL,'2017-11-17',NULL),(21,'Z-3','36076487','9BWC782TX9R906296','9BWC782TX9R906296','BYDL 43',6,3,'2009',NULL,NULL,NULL,7.4,NULL,22596.0,'VOLKSWAGEN','17220',NULL,NULL,0,NULL,'2017-08-17',NULL),(22,'Q-4','73917804','54F2AB720GWE11422','54F2AB720GWE11422','HYLG 42-5',2,4,'2016',NULL,NULL,NULL,0.0,0.0,0.0,'ROSENBAUER','COMMANDER',NULL,NULL,0,NULL,'2018-02-18',NULL),(23,'M-4','83M0172986','WF640AC0000002249','WF640AC0000002249','NF 2461-1',7,4,'1994',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','M 200',NULL,NULL,0,NULL,'2017-12-27',NULL),(24,'R-5','83M0716501','VF645ACA000010189','VF645ACA000010189','BSCF 87',8,5,'2008',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','MIDLUM 270',NULL,NULL,0,NULL,'2017-12-06',NULL),(25,'RX-5','L2000','WMAL20ZZZYY057018','WMAL20ZZZYY057018','DDPX 94-8',8,5,'2003',NULL,NULL,NULL,0.0,0.0,0.0,'MAN','LF-24',NULL,NULL,0,NULL,'2017-09-03',NULL),(26,'B-6','83M0353143','VF622ACA0A0013881','VF622ACA0A0013881','TV 3729',1,6,'1999',0,0,NULL,1224.0,995.3,38987.0,'RENAULT','PREMIUM 210',NULL,NULL,1,'2018-03-31','2017-12-29',NULL),(27,'BX-6','10413781','VF644BLM000000120','VF644BLM000000120','BGVF 56',1,6,'2009',NULL,NULL,NULL,3378.0,655.7,33213.0,'RENAULT','MIDLUM 240',NULL,NULL,1,NULL,'2017-12-29',NULL),(28,'Z-6','906985U0967858','9BM958074CB819386','9BM958074CB819386','DRPT83-9',6,6,'2012',0,0,NULL,10.0,NULL,14801.0,'MERCEDES BENZ','ATEGO',NULL,NULL,0,'2018-03-31','2017-11-15',NULL),(29,'K-2','ZG24434057','LJNMFE2K6DN003564','LJNMFE2K6DN003564','GTFT82-9',9,9,'2014',NULL,NULL,NULL,0.0,0.0,0.0,'ZNA','RICH',NULL,NULL,0,NULL,'2018-10-10',NULL),(30,'B-7','83M0432092','VF622ACA000101510','VF622ACA000101510','UP 8922',1,7,'2000',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','PREMIUM 210',NULL,NULL,1,NULL,'2018-01-18',NULL),(31,'BX-7','11316409','VF644AHM000001821','VF644AHM000001821','FVFP 57',1,7,'2012',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','MIDLUM 270',NULL,NULL,1,NULL,'2017-11-12',NULL),(32,'B-8','83M0447564','VF622AXA000102184','VF622AXA000102184','VE 5546',1,8,'2001',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','PREMIUM 260',NULL,NULL,1,NULL,'2018-12-28',NULL),(33,'BX-8','11310237','VF644AHM000001812','VF644AHM000001812','FVFP 56',1,8,'2012',NULL,NULL,NULL,0.0,0.0,0.0,'RENAULT','MIDLUM 270',NULL,NULL,1,NULL,'2017-12-29',NULL),(34,'RH-8',NULL,NULL,NULL,NULL,10,8,'2004',NULL,NULL,NULL,0.0,0.0,0.0,NULL,NULL,NULL,NULL,0,NULL,'2018-01-13',NULL),(35,'K-1','Y222488','JF1SJ5LC5HG265414','JF1SJ5LC5HG265414','HTHD54-1',9,9,'2016',NULL,NULL,NULL,0.0,NULL,0.0,'SUBARU','FORESTER AWD',NULL,NULL,0,NULL,'2018-07-30',NULL),(37,'BR','6420','VF6BA03A000006420','VF6BA03A000006420','NP 5851',1,9,'1987',0,0,NULL,2585.9,0.8,41886.0,'RENAULT','G 230',NULL,NULL,1,'2018-03-31','2018-01-04',NULL);
/*!40000 ALTER TABLE `maintenance_maquina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_maquina_conductor`
--

DROP TABLE IF EXISTS `maintenance_maquina_conductor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_maquina_conductor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `maquina_id` int(11) NOT NULL,
  `conductor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `maintenance_maquina_cond_maquina_id_conductor_id_a8d5da13_uniq` (`maquina_id`,`conductor_id`),
  KEY `maintenance_maquina__conductor_id_36c242be_fk_maintenan` (`conductor_id`),
  CONSTRAINT `maintenance_maquina__conductor_id_36c242be_fk_maintenan` FOREIGN KEY (`conductor_id`) REFERENCES `maintenance_conductor` (`id`),
  CONSTRAINT `maintenance_maquina__maquina_id_e85bcf10_fk_maintenan` FOREIGN KEY (`maquina_id`) REFERENCES `maintenance_maquina` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=397 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_maquina_conductor`
--

LOCK TABLES `maintenance_maquina_conductor` WRITE;
/*!40000 ALTER TABLE `maintenance_maquina_conductor` DISABLE KEYS */;
INSERT INTO `maintenance_maquina_conductor` VALUES (35,12,24),(36,12,25),(37,12,26),(38,12,27),(39,12,31),(34,12,38),(40,13,22),(41,13,23),(42,13,24),(43,13,25),(44,13,26),(45,13,27),(46,13,28),(48,13,30),(49,13,31),(50,13,32),(51,13,33),(56,13,38),(351,14,23),(352,14,24),(353,14,25),(354,14,26),(355,14,27),(356,14,28),(70,16,39),(71,16,40),(72,16,41),(73,16,42),(74,16,43),(75,16,44),(76,16,45),(77,16,46),(78,16,47),(383,16,48),(378,16,49),(79,16,50),(80,16,51),(81,16,52),(377,16,54),(379,16,124),(380,16,125),(82,17,39),(83,17,40),(84,17,41),(85,17,42),(86,17,43),(88,17,45),(89,17,46),(90,17,47),(93,17,50),(94,17,51),(95,17,52),(97,17,54),(382,17,124),(98,18,39),(99,18,40),(100,18,41),(101,18,42),(102,18,43),(103,18,44),(104,18,45),(105,18,46),(106,18,47),(107,18,50),(108,18,51),(384,18,52),(381,18,124),(114,19,55),(115,19,56),(116,19,57),(117,19,58),(118,19,59),(119,19,60),(120,19,61),(121,19,62),(122,19,63),(109,19,64),(110,19,65),(111,19,66),(112,19,67),(113,19,68),(390,19,129),(128,20,55),(130,20,57),(131,20,58),(132,20,59),(133,20,60),(134,20,61),(135,20,62),(124,20,65),(125,20,66),(126,20,67),(127,20,68),(391,20,129),(141,21,55),(142,21,56),(143,21,57),(145,21,59),(146,21,60),(147,21,61),(148,21,62),(149,21,63),(137,21,64),(138,21,65),(139,21,66),(140,21,67),(392,21,129),(150,22,69),(151,22,70),(152,22,71),(153,22,72),(154,22,73),(155,22,74),(156,22,75),(157,22,76),(158,22,77),(159,22,78),(160,22,79),(161,22,80),(162,22,81),(163,23,69),(164,23,70),(165,23,71),(166,23,72),(167,23,75),(168,23,76),(169,23,77),(170,23,78),(171,23,81),(172,24,82),(173,24,83),(174,24,84),(175,24,85),(176,24,86),(177,24,87),(178,24,88),(179,24,89),(180,24,90),(181,24,91),(182,25,82),(183,25,83),(184,25,84),(185,25,85),(186,25,86),(187,25,87),(188,25,88),(189,25,89),(190,25,90),(191,25,91),(200,26,92),(201,26,93),(202,26,94),(203,26,95),(192,26,96),(193,26,97),(194,26,99),(195,26,100),(196,26,101),(197,26,102),(198,26,103),(199,26,104),(385,26,126),(386,26,127),(389,26,128),(211,27,92),(212,27,93),(213,27,94),(214,27,95),(204,27,96),(205,27,97),(206,27,99),(207,27,100),(208,27,101),(374,27,102),(209,27,103),(210,27,104),(394,27,126),(393,27,128),(220,28,92),(221,28,93),(372,28,94),(222,28,95),(215,28,96),(216,28,97),(370,28,98),(217,28,99),(371,28,100),(218,28,101),(219,28,103),(396,28,126),(395,28,128),(223,30,105),(224,30,106),(225,30,107),(226,30,108),(227,30,109),(228,30,110),(229,30,111),(230,30,112),(231,30,113),(232,30,114),(233,31,106),(234,31,107),(235,31,108),(236,31,109),(237,31,110),(238,31,111),(239,31,112),(240,31,113),(241,32,115),(242,32,116),(243,32,117),(244,32,118),(245,32,119),(246,32,120),(247,32,121),(248,32,122),(249,32,123),(250,33,115),(251,33,116),(252,33,117),(253,33,118),(254,33,119),(255,33,120),(256,33,121),(257,33,122),(258,33,123),(259,34,115),(261,34,116),(260,34,123);
/*!40000 ALTER TABLE `maintenance_maquina_conductor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_repuestodetallemantencion`
--

DROP TABLE IF EXISTS `maintenance_repuestodetallemantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_repuestodetallemantencion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `repuesto` varchar(45) DEFAULT NULL,
  `detalle_mantencion_id` int(11) NOT NULL,
  `mantencion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_repuesto_mantencion_id_8a16d066_fk_maintenan` (`mantencion_id`),
  KEY `maintenance_repuestodetalle_detalle_mantencion_id_0fcc9076` (`detalle_mantencion_id`),
  CONSTRAINT `maintenance_repuesto_detalle_mantencion_i_0fcc9076_fk_maintenan` FOREIGN KEY (`detalle_mantencion_id`) REFERENCES `maintenance_detallemantencion` (`id`),
  CONSTRAINT `maintenance_repuesto_mantencion_id_8a16d066_fk_maintenan` FOREIGN KEY (`mantencion_id`) REFERENCES `maintenance_mantencion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_repuestodetallemantencion`
--

LOCK TABLES `maintenance_repuestodetallemantencion` WRITE;
/*!40000 ALTER TABLE `maintenance_repuestodetallemantencion` DISABLE KEYS */;
INSERT INTO `maintenance_repuestodetallemantencion` VALUES (3,'grasa',5,15);
/*!40000 ALTER TABLE `maintenance_repuestodetallemantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_servicentro`
--

DROP TABLE IF EXISTS `maintenance_servicentro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_servicentro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_servicentro`
--

LOCK TABLES `maintenance_servicentro` WRITE;
/*!40000 ALTER TABLE `maintenance_servicentro` DISABLE KEYS */;
INSERT INTO `maintenance_servicentro` VALUES (2,'COPEC','BULNES 522'),(3,'COPEC','RENE SORIANO 2335'),(4,'COPEC','JUAN MACKENNA 2019'),(5,'COPEC','RUTA 5 NORTE TRAFUN'),(6,'PETROBRAS','CARRERA MATTA');
/*!40000 ALTER TABLE `maintenance_servicentro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_serviciomantencion`
--

DROP TABLE IF EXISTS `maintenance_serviciomantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_serviciomantencion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(75) DEFAULT NULL,
  `division_id` int(11) DEFAULT NULL,
  `subdivision_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_servicio_division_id_d8101b40_fk_maintenan` (`division_id`),
  KEY `maintenance_serviciomantencion_subdivision_id_ef4ff8c3` (`subdivision_id`),
  CONSTRAINT `maintenance_servicio_division_id_d8101b40_fk_maintenan` FOREIGN KEY (`division_id`) REFERENCES `maintenance_division` (`id`),
  CONSTRAINT `maintenance_servicio_subdivision_id_ef4ff8c3_fk_maintenan` FOREIGN KEY (`subdivision_id`) REFERENCES `maintenance_subdivision` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_serviciomantencion`
--

LOCK TABLES `maintenance_serviciomantencion` WRITE;
/*!40000 ALTER TABLE `maintenance_serviciomantencion` DISABLE KEYS */;
INSERT INTO `maintenance_serviciomantencion` VALUES (1,'Estroboscopico','Estroboscopico',3,8),(2,'ENGRASE BOMBA','ENGRASE BOMBA',1,40),(3,'CAMBIO ACEITE','CAMBIO ACEITE',2,3);
/*!40000 ALTER TABLE `maintenance_serviciomantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_subdivision`
--

DROP TABLE IF EXISTS `maintenance_subdivision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_subdivision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `division_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maintenance_subdivis_division_id_5cbe54ff_fk_maintenan` (`division_id`),
  CONSTRAINT `maintenance_subdivis_division_id_5cbe54ff_fk_maintenan` FOREIGN KEY (`division_id`) REFERENCES `maintenance_division` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_subdivision`
--

LOCK TABLES `maintenance_subdivision` WRITE;
/*!40000 ALTER TABLE `maintenance_subdivision` DISABLE KEYS */;
INSERT INTO `maintenance_subdivision` VALUES (1,'ESTANQUE',1),(2,'MANIFOR',1),(3,'MOTOR',2),(4,'SUSPENSIÓN',2),(5,'FRENOS',2),(6,'TRANSMISIÓN',2),(7,'SIRENAS Y ALARMAS AUDIBLES',3),(8,'LUCES DE EMERGENCIA',3),(9,'LUCES PERIMETRALES',3),(10,'LUCES DE POSICIÓN',3),(11,'ÓPTICOS',3),(12,'TABLERO',3),(13,'TABLERO BOMBA',3),(14,'LUCES COMPARTIMIENTOS',3),(15,'LUCES DE CABINA',3),(16,'COMPUTACIÓN GENERAL',3),(17,'BATERIAS',3),(18,'TORRE DE ILUMINACIÓN',3),(19,'CABINA',4),(20,'CARROCERIA',4),(21,'ESTRUCTURA',5),(22,'EQUIPOS MAYORES',5),(23,'MOTOBOMBAS',5),(24,'GENERADORES',5),(25,'MOTOSIERRAS',5),(26,'MOTOAMOLADORA',5),(27,'COMPARTIMIENTOS',5),(28,'POLLOS',5),(29,'NEUMÁTICOS',6),(30,'VIDRIOS',6),(31,'ELEMENTOS AUXILIARES',6),(36,'COMPARTIMIENTOS',4),(37,'SELLOS',1),(38,'RODAMIENTOS BOMBA',1),(39,'CARDAN BOMBA',1),(40,'CUERPO BOMBA',1);
/*!40000 ALTER TABLE `maintenance_subdivision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_taller`
--

DROP TABLE IF EXISTS `maintenance_taller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_taller` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) NOT NULL,
  `razon_social` varchar(45) NOT NULL,
  `rut` varchar(12) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `contacto` varchar(45) DEFAULT NULL,
  `tel_contacto` int(11) DEFAULT NULL,
  `direccion` varchar(60) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_taller`
--

LOCK TABLES `maintenance_taller` WRITE;
/*!40000 ALTER TABLE `maintenance_taller` DISABLE KEYS */;
INSERT INTO `maintenance_taller` VALUES (2,'ELECTRICO','TALLER OSCIEL GUZMAN',NULL,NULL,NULL,NULL,NULL,NULL),(3,'DESABOLLADURA Y PINTURA','TALLER REPCAR',NULL,NULL,NULL,NULL,NULL,NULL),(4,'DESABOLLADURA Y PINTURA','MARCELO AGUALLO',NULL,NULL,NULL,NULL,NULL,NULL),(5,'SOLDADURAS','TALLER MARIO SOTO',NULL,NULL,NULL,NULL,NULL,NULL),(6,'SOLDADURAS','TALLER JUAN GOMEZ',NULL,NULL,NULL,NULL,NULL,NULL),(7,'MECANICA GENERAL','TALLER FEREXPO',NULL,NULL,NULL,NULL,NULL,NULL),(8,'MECANICA GENERAL','TALLER CARLOS VERA',NULL,NULL,NULL,NULL,NULL,NULL),(9,'MECANICA GENERAL','TALLER WALTER FONFACH',NULL,NULL,NULL,NULL,NULL,NULL),(10,'MECANICA GENERAL','TALLER SALFA SUR OSORNO',NULL,NULL,NULL,NULL,NULL,NULL),(11,'MECANICA GENERAL','TALLER SALFA SUR PUERTO MONTT',NULL,NULL,NULL,NULL,NULL,NULL),(12,'MECANICA GENERAL','TALLER KAUFMANN OSORNO',NULL,NULL,NULL,NULL,NULL,NULL),(13,'MECANICA GENERAL','TALLER MACO PUERTO MONTT',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `maintenance_taller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_tipomantencion`
--

DROP TABLE IF EXISTS `maintenance_tipomantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_tipomantencion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_tipomantencion`
--

LOCK TABLES `maintenance_tipomantencion` WRITE;
/*!40000 ALTER TABLE `maintenance_tipomantencion` DISABLE KEYS */;
INSERT INTO `maintenance_tipomantencion` VALUES (1,'Correctiva','Todas las mantenciones que se hacen cuando existe una falla de por medio como roturas de motor, etc'),(2,'Preventiva','Todas las mantenciones donde no existe una falla como cambio de aceite, filtros, etc.');
/*!40000 ALTER TABLE `maintenance_tipomantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_usuariocomp`
--

DROP TABLE IF EXISTS `maintenance_usuariocomp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_usuariocomp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `compania_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `maintenance_usuarioc_compania_id_8f938f73_fk_maintenan` (`compania_id`),
  CONSTRAINT `maintenance_usuarioc_compania_id_8f938f73_fk_maintenan` FOREIGN KEY (`compania_id`) REFERENCES `maintenance_compania` (`id`),
  CONSTRAINT `maintenance_usuariocomp_user_id_35dc7e40_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_usuariocomp`
--

LOCK TABLES `maintenance_usuariocomp` WRITE;
/*!40000 ALTER TABLE `maintenance_usuariocomp` DISABLE KEYS */;
INSERT INTO `maintenance_usuariocomp` VALUES (1,'3',2,9),(2,'2',3,9),(3,'1',4,2),(4,'1',6,3),(5,'1',8,6),(6,'0',5,2),(7,'0',7,3),(8,'0',9,6),(9,'3',1,9),(10,'0',10,6),(11,'0',11,2),(12,'0',12,3);
/*!40000 ALTER TABLE `maintenance_usuariocomp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-13 21:08:38
