/*ALL QUETYS FOR THIS PROJECT*/

--EX11

/*Afisati numele echipelor care au meciuri pe scena Main Stage.*/
select distinct concat(concat('Echipa ', ECHIPA.nume), 
' are meciuri si pe scena Main Stage') as Raspuns
from ECHIPA, MECI_MAP, MECI, MECI_HEADER, SCENA
where ECHIPA.id = MECI_MAP.id_echipa and MECI_MAP.id_meci = MECI.id 
and MECI.id = MECI_HEADER.id_meci and MECI_HEADER.id_scena = SCENA.id 
and upper(SCENA.nume) like upper('Main Stage');

/*Afisati titlul meciurilor, meciuri ce incep dupa ora 16:00,
iar titlul contine litera e, ordonate dupa titlul meciului.*/
select MECI.titlu from MECI
where MECI.titlu in 
(select MECI.titlu from MECI where MECI.id in 
(select MECI.id from MECI where 
DATEPART(hour, MECI.data_incepere)>16 and MECI.titlu like '%e%'))
order by MECI.titlu

/*Afisati pentru fiecare jucator numele si lane-ul jucat si numarul
de campioni jucati sub forma unui mesaj, utilizand case, ordonati descrescator.*/
select j.nume as Nume,j.lane as Lane,
CASE
	when (select count(id_jucator) from CAMPION_POOL
	where CAMPION_POOL.id_jucator = j.id) >= 4 then '4 Campioni'
	when (select count(id_jucator) from CAMPION_POOL
	where CAMPION_POOL.id_jucator = j.id) >= 3 then '3 Campioni'
	when (select count(id_jucator) from CAMPION_POOL
	where CAMPION_POOL.id_jucator = j.id) >= 2 then '2 Campioni'
	else '1 Campion'
END AS [Campioni jucati]
from JUCATOR j
where j.lane is not null
order by [Campioni jucati] desc

/* Afisati detaliile meciurilor jucate de catre echipe din
regiunea KOR in turnee ce au avut loc cel mult cu un an in urma.*/
select PREZENTATOR.nume as [Nume prezentator], SCENA.nume as [Numele scenei],
MECI.titlu as [Titlul meciului], MOD_JOC.nume as [Modul jocului]
from MECI_HEADER
inner join MECI on MECI_HEADER.id_meci= MECI.id
inner join SCENA on MECI_HEADER.id_scena = SCENA.id
inner join PREZENTATOR on MECI_HEADER.id_prezentator = PREZENTATOR.id
inner join MOD_JOC on MECI_HEADER.id_mod = MOD_JOC.id
where MECI.id in (select id_meci from MECI_MAP where id_echipa in 
(select id from ECHIPA where ECHIPA.id_regiune = 
(select id from REGIUNE where REGIUNE.nume = 'KOR')) and id_echipa
in (select id_echipa from GRUPA_MAP where id_grupa
in (select id from GRUPA where id_turneu in (select
id from TURNEU where DATEDIFF(year, convert(date, sysdatetime()),TURNEU.data_incepere) <= 1 ))));

/*Afisati top 5 echipe al caror jucatori joaca in total mai multi campioni
decat average-ul tuturor echipelor, ordonat descrscator dupa numarul de campioni jucati.*/
with grouped
as(
	select COUNT(CAMPION_POOL.id_jucator) as [Numar campioni jucati]
	, ECHIPA.nume as [Numele echipei] from CAMPION_POOL
	inner join JUCATOR on CAMPION_POOL.id_jucator = JUCATOR.id
	inner join ECHIPA on JUCATOR.id_echipa = ECHIPA.id
	group by ECHIPA.nume)
select top 5 [Numar campioni jucati], [Numele echipei] from grouped
where [Numar campioni jucati] > (select avg([Numar campioni jucati]) from grouped)
order by [Numar campioni jucati] desc


--EX12

/*Prezentatorul David Turley se va pensiona, fiind inlocuit de George Yankee.*/
UPDATE PREZENTATOR
SET nume = 'George Yankee'
where id in (select id from PREZENTATOR where nume = 'David Turley')

/*Bjergesen a fost transferat in locul lui Caps.*/
UPDATE JUCATOR
SET nume = 'Bjergesen', id_regiune = 4
where id in (select id from JUCATOR where nume = 'Caps')

/*Deoarece campionii Ashe si Hecarim si sunt foarte off-meta,
toti pro-playerii au ales sa joace un nou campion ce este foarte bun in acest meta, respectiv Jhin*/
UPDATE CAMPION_POOL
SET id_campion = 15
where id_campion in (select id from CAMPION where nume = 'Ashe' or nume = 'Hecarim')


--EX13

create sequence SEQ_TURNEU
as integer
start with 1
increment by 1
maxvalue 10000;


--EX14

create view [SKT T1] as
select j.nume as [Jucatorii echipei SKT T1] from JUCATOR j
where j.id_echipa = (select e.id from ECHIPA e where e.tag = 'SKT')

/*ALLOWED-UPDATE ROW deoarece nu folosim functii grup sau clauza group by sau cuvantul cheie distinct,
sau pseudocoloana ROWNUM si nici coloane definite prin expresii.*/
update [SKT T1] 
set [SKT T1].[Jucatorii echipei SKT T1] = 'Kafu1'
where [SKT T1].[Jucatorii echipei SKT T1] = 'Keria'

/*NOT ALLOWED-INSERT ROW deoarece exista coloane NOT NULL fara valoare implicita in
tabelul de baza care nu au fost selectate in vedere (in cazult nostru coloana lane).*/
insert into [SKT T1] values ('Kafu2')


--EX15

create index index_jucator_nume_lane
on JUCATOR(id_regiune, nume, lane)

/*Afiseaza id-ul regiunii, numele si lane-ul jucatorilor unde id-ul regiunii este 1 si lane-ul este 'TOP'.*/
select id_regiune, nume, lane from JUCATOR
where id_regiune = 1 and lane = 'TOP'


--EX16

/*Sa afiseze ce prezentatori nu au prezentat niciun meci, ce scena nu a fost folosita
si ce mod de joc nu a fost folosit.*/
select p.nume, s.nume, mj.nume, mj.dimensiune from MECI_HEADER mh
full outer join MECI m on mh.id_meci = m.id
full outer join SCENA s on mh.id_scena = s.id
full outer join PREZENTATOR p on p.id = mh.id_prezentator
full outer join MOD_JOC mj on mj.id = mh.id_mod
where p.nume is null or s.nume is null or mj.nume is null

/*Sa se obtina toti jucatorii care sunt in echipe ce provin din regiunile cu id 1 sau 4.*/
select * from JUCATOR j
where not exists (
select e.id from ECHIPA e
where j.id_echipa = e.id
except
select e.id from ECHIPA e
where e.id_regiune != 1 and e.id_regiune != 4
)


/*Sa se obtina prezentatorii ce nu prezinta meciuri pe scena cu id-ul numarul 1*/
select * from PREZENTATOR p
where exists (
select id_meci from MECI_HEADER
where p.id = MECI_HEADER.id_prezentator
except
select id_meci from MECI_HEADER
where id_scena = 1
)