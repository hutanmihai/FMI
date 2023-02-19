create sequence SEQ_TURNEU
as integer
start with 1
increment by 1
maxvalue 10000;

insert into TURNEU values (next value for SEQ_TURNEU,'MSI', 'Roma', '2022-05-10'),
(next value for SEQ_TURNEU,'ALLSTARS', 'New York', '2022-01-12'),
(next value for SEQ_TURNEU,'WORLDS', 'Beijing', '2021-10-01'),
(next value for SEQ_TURNEU,'LCK-SUMMER', 'Seul', '2021-06-05'),
(next value for SEQ_TURNEU,'NA-SPRING', 'Boston', '2021-03-13'),
(next value for SEQ_TURNEU,'EUW-SUMMER', 'Paris', '2022-06-05'),
(next value for SEQ_TURNEU,'NA-SUMMER', 'Los Angeles', '2022-07-03'),
(next value for SEQ_TURNEU,'EUW-SPRING', 'London', '2022-04-01'),
(next value for SEQ_TURNEU,'LCK-SPRING', 'Seul', '2021-03-05'),
(next value for SEQ_TURNEU,'OCE-SUMMER','Sydney','2022-07-01')

insert into PREZENTATOR values ('James Patterson'),('David Turley'),
('Sam Hartman'),('Mark Zimmerman'),('Emily Rand'),('Barento Mohammed'),
('Julian Carr'),('Isaac Bentley'),('Max Anderson'),('Jordan Corby')

insert into SCENA values ('Main Stage'),('Second Stage'),('Third Stage'),
('Horn Stage'),('Panther Stage')

insert into MOD_JOC values ('Normal', 'Summoners Rift', '5'),
('Ranked', 'Summoners Rift', '5'),('Flex', 'Summoners Rift', '5'),
('Normal', 'Summoners Rift', '5'),('Normal', 'Twisted Treelines', '3'),
('Ranked', 'Twisted Treelines', '3'),('Flex', 'Twisted Treelines', '3'),
('Normal', 'ARAM', '5'),('Ranked', 'ARAM', '5'),
('Flex', 'ARAM', '5'),('Ranked', 'ARAM', '1')

insert into MECI values ('Revenge', '2022-05-10 12:00:00'),
('Revenge', '2022-05-11 16:00:00'),('Warriors', '2022-05-13 16:00:00'),
('Destroyers', '2022-05-14 16:00:00'),('Debut', '2021-10-01 12:00:00'),
('Academy', '2021-10-02 12:00:00'),('Academy', '2021-05-03 18:00:00'),
('RunnerUps', '2022-01-12 18:00:00'),('RunnerUps', '2022-01-12 18:00:00'),
('Academy', '2021-01-13 18:00:00')

insert into MECI_HEADER values (1,1,1,3),(2,2,1,3),(3,4,2,7),
(4,7,3,7),(5,9,2,10),(6,10,3,5),(7,3,1,4),
(8,6,1,8),(9,8,3,9),(10,10,4,10)

insert into GRUPA values ('A',1),('B',1),('C',1),('D',1),
('A',2),('B',2),('C',2),('D',2),('A',3),('B',3),('C',3),
('D',3),('A',4),('B',4),('C',4),('D',4),
('A',5),('B',5),('C',5),('D',5),('A',6),
('B',6),('C',6),('D',6)

insert into REGIUNE values ('KOR'),('EUNE'),('EUW'),
('NA'),('OCE'),('SA'),('TUR'),('RUS')

insert into ECHIPA values (1,'SKT-T1', 'SKT'),
(1,'Royal Never Give Up', 'RNG'),(3,'G2 Esports', 'G2'),
(4,'Evil Geniuses ', 'EG'),(6,'PSG Talon Esports', 'PSG'),
(6,'Canids Kalunga', 'RED'),(1,'Team Aze', 'AZE'),
(5,'Order', 'ORD'),(7,'fastpayWildcats', 'IW'),
(8,'SaigonBuffaloEsports', 'SGB')

insert into GRUPA_MAP values (1,1),(1,2),(1,3),
(1,4),(2,5),(2,6),(2,7),(2,8),(3,9),(3,10)

insert into MECI_MAP values (1,1),(2,1),(3,2),
(4,2),(1,3),(3,3),(1,4),(4,4),(2,5),(3,5)
,(5,6),(6,6),(5,7),(7,7),(6,8),(7,8),
(8,9),(5,9),(5,10),(6,10)

