/*S� se afi?eze id-ul, numele, prenumele, indemniza?ia sportivilor, dac� sunt medalia?i, numele, tipul, data de start 
 ?i data de final a competi?iei la care au participat. Acestea vor fi afi?ate pentru sportivii 
  care nu primesc indemniza?ie( pentru cei care nu primesc indemniza?ie se va trece 0 �n coloana indemniza?ie )
 sau care participa la competi?ii care au �n componen?� primele 4 litere "CUPA"
  ?i care �n ambele cazuri trebuie s� fi participat la competi?ii care au avut loc cel mult acum 5 ani 
  fa?� de data curent�. De asemenea, numele si prenumele vor fi concatenate, iar coloana se va numi corespunz�tor. Coloanele 
  id_sportiv, indemnizatie ?i numele competi?iei se vor numi corespunz�tor. Mai mult, aceste date trebuie ordonate dup� numele
  sportivului.*/

 select sp.id_sportiv as "Id-ul sportivului",concat(sp.nume,'  ')||sp.prenume as "Nume sportiv",
 nvl(sp.indemnizatie,0) "indemnizatie", part.medaliat, comp.nume as "Nume competitie",comp.data_start,
 comp.data_final, t.tip_competitie
 
 from sportiv sp join participa part on(sp.id_sportiv=part.id_sportiv)
                join competitie comp on(comp.id_competitie= part.id_competitie)
                join tip t on(t.id_tip=comp.id_tip)
where (sp.indemnizatie!=0 or UPPER(SUBSTR(comp.nume, 1, 4)) ='CUPA') and MONTHS_BETWEEN(sysdate,comp.data_final)<60 --5 ani
order by "Nume sportiv";

/*
Pentru cluburile �n care indemniza?ia maxim� este mai mare sau egal� cu 500 ?i
indemniza?ia minim� mai mic� sau egal� cu 300,
s� se ob�in� codul,
numele acestor cluburi �i indemniza?ia maxim� pe club ?i indemniza?ia minim�.
Nu se ?ine cont de valorile null de la sportivii
care nu au indemniza?ie

*/

-- Pentru a se rezolva s-au folosit grup�ri de date, func?ii grup( Min, Max) si filtrare la nivel de grupuri

SELECT id_club, nume_club, MAX(indemnizatie)AS "INDEMNIZATIA MAXIMA", Min(indemnizatie)AS "INDEMNIZATIA MINIMA"
FROM sportiv  JOIN antrenor USING(id_antrenor)
             JOIN club USING (id_club)
GROUP BY id_club,nume_club
HAVING MAX(indemnizatie) >= 500 AND MIN(indemnizatie)<=300;

/*
-- S� se afiseze ?�rile ordonate dup� nume �n care a concurat sportivul cu id-ul 11.
*/
--s-au utilizat: subcereri nesincronizate pe 5 tabele ?i order
 
select id_tara,nume_tara
from tara
                WHERE id_tara IN(select id_tara
                                from oras
                                where id_oras IN(select id_oras
                                                from competitie
                                                where id_competitie IN (select id_competitie
                                                                    from participa
                                                                    where id_sportiv= (select id_sportiv
                                                                                        from sportiv  
                                                                                        where ID_SPORTIV=11
                                                                                        )
                                                                        )
                                                    )
                                )
order by nume_tara;



/*
Pentru fiecare club care are antrenori (s� se ?tie c� �n aceast� diagram� un club trebuie sa aib� minimum un antrenor)
 s� se afi?eze id-ul clubului, suma total� a salariilor primite de antrenorii de la acel club
 ?i �ntr-o coloan� cu numele STATUS BUGET SALARII s� se afi?eze un mesaj care indic� statusul bugetului pentru salarii:
 pentru sumele mai mari de 1400 se va afi?a mesajul: SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MARE
pentru sumele �ntre 1200 ?i 1400 se va afi?a mesajul:SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MEDIE
 iar pentru restul se va afi?a mesajul: SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MICA

*/

-- s-au folosit: clauza WITH, group by, order si CASE
with salarii as(select id_club, sum(salariu) SUMA
            from  antrenor 
            group by id_club
            order by id_club
            )

