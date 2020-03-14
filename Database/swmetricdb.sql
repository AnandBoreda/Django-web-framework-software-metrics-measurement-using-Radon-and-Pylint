create database if not exists `softwaremetric`;

USE `softwaremetric`;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into `django_session` values 

('d38w2jae2dpsvudvf9jja71hand4i4an','N2Y5YzdhYmQzMmRmNzQyNDc1MmZhNGU5NjVmMjc5MWEzN2FiM2IzZjp7Im5hbWUiOiJuYXZlZW4iLCJtYWlsIjoibmF2ZWVuMTIzQGdtYWlsLmNvbSJ9','2020-02-03 09:11:10'),

('j1r1pdeautg61kmcooiyw6pwuv9iq4e9','NjIxYWZiMDMwMWM4ZTk1ZjNlMTE5NjRjYmUxOWFmMTc5MWM3MmZjMjp7Im5hbWUiOiJNZWdoYW5hIiwibWFpbCI6Im1lZ2hhbmFAZ21haWwuY29tIn0=','2020-02-02 10:36:49');

DROP TABLE IF EXISTS `Metrics_upload`;

CREATE TABLE `Metrics_upload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(100) NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

insert into `Metrics_upload` values 

(1,'text','files/pdfs/arrays_spjerLp.py'),

(2,'py','files/pdfs/test.py'),

(3,'pattern','files/pdfs/pattern.py'),

(4,'radioview','files/pdfs/views.py'),

(5,'views1','files/pdfs/views_buO9eOI.py');
/*Table structure for table `metrics_user` */

DROP TABLE IF EXISTS `Metrics_user`;

CREATE TABLE `Metrics_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `mail` varchar(254) NOT NULL,
  `passwd` varchar(40) NOT NULL,
  `cwpasswd` varchar(40) NOT NULL,
  `qualification` varchar(40) NOT NULL,
  `mobileno` varchar(50) NOT NULL,
  `status` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB
 AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `metrics_user` */

insert into `Metrics_user` values 

(1,'Anand ','Anand.boreda@pm.me','123','123','B.tech','8374563449','Activated'),

(2,'Anil','anilchowdaryabburi643@gmail.com','123','123','B.tech','9618289819','Activated'),

(3,'Syed Moiz','sd.moiz01@gmail.com','123','123','B.tech','7095200226','Activated'),

(4,'Yashwanth ','madalayashwanth49@gmail.com','123','123','btech','9700347030','Activated');

SET FOREIGN_KEY_CHECKS=1;
