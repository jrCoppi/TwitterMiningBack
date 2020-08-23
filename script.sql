#CREATE DATABSE
CREATE DATABASE TwitterMining;
use TwitterMining;

CREATE TABLE `termo` (
   `id_termo` int(11) unsigned NOT NULL AUTO_INCREMENT,
   `ds_termo` MEDIUMTEXT DEFAULT NULL,
   PRIMARY KEY (`id_termo`)
 ) ENGINE=InnoDB;
 
 CREATE TABLE `pesquisa` (
   `id_pesquisa` int(11) unsigned NOT NULL AUTO_INCREMENT,
   `dt_pesquisa` datetime DEFAULT NULL,
   `id_termo` int(11) unsigned DEFAULT NULL,
   PRIMARY KEY (`id_pesquisa`),
   CONSTRAINT `termo_pesquisa` FOREIGN KEY (`id_termo`) REFERENCES `termo` (`id_termo`)
 ) ENGINE=InnoDB;
 
 CREATE TABLE `post` (
   `id_post` int(11) unsigned NOT NULL AUTO_INCREMENT,
   `ds_post` varchar(255) DEFAULT NULL,
   PRIMARY KEY (`id_post`)
 ) ENGINE=InnoDB;
 
 CREATE TABLE `pesquisa_post` (
   `id_pesquisa_post` int(11) unsigned NOT NULL AUTO_INCREMENT,
   `id_pesquisa` int(11) unsigned NOT NULL,
   `id_post` int(11) unsigned NOT NULL,
   PRIMARY KEY (`id_pesquisa_post`),
   KEY `id_pesquisa` (`id_pesquisa`),
   KEY `id_post` (`id_post`),
   CONSTRAINT `pesquisa_fk` FOREIGN KEY (`id_pesquisa`) REFERENCES `pesquisa` (`id_pesquisa`),
   CONSTRAINT `post_fk` FOREIGN KEY (`id_post`) REFERENCES `post` (`id_post`)
 ) ENGINE=InnoDB;