--EX1
DECLARE
    x NUMBER(1) := 5;
    y x%TYPE    := NULL;
BEGIN
    IF x <> y THEN
        dbms_output.put_line('valoare <> null este = true');
    ELSE
        dbms_output.put_line('valoare <> null este != true');
    END IF;
    x := NULL;
    IF x = y THEN
        dbms_output.put_line('null = null este = true');
    ELSE
        dbms_output.put_line('null = null este != true');
    END IF;
END; /

--EX2

--a)
DECLARE
    TYPE emp_record IS RECORD
                       (
                           cod     employees.employee_id%TYPE,
                           salariu employees.salary%TYPE,
                           job     employees.job_id%TYPE
                       );
    v_ang emp_record;
BEGIN
    v_ang.cod := 700;
    v_ang.salariu := 9000;
    v_ang.job := 'SA_MAN';
    dbms_output.put_line('Angajatul cu codul ' || v_ang.cod ||
                         ' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/

--b)
DECLARE
    TYPE emp_record IS RECORD
                       (
                           cod     employees.employee_id%TYPE,
                           salariu employees.salary%TYPE,
                           job     employees.job_id%TYPE
                       );
    v_ang emp_record;
BEGIN
    SELECT employee_id, salary, job_id
    INTO v_ang
    FROM employees
    WHERE employee_id = 101;
    dbms_output.put_line('Angajatul cu codul ' || v_ang.cod ||
                         ' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/

--c)
DECLARE
    TYPE emp_record IS RECORD
                       (
                           cod     employees.employee_id%TYPE,
                           salariu employees.salary%TYPE,
                           job     employees.job_id%TYPE
                       );
    v_ang emp_record;
BEGIN
    DELETE
    FROM emp_300
    WHERE employee_id = 100
    RETURNING employee_id
        , salary
        , job_id
    INTO v_ang;
    dbms_output.put_line('Angajatul cu codul ' || v_ang.cod ||
                         ' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/
ROLLBACK;

--EX3
DECLARE
    v_ang1 employees%ROWTYPE;
    v_ang2 employees%ROWTYPE;
BEGIN
    -- sterg angajat 100 si mentin in variabila linia stearsa
    DELETE
    FROM emp_300
    WHERE employee_id = 100
    RETURNING employee_id
        , first_name
        , last_name
        , email
        , phone_number
        , hire_date
        , job_id
        , salary
        , commission_pct
        , manager_id
        , department_id
    INTO v_ang1;
-- inserez in tabel linia stearsa
    INSERT INTO emp_300
    VALUES v_ang1;
-- sterg angajat 101
    DELETE
    FROM emp_300
    WHERE employee_id = 101;
-- obtin datele din tabelul employees
    SELECT *
    INTO v_ang2
    FROM employees
    WHERE employee_id = 101;
-- inserez o linie oarecare in emp_***
    INSERT INTO emp_300
    VALUES (1000, 'FN', 'LN', 'E', NULL, SYSDATE, 'AD_VP', 1000, NULL, 100, 90);
-- modific linia adaugata anterior cu valorile variabilei v_ang2
    UPDATE emp_300
    SET row = v_ang2
    WHERE employee_id = 1000;
END;
/

--EX4
DECLARE
    TYPE tablou_indexat IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
    t tablou_indexat;
BEGIN
    --a)
    FOR i IN 1..10
        LOOP
            t(i) := i;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(t(i) || ' ');
        END LOOP;
    dbms_output.new_line;
    --b)
    FOR i IN 1..10
        LOOP
            IF i MOD 2 = 1 THEN
                t(i) := NULL;
            END IF;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(NVL(t(i), 0) || ' ');
        END LOOP;
    dbms_output.new_line;
    --c)
    t.delete(t.first);
    t.delete(5, 7);
    t.delete(t.last);
    dbms_output.put_line('Primul element are indicele ' || t.first ||
                         ' si valoarea ' || NVL(t(t.first), 0));
    dbms_output.put_line('Ultimul element are indicele ' || t.last ||
                         ' si valoarea ' || NVL(t(t.last), 0));
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            IF t.EXISTS(i) THEN
                dbms_output.put(NVL(t(i), 0) || ' ');
            END IF;
        END LOOP;
    dbms_output.new_line;
    --d)
    t.delete;
    dbms_output.put_line('Tabloul are ' || t.count || ' elemente.');
END; /

--EX5
DECLARE
    TYPE tablou_indexat IS TABLE OF emp_300%ROWTYPE
        INDEX BY
        binary_integer;
    t tablou_indexat;
BEGIN
    -- stergere din tabel si salvare in tablou
    DELETE
    FROM emp_300
    WHERE rownum <= 2
    RETURNING employee_id
        , first_name
        , last_name
        , email
        , phone_number
        , hire_date
        , job_id
        , salary
        , commission_pct
        , manager_id
        , department_id
        BULK COLLECT
    INTO t;
--afisare elemente tablou
    dbms_output.put_line(t(1).employee_id || ' ' || t(1).last_name);
    dbms_output.put_line(t(2).employee_id || ' ' || t(2).last_name);
--inserare cele 2 linii in tabel
    INSERT INTO emp_300 VALUES t(1);
    INSERT INTO emp_300 VALUES t(2);
END;
/

--EX6
DECLARE
    TYPE tablou_imbricat IS TABLE OF NUMBER;
    t tablou_imbricat := tablou_imbricat();
BEGIN
    --a)
    FOR i IN 1..10
        LOOP
            t.extend;
            t(i) := i;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(t(i) || ' ');
        END LOOP;
    dbms_output.new_line;
    --b)
    FOR i IN 1..10
        LOOP
            IF i MOD 2 = 1 THEN
                t(i) := NULL;
            END IF;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(NVL(t(i), 0) || ' ');
        END LOOP;
    dbms_output.new_line;
