--17. Optimizarea unei cereri, aplicând regulile de optimizare ce derivã din proprietã?ile operatorilor algebrei rela?ionale.
--Cererea va fi exprimatã prin expresie algebricã, arbore algebric ?i limbaj (SQL), atât anterior cât ?i ulterior optimizãrii. 

/*Sã se afiseze id-ul, numele, prenumele, indemniza?ia sportivilor, dacã sunt medalia?i,
numele, tipul, data de start ?i data de finalã a competi?iei la care au participat.
Acestea vor fi afi?ate pentru sportivii care nu primesc indemniza?ie
( pentru cei care nu primesc indemniza?ie se va trece 0 în coloana indemniza?ie )
sau care participã la competi?ii care au în componen?ã primele 4 litere "CUPA"
?i care în ambele cazuri trebuie sã fi participat la competi?ii care au avut loc cel mult acum 5 ani fa?ã de data curentã.
De asemenea, numele ?i prenumele vor fi concatenate,
iar coloana se va numi corespunzãtor.
Coloanele sportiv, indemniza?ie ?i numele competitiei se vor numi corespunzator.
Mai mult, aceste date trebuie ordonate dupã numele sportivului.*/

select sp.id_sportiv as "Id-ul sportivului", concat(sp.nume,' ')||sp.prenume as "Nume sportiv",
nvl(sp.indemnizatie,0) "indemnizatie", part.medaliat, comp.nume as "Nume competitie", comp.data_start, comp.data_final,
t.tip_competitie

from sportiv sp join participa part on(sp.id_sportiv = part.id_sportiv)
                join competitie comp on (comp.id_competitie = part.id_competitie)
                join tip t on (t.id_tip = comp.id_tip)

where (sp.indemnizatie ! = 0  or upper(substr(comp.nume,1,4)) = 'CUPA')
and months_between (sysdate,comp.data_final)<60 --5 ani
order by "Nume sportiv";
