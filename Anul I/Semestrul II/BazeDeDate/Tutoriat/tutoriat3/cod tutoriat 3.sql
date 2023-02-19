--TUTORIAT 3
--RECAPITULARE JOIN
--LAB 3
--3
--S� se afi?eze numele, salariul, titlul job-ului, ora�ul �i �ara 
--�n care lucreaz� angaja?ii condu?i direct de King.

--am facut joinuri fara sa ne intereseze ca vrem angajatii condusi direct de King
SELECT last_name,salary,job_title,city,country_name
from employees join jobs on (employees.job_id = jobs.job_id)
               join departments on(employees.department_id = departments.department_id)
               join locations on (departments.location_id = locations.location_id)
               join countries on (locations.country_id = countries.country_id);
               
--ii vrem doar pe cei condusi direct de King => trebuie sa face un self join pt ca King este tot 
-- un agajat
select e.last_name,e.salary,job_title,city,country_name
from employees e join employees man_king on (e.manager_id = man_king.employee_id)
-- self join si vrem ca id_ul managerului e sa fie egal cu id_ul managerului 
                join jobs on (e.job_id = jobs.job_id)
                join departments on (e.department_id =  departments.department_id)
                join locations on (departments.location_id = locations.location_id)
                join countries on (locations.country_id = countries.country_id)
where upper(man_king.last_name) = upper('King');

--LAB2
--27.S�  se  afi�eze  numele  salariatului  �i  data  angaj�rii
--�mpreun�  cu  numele  �i  data angaj�rii �efului direct 
--pentru salaria�ii care au fost angaja�i �naintea �efilor lor.
--Se vor eticheta coloanele Angajat, Data_ang, Manager si Data_mgr.

--SEF DIRECT => SELF JOIN

select e.last_name Angajat, e.hire_date Data_ang, man.last_name Manager, man.hire_date Data_mgr
from employees e, employees man
where e.manager_id = man.employee_id --daca man e seful direct al angajatului
      and e.hire_date < man.hire_date;


--OPERATORI PE MULTIMI
--lAB 3
--11
--Se cer codurile departamentelor al c�ror nume con�ine �irul �re� 
--sau �n care lucreaz� angaja�i av�nd codul job-ului �SA_REP�.


SELECT department_id
from departments
where upper(department_name) like (upper('%re%')) --al c�ror nume con�ine �irul �re�

UNION --SAU

SELECT department_id
FROM employees
where upper(job_id) like ('SA_REP') -- �n care lucreaz� angaja�i av�nd codul job-ului �SA_REP�
     AND department_id is not null;


--13
--S� se ob?in� codurile departamentelor 
--�n care nu lucreaza nimeni (nu este introdus nici un salariat �n tabelul employees).

select department_id
from departments     --lista intreaga de departamente

MINUS

select department_id
from employees;         --departamentele in care lucreaza angajati


--14
--Se cer codurile departamentelor
--al c�ror nume con�ine �irul �re� 
--�i �n care lucreaz� angaja�i av�nd codul job-ului �HR_REP�. 

select department_id
from departments
where upper(department_name) like ('%RE%')

intersect

select department_id
from employees
where upper(job_id) like ('HR_REP') AND department_id is not null;


--SUBCERERI NECORELATE (subcerea se poate rula singura, fara sa aiba nevoie de ceva din cererea mare)

--18
--Folosind  subcereri,
--s�  se  afi�eze  numele  �i  salariul  angaja�ilor
--condu�i  direct  de pre�edintele companiei 
--(acesta este considerat angajatul care nu are manager).

SELECT last_name,salary
from employees
where manager_id = (select employee_id
                    from employees
                    where manager_id is null);

--in subcerere vom afla id-ul presedintelui companiei (care nu are manager)
--si in cerere avem la conditia de where ca managerul sa aiba id-ul gasit in subcerere

--19
--Scrie?i o cerere pentru a afi�a
--numele, codul departamentului ?i salariul angaja?ilor
--al c�ror 
--cod de departament ?i salariu  coincid
--cu codul departamentului ?i salariul unui angajat care c�?tig� comision.

select last_name,department_id,salary
from employees
where (department_id,salary) in (select department_id,salary
                                from employees
                                where commission_pct is not null
                                and department_id is not null);





















