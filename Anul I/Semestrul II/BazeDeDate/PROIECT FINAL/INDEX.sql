create index index_jucator_nume_lane
on JUCATOR(id_regiune, nume, lane)

/*Afiseaza id-ul regiunii, numele si lane-ul jucatorilor unde id-ul regiunii este 1 si lane-ul este 'TOP'.*/
select id_regiune, nume, lane from JUCATOR
where id_regiune = 1 and lane = 'TOP'