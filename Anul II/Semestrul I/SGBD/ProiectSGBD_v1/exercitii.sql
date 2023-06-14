/* Observații:
    • Proiectul trebuie realizat individual.
    • Cerințele 1-12 sunt obligatorii pentru a putea obține punctajul necesar și a intra în prima etapă de
    examinare.
    • Baza de date trebuie să fie în a treia formă normală (FN3).
    • Pentru a fi luat în considerare proiectul trebuie să conțină:
         -> un fișier text care să conțină codul SQL, respectiv în PL/SQL pentru toate cerințele (4-12/14);
         -> un fișier docx/pdf care să integreze toate cerințele cu rezolvările lor în SQL, respectiv în PL/SQL
         (sub formă de text, nu ca imagine), incluzând print-screen-uri prin care să se
         demonstreze că tot codul inclus în proiect a fost rulat în Oracle.
    • Informațiile pentru modul de încărcare a proiectelor le veți găsi pe Teams.
    • Deadline încărcare proiecte vineri, 13 ianuarie 2023, ora 23:59. */

------------------------------------------------------------------------------------------------------------------------

-- EX6
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat
-- independent care să utilizeze două tipuri diferite de colecții studiate. Apelați subprogramul.

-- Cerința 6:
-- Pentru un turneu al carui nume este dat, pentru fiecare regiune, afisati toate echipele si jucatorii ce apartin
-- acelei regiuni sau mesajul 'Nu exista!'.

CREATE OR REPLACE PROCEDURE ex6(nume_turneu turneu.nume%TYPE)
AS
    TYPE tabl_idx IS TABLE OF regiune%ROWTYPE INDEX BY PLS_INTEGER;
    v_regiuni tabl_idx;
    TYPE tip_lista_nested IS TABLE OF echipa%ROWTYPE;
    v_echipe  tip_lista_nested := tip_lista_nested();
    TYPE tabl_index IS TABLE OF VARCHAR2(200) INDEX BY PLS_INTEGER;
    v_nume    tabl_index;
    v_numar   NUMBER(5);
BEGIN
    SELECT * BULK COLLECT INTO v_regiuni FROM regiune;

    SELECT COUNT(*)
    INTO v_numar
    FROM echipa e,
         turneu t,
         grupa_map gm,
         grupa g
    WHERE e.id = gm.id_echipa
      AND t.id = gm.id_grupa
      AND g.id = gm.id_grupa
      AND t.id = g.id_turneu
      AND UPPER(t.nume) LIKE UPPER(nume_turneu);

    v_echipe.extend(v_numar + 1);

    SELECT e.id, e.nume, e.tag, e.id_regiune BULK COLLECT
    INTO v_echipe
    FROM echipa e,
         turneu t,
         grupa_map gm,
         grupa g
    WHERE e.id = gm.id_echipa
      AND t.id = gm.id_grupa
      AND g.id = gm.id_grupa
      AND t.id = g.id_turneu
      AND UPPER(t.nume) LIKE UPPER(nume_turneu);

    FOR i IN v_regiuni.first..v_regiuni.last
        LOOP
            dbms_output.put_line('REGIUNEA: ' || v_regiuni(i).nume);
            dbms_output.put_line('---------------------------------');
            FOR j IN v_echipe.first..v_echipe.last
                LOOP
                    dbms_output.put_line('ECHIPA: ' || v_echipe(j).nume);
                    dbms_output.put_line('---------------------------------');
                    SELECT j.nume BULK COLLECT
                    INTO v_nume
                    FROM jucator j,
                         echipa e,
                         regiune r
                    WHERE j.id_echipa = e.id
                      AND j.id_regiune = r.id
                      AND e.nume = v_echipe(j).nume
                      AND r.nume = v_regiuni(i).nume;
                    IF v_nume.count > 0 THEN
                        FOR k IN v_nume.first..v_nume.last
                            LOOP
                                dbms_output.put_line(v_nume(k));
                            END LOOP;
                    ELSE
                        dbms_output.put_line('Nu exista!');
                    END IF;
                    dbms_output.put_line('---------------------------------');
                    dbms_output.put_line('---------------------------------');
                END LOOP;
        END LOOP;
END;
/

BEGIN
    ex6('MSI');
END;
/

------------------------------------------------------------------------------------------------------------------------

-- EX7
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat independent care
-- să utilizeze 2 tipuri diferite de cursoare studiate, unul dintre acestea fiind cursorparametrizat.