insert into CAMPION values ('Aatrox','the Darkin Blade','Blood Well'),
('Ahri','the Nine-Tailed Fox','Mana'),('Akali','the Rogue Assassin','Energy'),
('Alistar','the Minotaur','Mana'),('Amumu','the Sad Mummy','Mana'),
('Anivia','the Cryophoenix','Mana'),('Annie','the Dark Child','Mana'),
('Ashe','the Frost Archer','Mana'),('Fiddlesticks','the Ancient Fear','Mana'),
('Fizz','the Tidal Trickster','Mana'),('Gangplank','the Saltwater Scourge','Mana'),
('Hecarim','the Shadow of War','Mana'),('Jax','Grandmaster at Arms','Mana'),
('Jayce','the Defender of Tomorrow','Mana'),('Jhin','the Virtuoso','Mana'),
('Jinx','the Loose Cannon','Mana'),('KhaZix','the Voidreaver','Mana'),
('Lee Sin','the Blind Monk','Energy'),('Zed','the Master of Shadows','Energy'),
('Lux','the Lady of Luminosity','Mana')

insert into JUCATOR values (1,1,'Zeus','TOP'),(1,1,'Oner','JUNGLE'),
(1,1,'Faker','MID'),(1,1,'Gumayusi','BOT'),(1,1,'Keria','BOT'),
(2,1,'Bin','TOP'),(2,1,'Wei','JUNGLE'),(2,1,'Xiaohu','MID'),
(2,1,'Gala','BOT'),(2,1,'Ming','BOT'),
(3,3,'BrokenBlade','TOP'),(3,2,'Jankos','JUNGLE'),
(3,3,'Caps','MID'),(3,3,'Flakked','BOT'),(3,3,'Targamas','BOT'),
(4,1,'Impact','TOP'),(4,2,'Inspired','JUNGLE'),
(4,4,'Jojopyun','MID'),(4,4,'Danny','BOT'),(4,4,'Vulcan','BOT'),
(5,5,'Hanabi','TOP'),(5,1,'Juhan','JUNGLE'),
(5,1,'Bay','MID'),(5,5,'Unified','BOT'),(5,5,'Kaiwing','BOT'),
(6,6,'Guigo','TOP'),(6,6,'Aegis','JUNGLE'),
(6,6,'Avenger','MID'),(6,6,'TitaN','BOT'),(6,6,'Jojo','BOT'),
(7,1,'Lonely','TOP'),(7,6,'Dimitry','JUNGLE'),
(7,6,'Aloned','MID'),(7,1,'5Kid','BOT'),(7,6,'Straight','BOT'),
(8,5,'BioPanther','TOP'),(8,5,'Maximize','JUNGLE'),
(8,5,'Kisee','MID'),(8,5,'Puma','BOT'),(8,5,'Corporal','BOT'),
(9,7,'StarScreen','TOP'),(9,7,'Ferret','JUNGLE'),
(9,7,'Serin','MID'),(9,7,'HolyPhoenix','BOT'),(9,7,'Farfetch','BOT'),
(10,8,'Hasmed','TOP'),(10,8,'Bean J','JUNGLE'),
(10,8,'Froggy','MID'),(10,8,'Shogun','BOT'),(10,8,'Taki','BOT')

insert into CAMPION_POOL values 
(1,1),(1,3),(1,5),(2,2),(2,4),(2,6),
(3,2),(3,3),(3,6),(5,18),(4,20),(4,11),
(5,5),(6,10),(7,11),(8,13),(8,14),(8,15),
(9,19),(9,20),(10,18),(13,9),(12,10),(11,11),
(12,12),(13,13),(14,14),(15,15),(16,16),
(15,17),(16,18),(17,19),(17,20),(18,2),
(18,3),(17,18),
(18,4),(19,5),(19,6),(20,7),(20,8),(19,7),
(21,20),(21,18),(21,13),(23,9),(22,8),(22,10),
(23,10),(24,15),(24,16),(25,19),(25,18),
(25,17),(26,12),(26,13),(27,13),
(28,15),(28,14),(27,14),
(29,16),(29,17),(29,3),(30,6),(30,5),
(31,5),(32,1),(32,2),(31,1),
(32,9),(33,4),(33,3),(35,1),(34,2),(33,9),
(35,3),(36,8),(36,7),(37,10),(37,11),(37,12),
(38,20),(38,19),(38,10),(39,20),(39,2),(39,3),
(40,1),(41,2),(41,3),(42,4),(42,1),(42,2),
(43,5),(44,6),(43,7),(45,8),(45,9),(44,10),
(45,13),(46,12),(46,11),(47,14),(47,15),(47,16),
(48,19),(48,18),(49,17),(49,20),(49,2),
(48,3),(50,8),(50,7),(50,4)