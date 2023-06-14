------------------------------- DROP TABLES -------------------------------

-- DROP TABLE meci_header;
-- DROP TABLE scena;
-- DROP TABLE prezentator;
-- DROP TABLE mod_joc;
--
-- DROP TABLE meci_map;
-- DROP TABLE meci;
--
-- DROP TABLE campion_pool;
-- DROP TABLE campion;
-- DROP TABLE jucator;
--
-- DROP TABLE grupa_map;
-- DROP TABLE grupa;
-- DROP TABLE turneu;
--
-- DROP TABLE echipa;
-- DROP TABLE regiune;
--
-- BEGIN
--    FOR rec IN (SELECT trigger_name FROM user_triggers)
--    LOOP
--       EXECUTE IMMEDIATE 'DROP TRIGGER ' || rec.trigger_name;
--    END LOOP;
-- END;
-- /
--
-- DROP TABLE istoric;


----------------------------------- SCENA -----------------------------------
CREATE TABLE scena
(
    id   NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_scena PRIMARY KEY,
    nume VARCHAR2(50)
        CONSTRAINT nume_scena NOT NULL
)

INSERT INTO scena(nume)
VALUES ('Main Stage')

INSERT INTO scena(nume)
VALUES ('Second Stage')

INSERT INTO scena(nume)
VALUES ('Third Stage')

INSERT INTO scena(nume)
VALUES ('Horn Stage')

INSERT INTO scena(nume)
VALUES ('Panther Stage')

COMMIT;

----------------------------------- PREZENTATOR -----------------------------------
CREATE TABLE prezentator
(
    id   NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_prezentator PRIMARY KEY,
    nume VARCHAR2(50)
        CONSTRAINT nume_prezentator NOT NULL
)

INSERT INTO prezentator(nume)
VALUES ('James Patterson')

INSERT INTO prezentator(nume)
VALUES ('David Turley')

INSERT INTO prezentator(nume)
VALUES ('Sam Hartman')

INSERT INTO prezentator(nume)
VALUES ('Mark Zimmerman')

INSERT INTO prezentator(nume)
VALUES ('Emily Rand')

INSERT INTO prezentator(nume)
VALUES ('Barento Mohammed')

INSERT INTO prezentator(nume)
VALUES ('Julian Carr')

INSERT INTO prezentator(nume)
VALUES ('Isaac Bentley')

INSERT INTO prezentator(nume)
VALUES ('Max Anderson')

INSERT INTO prezentator(nume)
VALUES ('Jordan Corby')

COMMIT;

----------------------------------- MOD_JOC -----------------------------------
CREATE TABLE mod_joc
(
    id         NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_mod_joc PRIMARY KEY,
    nume       VARCHAR2(50)
        CONSTRAINT nume_mod_joc NOT NULL,
    harta      VARCHAR2(50)
        CONSTRAINT harta_mod_joc NOT NULL,
    dimensiune NUMBER(5)
        CONSTRAINT dimensiune_mod_joc NOT NULL
)

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Normal', 'Summoners Rift', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Ranked', 'Summoners Rift', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Flex', 'Summoners Rift', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Normal', 'Summoners Rift', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Normal', 'Twisted Treelines', '3')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Ranked', 'Twisted Treelines', '3')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Flex', 'Twisted Treelines', '3')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Normal', 'ARAM', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Ranked', 'ARAM', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Flex', 'ARAM', '5')

INSERT INTO mod_joc(nume, harta, dimensiune)
VALUES ('Ranked', 'ARAM', '1')

COMMIT;

----------------------------------- MECI -----------------------------------
CREATE TABLE meci
(
    id    NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_meci PRIMARY KEY,
    titlu VARCHAR2(50)
        CONSTRAINT titlu_meci NOT NULL,
    data  DATE
        CONSTRAINT data_meci NOT NULL
)

