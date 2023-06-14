--EX2
CREATE OR REPLACE TYPE tip_orase_hma IS TABLE OF VARCHAR2(250);

CREATE TABLE excursie_hma
(
    cod_excursie NUMBER(4)
        CONSTRAINT pk_excursie_hma PRIMARY KEY,
    denumire     VARCHAR(20),
    orase        tip_orase_hma,
    status       VARCHAR(20)
        CONSTRAINT check_status_hma CHECK (status IN ('UNAVAILABLE', 'AVAILABLE'))
)
    NESTED TABLE orase STORE AS tabel_orase_hma;

SELECT *
FROM excursie_hma

--a
INSERT INTO excursie_hma
VALUES (1, 'FRANTA', tip_orase_hma('PARIS1', 'TOULOUSE', 'METZ', 'NANCY', 'LION'), 'AVAILABLE');

INSERT INTO excursie_hma
VALUES (2, 'GERMANIA', tip_orase_hma('BERLIN', 'MUNCHEN', 'HAMBURG', 'FRANKFURT', 'STUTTGARD'), 'UNAVAILABLE');

INSERT INTO excursie_hma
VALUES (3, 'ITALIA', tip_orase_hma('ROMA', 'VENETIA', 'MILANO', 'GENOVA', 'FLORENTA'), 'AVAILABLE');

INSERT INTO excursie_hma
VALUES (4, 'CEHIA', tip_orase_hma('PRAGA', 'BRNO', 'PLZEN', 'KARLOVY VARY', 'HRDEC'), 'AVAILABLE');

INSERT INTO excursie_hma
VALUES (5, 'SPAIN', tip_orase_hma('MADRID', 'BARCELONA', 'SEVILLA', 'VALENCIA', 'BILBAO'), 'UNAVAILABLE');

COMMIT;


--b1

DECLARE
    cod  NUMBER(4)    := &id;
    oras VARCHAR(200) := '&oras';
BEGIN
    INSERT INTO TABLE ( SELECT orase FROM excursie_hma WHERE cod_excursie = cod) VALUES (UPPER(oras));
    dbms_output.put_line('Insert succeeded');
END;
/
ROLLBACK;


--b2
DECLARE
    tabel tip_orase_hma := tip_orase_hma();
    aux   tip_orase_hma := tip_orase_hma();
    cod   NUMBER(4)     := &id;
    oras  VARCHAR(200)  := '&oras';
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            aux.extend;
            IF i = 1
            THEN
                aux(i) := tabel(i);
            END IF;
            IF i = 2
            THEN
                aux(i) := UPPER(oras);
                aux.extend;
                aux(i + 1) := tabel(i);
            END IF;
            IF i > 2
            THEN
                aux(i + 1) := tabel(i);
            END IF;
        END LOOP;

    UPDATE excursie_hma
    SET orase = aux
    WHERE cod_excursie = cod;
END;
/
ROLLBACK;


-- b3
DECLARE
    tabel  tip_orase_hma := tip_orase_hma();
    cod    NUMBER(4)     := &id;
    oras_1 VARCHAR(200)  := '&oras1';
    oras_2 VARCHAR(200)  := '&oras2';
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            IF tabel(i) = oras_1
            THEN
                tabel(i) := UPPER(oras_2);
            ELSE
                IF tabel(i) = oras_2
                THEN
                    tabel(i) := UPPER(oras_1);
                END IF;
            END IF;
        END LOOP;

    UPDATE excursie_hma
    SET orase = tabel
    WHERE cod_excursie = cod;
END;
/
ROLLBACK;


--b4
DECLARE
    tabel tip_orase_hma := tip_orase_hma();
    aux   tip_orase_hma := tip_orase_hma();
    cod   NUMBER(4)     := &id;
    oras  VARCHAR(30)   := UPPER('&oras');
    k     NUMBER(6)     := 1;

BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            IF tabel(i) != oras
            THEN
                aux.extend;
                aux(k) := tabel(i);
                k := k + 1;
            END IF;
        END LOOP;

    UPDATE excursie_hma
    SET orase = aux
    WHERE cod_excursie = cod;

    dbms_output.put_line(oras || ' deleted succesfully!');
END;


--c
DECLARE
    tabel tip_orase_hma := tip_orase_hma();
    cod   NUMBER(4)     := &id;

BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma
    WHERE cod_excursie = cod;

    dbms_output.put_line('Nr orase: ' || tabel.count);

    FOR i IN 1..tabel.count
        LOOP
            dbms_output.put_line(tabel(i));
        END LOOP;

END;
/


--d
DECLARE
    tabel  tip_orase_hma := tip_orase_hma();
    TYPE tip_coduri IS VARRAY(5) OF NUMBER(6);
    coduri tip_coduri;
    cod    NUMBER(6) ;
BEGIN
    SELECT cod_excursie BULK COLLECT
    INTO coduri
    FROM excursie_hma;


    FOR i IN coduri.first..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma
            WHERE cod_excursie = cod;
            dbms_output.put_line('Pentru excursia cu codul ' || cod || ':');
            FOR i IN 1..tabel.count
                LOOP
                    dbms_output.put_line(tabel(i));
                END LOOP;
            dbms_output.put_line('');
        END LOOP;
END;
/


--e
DECLARE
    tabel  tip_orase_hma := tip_orase_hma();
    TYPE tip_coduri IS VARRAY(5) OF NUMBER(6);
    coduri tip_coduri;
    cod    NUMBER(6) ;
    minim  NUMBER(6);
BEGIN
    SELECT cod_excursie BULK COLLECT
    INTO coduri
    FROM excursie_hma;

    cod := coduri(1);
    SELECT orase
    INTO tabel
    FROM excursie_hma
    WHERE cod_excursie = cod;

    minim := tabel.count;

    FOR i IN 2..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma
            WHERE cod_excursie = cod;
            IF tabel.count < minim
            THEN
                minim := tabel.count;
            END IF;
        END LOOP;

    dbms_output.put_line('Minimul este: ' || minim);

    FOR i IN coduri.first..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma
            WHERE cod_excursie = cod;
            IF tabel.count = minim THEN
                UPDATE excursie_hma
                SET status = 'UNAVAILABLE'
                WHERE cod_excursie = cod;
            END IF;
        END LOOP;

END;
/
ROLLBACK;


--EX3
CREATE OR REPLACE TYPE tip_orase_hma2 IS VARRAY(300) OF VARCHAR2(200);

CREATE TABLE excursie_hma2
(
    cod_excursie NUMBER(4)
        CONSTRAINT pk_excursie_hma2 PRIMARY KEY,
    denumire     VARCHAR(20),
    orase        tip_orase_hma2,
    status       VARCHAR(20)
        CONSTRAINT check_status_hma2 CHECK (status IN ('UNAVAILABLE', 'AVAILABLE'))
);

SELECT *
FROM excursie_hma2;

--a
INSERT INTO excursie_hma2
VALUES (1, 'FRANTA', tip_orase_hma2('PARIS', 'TOULOUSE', 'METZ', 'NANCY', 'LION'), 'AVAILABLE');

INSERT INTO excursie_hma2
VALUES (2, 'GERMANIA', tip_orase_hma2('BERLIN', 'MUNCHEN', 'HAMBURG', 'FRANKFURT', 'STUTTGARD'), 'UNAVAILABLE');

INSERT INTO excursie_hma2
VALUES (3, 'ITALIA', tip_orase_hma2('ROMA', 'VENETIA', 'MILANO', 'GENOVA', 'FLORENTA'), 'AVAILABLE');

INSERT INTO excursie_hma2
VALUES (4, 'CEHIA', tip_orase_hma2('PRAGA', 'BRNO', 'PLZEN', 'KARLOVY VARY', 'HRDEC'), 'AVAILABLE');

INSERT INTO excursie_hma2
VALUES (5, 'SPAIN', tip_orase_hma2('MADRID', 'BARCELONA', 'SEVILLA', 'VALENCIA', 'BILBAO'), 'UNAVAILABLE');

COMMIT;


--b1
DECLARE
    cod   NUMBER(4)      := &id;
    oras  VARCHAR(200)   := '&oras';
    tabel tip_orase_hma2 := tip_orase_hma2();
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    tabel.extend;
    tabel(tabel.count) := oras;

    UPDATE excursie_hma2
    SET orase = tabel
    WHERE cod_excursie = cod;
END;
/
ROLLBACK;


