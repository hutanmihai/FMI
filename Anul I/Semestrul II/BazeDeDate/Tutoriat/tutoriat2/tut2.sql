--tutoriat2
--6. Sã se afiºeze codul salariatului, numele, salariul, salariul mãrit cu 15%,
--exprimat cu douã zecimale ºi numãrul de sute al salariului nou rotunjit la 2 zecimale.
--Etichetaþi ultimele douã coloane “Salariu nou”, respectiv “Numar sute”.
--Se vor lua în considerare salariaþii al cãror salariu nu este divizibil cu 1000.

select employee_id,last_name,salary, round(salary+salary*0.15,2) "Salariu nou", round((salary+0.15*salary)/100,2) "Numar sute"
from employees
where mod(salary,1000)!=0;


--7.Sã se afiºeze detalii despre salariaþii care au lucrat un numãr întreg de sãptãmâni pânã la data curentã.
select last_name, ROUND(SYSDATE-hire_date) "Nr zile"
from employees
where mod( ROUND(SYSDATE-hire_date),7)=0;

--15. Sã se listeze numele, salariul ºi comisionul tuturor
--angajaþilor al cãror venit lunar (salariu + valoare comision) depãºeºte 10000.

select last_name,salary, commission_pct
from employees
where salary+salary* nvl(commission_pct,0) >10000;

--14 Sã se afiºeze numele angajaþilor ºi comisionul.
--Dacã un angajat nu câºtigã comision, sã se scrie “Fara comision”. Etichetaþi coloana “Comision”.
select last_name, nvl(to_char(commission_pct),'Fara comision') "Comision"
from employees;

--18 Sã se listeze codurile ?i denumirile job-urilor care existã în departamentul 30.

select jobs.job_id,jobs.job_title
from jobs join employees on (jobs.job_id = employees.job_id)
where department_id = 30;

select j.job_id, job_title
from jobs j, employees e
where department_id = 30 and j.job_id = e.job_id;

--19.Sã se afiºeze numele angajatului, numele departamentului ºi
--ora?ul pentru toþi angajaþii care câºtigã comision.

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


--toþi angajaþii
select first_name||' '||last_name "Name", commission_pct,department_name,city
from employees left join departments on (employees.department_id = departments.department_id)
left join locations on (departments.location_id = locations.location_id)
where commission_pct is not null;


--22.Sã se afiºeze codul angajatului ºi numele acestuia, 
--împreunã cu numele ºi codul ºefului sãu direct. 
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











