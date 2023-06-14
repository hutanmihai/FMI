--2
BEGIN
    <<principal>>
        DECLARE
        v_client_id     NUMBER(4)    := 1600;
        v_client_nume   VARCHAR2(50) := 'N1';
        v_nou_client_id NUMBER(3)    := 500;
    BEGIN
        <<secundar>>
            DECLARE
            v_client_id       number(4)    := 0;
            v_client_nume     varchar2(50) := 'N2';
            v_nou_client_id   number(3)    := 300;
            v_nou_client_nume VARCHAR2(50) := 'N3';
        BEGIN
            v_client_id := v_nou_client_id;
            principal.v_client_nume :=
                        v_client_nume || ' ' || v_nou_client_nume;
            --poziția 1
        END;
        v_client_id := (v_client_id * 12) / 10;
        --poziția 2
    END;
END;
/

-- Determinați:
-- valoarea variabilei v_client_id la poziția 1;
-- valoarea variabilei v_client_nume la poziția 1;
-- valoarea variabilei v_nou_client_id la poziția 1;
-- valoarea variabilei v_nou_client_nume la poziția 1; - valoarea variabilei v_id_client la poziția 2;
-- valoarea variabilei v_client_nume la poziția 2.

-- Soluție:
-- Poz1 v_client_id 300
-- Poz1 v_client_nume N2
-- Poz1 v_nou_client_id 300
-- Poz1 v_nou_client_nume N3
-- Poz2 v_client_id 1920
-- Poz2 v_client_nume N2 N3
------------------------------------------------------------------------------------------------------------------------

--3
-- Creați un bloc anonim care să afișeze propoziția "Invat PL/SQL" pe ecran.

-- Varianta 1 - Afișare folosind variabile de legătură
VARIABLE g_mesaj VARCHAR2(50)
BEGIN
    :g_mesaj := 'Invat PL/SQL';
END; /
PRINT g_mesaj

-- Varianta 2 - Afișare folosind procedurile din pachetul standard DBMS_OUTPUT
BEGIN
    dbms_output.put_line('Invat PL/SQL');
END; /
------------------------------------------------------------------------------------------------------------------------

--4
-- Definiți un bloc anonim în care să se afle numele departamentului cu cei mai mulți angajați.
-- Comentați cazul în care există cel puțin două departamente cu număr maxim de angajați.
DECLARE
    v_dep departments.department_name%TYPE;
BEGIN
    SELECT department_name
    INTO v_dep
    FROM employees e,
         departments d
    WHERE e.department_id = d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                       FROM employees
                       GROUP BY department_id);
    dbms_output.put_line('Departamentul ' || v_dep);
END; /
------------------------------------------------------------------------------------------------------------------------

--5
-- Rezolvați problema anterioară utilizând variabile de legătură. Afișați rezultatul atât din bloc,
-- cât și din exteriorul acestuia.
VARIABLE rezultat VARCHAR2(35)
BEGIN
    SELECT department_name
    INTO :rezultat
    FROM employees e,
         departments d
    WHERE e.department_id = d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                       FROM employees
                       GROUP BY department_id);
    dbms_output.put_line('Departamentul ' || :rezultat);
END;
/
PRINT rezultat
------------------------------------------------------------------------------------------------------------------------

--6
-- Modificați exercițiul anterior astfel încât să obțineți și numărul de angajați din departamentul respectiv.
DECLARE
    v_dep departments.department_name%TYPE;
BEGIN
    SELECT department_name || ' ' || COUNT(*)
    INTO v_dep
    FROM employees e,
         departments d
    WHERE e.department_id = d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                       FROM employees
                       GROUP BY department_id);
    dbms_output.put_line('Departamentul ' || v_dep);
END; /
------------------------------------------------------------------------------------------------------------------------

--7
--Determinați salariul anual și bonusul pe care îl primește un salariat al cărui cod este dat de la tastatură.
--Bonusul este determinat astfel: dacă salariul anual este cel puțin 200001, atunci bonusul este 20000;
--dacă salariul anual este cel puțin 100001 și cel mult 200000, atunci bonusul este 10000,
--iar dacă salariul anual este cel mult 100000, atunci bonusul este 5000. Afișați bonusul obținut.
--Comentați cazul în care nu există niciun angajat cu codul introdus.

--Obs. Se folosește instrucțiunea IF.
--      IF condiție1 THEN
--         secvența_de_comenzi_1
--      [ELSIF condiție2 THEN
--         secvența_de_comenzi_2]
-- ... [ELSE
--         secvența_de_comenzi_n]
--      END IF;