-- Cerința 7:
-- Pentru jucatorii care apartin regiunii KOR, afisati campionii pe care ii joaca si folosesc ca resursa mana.

CREATE OR REPLACE PROCEDURE ex7(atr_regiune_nume regiune.nume%TYPE, atr_resursa campion.resursa%TYPE)
AS
    CURSOR
        regiuni(regiune_nume regiune.nume%TYPE) IS
        SELECT r.id
        FROM regiune r
        WHERE UPPER(r.nume) LIKE UPPER(atr_regiune_nume);
    CURSOR
        jucatori IS
        SELECT j.nume, j.id, j.id_regiune
        FROM jucator j;
    CURSOR
        campioni(jucator_id jucator.id%TYPE) IS
        SELECT c.nume || ' ' || '->' || ' ' || c.resursa AS result
        FROM campion c,
             campion_pool cp
        WHERE c.id = cp.id_campion
          AND cp.id_jucator = jucator_id
          AND UPPER(c.resursa) LIKE UPPER(atr_resursa);
    v_nume_jucator jucator.nume%TYPE;
    v_id_jucator   jucator.id%TYPE;
    v_id_regiune   regiune.id%TYPE;

BEGIN
    FOR regiune IN regiuni(atr_regiune_nume)
        LOOP
            dbms_output.put_line('Jucatorii din regiunea ' || atr_regiune_nume || ' sunt: ');
            dbms_output.put_line('------------------------------------------------');
            OPEN jucatori;
            LOOP
                FETCH jucatori INTO v_nume_jucator, v_id_jucator, v_id_regiune;
                EXIT WHEN jucatori%NOTFOUND;
                IF v_id_regiune = regiune.id THEN
                    dbms_output.put_line('Jucatorul: ' || v_nume_jucator);
                    FOR campion IN campioni(v_id_jucator)
                        LOOP
                            dbms_output.put_line(campion.result);
                        END LOOP;
                    dbms_output.put_line('------------------------------------------------');
                END IF;
            END LOOP;
        END LOOP;
END;
/

BEGIN
    ex7('KOR', 'mana');
END;
/

------------------------------------------------------------------------------------------------------------------------

-- EX8
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat
-- independent de tip funcție care să utilizeze într-o singură comandă SQL 3 dintre tabelele definite.
-- Definiți minim 2 excepții. Apelați subprogramul astfel încât să evidențiați toate cazurile tratate.

-- Cerința 8:
-- Pentru un jucator dat afisati numarul de campioni pe care acesta ii joaca,
-- daca acesta nu joaca pe lane-ul mid.

CREATE OR REPLACE FUNCTION ex8(atr_jucator_id jucator.id%TYPE)
    RETURN number
    IS
    v_numar_campioni NUMBER(10);
    TYPE tip_tabel IS TABLE OF campion_pool%ROWTYPE INDEX BY PLS_INTEGER;
    v_tabel          tip_tabel;
    TYPE tip_tabel2 IS TABLE OF jucator%ROWTYPE INDEX BY PLS_INTEGER;
    v_tabel2         tip_tabel2;
    v_nume_jucator   jucator.nume%TYPE;

    negative_id EXCEPTION;
    no_data_found_1 EXCEPTION;
    no_data_found_2 EXCEPTION;
    no_player_found EXCEPTION;

BEGIN
    IF atr_jucator_id < 0 THEN
        RAISE negative_id;
    END IF;

    SELECT * BULK COLLECT
    INTO v_tabel2
    FROM jucator
    WHERE id = atr_jucator_id;

    IF SQL%NOTFOUND THEN
        RAISE no_player_found;
    END IF;

    SELECT * BULK COLLECT
    INTO v_tabel
    FROM campion_pool cp
    WHERE cp.id_jucator = atr_jucator_id;

    IF SQL%NOTFOUND THEN
        RAISE no_data_found_1;
    END IF;

    SELECT j.nume INTO v_nume_jucator FROM jucator j WHERE j.id = atr_jucator_id;

    SELECT COUNT(c.id)
    INTO v_numar_campioni
    FROM campion c
             JOIN campion_pool cp ON c.id = cp.id_campion
             JOIN jucator j ON j.id = cp.id_jucator
    WHERE cp.id_jucator = atr_jucator_id
      AND j.lane NOT LIKE 'MID';

    IF v_numar_campioni = 0 THEN
        RAISE no_data_found_2;
    ELSE
        RETURN v_numar_campioni;
    END IF;

