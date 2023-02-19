--ex subcereri necorelate
select*from sportiv;

--inseram sportivul
INSERT INTO sportiv(id_sportiv,gen,nume,prenume,anul_nasterii,id_nationalitate,tip_sportiv,indemnizatie,id_antrenor)
VALUES (13,'M','MAREL','RADU',TO_DATE('20-09-1966','dd-mm-yyyy'),1,'SPORTIV',NULL,50);

select nume,prenume,decode(nvl(indemnizatie,0),0,'Sportivul nu face parte din lot',800,'sportiv foarte valoros din lot','sportiv din lot')as "Stadiu sportiv"
from sportiv sp
where sp.anul_nasterii  in(select anul_nasterii
                        		from antrenor antr
                        		where sp.anul_nasterii=antr.anul_nasterii 
                                and substr(antr.nume,1,1) in (select substr(cl.nume_club,1,1)
                                                                from club cl
                                                            where substr(antr.nume,1,1)=substr(cl.nume_club,1,1)
                                                            )
                        );

ROLLBACK;


--create.update

CREATE TABLE CLUB_tutoriat
(id_club NUMBER(5),
nume_club VARCHAR2(50) CONSTRAINT nume_club_tut_nn NOT NULL,
UNIQUE (nume_club)
);
ALTER TABLE CLUB_tutoriat 
ADD CONSTRAINT id_club_tut_pk PRIMARY KEY (id_club);

CREATE TABLE ANTRENOR_tutoriat
(
id_antrenor NUMBER(5),
nume VARCHAR2(25) CONSTRAINT nume_antrenor_tut_nn NOT NULL,
prenume VARCHAR2(25) CONSTRAINT prenume_antrenor_tut_nn NOT NULL,
anul_nasterii DATE CONSTRAINT nastere_tut_nn NOT NULL,
gen CHAR(1) CONSTRAINT gen_tut_nn NOT NULL, 
ani_experienta NUMBER(3),--poate fi null
salariu NUMBER(8,2) CONSTRAINT salariu_tut_min CHECK (salariu>300.00),
id_club NUMBER(5),
CONSTRAINT genul_tut CHECK (gen='M' OR gen='F')
);
ALTER TABLE ANTRENOR_tutoriat 
ADD CONSTRAINT id_antrenor_tut_pk PRIMARY KEY(id_antrenor);
ALTER TABLE ANTRENOR_tutoriat 
ADD CONSTRAINT id_club_tut_fk FOREIGN KEY(id_club) REFERENCES CLUB_tutoriat (id_club);

select * from club_tutoriat;
select*from antrenor_tutoriat;

--inserari
--Crearea unei secven?e care este utilizatã pentru inserarea înregistrãrilor 
SELECT * FROM club_tutoriat;
CREATE SEQUENCE SEQ_club_tutoriat
INCREMENT BY 10
START WITH 10
MAXVALUE 10000
NOCYCLE;

INSERT INTO club_tutoriat
VALUES(SEQ_club_tutoriat.NEXTVAL, 'AQUA TEAM');

INSERT INTO club_tutoriat
VALUES(SEQ_club_tutoriat.NEXTVAL, 'DELFINUL BUCURESTI');

INSERT INTO club_tutoriat
VALUES(SEQ_club_tutoriat.NEXTVAL, 'BUCHAREST SPORT CLUB ELITE');

INSERT INTO club_tutoriat
VALUES(SEQ_club_tutoriat.NEXTVAL, 'STEAUA CSA');

INSERT INTO club_tutoriat
VALUES(SEQ_club_tutoriat.NEXTVAL, 'ATACK TEAM');

SELECT *FROM club_tutoriat;

COMMIT;

SELECT *FROM club_tutoriat;


SELECT *FROM antrenor_tutoriat;

INSERT INTO antrenor_tutoriat(id_antrenor,nume,prenume,anul_nasterii,gen,ani_experienta,salariu,id_club)
VALUES (1,'BECHERU','CATALIN',TO_DATE('10-09-1981','dd-mm-yyyy'),'M',10,500,20);

INSERT INTO antrenor_tutoriat(id_antrenor,nume,prenume,anul_nasterii,gen,ani_experienta,salariu,id_club)
VALUES (2,'BECHERU','IULIA',TO_DATE('20-12-1984','dd-mm-yyyy'),'F',8,400.54,20);

commit;

--exemplu update
update antrenor_tutoriat
set salariu = salariu*0.2+salariu
where ani_experienta>9;
ROLLBACK;

drop table club_tutoriat;
drop table antrenor_tutoriat;