INSERT INTO meci(titlu, data)
VALUES ('Revenge', TO_DATE('2022-05-10', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Revenge', TO_DATE('2022-05-11', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Warriors', TO_DATE('2022-05-13', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Destroyers', TO_DATE('2022-05-14', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Debut', TO_DATE('2021-10-01', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Academy', TO_DATE('2021-10-02', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Academy', TO_DATE('2021-05-03', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('RunnerUps', TO_DATE('2022-01-12', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('RunnerUps', TO_DATE('2022-01-12', 'YYYY-MM-DD'))

INSERT INTO meci(titlu, data)
VALUES ('Academy', TO_DATE('2021-01-13', 'YYYY-MM-DD'))

COMMIT;

----------------------------------- CAMPION -----------------------------------
CREATE TABLE campion
(
    id      NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_campion PRIMARY KEY,
    nume    VARCHAR2(50)
        CONSTRAINT nume_campion NOT NULL,
    titlu   VARCHAR2(50)
        CONSTRAINT titlu_campion NOT NULL,
    resursa VARCHAR2(50)
        CONSTRAINT resursa_campion NOT NULL
)

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Aatrox', 'the Darkin Blade', 'Blood Well')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Ahri', 'the Nine-Tailed Fox', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Akali', 'the Rogue Assassin', 'Energy')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Alistar', 'the Minotaur', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Amumu', 'the Sad Mummy', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Anivia', 'the Cryophoenix', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Annie', 'the Dark Child', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Ashe', 'the Frost Archer', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Fiddlesticks', 'the Ancient Fear', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Fizz', 'the Tidal Trickster', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Gangplank', 'the Saltwater Scourge', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Hecarim', 'the Shadow of War', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Jax', 'Grandmaster at Arms', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Jayce', 'the Defender of Tomorrow', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Jhin', 'the Virtuoso', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Jinx', 'the Loose Cannon', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('KhaZix', 'the Voidreaver', 'Mana')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Lee Sin', 'the Blind Monk', 'Energy')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Zed', 'the Master of Shadows', 'Energy')

INSERT INTO campion(nume, titlu, resursa)
VALUES ('Lux', 'the Lady of Luminosity', 'Mana')

COMMIT;

----------------------------------- TURNEU -----------------------------------
CREATE TABLE turneu
(
    id   NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_turneu PRIMARY KEY,
    nume VARCHAR2(50)
        CONSTRAINT nume_turneu NOT NULL,
    oras VARCHAR2(50)
        CONSTRAINT oras_turneu NOT NULL,
    data DATE
        CONSTRAINT data_turneu NOT NULL
)

INSERT INTO turneu(nume, oras, data)
VALUES ('MSI', 'Roma', TO_DATE('2022-05-10', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('ALLSTARS', 'New York', TO_DATE('2022-01-12', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('WORLDS', 'Beijing', TO_DATE('2021-10-01', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('LCK-SUMMER', 'Seul', TO_DATE('2021-06-05', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('NA-SPRING', 'Boston', TO_DATE('2021-03-13', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('EUW-SUMMER', 'Paris', TO_DATE('2022-06-05', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('NA-SUMMER', 'Los Angeles', TO_DATE('2022-07-03', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('EUW-SPRING', 'London', TO_DATE('2022-04-01', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('LCK-SPRING', 'Seul', TO_DATE('2021-03-05', 'YYYY-MM-DD'))

INSERT INTO turneu(nume, oras, data)
VALUES ('OCE-SUMMER', 'Sydney', TO_DATE('2022-07-01', 'YYYY-MM-DD'))

COMMIT;

----------------------------------- REGIUNE -----------------------------------
CREATE TABLE regiune
(
    id   NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_regiune PRIMARY KEY,
    nume VARCHAR2(50)
        CONSTRAINT nume_regiune NOT NULL
)

INSERT INTO regiune(nume)
VALUES ('KOR')

INSERT INTO regiune(nume)
VALUES ('EUNE')

INSERT INTO regiune(nume)
VALUES ('EUW')

INSERT INTO regiune(nume)
VALUES ('NA')

INSERT INTO regiune(nume)
VALUES ('OCE')

INSERT INTO regiune(nume)
VALUES ('SA')

INSERT INTO regiune(nume)
VALUES ('TUR')

INSERT INTO regiune(nume)
VALUES ('RUS')

COMMIT;

----------------------------------- GRUPA -----------------------------------
CREATE TABLE grupa
(
    id        NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_grupa PRIMARY KEY,
    nume      VARCHAR2(50)
        CONSTRAINT nume_grupa NOT NULL,
    id_turneu NUMBER(5) NOT NULL,
    CONSTRAINT fk_turneu_grupa FOREIGN KEY (id_turneu) REFERENCES turneu (id)
)

-- ('A',1),('B',1),('C',1),('D',1),
-- ('A',2),('B',2),('C',2),('D',2),('A',3),('B',3),('C',3),
-- ('D',3),('A',4),('B',4),('C',4),('D',4),
-- ('A',5),('B',5),('C',5),('D',5),('A',6),
-- ('B',6),('C',6),('D',6)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 1)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 1)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 1)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 1)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 2)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 2)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 2)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 2)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 3)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 3)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 3)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 3)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 4)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 4)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 4)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 4)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 5)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 5)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 5)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 5)

INSERT INTO grupa(nume, id_turneu)
VALUES ('A', 6)

INSERT INTO grupa(nume, id_turneu)
VALUES ('B', 6)

INSERT INTO grupa(nume, id_turneu)
VALUES ('C', 6)

INSERT INTO grupa(nume, id_turneu)
VALUES ('D', 6)

COMMIT;

----------------------------------- ECHIPA -----------------------------------
CREATE TABLE echipa
(
    id         NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_echipa PRIMARY KEY,
    nume       VARCHAR2(50)
        CONSTRAINT nume_echipa NOT NULL,
    tag        VARCHAR2(50)
        CONSTRAINT tag_echipa NOT NULL,
    id_regiune NUMBER(5) NOT NULL,
    CONSTRAINT fk_regiune_echipa FOREIGN KEY (id_regiune) REFERENCES regiune (id)
)

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (1, 'SKT-T1', 'SKT')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (1, 'Royal Never Give Up', 'RNG')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (3, 'G2 Esports', 'G2')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (4, 'Evil Geniuses ', 'EG')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (6, 'PSG Talon Esports', 'PSG')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (6, 'Canids Kalunga', 'RED')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (1, 'Team Aze', 'AZE')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (5, 'Order', 'ORD')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (7, 'fastpayWildcats', 'IW')

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (8, 'SaigonBuffaloEsports', 'SGB')

COMMIT;

----------------------------------- GRUPA_MAP -----------------------------------
CREATE TABLE grupa_map
(
    id_grupa  NUMBER(5)
        CONSTRAINT pk_grupa_map_grupa REFERENCES grupa (id),
    id_echipa NUMBER(5)
        CONSTRAINT pk_grupa_map_echipa REFERENCES echipa (id),
    CONSTRAINT pk_grupa_map PRIMARY KEY (id_grupa, id_echipa)
)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (1, 1)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (1, 2)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (1, 3)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (1, 4)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (2, 5)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (2, 6)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (2, 7)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (2, 8)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (3, 9)

INSERT INTO grupa_map(id_grupa, id_echipa)
VALUES (3, 10)

COMMIT;

----------------------------------- JUCATOR -----------------------------------
CREATE TABLE jucator
(
    id         NUMBER(5) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT pkey_jucator PRIMARY KEY,
    nume       VARCHAR2(50)
        CONSTRAINT nume_jucator NOT NULL,
    lane       VARCHAR2(50)
        CONSTRAINT lane_jucator NOT NULL,
    id_echipa  NUMBER(5) NOT NULL,
    CONSTRAINT fk_echipa_jucator FOREIGN KEY (id_echipa) REFERENCES echipa (id),
    id_regiune NUMBER(5) NOT NULL,
    CONSTRAINT fk_regiune_jucator FOREIGN KEY (id_regiune) REFERENCES regiune (id)
)

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (1, 1, 'Zeus', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (1, 1, 'Oner', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (1, 1, 'Faker', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (1, 1, 'Gumayusi', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (1, 1, 'Keria', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (2, 1, 'Bin', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (2, 1, 'Wei', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (2, 1, 'Xiaohu', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (2, 1, 'Gala', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (2, 1, 'Ming', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (3, 3, 'BrokenBlade', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (3, 2, 'Jankos', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (3, 3, 'Caps', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (3, 3, 'Flakked', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (3, 3, 'Targamas', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (4, 1, 'Impact', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (4, 2, 'Inspired', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (4, 4, 'Jojopyun', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (4, 4, 'Danny', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (4, 4, 'Vulcan', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (5, 5, 'Hanabi', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (5, 1, 'Juhan', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (5, 1, 'Bay', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (5, 5, 'Unified', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (5, 5, 'Kaiwing', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (6, 6, 'Guigo', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (6, 6, 'Aegis', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (6, 6, 'Avenger', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (6, 6, 'TitaN', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (6, 6, 'Jojo', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (7, 1, 'Lonely', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (7, 6, 'Dimitry', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (7, 6, 'Aloned', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (7, 1, '5Kid', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (7, 6, 'Straight', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (8, 5, 'BioPanther', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (8, 5, 'Maximize', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (8, 5, 'Kisee', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (8, 5, 'Puma', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (8, 5, 'Corporal', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (9, 7, 'StarScreen', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (9, 7, 'Ferret', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (9, 7, 'Serin', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (9, 7, 'HolyPhoenix', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (9, 7, 'Farfetch', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (10, 8, 'Hasmed', 'TOP')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (10, 8, 'Bean J', 'JUNGLE')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (10, 8, 'Froggy', 'MID')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (10, 8, 'Shogun', 'BOT')

INSERT INTO jucator(id_echipa, id_regiune, nume, lane)
VALUES (10, 8, 'Taki', 'BOT')

COMMIT;

----------------------------------- CAMPION_POOL -----------------------------------
CREATE TABLE campion_pool
(
    id_campion NUMBER(5)
        CONSTRAINT pk_campion_pool_campion REFERENCES campion (id),
    id_jucator NUMBER(5)
        CONSTRAINT pk_campion_pool_jucator REFERENCES jucator (id),
    CONSTRAINT pk_campion_pool PRIMARY KEY (id_campion, id_jucator)
)

-- (1,1),(1,3),(1,5),(2,2),(2,4),(2,6),(3,2),(3,3),(3,6),(5,18),(4,20),(4,11),(5,5),(6,10),(7,11),(8,13),(8,14),(8,15),
-- (9,19),(9,20),(10,18),(13,9),(12,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(15,17),(16,18),(17,19),(17,20),
-- (18,2),(18,3),(17,18),(18,4),(19,5),(19,6),(20,7),(20,8),(19,7),(21,20),(21,18),(21,13),(23,9),(22,8),(22,10),(23,10),
-- (24,15),(24,16),(25,19),(25,18),(25,17),(26,12),(26,13),(27,13),(28,15),(28,14),(27,14),(29,16),(29,17),(29,3),(30,6),
-- (30,5),(31,5),(32,1),(32,2),(31,1),(32,9),(33,4),(33,3),(35,1),(34,2),(33,9),(35,3),(36,8),(36,7),(37,10),(37,11),
-- (37,12),(38,20),(38,19),(38,10),(39,20),(39,2),(39,3),(40,1),(41,2),(41,3),(42,4),(42,1),(42,2),(43,5),(44,6),(43,7),
-- (45,8),(45,9),(44,10),(45,13),(46,12),(46,11),(47,14),(47,15),(47,16),(48,19),(48,18),(49,17),(49,20),(49,2),(48,3),
-- (50,8),(50,7),(50,4)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (1, 1)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (1, 3)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (1, 5)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (2, 2)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (2, 4)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (2, 6)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (3, 2)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (3, 3)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (3, 6)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (5, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (4, 20)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (4, 11)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (5, 5)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (6, 10)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (7, 11)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (8, 13)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (8, 14)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (8, 15)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (9, 19)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (9, 20)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (10, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (13, 9)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (12, 10)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (11, 11)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (12, 12)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (13, 13)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (14, 14)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (15, 15)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (16, 16)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (15, 17)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (16, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (17, 19)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (17, 20)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (18, 2)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (18, 3)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (17, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (18, 4)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (19, 5)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (20, 6)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (19, 7)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (21, 8)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (21, 9)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (20, 10)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (21, 13)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (22, 12)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (22, 11)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (23, 14)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (23, 15)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (23, 16)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (24, 19)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (24, 20)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (25, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (26, 17)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (27, 16)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (28, 15)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (29, 14)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (30, 13)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (31, 12)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (32, 11)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (33, 10)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (34, 9)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (35, 8)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (36, 7)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (37, 6)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (38, 5)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (39, 4)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (40, 3)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (41, 2)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (42, 1)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (43, 20)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (44, 19)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (45, 18)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (46, 17)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (47, 16)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (48, 15)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (49, 14)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (50, 13)

INSERT INTO campion_pool(id_jucator, id_campion)
VALUES (50, 12)

COMMIT;

----------------------------------- MECI_MAP -----------------------------------
CREATE TABLE meci_map
(
    id_echipa NUMBER(5)
        CONSTRAINT pk_meci_map_echipa REFERENCES echipa (id),
    id_meci   NUMBER(5)
        CONSTRAINT pk_meci_map_meci REFERENCES meci (id),
    CONSTRAINT pk_meci_map PRIMARY KEY (id_echipa, id_meci)
)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (1, 1)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (2, 1)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (3, 2)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (4, 2)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (1, 3)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (3, 3)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (1, 4)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (4, 4)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (2, 5)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (3, 5)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (5, 6)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (6, 6)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (5, 7)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (7, 7)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (6, 8)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (7, 8)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (8, 9)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (5, 9)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (5, 10)

INSERT INTO meci_map(id_echipa, id_meci)
VALUES (6, 10)

COMMIT;

----------------------------------- MECI_HEADER -----------------------------------
CREATE TABLE meci_header
(
    id_meci        NUMBER(5)
        CONSTRAINT pk_meci_header_meci REFERENCES meci (id),
    id_prezentator NUMBER(5)
        CONSTRAINT pk_meci_header_prezentator REFERENCES prezentator (id),
    id_scena       NUMBER(5)
        CONSTRAINT pk_meci_header_scena REFERENCES scena (id),
    id_mod         NUMBER(5)
        CONSTRAINT pk_meci_header_mod REFERENCES mod_joc (id),
    CONSTRAINT pk_meci_header PRIMARY KEY (id_meci, id_prezentator, id_scena, id_mod)
)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (1, 1, 3, 1)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (2, 2, 1, 3)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (3, 4, 2, 7)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (4, 7, 3, 7)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (5, 9, 2, 10)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (6, 10, 3, 5)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (7, 3, 1, 4)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (8, 6, 1, 8)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (9, 8, 3, 9)

INSERT INTO meci_header(id_meci, id_prezentator, id_scena, id_mod)
VALUES (10, 10, 4, 10)

COMMIT;