SET VERIFY OFF
DECLARE
    v_cod           employees.employee_id%TYPE := &p_cod;
    v_bonus         NUMBER(8);
    v_salariu_anual NUMBER(8);
BEGIN
    SELECT salary * 12
    INTO v_salariu_anual
    FROM employees
    WHERE employee_id = v_cod;
    IF v_salariu_anual >= 200001
    THEN
        v_bonus := 20000;
    ELSIF v_salariu_anual BETWEEN 100001 AND 200000
    THEN
        v_bonus := 10000;
    ELSE
        v_bonus := 5000;
    END IF;
    dbms_output.put_line('Bonusul este ' || v_bonus);
END;
/
SET VERIFY ON
------------------------------------------------------------------------------------------------------------------------

--8
--Rezolvați problema anterioară folosind instrucțiunea CASE.
-- CASE test_var
--          WHEN valoare_1 THEN secvența_de_comenzi_1;
--          WHEN valoare_2 THEN secvența_de_comenzi_2;
-- ...
--     WHEN valoare_k THEN secvența_de_comenzi_k;
--     [ELSE altă_secvență;]
-- END CASE;
-- sau
-- CASE
--     WHEN condiție_1 THEN secvența_de_comenzi_1;
--     WHEN condiție_2 THEN secvența_de_comenzi_2,
--      ...
--     WHEN condiție_k THEN secvența_de_comenzi_k;
--     [ELSE alta_secvența;]
-- END CASE [eticheta];

-- Clauza ELSE este opțională.
-- Dacă aceasta este necesară în implementarea unei probleme, dar practic lipsește,
-- iar test_var nu ia nici una dintre valorile ce apar în clauzele WHEN,
-- atunci se declanșează eroarea predefinită CASE_NOT_FOUND (ORA - 6592).

DECLARE
    v_cod           employees.employee_id%TYPE := &p_cod;
    v_bonus         NUMBER(8);
    v_salariu_anual NUMBER(8);
BEGIN
    SELECT salary * 12
    INTO v_salariu_anual
    FROM employees
    WHERE employee_id = v_cod;
    CASE
        WHEN v_salariu_anual >= 200001
            THEN v_bonus := 20000;
        WHEN v_salariu_anual BETWEEN 100001 AND 200000
            THEN v_bonus := 10000;
        ELSE v_bonus := 5000;
        END CASE;
    dbms_output.put_line('Bonusul este ' || v_bonus);
END;
/
------------------------------------------------------------------------------------------------------------------------

--9
-- Scrieți un bloc PL/SQL în care stocați prin variabile de substituție un cod de angajat,
-- un cod de departament și procentul cu care se mărește salariul acestuia.
-- Să se mute salariatul în noul departament și să i se crească salariul în mod corespunzător.
-- Dacă modificarea s-a putut realiza (există în tabelulemp_prof un salariat având codul respectiv)
-- să se afișeze mesajul “Actualizare realizata”, iar în caz contrar mesajul “Nu exista un angajat cu acest cod”.
-- Anulați modificările realizate.

DEFINE p_cod_sal= 200
DEFINE p_cod_dept = 80
DEFINE p_procent =20
DECLARE
    v_cod_sal  emp_prof.employee_id%TYPE   := &p_cod_sal;
    v_cod_dept emp_prof.department_id%TYPE := &p_cod_dept;
    v_procent  NUMBER(8)                   := &p_procent;
BEGIN
    UPDATE emp_prof
    SET department_id = v_cod_dept,
        salary=salary + (salary * v_procent / 100)
    WHERE employee_id = v_cod_sal;
    IF SQL%ROWCOUNT = 0 THEN
        dbms_output.put_line('Nu exista un angajat cu acest cod');
    ELSE
        dbms_output.put_line('Actualizare realizata');
    END IF;
END;
/
ROLLBACK;
------------------------------------------------------------------------------------------------------------------------

--10
-- Creați tabelul zile_***(id, data, nume_zi).
-- Introduceți în tabelul zile_*** informațiile corespunzătoare tuturor zilelor care au rămas din luna curentă.
-- LOOP
--         secvența_de_comenzi
-- END LOOP;
-- Comanda se execută cel puțin o dată.
-- Dacă nu este utilizată comanda EXIT, ciclarea ar putea continua la infinit.

DECLARE
    contor NUMBER(6) := 1;
    v_data DATE;
    maxim  NUMBER(2) := LAST_DAY(SYSDATE) - SYSDATE;
