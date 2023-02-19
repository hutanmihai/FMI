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

select * from CAMPION