select id_club,SUMA,
CASE  WHEN SUMA>1400 THEN 'SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MARE '
      WHEN SUMA< 1400 AND SUMA>1200 THEN 'SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MEDIE'
      ELSE 'SUMA ALOCATA DE CLUB PENTRU A PLATI SALARIUL TUTUROR ANTRENORILOR ESTE MICA'
END as "STATUS BUGET SALARII"
from salarii;



--OPERATII DE SUPRIMARE A DATELOR

--1. S� se creasc� cu 20% salariul antrenorilor care lucreaz� la clubul Delfinul Bucuresti. S� se anuleze modific�rile.
update antrenor
set salariu=salariu*1.2
where salariu IN( select salariu 
                from antrenor
                where id_club=(select id_club
                                from club
                                where nume_club=upper('DELFINUL BUCURESTI')));
SELECT *FROM ANTRENOR; --pentru verificare
ROLLBACK;


--2. S� se elimine tipurile de competi?ii care nu au nicio competi?ie aferent�. S� se anuleze modific�rile.
select * from competitie;
select * from tip;
delete 
from TIP
where id_tip not in(select unique id_tip
                    from competitie);
 ROLLBACK;  

--3. S� se majoreze cu 10% indemniza?ia pentru sportivii din lot care au ob?inut medalie la oricare dintre competi?ii. 
--   S� se anuleze modific�rile.
select * from participa;
select* from sportiv;
 update sportiv
 set indemnizatie=indemnizatie*1.1
 where id_sportiv IN (select unique id_sportiv
                    from participa
                    where medaliat=1)--exist� situa?ii �n care ?i un sportiv care nu se afl� �n lot poate s� ob?in� medalie
        and tip_sportiv=upper('SPORTIV LOT');
        --de aceea s-a mai ad�ugat aceas� condi?ie �n where pentru a verifica dac� sprtivul este din lot
                                            
 ROLLBACK;


/*Formula?i �n limbaj natural ?i implementa?i �n SQL:
o cerere ce utilizeaz� opera?ia outerjoin pe minimum 4 tabele ?i dou� cereri ce utilizeaz� opera?ia division.
*/
--DIVISION
/*S� se afi?eze id-ul sportivilor , numele ?i prenumele sportivilor care particip�
la CEL PUTIN acelea?i competi?ii ca sportivul cu id-ul 7.
Numele ?i prenumele trebuie concatenate, iar coloana trebuie numit� corespunz�tor.

REZOLVARE

Sportivii care particip� la cel pu?in acelea?i competi?ii cu sportivul cu id-ul 7
 sunt cei care partcip� ?i la alte competi?ii, dar obligatoriu la toate competi?iile 
 la care a participat sportivul cu id-ul 7 ( la competi?ia cu id-ul 5)
*/
SELECT w.id_sportiv, nume||' '||prenume "Numele intreg"
FROM participa w JOIN sportiv e ON (w.id_sportiv = e.id_sportiv)
WHERE id_competitie  IN (SELECT id_competitie 
                        FROM participa
                        WHERE id_sportiv = 7
                        ) -- sportivii care particip� la competi?iile sportivului cu id-ul 7
 AND w.id_sportiv != 7
GROUP BY w.id_sportiv, nume,prenume
HAVING COUNT(*) = (SELECT COUNT(id_competitie)--sa fie egal cu numarul de competitii ale sportivului 7
                    FROM participa
                    WHERE id_sportiv = 7
                    );

--select * from participa;
--SELECT id_competitie 
--FROM participa
--WHERE id_sportiv = 7;

/*S� se afi?eze numele ?i prenumele tuturor sportivilor. 
Pentru fiecare sportiv �n parte se va afi?a numele sponsorului/sponsorilor
care �l sponsorizeaz� pe sportiv, c�t ?i  numele tuturor probelor,
 la care a participat sportivul (se dore?te ca probele la care a participat s� se afi?eze cu to?i sponsorii).
*/
select s.nume as "NUME SPORTIV",s.prenume AS "PRENUME SPORTIV",spons.nume AS "NUME SPONSOR", prob.nume AS "PROBA"
from sportiv s full outer join sponsorizeaza p on(s.id_sportiv= p.id_sportiv)
                full outer join participa pr on(s.id_sportiv= pr.id_sportiv )
                full outer join proba prob on (prob.id_proba=pr.id_proba)
                full outer join sponsor spons on(spons.id_sponsor=p.id_sponsor);
