BEGIN
    LOOP
        v_data := SYSDATE + contor;
        INSERT INTO zile_***
        VALUES (contor, v_data, to_char(v_data, 'Day'));
        contor := contor + 1;
        EXIT WHEN contor > maxim;
    END LOOP;
END;
/
------------------------------------------------------------------------------------------------------------------------

--11
-- Rezolvați cerința anterioară folosind instrucțiunea WHILE.
-- WHILE condiție LOOP
--     secvența_de_comenzi
-- END LOOP;
-- Dacă condiția este evaluată ca fiind FALSE sau NULL,
-- atunci secvența de comenzi nu este executată și controlul trece la instrucțiunea imediat următoare după END LOOP.

DECLARE
    contor NUMBER(6) := 1;
    v_data DATE;
    maxim  NUMBER(2) := LAST_DAY(SYSDATE) - SYSDATE;
BEGIN
    WHILE contor <= maxim
        LOOP
            v_data := SYSDATE + contor;
            INSERT INTO zile_***
            VALUES (contor, v_data, to_char(v_data, 'Day'));
            contor := contor + 1;
        END LOOP;
END;
/
------------------------------------------------------------------------------------------------------------------------

--12
-- Rezolvați cerința anterioară folosind instrucțiunea FOR.
-- FOR contor_ciclu IN [REVERSE] lim_inf..lim_sup LOOP
--         secvența_de_comenzi;
-- END LOOP;
-- Variabila contor_ciclu nu trebuie declarată, ea fiind implicit de tip BINARY_INTEGER. Aceasta este neidentificată în afara ciclului.
-- Pasul are implicit valoarea 1 și nu poate fi modificat.
-- Limitele domeniului pot fi variabile sau expresii, dar care pot fi convertite la întreg.

DECLARE
    v_data DATE;
    maxim  NUMBER(2) := LAST_DAY(SYSDATE) - SYSDATE;
BEGIN
    FOR contor IN 1..maxim
        LOOP
            v_data := SYSDATE + contor;
            INSERT INTO zile_***
            VALUES (contor, v_data, to_char(v_data, 'Day'));
        END LOOP;
END;
/
------------------------------------------------------------------------------------------------------------------------

--13
-- Să se declare și să se inițializeze cu 1 variabila i de tip POZITIVE și cu 10 constanta max_loop de tip POZITIVE.
-- Să se implementeze un ciclu LOOP care incrementează pe i până când acesta ajunge la o valoare > max_loop,
-- moment în care ciclul LOOP este părăsit și se sare la instrucțiunea i:=1.
-- Obs. Se utilizează instrucțiunile GOTO/EXIT.
-- Instrucțiunea EXIT permite ieșirea dintr-un ciclu. Controlul trece fie la prima instrucțiune
-- situată după END LOOP-ul corespunzător, fie la instrucțiunea având eticheta nume_eticheta.
-- EXIT [nume_eticheta] [WHEN condiție];
-- Numele etichetelor urmează aceleași reguli ca și cele definite pentru identificatori.
-- Eticheta se plasează înaintea comenzii, fie pe aceeași linie, fie pe o linie separată.
-- Etichetele se definesc prin intercalare între “<<” și “>>”.
-- GOTO nume_eticheta;

--Nu este permis saltul:
-- • în interiorul unui bloc (subbloc);
-- • în interiorul unei comenzi IF, CASE sau LOOP;
-- • de la o clauză a comenzii CASE, la altă clauză aceleași comenzi;
-- • de la tratarea unei excepții, în blocul curent;
-- • în exteriorul unui subprogram.

--VARIANTA 1
DECLARE
    i                 POSITIVE := 1;
    max_loop CONSTANT POSITIVE := 10;
BEGIN
    LOOP
        i := i + 1;
        IF i > max_loop THEN
            dbms_output.put_line('in loop i=' || i);
            GOTO urmator;
        END IF;
    END LOOP;
    <<urmator>>
        i := 1;
    dbms_output.put_line('dupa loop i=' || i);
END;
/

--VARIANTA2
DECLARE
    i                 POSITIVE := 1;
    max_loop CONSTANT POSITIVE := 10;
BEGIN
    i := 1;
    LOOP
        i := i + 1;
        dbms_output.put_line('in loop i=' || i);
        EXIT WHEN i > max_loop;
    END LOOP;
    i := 1;
    dbms_output.put_line('dupa loop i=' || i);
END; /
------------------------------------------------------------------------------------------------------------------------