--2
DECLARE
    tabel tip_orase_hma2 := tip_orase_hma2();
    aux   tip_orase_hma2 := tip_orase_hma2();
    cod   NUMBER(4)      := &id;
    oras  VARCHAR(200)   := '&oras';
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            aux.extend;
            IF i = 1
            THEN
                aux(i) := tabel(i);
            END IF;
            IF i = 2
            THEN
                aux(i) := UPPER(oras);
                aux.extend;
                aux(i + 1) := tabel(i);
            END IF;
            IF i > 2
            THEN
                aux(i + 1) := tabel(i);
            END IF;
        END LOOP;

    UPDATE excursie_hma2
    SET orase = aux
    WHERE cod_excursie = cod;
END;
/
ROLLBACK;


--3
DECLARE
    tabel tip_orase_hma2 := tip_orase_hma2();
    cod   NUMBER(4)      := &id;
    oras1 VARCHAR(200)   := '&oras1';
    oras2 VARCHAR(200)   := '&oras2';
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            IF tabel(i) = oras1
            THEN
                tabel(i) := UPPER(oras2);
            ELSE
                IF tabel(i) = oras2
                THEN
                    tabel(i) := UPPER(oras1);
                END IF;
            END IF;
        END LOOP;

    UPDATE excursie_hma2
    SET orase = tabel
    WHERE cod_excursie = cod;
END;
/
ROLLBACK;


--4
DECLARE
    tabel tip_orase_hma2 := tip_orase_hma2();
    aux   tip_orase_hma2 := tip_orase_hma2();
    cod   NUMBER(4)      := &id;
    oras  VARCHAR(200)   := '&oras';
    id    NUMBER(6)      := 1;
BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    FOR i IN 1..tabel.count
        LOOP
            IF tabel(i) != oras
            THEN
                aux.extend;
                aux(id) := tabel(i);
                id := id + 1;
            END IF;
        END LOOP;

    UPDATE excursie_hma2
    SET orase = aux
    WHERE cod_excursie = id;
END;
/
ROLLBACK;


--c
DECLARE
    tabel tip_orase_hma2 := tip_orase_hma2();
    cod   NUMBER(4)      := &id;

BEGIN
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    dbms_output.put_line('Nr orase: ' || tabel.count);

    FOR i IN 1..tabel.count
        LOOP
            dbms_output.put_line(tabel(i));
        END LOOP;

END;
/


--d
DECLARE
    tabel  tip_orase_hma2 := tip_orase_hma2();
    TYPE tip_coduri IS VARRAY(5) OF NUMBER(6);
    coduri tip_coduri;
    cod    NUMBER(6) ;
BEGIN
    SELECT cod_excursie BULK COLLECT
    INTO coduri
    FROM excursie_hma2;


    FOR i IN coduri.first..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma2
            WHERE cod_excursie = cod;
            dbms_output.put_line('Pentru excursia cu codul ' || cod || ':');
            FOR i IN 1..tabel.count
                LOOP
                    dbms_output.put_line(tabel(i));
                END LOOP;
            dbms_output.put_line('');
        END LOOP;


END;
/


--e
DECLARE
    tabel  tip_orase_hma2 := tip_orase_hma2();
    TYPE tip_coduri IS VARRAY(5) OF NUMBER(6);
    coduri tip_coduri;
    cod    NUMBER(6) ;
    minim  NUMBER(6);
    id     NUMBER(10);
BEGIN
    SELECT cod_excursie BULK COLLECT
    INTO coduri
    FROM excursie_hma2;

    id := coduri(1);
    SELECT orase
    INTO tabel
    FROM excursie_hma2
    WHERE cod_excursie = cod;

    minim := tabel.count;

    FOR i IN 2..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma2
            WHERE cod_excursie = cod;
            IF tabel.count < minim
            THEN
                minim := tabel.count;
            END IF;
        END LOOP;

    dbms_output.put_line('Minimul este: ' || minim);

    FOR i IN coduri.first..coduri.last
        LOOP
            cod := coduri(i);
            SELECT orase
            INTO tabel
            FROM excursie_hma2
            WHERE cod_excursie = cod;
            IF tabel.count = minim THEN
                UPDATE excursie_hma2
                SET status = 'UNAVAILABLE'
                WHERE cod_excursie = cod;
            END IF;
        END LOOP;

END;
/

ROLLBACK;