EXCEPTION
    WHEN negative_id THEN
        dbms_output.put_line('ID-ul nu poate fi negativ!');
        RETURN -1;
    WHEN no_data_found_1 THEN
        dbms_output.put_line('Nu exista date pentru acest jucator!');
        RETURN -1;
    WHEN no_data_found_2 THEN
        dbms_output.put_line('Jucatorul ' || v_nume_jucator || ' joaca pe lane-ul MID!');
        RETURN -1;
    WHEN no_player_found THEN
        dbms_output.put_line('Nu exista jucator cu acest ID!');
        RETURN -1;
    WHEN OTHERS THEN
        dbms_output.put_line('Cod eroare' || SQLCODE);
        dbms_output.put_line('Mesaj eroare' || SQLERRM);
        RETURN -1;
END;
/

DECLARE
    v_numar      NUMBER;
    v_id_jucator jucator.id%TYPE := &id_jucator;
BEGIN
    v_numar := ex8(v_id_jucator);
    IF v_numar > -1 THEN
        dbms_output.put_line('Jucatorul cu id-ul ' || v_id_jucator || ' joaca ' || v_numar || ' campioni');
    END IF;
END;
/

-- Apelare cu id-ul 1 -> 3 campioni
-- Apelare cu id-ul 4 -> 2 campioni
-- Apelare cu id-ul -1 -> ID-ul nu poate fi negativ!
-- Apelare cu id-ul 3 -> Jucatorul Faker joaca pe lane-ul MID!
-- Apelare cu id-ul 60 -> Nu exista jucator cu acest ID!

DELETE
FROM campion_pool
WHERE id_jucator = 6;
-- Apelare cu id-ul 6 -> Nu exista date pentru acest jucator!

------------------------------------------------------------------------------------------------------------------------

-- EX9
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat independent
-- de tip procedură care să utilizeze într-o singură comandă SQL 5 dintre tabelele definite.
-- Tratați toate excepțiile care pot apărea, incluzând excepțiile NO_DATA_FOUND și TOO_MANY_ROWS.
-- Apelați subprogramul astfel încât să evidențiați toate cazurile tratate.

-- Cerința 9:
-- Pentru o echipa al carei nume este dat, afisati echipele adverse din meciurile ce au loc pe scena "Horn Stage",
-- prezentate de "Jordan Corby".

CREATE OR REPLACE PROCEDURE ex9(nume_echipa echipa.nume%TYPE)
AS
    TYPE tabel_index_echipa IS TABLE OF echipa%ROWTYPE INDEX BY PLS_INTEGER;
    v_echipa         tabel_index_echipa;
    TYPE tabel_index_echipa_adversa IS TABLE OF echipa.nume%TYPE INDEX BY PLS_INTEGER;
    v_echipa_adversa tabel_index_echipa_adversa;
    v_id_echipa      echipa.id%TYPE;

    no_data_found_1 EXCEPTION;
    no_data_found_2 EXCEPTION;
    too_many_rows EXCEPTION;

BEGIN
    SELECT * BULK COLLECT
    INTO v_echipa
    FROM echipa e
    WHERE e.nume = nume_echipa;

    IF SQL%NOTFOUND THEN
        RAISE no_data_found_1;
    END IF;

    IF v_echipa.count > 1 THEN
        RAISE too_many_rows;
    END IF;

    SELECT e.id INTO v_id_echipa FROM echipa e WHERE e.nume = nume_echipa;

    SELECT e.nume BULK COLLECT
    INTO v_echipa_adversa
    FROM echipa e
             JOIN meci_map mm ON e.id = mm.id_echipa
             JOIN meci m ON m.id = mm.id_meci
             JOIN meci_header mh ON mh.id_meci = m.id
             JOIN scena s ON s.id = mh.id_scena
             JOIN prezentator p ON p.id = mh.id_prezentator
    WHERE e.nume != nume_echipa
      AND s.nume = 'Horn Stage'
      AND p.nume = 'Jordan Corby'
      AND v_id_echipa IN (SELECT mm.id_echipa FROM meci_map mm WHERE mm.id_meci = m.id);

    IF v_echipa_adversa.count = 0 THEN
        RAISE no_data_found_2;
    END IF;

    dbms_output.put_line('Echipele adversare ale celor din ' || nume_echipa || ' sunt: ');
    FOR i IN 1 .. v_echipa_adversa.count
        LOOP
            dbms_output.put_line(v_echipa_adversa(i));
        END LOOP;

