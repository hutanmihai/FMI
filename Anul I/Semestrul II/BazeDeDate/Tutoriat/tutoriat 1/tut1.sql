--tutoriat 1

--ex1
--Afisati numele concatenat cu prenumele si cu job_id-ul, separate prin virgula si spatiu.
--Etichetati coloana "Detalii angajat"

select last_name||','||first_name||','||job_id "Detalii angajat"
from employees;

--ex2
--o cerere pt a afisa numele,prenumele ang si salariul ang pt ang al caror salariu
--nu se afla in intervalul [1500,2850]

select last_name||' '|| first_name "Nume si Prenume", salary
from employees
where salary not between 1500 and 2850;

--ex3
--afisati nume sal si codul dep pt toti ang din dep 10 si 20, carae iau un salariu > 1500 in ord alf.

select first_name "Angajat", department_id "Cod departament"
from employees
where department_id IN (10,20) and salary>1500
order by first_name;

--invers alfabetic
select first_name "Angajat", department_id "Cod departament"
from employees
where department_id IN (10,20) and salary>1500
order by first_name desc;

--ex4
--afisati numele , salariul si comisionul pt toti salariatii care castiga comision
select last_name,salary,commission_pct
from employees
where commission_pct is not null;

--ex5
--listati numele tuturor angajitor care au 2 litere 'L' in nume si lucreaza in departament 30 
--sau managerul lor este 120

select first_name
from employees
where upper(first_name) like ('%L%L%') and (department_id=30 or manager_id=120);

--ex6
--afisam nume,job,salariu pt toti salariatii al caror job contine sirul "CLERK"
--sau "REP" SI salariul nu este egal cu 1000 sau 2000

SELECT last_name,job_id,salary
from employees
where (upper(job_id) LIKE ('%CLERK%') OR upper(job_id) LIKE ('%REP%')) and (salary not in (1000,2000));

-- _ inlocuieste un singur caracter

--LAB2

--1.
SELECT CONCAT(first_name,' ')||last_name||' castiga '||salary||' lunar dar doreste '||salary*3 "Salariu ideal"
FROM employees;

--2
select initcap(first_name) as prenume, upper(last_name) as nume, length(last_name) as lungime
from employees
where (upper(last_name) like ('J%')) or (upper(last_name) like ('M%')) or (upper(last_name) like ('__A%'))
order by lungime desc;

select initcap(first_name) as prenume, upper(last_name) as nume, length(last_name) as lungime
from employees
where (upper(last_name) like ('J%')) or (upper(last_name) like ('M%')) or (substr(upper(last_name),3,1)= 'A')
order by lungime desc;










