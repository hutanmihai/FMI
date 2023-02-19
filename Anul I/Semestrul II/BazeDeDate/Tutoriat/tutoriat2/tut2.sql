--tutoriat2
--6. S� se afi�eze codul salariatului, numele, salariul, salariul m�rit cu 15%,
--exprimat cu dou� zecimale �i num�rul de sute al salariului nou rotunjit la 2 zecimale.
--Eticheta�i ultimele dou� coloane �Salariu nou�, respectiv �Numar sute�.
--Se vor lua �n considerare salaria�ii al c�ror salariu nu este divizibil cu 1000.

select employee_id,last_name,salary, round(salary+salary*0.15,2) "Salariu nou", round((salary+0.15*salary)/100,2) "Numar sute"
from employees
where mod(salary,1000)!=0;


--7.S� se afi�eze detalii despre salaria�ii care au lucrat un num�r �ntreg de s�pt�m�ni p�n� la data curent�.
select last_name, ROUND(SYSDATE-hire_date) "Nr zile"
from employees
where mod( ROUND(SYSDATE-hire_date),7)=0;

--15. S� se listeze numele, salariul �i comisionul tuturor
--angaja�ilor al c�ror venit lunar (salariu + valoare comision) dep�e�te 10000.

select last_name,salary, commission_pct
from employees
where salary+salary* nvl(commission_pct,0) >10000;

--14 S� se afi�eze numele angaja�ilor �i comisionul.
--Dac� un angajat nu c�tig� comision, s� se scrie �Fara comision�. Eticheta�i coloana �Comision�.
select last_name, nvl(to_char(commission_pct),'Fara comision') "Comision"
from employees;

--18 S� se listeze codurile ?i denumirile job-urilor care exist� �n departamentul 30.

select jobs.job_id,jobs.job_title
from jobs join employees on (jobs.job_id = employees.job_id)
where department_id = 30;

select j.job_id, job_title
from jobs j, employees e
where department_id = 30 and j.job_id = e.job_id;

--19.S� se afi�eze numele angajatului, numele departamentului �i
--ora?ul pentru to�i angaja�ii care c�tig� comision.

--care sunt angajatii care au comision
select first_name||' '||last_name "Name", commission_pct,department_id
from employees
where commission_pct is not null;
--sunt 35 de angajati, iar unul dintre nu are deoartament

select first_name||' '||last_name "Name", commission_pct,department_name,city
from employees join departments on (employees.department_id = departments.department_id)
join locations on (departments.location_id = locations.location_id)
where commission_pct is not null;
--sunt 34 de angajati


--to�i angaja�ii
select first_name||' '||last_name "Name", commission_pct,department_name,city
from employees left join departments on (employees.department_id = departments.department_id)
left join locations on (departments.location_id = locations.location_id)
where commission_pct is not null;


--22.S� se afi�eze codul angajatului �i numele acestuia, 
--�mpreun� cu numele �i codul �efului s�u direct. 
--Se vor eticheta coloanele Ang#, Angajat, Mgr#, Manager.

select *
from employees;

select ang.employee_id Ang#, ang.last_name Angajat,sef.employee_id Mgr#, sef.last_name Manager
from employees ang, employees sef
where ang.manager_id = sef.employee_id;

--pentru a lua in considerare si angajatii fara manager

select ang.employee_id Ang#, ang.last_name Angajat,sef.employee_id Mgr#, sef.last_name Manager
from employees ang, employees sef
where ang.manager_id = sef.employee_id (+);

-- (+) se traduce prin operatia de outer join 
-- se pune in partea deficitara => la noi se pune in dreptul lui employees
-- pt ca exista angajati care nu au manager