EXCEPTION
    WHEN no_data_found_1 THEN
        dbms_output.put_line('Nu exista date pentru aceasta echipa!');
    WHEN no_data_found_2 THEN
        dbms_output.put_line('Nu exista echipe adversare care sa indeplineasca conditiile!');
    WHEN too_many_rows THEN
        dbms_output.put_line('Exista mai multe echipe cu acest nume!');
    WHEN OTHERS THEN
        dbms_output.put_line('Cod eroare' || SQLCODE);
        dbms_output.put_line('Mesaj eroare' || SQLERRM);
END;
/

DECLARE
    nume echipa.nume%TYPE := 'SKT-T1';
BEGIN
    ex9(nume);
END;
/

-- Pentru nume = 'Canids Kalunga' -> PSG Talon Esports
-- Pentru nume = 'PSG Talon Esports' -> Canids Kalunga
-- Pentru nume = 'Fnatic' -> "Nu exista date pentru aceasta echipa!"
-- Pentru nume = 'Order' -> "Nu exista echipe adversare care sa indeplineasca conditiile!"

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (2, 'SKT-T1', 'SKT_V2')
-- Pentru nume = 'SKT-T1' -> "Exista mai multe echipe cu acest nume!"


--EX9 modificat pentru a folosit exceptiile predefinite in SQL, no_data_found si too_many_rows
CREATE OR REPLACE PROCEDURE ex9(nume_echipa echipa.nume%TYPE)
AS
    TYPE tabel_index_echipa IS TABLE OF echipa%ROWTYPE INDEX BY PLS_INTEGER;
    v_echipa         tabel_index_echipa;
    TYPE tabel_index_echipa_adversa IS TABLE OF echipa.nume%TYPE INDEX BY PLS_INTEGER;
    v_echipa_adversa tabel_index_echipa_adversa;
    v_id_echipa      echipa.id%TYPE;

BEGIN
    SELECT * BULK COLLECT
    INTO v_echipa
    FROM echipa e
    WHERE e.nume = nume_echipa;


    SELECT e.id INTO v_id_echipa FROM echipa e WHERE e.nume = nume_echipa;

    SELECT e.nume BULK COLLECT
    INTO v_echipa_adversa
    FROM echipa e
             JOIN meci_map mm ON e.id = mm.id_echipa
             JOIN meci m ON m.id = mm.id_meci
             JOIN meci_header mh ON mh.id_meci = m.id
             JOIN scena s ON s.id = mh.id_scena
             JOIN prezentator p ON p.id = mh.id_prezentator
    WHERE e.nume != nume_echipa
      AND s.nume = 'Horn Stage'
      AND p.nume = 'Jordan Corby'
      AND v_id_echipa IN (SELECT mm.id_echipa FROM meci_map mm WHERE mm.id_meci = m.id);

    IF v_echipa_adversa.count = 0 THEN
        RAISE no_data_found;
    END IF;

    dbms_output.put_line('Echipele adversare ale celor din ' || nume_echipa || ' sunt: ');
    FOR i IN 1 .. v_echipa_adversa.count
        LOOP
            dbms_output.put_line(v_echipa_adversa(i));
        END LOOP;
END;
/

DECLARE
    nume echipa.nume%TYPE := 'SKT-T1';
BEGIN
    ex9(nume);
END;
/

-- Pentru nume = 'Canids Kalunga' -> PSG Talon Esports
-- Pentru nume = 'PSG Talon Esports' -> Canids Kalunga
-- Pentru nume = 'Fnatic' -> no_data_found
-- Pentru nume = 'Order' -> no_data_found

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (2, 'SKT-T1', 'SKT_V2')
-- Pentru nume = 'SKT-T1' -> too_many_rows


------------------------------------------------------------------------------------------------------------------------

-- EX10
-- Definiți un trigger de tip LMD la nivel de comandă. Declanșați trigger-ul.

-- Cerința 10:
-- Voi realiza un trigger care se va declansa atunci cand vreau sa modific tabela TURNEU cu conditiile:
-- 1. Nu pot modifica tabela TURNEU intre orele 08:00-10:00
-- 2. Nu pot modifica tabela in ziua de Craciun si Ziua de Anul Nou