-- punctul c
    t.delete(t.first);
    t.delete(5, 7);
    t.delete(t.last);
    dbms_output.put_line('Primul element are indicele ' || t.first ||
                         ' si valoarea ' || NVL(t(t.first), 0));
    dbms_output.put_line('Ultimul element are indicele ' || t.last ||
                         ' si valoarea ' || NVL(t(t.last), 0));
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            IF t.exists(i) THEN
                dbms_output.put(NVL(t(i), 0) || ' ');
            END IF;
        END LOOP;
    dbms_output.new_line;
    --d)
    t.delete;
    dbms_output.put_line('Tabloul are ' || t.count || ' elemente.');
END; /

--EX7
DECLARE
    TYPE tablou_imbricat IS TABLE OF CHAR(1);
    t tablou_imbricat := tablou_imbricat('m', 'i', 'n', 'i', 'm');
    i INTEGER;
BEGIN
    i := t.first;
    WHILE i <= t.last
        LOOP
            dbms_output.put(t(i));
            i := t.next(i);
        END LOOP;
    dbms_output.new_line;
    i := t.last;
    WHILE i >= t.first
        LOOP
            dbms_output.put(t(i));
            i := t.prior(i);
        END LOOP;
    dbms_output.new_line;
    t.delete(2);
    t.delete(4);
    i := t.first;
    WHILE i <= t.last
        LOOP
            dbms_output.put(t(i));
            i := t.next(i);
        END LOOP;
    dbms_output.new_line;
    i := t.last;
    WHILE i >= t.first
        LOOP
            dbms_output.put(t(i));
            i := t.prior(i);
        END LOOP;
    dbms_output.new_line;
END; /

--EX8
DECLARE
    TYPE vector IS VARRAY(20) OF NUMBER;
    t vector := vector();
BEGIN
    --a)
    FOR i IN 1..10
        LOOP
            t.extend; t(i) := i;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(t(i) || ' ');
        END LOOP;
    dbms_output.new_line;
    --b)
    FOR i IN 1..10
        LOOP
            IF i MOD 2 = 1 THEN
                t(i) := NULL;
            END IF;
        END LOOP;
    dbms_output.put('Tabloul are ' || t.count || ' elemente: ');
    FOR i IN t.first..t.last
        LOOP
            dbms_output.put(NVL(t(i), 0) || ' ');
        END LOOP;
    dbms_output.new_line;
    --c)
-- metodele DELETE(n), DELETE(m,n) nu sunt valabile pentru vectori!!!
-- din vectori nu se pot sterge elemente individuale!!!
    --d)
    t.delete;
    dbms_output.put_line('Tabloul are ' || t.count || ' elemente.');
END;
/

--EX9
CREATE OR REPLACE TYPE subordonati_*** AS VARRAY(10) OF NUMBER(4);
/
CREATE TABLE manageri_*** (cod_mgr NUMBER(10),
                           nume VARCHAR2(20),
                           lista subordonati_***);
DECLARE
    v_sub   subordonati_***:= subordonati_***(100,200,300);
    v_lista manageri_***.lista%TYPE;
BEGIN
    INSERT INTO manageri_***
    VALUES (1, 'Mgr 1', v_sub);
    INSERT INTO manageri_***
    VALUES (2, 'Mgr 2', NULL);
    INSERT INTO manageri_***
    VALUES (3, 'Mgr 3', subordonati_***(400, 500));
    SELECT lista
    INTO v_lista
    FROM manageri_***
    WHERE cod_mgr=1;
    FOR j IN v_lista.first..v_lista.last
        LOOP
            dbms_output.put_line(v_lista(j));
        END LOOP;
END;
/
SELECT *
FROM manageri_***;
DROP TABLE manageri_***;
DROP TYPE subordonati_***;

--EX10
CREATE TABLE emp_test_*** AS
SELECT employee_id, last_name
FROM employees
WHERE rownum <= 2;
CREATE OR REPLACE TYPE tip_telefon_*** IS TABLE OF VARCHAR(12);
/
ALTER TABLE emp_test_***
ADD (telefon tip_telefon_***)
NESTED TABLE telefon STORE AS tabel_telefon_***;
INSERT INTO emp_test_***
VALUES (500, 'XYZ', tip_telefon_***('074XXX', '0213XXX', '037XXX'));
UPDATE emp_test_***
SET telefon = tip_telefon_***('073XXX', '0214XXX')
    WHERE employee_id=100;
SELECT a.employee_id, b.*
FROM emp_test_*** A, TABLE (A.telefon) b;
DROP TABLE emp_test_***;
DROP TYPE tip_telefon_***;

--EX11
--VAR1
DECLARE
    TYPE tip_cod IS VARRAY(5) OF NUMBER(3);
    coduri tip_cod := tip_cod(205, 206);
BEGIN
    FOR i IN coduri.first..coduri.last
        LOOP
            DELETE
            FROM emp_***
            WHERE employee_id = coduri (I);
        END LOOP;
END;
/
SELECT employee_id
FROM emp_***;
ROLLBACK

--VAR2
DECLARE
    TYPE tip_cod IS VARRAY(20) OF NUMBER;
    coduri tip_cod := tip_cod(205, 206);
BEGIN
    FORALL i IN coduri.first..coduri.last
        DELETE FROM emp_***
    WHERE  employee_id = coduri (I);
END;
/
SELECT employee_id
FROM emp_***;
ROLLBACK;
