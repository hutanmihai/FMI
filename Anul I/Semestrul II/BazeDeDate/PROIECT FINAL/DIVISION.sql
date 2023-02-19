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