CREATE OR
    REPLACE TRIGGER ex10
    BEFORE
        INSERT OR UPDATE OR
        DELETE
    ON turneu
DECLARE

BEGIN
    IF ((TO_CHAR(SYSDATE, 'HH24') BETWEEN 8 AND 10) OR
        (TO_CHAR(SYSDATE, 'MMDD') = '1225' OR TO_CHAR(SYSDATE, 'MMDD') = '0101')) THEN
        RAISE_APPLICATION_ERROR(-20001, 'Nu poti modifica tabela in acest interval de timp sau in aceasta zi!');
    END IF;
END;
/

INSERT INTO turneu (nume, oras, data)
VALUES ('TurneuName', 'Stockholm', TO_DATE('2022-05-10', 'YYYY-MM-DD'));

------------------------------------------------------------------------------------------------------------------------

-- EX11
-- Definiți un trigger de tip LMD la nivel de linie. Declanșați trigger-ul.

-- Cerința 11:
-- Voi realiza un trigger care se va declansa atunci cand vreau sa modific tabela meci cu conditiile:
-- 1. Data meciului nu poate fi mai veche de 1 Aprilie 2011
-- (data in care a avut loc primul joc de League of Legends oficial).
-- 2. Data meciului nu poate fi in ziua de Craciun si Ziua de Anul Nou.

CREATE
    OR
    REPLACE TRIGGER ex11
    BEFORE
        INSERT OR UPDATE OR
        DELETE
    ON meci
    FOR EACH ROW
DECLARE
BEGIN
    IF (TO_DATE(:new.data, 'YYYY-MM-DD') <= TO_DATE('2011-04-01', 'YYYY-MM-DD') OR
        (TO_CHAR(:new.data, 'MMDD') = '1225' OR TO_CHAR(:new.data, 'MMDD') = '0101')) THEN
        RAISE_APPLICATION_ERROR(-20001,
                                'Probleme cu data introdusa,' ||
                                ' data nu poate fi mai veche de 1 Aprilie 2011' ||
                                ' sau in ziua de Craciun sau in Ziua de Anul Nou!');
    END IF;
END;

INSERT INTO meci (titlu, data)
VALUES ('MeciName', TO_DATE('2022-01-01', 'YYYY-MM-DD'));

INSERT INTO meci (titlu, data)
VALUES ('MeciName', TO_DATE('2010-10-10', 'YYYY-MM-DD'));

------------------------------------------------------------------------------------------------------------------------

-- EX12
-- Definiți un trigger de tip LDD. Declanșați trigger-ul.

-- Cerința 12:
-- Voi realiza un trigger care se va declansa atunci cand se executa operatii LDD.
-- Acesta va stoca intr-o noua table numita istoric utilizatorul,
-- operatia executata si baza de date in care are loc operatia.

CREATE
    TABLE
    istoric
(
    id           NUMBER(10) GENERATED ALWAYS AS IDENTITY
        CONSTRAINT istoric_pk PRIMARY KEY,
    utilizator   VARCHAR2(50)
        CONSTRAINT utilizator_istoric NOT NULL,
    operatie     VARCHAR2(50)
        CONSTRAINT operatie_istoric NOT NULL,
    baza_de_date VARCHAR2(50)
        CONSTRAINT baza_de_date_istoric NOT NULL
);

SELECT *
FROM istoric;

CREATE
    OR
    REPLACE TRIGGER ex12
    AFTER CREATE OR ALTER OR DROP
    ON SCHEMA
BEGIN
    INSERT INTO istoric (utilizator, operatie, baza_de_date)
    VALUES (sys.login_user, sys.sysevent, sys.database_name);
END;
/

CREATE
    TABLE
    test
(
    id   NUMBER(10),
    nume VARCHAR2(50)
);

ALTER
    TABLE
    test
    ADD
        (prenume VARCHAR2(50));

ALTER TABLE
    test
    DROP COLUMN prenume;

DROP
    TABLE
    test;

SELECT *
FROM istoric;

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------- OPTIONAL ----------------------------------------------------------

-- EX13
-- Definiți un pachet care să conțină toate obiectele definite în cadrul proiectului.

CREATE OR REPLACE PACKAGE proiect_sgbd_hutan_mihai AS
    PROCEDURE ex6(nume_turneu turneu.nume%TYPE);
    PROCEDURE ex7(atr_regiune_nume regiune.nume%TYPE, atr_resursa campion.resursa%TYPE);
    FUNCTION ex8(atr_jucator_id jucator.id%TYPE) RETURN NUMBER;
    PROCEDURE ex9(nume_echipa echipa.nume%TYPE);
