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


