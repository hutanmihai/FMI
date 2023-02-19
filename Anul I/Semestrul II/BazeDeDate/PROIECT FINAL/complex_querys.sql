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