END proiect_sgbd_hutan_mihai;
/

CREATE OR REPLACE PACKAGE BODY proiect_sgbd_hutan_mihai
AS
    -- Cerința 6:
    -- Pentru un turneu al carui nume este dat, pentru fiecare regiune, afisati toate echipele si jucatorii ce apartin
    -- acelei regiuni sau mesajul 'Nu exista!'.

    PROCEDURE ex6(nume_turneu turneu.nume%TYPE)
    AS
        TYPE tabl_idx IS TABLE OF regiune%ROWTYPE INDEX BY PLS_INTEGER;
        v_regiuni tabl_idx;
        TYPE tip_lista_nested IS TABLE OF echipa%ROWTYPE;
        v_echipe  tip_lista_nested := tip_lista_nested();
        TYPE tabl_index IS TABLE OF VARCHAR2(200) INDEX BY PLS_INTEGER;
        v_nume    tabl_index;
        v_numar   NUMBER(5);
    BEGIN
        SELECT * BULK COLLECT INTO v_regiuni FROM regiune;

        SELECT COUNT(*)
        INTO v_numar
        FROM echipa e,
             turneu t,
             grupa_map gm,
             grupa g
        WHERE e.id = gm.id_echipa
          AND t.id = gm.id_grupa
          AND g.id = gm.id_grupa
          AND t.id = g.id_turneu
          AND UPPER(t.nume) LIKE UPPER(nume_turneu);

        v_echipe.extend(v_numar + 1);

        SELECT e.id, e.nume, e.tag, e.id_regiune BULK COLLECT
        INTO v_echipe
        FROM echipa e,
             turneu t,
             grupa_map gm,
             grupa g
        WHERE e.id = gm.id_echipa
          AND t.id = gm.id_grupa
          AND g.id = gm.id_grupa
          AND t.id = g.id_turneu
          AND UPPER(t.nume) LIKE UPPER(nume_turneu);

        FOR i IN v_regiuni.first..v_regiuni.last
            LOOP
                dbms_output.put_line('REGIUNEA: ' || v_regiuni(i).nume);
                dbms_output.put_line('---------------------------------');
                FOR j IN v_echipe.first..v_echipe.last
                    LOOP
                        dbms_output.put_line('ECHIPA: ' || v_echipe(j).nume);
                        dbms_output.put_line('---------------------------------');
                        SELECT j.nume BULK COLLECT
                        INTO v_nume
                        FROM jucator j,
                             echipa e,
                             regiune r
                        WHERE j.id_echipa = e.id
                          AND j.id_regiune = r.id
                          AND e.nume = v_echipe(j).nume
                          AND r.nume = v_regiuni(i).nume;
                        IF v_nume.count > 0 THEN
                            FOR k IN v_nume.first..v_nume.last
                                LOOP
                                    dbms_output.put_line(v_nume(k));
                                END LOOP;
                        ELSE
                            dbms_output.put_line('Nu exista!');
                        END IF;
                        dbms_output.put_line('---------------------------------');
                        dbms_output.put_line('---------------------------------');
                    END LOOP;
            END LOOP;
    END ex6;

    -- Cerința 7:
    -- Pentru jucatorii care apartin regiunii KOR, afisati campionii pe care ii joaca si folosesc ca resursa mana.

    PROCEDURE ex7(atr_regiune_nume regiune.nume%TYPE, atr_resursa campion.resursa%TYPE)
    AS
        CURSOR
            regiuni(regiune_nume regiune.nume%TYPE) IS
            SELECT r.id
            FROM regiune r
            WHERE UPPER(r.nume) LIKE UPPER(atr_regiune_nume);
        CURSOR
            jucatori IS
            SELECT j.nume, j.id, j.id_regiune
            FROM jucator j;
        CURSOR
            campioni(jucator_id jucator.id%TYPE) IS
            SELECT c.nume || ' ' || '->' || ' ' || c.resursa AS result
            FROM campion c,
                 campion_pool cp
            WHERE c.id = cp.id_campion
              AND cp.id_jucator = jucator_id
              AND UPPER(c.resursa) LIKE UPPER(atr_resursa);
        v_nume_jucator jucator.nume%TYPE;
        v_id_jucator   jucator.id%TYPE;
        v_id_regiune   regiune.id%TYPE;

    BEGIN
        FOR regiune IN regiuni(atr_regiune_nume)
            LOOP
                dbms_output.put_line('Jucatorii din regiunea ' || atr_regiune_nume || ' sunt: ');
                dbms_output.put_line('------------------------------------------------');
                OPEN jucatori;
                LOOP
                    FETCH jucatori INTO v_nume_jucator, v_id_jucator, v_id_regiune;
                    EXIT WHEN jucatori%NOTFOUND;
                    IF v_id_regiune = regiune.id THEN
                        dbms_output.put_line('Jucatorul: ' || v_nume_jucator);
                        FOR campion IN campioni(v_id_jucator)
                            LOOP
                                dbms_output.put_line(campion.result);
                            END LOOP;
                        dbms_output.put_line('------------------------------------------------');
                    END IF;
                END LOOP;
            END LOOP;
    END ex7;

    -- Cerința 8:
    -- Pentru un jucator dat afisati numarul de campioni pe care acesta ii joaca,
    -- daca acesta nu joaca pe lane-ul mid.

    FUNCTION ex8(atr_jucator_id jucator.id%TYPE)
        RETURN number
        IS
        v_numar_campioni NUMBER(10);
        TYPE tip_tabel IS TABLE OF campion_pool%ROWTYPE INDEX BY PLS_INTEGER;
        v_tabel          tip_tabel;
        TYPE tip_tabel2 IS TABLE OF jucator%ROWTYPE INDEX BY PLS_INTEGER;
        v_tabel2         tip_tabel2;
        v_nume_jucator   jucator.nume%TYPE;

        negative_id EXCEPTION;
        no_data_found_1 EXCEPTION;
        no_data_found_2 EXCEPTION;
        no_player_found EXCEPTION;

    BEGIN
        IF atr_jucator_id < 0 THEN
            RAISE negative_id;
        END IF;

        SELECT * BULK COLLECT
        INTO v_tabel2
        FROM jucator
        WHERE id = atr_jucator_id;

        IF SQL%NOTFOUND THEN
            RAISE no_player_found;
        END IF;

        SELECT * BULK COLLECT
        INTO v_tabel
        FROM campion_pool cp
        WHERE cp.id_jucator = atr_jucator_id;

        IF SQL%NOTFOUND THEN
            RAISE no_data_found_1;
        END IF;

        SELECT j.nume INTO v_nume_jucator FROM jucator j WHERE j.id = atr_jucator_id;

        SELECT COUNT(c.id)
        INTO v_numar_campioni
        FROM campion c
                 JOIN campion_pool cp ON c.id = cp.id_campion
                 JOIN jucator j ON j.id = cp.id_jucator
        WHERE cp.id_jucator = atr_jucator_id
          AND j.lane NOT LIKE 'MID';

        IF v_numar_campioni = 0 THEN
            RAISE no_data_found_2;
        ELSE
            RETURN v_numar_campioni;
        END IF;

    EXCEPTION
        WHEN negative_id THEN
            dbms_output.put_line('ID-ul nu poate fi negativ!');
            RETURN -1;
        WHEN no_data_found_1 THEN
            dbms_output.put_line('Nu exista date pentru acest jucator!');
            RETURN -1;
        WHEN no_data_found_2 THEN
            dbms_output.put_line('Jucatorul ' || v_nume_jucator || ' joaca pe lane-ul MID!');
            RETURN -1;
        WHEN no_player_found THEN
            dbms_output.put_line('Nu exista jucator cu acest ID!');
            RETURN -1;
        WHEN OTHERS THEN
            dbms_output.put_line('Cod eroare' || SQLCODE);
            dbms_output.put_line('Mesaj eroare' || SQLERRM);
            RETURN -1;
    END ex8;

    -- Cerința 9:
    -- Pentru o echipa al carei nume este dat, afisati echipele adverse din meciurile ce au loc pe scena "Horn Stage",
    -- prezentate de "Jordan Corby".

    PROCEDURE ex9(nume_echipa echipa.nume%TYPE)
    AS
        TYPE tabel_index_echipa IS TABLE OF echipa%ROWTYPE INDEX BY PLS_INTEGER;
        v_echipa         tabel_index_echipa;
        TYPE tabel_index_echipa_adversa IS TABLE OF echipa.nume%TYPE INDEX BY PLS_INTEGER;
        v_echipa_adversa tabel_index_echipa_adversa;
        v_id_echipa      echipa.id%TYPE;

        no_data_found_1 EXCEPTION;
        no_data_found_2 EXCEPTION;
        too_many_rows EXCEPTION;

    BEGIN
        SELECT * BULK COLLECT
        INTO v_echipa
        FROM echipa e
        WHERE e.nume = nume_echipa;

        IF SQL%NOTFOUND THEN
            RAISE no_data_found_1;
        END IF;

        IF v_echipa.count > 1 THEN
            RAISE too_many_rows;
        END IF;

        SELECT e.id INTO v_id_echipa FROM echipa e WHERE e.nume = nume_echipa;

        SELECT e.nume BULK COLLECT
        INTO v_echipa_adversa
        FROM echipa e
                 JOIN meci_map mm ON e.id = mm.id_echipa
                 JOIN meci m ON m.id = mm.id_meci
                 JOIN meci_header mh ON mh.id_meci = m.id
                 JOIN scena s ON s.id = mh.id_scena
                 JOIN prezentator p ON p.id = mh.id_prezentator
        WHERE e.nume != nume_echipa
          AND s.nume = 'Horn Stage'
          AND p.nume = 'Jordan Corby'
          AND v_id_echipa IN (SELECT mm.id_echipa FROM meci_map mm WHERE mm.id_meci = m.id);

        IF v_echipa_adversa.count = 0 THEN
            RAISE no_data_found_2;
        END IF;

        dbms_output.put_line('Echipele adversare ale celor din ' || nume_echipa || ' sunt: ');
        FOR i IN 1 .. v_echipa_adversa.count
            LOOP
                dbms_output.put_line(v_echipa_adversa(i));
            END LOOP;

    EXCEPTION
        WHEN no_data_found_1 THEN
            dbms_output.put_line('Nu exista date pentru aceasta echipa!');
        WHEN no_data_found_2 THEN
            dbms_output.put_line('Nu exista echipe adversare care sa indeplineasca conditiile!');
        WHEN too_many_rows THEN
            dbms_output.put_line('Exista mai multe echipe cu acest nume!');
        WHEN OTHERS THEN
            dbms_output.put_line('Cod eroare' || SQLCODE);
            dbms_output.put_line('Mesaj eroare' || SQLERRM);
    END ex9;
END proiect_sgbd_hutan_mihai;
/

-- TESTARE PACKAGE
BEGIN
    proiect_sgbd_hutan_mihai.ex6('MSI');
    proiect_sgbd_hutan_mihai.ex7('KOR', 'mana');

    -- Apelare cu id-ul 1 -> 3 campioni
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(1));

    -- Apelare cu id-ul 4 -> 2 campioni
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(4));

    -- Apelare cu id-ul -1 -> ID-ul nu poate fi negativ!
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(-1));

    -- Apelare cu id-ul 3 -> Jucatorul Faker joaca pe lane-ul MID!
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(3));

    -- Apelare cu id-ul 60 -> Nu exista jucator cu acest ID!
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(60));
END;
/

DELETE
FROM campion_pool
WHERE id_jucator = 6;

BEGIN
    -- Apelare cu id-ul 6 -> Nu exista date pentru acest jucator!
    dbms_output.put_line('Rezultat ex8: ' || proiect_sgbd_hutan_mihai.ex8(6));
END;
/

BEGIN
    -- Pentru nume = 'Canids Kalunga' -> PSG Talon Esports
    proiect_sgbd_hutan_mihai.ex9('Canids Kalunga');
    -- Pentru nume = 'PSG Talon Esports' -> Canids Kalunga
    proiect_sgbd_hutan_mihai.ex9('PSG Talon Esports');
    -- Pentru nume = 'Fnatic' -> "Nu exista date pentru aceasta echipa!"
    proiect_sgbd_hutan_mihai.ex9('Fnatic');
    -- Pentru nume = 'Order' -> "Nu exista echipe adversare care sa indeplineasca conditiile!"
    proiect_sgbd_hutan_mihai.ex9('Order');
END;
/

INSERT INTO echipa(id_regiune, nume, tag)
VALUES (2, 'SKT-T1', 'SKT_V2');
BEGIN
    -- Pentru nume = 'SKT-T1' -> "Exista mai multe echipe cu acest nume!"
    proiect_sgbd_hutan_mihai.ex9('SKT-T1');
END;
/

------------------------------------------------------------------------------------------------------------------------
