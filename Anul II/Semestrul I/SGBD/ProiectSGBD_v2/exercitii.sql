------------------------------------------------------------------------------------------------------------------------

-- EX6
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat
-- independent care să utilizeze două tipuri diferite de colecții studiate. Apelați subprogramul.

-- Pentru un turneu dat, pentru fiecare rol, sa se afiseze id-ul jucatorului ce joaca acel rol
-- si are numarul maxim de kill-uri facute de acesta intr-un singur meci. Afisati si numarul de killuri.

CREATE OR REPLACE PROCEDURE ex6(p_tournament_name IN tournaments.tournament_name%TYPE) AS
    TYPE t_role_kills IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
    TYPE t_role_players IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
    TYPE t_result IS TABLE OF VARCHAR2(100);
    v_result        t_result := t_result();
    v_role_kills    t_role_kills;
    v_role_players  t_role_players;
    v_max_kills     NUMBER;
    v_player_id     players.id%TYPE;
    v_role_id       roles.id%TYPE;
    v_tournament_id tournaments.id%TYPE;
BEGIN
    SELECT id INTO v_tournament_id FROM tournaments WHERE tournament_name = p_tournament_name;

    FOR r IN (SELECT id FROM roles)
        LOOP
            v_role_id := r.id;
            SELECT ps.player_id, MAX(ps.kills)
            INTO v_player_id, v_max_kills
            FROM player_statistics ps
                     JOIN matches m ON m.id = ps.match_id
                     JOIN players p ON p.id = ps.player_id
            WHERE m.tournament_id = v_tournament_id
              AND p.role_id = v_role_id
            GROUP BY ps.player_id
            ORDER BY MAX(ps.kills) DESC
                FETCH FIRST ROW ONLY;

            IF v_role_kills.EXISTS(v_role_id) THEN
                IF v_max_kills > v_role_kills(v_role_id) THEN
                    v_role_kills(v_role_id) := v_max_kills;
                    v_role_players(v_role_id) := v_player_id;
                END IF;
            ELSE
                v_role_kills(v_role_id) := v_max_kills;
                v_role_players(v_role_id) := v_player_id;
            END IF;
        END LOOP;

    v_role_id := v_role_kills.first;
    WHILE v_role_id IS NOT NULL
        LOOP
            v_result.extend;
            v_result(v_result.count) := 'Player with id ' || v_role_players(v_role_id) || ' in role ' || v_role_id ||
                                        ' had the maximum kills: ' || v_role_kills(v_role_id);
            v_role_id := v_role_kills.next(v_role_id);
        END LOOP;

    FOR i IN 1 .. v_result.count
        LOOP
            dbms_output.put_line(v_result(i));
        END LOOP;
END ex6;
/

BEGIN
    ex6('Worlds 2022');
END;
/

-- EXPECTED
-- Player with id 3 in role 1 had the maximum kills: 8
-- Player with id 2 in role 2 had the maximum kills: 6
-- Player with id 8 in role 3 had the maximum kills: 8
-- Player with id 4 in role 4 had the maximum kills: 5
-- Player with id 15 in role 5 had the maximum kills: 1


------------------------------------------------------------------------------------------------------------------------

-- EX7
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat independent care
-- să utilizeze 2 tipuri diferite de cursoare studiate, unul dintre acestea fiind cursorparametrizat.

-- Afișați numele echipelor și numărul de meciuri câștigate de acestea intr-un turneu dat.

CREATE OR REPLACE PROCEDURE ex7(p_tournament_name IN tournaments.tournament_name%TYPE)
    IS
    -- ADDED PARAMETERIZED CURSOR
    CURSOR c_team_id(pc_tournament_name IN tournaments.tournament_name%TYPE)
        IS
        SELECT id
        FROM tournaments
        WHERE tournament_name = pc_tournament_name;
    CURSOR c_teams
        IS
        SELECT id, team_name
        FROM teams;
    TYPE ref_cur_type IS REF CURSOR;
    v_team_wins     ref_cur_type;
    v_team_id       teams.id%TYPE;
    v_team_name     teams.team_name%TYPE;
    v_wins          NUMBER;
    v_tournament_id tournaments.id%TYPE;
BEGIN
    -- OLD IMPLEMENTATION BEFORE ADDING PARAMETERIZED CURSOR:
    -- SELECT id INTO v_tournament_id FROM tournaments WHERE tournament_name = p_tournament_name;
    OPEN c_team_id(p_tournament_name);
    FETCH c_team_id INTO v_tournament_id;
    CLOSE c_team_id;

    OPEN c_teams;
    LOOP
        FETCH c_teams INTO v_team_id, v_team_name;
        EXIT WHEN c_teams%NOTFOUND;

        OPEN v_team_wins FOR
            SELECT COUNT(*) AS wins
            FROM match_results mr
                     JOIN matches m ON m.id = mr.match_id
            WHERE m.tournament_id = v_tournament_id
              AND mr.winning_team_id = v_team_id;

        FETCH v_team_wins INTO v_wins;
        CLOSE v_team_wins;

        dbms_output.put_line('Team: ' || v_team_name || ' - Wins: ' || v_wins);
    END LOOP;
    CLOSE c_teams;
END ex7;
/

BEGIN
    ex7('Worlds 2022');
END;
/

-- EXPECTED
-- Team: TSM - Wins: 4
-- Team: Fnatic - Wins: 3
-- Team: SK Telecom T1 - Wins: 2
-- Team: EDward Gaming - Wins: 1
-- Team: Royal Never Give Up - Wins: 0

------------------------------------------------------------------------------------------------------------------------

-- EX8
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat
-- independent de tip funcție care să utilizeze într-o singură comandă SQL 3 dintre tabelele definite.
-- Definiți minim 2 excepții. Apelați subprogramul astfel încât să evidențiați toate cazurile tratate.

-- Afisati numele jucatorilor care au un KDA mai mare decat media KDA-urilor tuturor jucatorilor dintr-un turneu dat.
-- KDA = (kills + assists) / deaths, in cazul in care deaths = 0, KDA = kills + assists

CREATE OR REPLACE TYPE players_table IS TABLE OF VARCHAR2(100);

CREATE OR REPLACE FUNCTION ex8(p_tournament_name IN tournaments.tournament_name%TYPE)
    RETURN players_table IS
    v_kda_avg           NUMBER;
    v_player_name       VARCHAR2(100);
    v_player_kda        NUMBER;
    v_tournament_exists NUMBER;
    e_tournament_not_found EXCEPTION;
    e_no_statistics_found EXCEPTION;
    e_multiple_tournaments_found EXCEPTION;
    v_players_above_avg players_table := players_table();
    CURSOR c_kda_cursor IS
        SELECT p.summoner_name,
               (SUM(ps.kills) + SUM(ps.assists)) / (NULLIF(SUM(ps.deaths), 0)) AS player_kda
        FROM players p
                 JOIN player_statistics ps ON ps.player_id = p.id
                 JOIN matches m ON m.id = ps.match_id
                 JOIN tournaments t ON t.id = m.tournament_id
        WHERE t.tournament_name = p_tournament_name
        GROUP BY p.summoner_name;
BEGIN
    SELECT COUNT(*)
    INTO v_tournament_exists
    FROM tournaments
    WHERE tournament_name = p_tournament_name;

    IF v_tournament_exists = 0 THEN
        RAISE e_tournament_not_found;
    ELSIF v_tournament_exists > 1 THEN
        RAISE e_multiple_tournaments_found;
    END IF;

    SELECT AVG((ps.kills + ps.assists) / NULLIF(ps.deaths, 0))
    INTO v_kda_avg
    FROM players p
             JOIN player_statistics ps ON ps.player_id = p.id
             JOIN matches m ON m.id = ps.match_id
             JOIN tournaments t ON t.id = m.tournament_id
    WHERE t.tournament_name = p_tournament_name;

    IF v_kda_avg IS NULL THEN
        RAISE e_no_statistics_found;
    END IF;

    OPEN c_kda_cursor;
    LOOP
        FETCH c_kda_cursor INTO v_player_name, v_player_kda;
        EXIT WHEN c_kda_cursor%NOTFOUND;
        IF v_player_kda > v_kda_avg THEN
            v_players_above_avg.extend;
            v_players_above_avg(v_players_above_avg.count) := v_player_name;
        END IF;
    END LOOP;
    CLOSE c_kda_cursor;

    RETURN v_players_above_avg;

EXCEPTION
    WHEN e_no_statistics_found THEN
        RAISE_APPLICATION_ERROR(-20001, 'No statistics found for tournament ' || p_tournament_name || '.');
        RETURN NULL;
    WHEN e_multiple_tournaments_found THEN
        RAISE_APPLICATION_ERROR(-20002,
                                'Multiple tournaments found with name ' || p_tournament_name || '.');
        RETURN NULL;
    WHEN e_tournament_not_found THEN
        RAISE_APPLICATION_ERROR(-20003, 'Tournament with name ' || p_tournament_name || ' does not exist.');
        RETURN NULL;
END ex8;
/

DECLARE
    players players_table;
BEGIN
    players := ex8('Worlds 2022');
    FOR i IN 1..players.count
        LOOP
            dbms_output.put_line(players(i));
        END LOOP;
END;
/

-- EXPECTED
-- Spica
-- Doublelift
-- Ming
-- Bjergsen
-- Hylissang
-- Effort
-- Meiko
-- Biofrost
-- Selfmade

DECLARE
    players players_table;
BEGIN
    players := ex8('Worlds 2021');
    FOR i IN 1..players.count
        LOOP
            dbms_output.put_line(players(i));
        END LOOP;
END;
/

-- EXPECTED
-- No statistics found for tournament Worlds 2021.

-- Cream un turneu cu un nume ce este deja prezent in baza de date
-- pentru a testa exceptia multiple_tournaments_found.

INSERT INTO tournaments (tournament_name, start_date, end_date, location, id)
VALUES ('Worlds 2020', TO_DATE('2020-09-29', 'YYYY-MM-DD'), TO_DATE('2020-11-06', 'YYYY-MM-DD'), 'London', 999);
COMMIT;

DECLARE
    players players_table;
BEGIN
    players := ex8('Worlds 2020');
    FOR i IN 1..players.count
        LOOP
            dbms_output.put_line(players(i));
        END LOOP;
END;
/

-- EXPECTED
-- Multiple tournaments found with name Worlds 2020.

-- Stergem turneul creat anterior.
DELETE
FROM tournaments
WHERE id = 999;


DECLARE
    players players_table;
BEGIN
    players := ex8('BadName');
    FOR i IN 1..players.count
        LOOP
            dbms_output.put_line(players(i));
        END LOOP;
END;
/

-- EXPECTED
-- Tournament with name BadName does not exist.

------------------------------------------------------------------------------------------------------------------------

-- EX9
-- Formulați în limbaj natural o problemă pe care să o rezolvați folosind un subprogram stocat independent
-- de tip procedură care să utilizeze într-o singură comandă SQL 5 dintre tabelele definite.
-- Tratați toate excepțiile care pot apărea, incluzând excepțiile NO_DATA_FOUND și TOO_MANY_ROWS.
-- Apelați subprogramul astfel încât să evidențiați toate cazurile tratate.

-- Afisati numele campionilor si media de cs ce sunt in top 5 in functie de media de cs pe meci
-- pentru un anumit turneu.

CREATE OR REPLACE PROCEDURE ex9(p_tournament_name IN tournaments.tournament_name%TYPE)
    IS
    TYPE r_cs_champions_type IS RECORD
                                (
                                    champion_name champions.champion_name%TYPE,
                                    average_cs    NUMBER
                                );
    TYPE t_cs_champions_table IS TABLE OF r_cs_champions_type;
    v_cs_champions      t_cs_champions_table;
    v_tournament_exists NUMBER;
    CURSOR c_top5_avg IS
        SELECT c.champion_name, AVG(ps.cs) AS average_cs
        FROM champions c
                 JOIN champion_picks cp ON c.id = cp.champion_id
                 JOIN player_statistics ps ON cp.player_id = ps.player_id AND cp.match_id = ps.match_id
                 JOIN matches m ON cp.match_id = m.id
                 JOIN tournaments t ON m.tournament_id = t.id
        WHERE t.tournament_name = p_tournament_name
        GROUP BY c.champion_name
        HAVING AVG(ps.cs) > 250
        ORDER BY AVG(ps.cs) DESC;
BEGIN
    SELECT id INTO v_tournament_exists FROM tournaments WHERE tournament_name = p_tournament_name;

    OPEN c_top5_avg;
    FETCH c_top5_avg BULK COLLECT INTO v_cs_champions;
    CLOSE c_top5_avg;

    FOR i IN 1..LEAST(v_cs_champions.count, 5)
        LOOP
            dbms_output.put_line('Champion ' || v_cs_champions(i).champion_name || ' has an average CS of ' ||
                                 ROUND(v_cs_champions(i).average_cs, 0));
        END LOOP;
EXCEPTION
    WHEN no_data_found THEN
        RAISE_APPLICATION_ERROR(-20001, 'Tournament with name ' || p_tournament_name || ' does not exist.');
    WHEN too_many_rows THEN
        RAISE_APPLICATION_ERROR(-20002, 'Multiple tournaments with name ' || p_tournament_name || ' exist.');
END ex9;
/

BEGIN
    ex9('Worlds 2022');
END;
/

-- EXPECTED
-- Champion Maokai has an average CS of 343
-- Champion Fiora has an average CS of 322
-- Champion Gnar has an average CS of 316
-- Champion Camille has an average CS of 289
-- Champion Ahri has an average CS of 283

BEGIN
    ex9('BadName');
END;
/

-- EXPECTED
-- Tournament with name BadName does not exist.

-- Cream un turneu cu un nume ce este deja prezent in baza de date
-- pentru a testa exceptia multiple_tournaments_found.

INSERT INTO tournaments (tournament_name, start_date, end_date, location, id)
VALUES ('Worlds 2020', TO_DATE('2020-09-29', 'YYYY-MM-DD'), TO_DATE('2020-11-06', 'YYYY-MM-DD'), 'London', 999);
COMMIT;

BEGIN
    ex9('Worlds 2020');
END;
/

-- EXPECTED
-- Multiple tournaments with name Worlds 2020 exist.

-- Stergem turneul creat anterior.
DELETE
FROM tournaments
WHERE id = 999;

------------------------------------------------------------------------------------------------------------------------

-- EX10
-- Definiți un trigger de tip LMD la nivel de comandă. Declanșați trigger-ul.

-- Acest trigger se asigura de faptul ca nu se pot actualiza sau sterge date din tabela regions.

CREATE OR REPLACE TRIGGER trigger_ex10
    BEFORE UPDATE OR DELETE
    ON regions
BEGIN
    IF UPDATING THEN
        RAISE_APPLICATION_ERROR(-20001, 'Regions cannot be updated');
    ELSIF DELETING THEN
        RAISE_APPLICATION_ERROR(-20002, 'Regions cannot be deleted');
    END IF;
END;
/

-- UPDATE regions SET region_name = 'Europe' WHERE id = 1;
-- EXPECTED:
-- ORA-20001: Regions cannot be updated

-- DELETE FROM regions WHERE id = 1;
-- EXPECTED:
-- ORA-20002: Regions cannot be deleted


------------------------------------------------------------------------------------------------------------------------

-- EX11
-- Definiți un trigger de tip LMD la nivel de linie. Declanșați trigger-ul.

-- Acest trigger se asigura de faptul ca la inserarea sau actualizarea datelor din tabela match_result,
-- echipa castigatoare este una dintre cele doua echipe care au jucat meciul respectiv.

CREATE OR REPLACE TRIGGER trigger_ex11
    BEFORE INSERT OR UPDATE
    ON match_results
    FOR EACH ROW
DECLARE
    v_team1_id teams.id%TYPE;
    v_team2_id teams.id%TYPE;
BEGIN
    SELECT team1_id, team2_id INTO v_team1_id, v_team2_id FROM matches WHERE id = :new.match_id;

    IF (:new.winning_team_id <> v_team1_id AND :new.winning_team_id <> v_team2_id) THEN
        RAISE_APPLICATION_ERROR(-20001, 'Team ' || :new.winning_team_id || ' is not in match ' || :new.match_id);
    END IF;
END;
/

-- INSERT INTO match_results (match_id, winning_team_id)
-- VALUES (1, 6);
-- EXPECTED:
-- ORA-20001: Team 6 is not in match 1

-- INSERT INTO match_results (match_id, winning_team_id)
-- VALUES (28, 6);
-- EXPECTED:
-- ORA-01403: no data found

------------------------------------------------------------------------------------------------------------------------

-- EX12
-- Definiți un trigger de tip LDD. Declanșați trigger-ul.

-- Acest trigger se asigura de faptul ca doar userul ADMIN poate crea, sterge sau modifica tabele.

CREATE OR REPLACE TRIGGER trigger_ex12
    BEFORE CREATE OR DROP OR ALTER
    ON SCHEMA
BEGIN
    IF (sys.login_user() <> 'ADMIN') THEN
        RAISE_APPLICATION_ERROR(-20001, 'Only ADMIN user can create, drop or alter tables');
    END IF;
END;
/

-- Pentru a testa acest trigger, trebuie sa va logati cu un user care nu este ADMIN.
-- Pentru simplitate la rulare voi schimba conditia ca userul logat sa fie ADMIN2 pentru a declansa exceptia.

-- CREATE TABLE test_table (id NUMBER);
-- DROP TABLE test_table;

-- EXPECTED:
-- ORA-20001: Only ADMIN user can create, drop or alter tables

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------- OPTIONAL ----------------------------------------------------------

-- EX13
-- Definiți un pachet care să conțină toate obiectele definite în cadrul proiectului.

CREATE OR REPLACE PACKAGE package_ex13 AS

    TYPE players_table_package IS TABLE OF VARCHAR2(100);
    PROCEDURE ex6(p_tournament_name IN tournaments.tournament_name%TYPE);
    PROCEDURE ex7(p_tournament_name IN tournaments.tournament_name%TYPE);
    FUNCTION ex8(p_tournament_name IN tournaments.tournament_name%TYPE) RETURN players_table_package;
    PROCEDURE ex9(p_tournament_name IN tournaments.tournament_name%TYPE);

END package_ex13;
/

CREATE OR REPLACE PACKAGE BODY package_ex13 AS
    -- Pentru un turneu dat, pentru fiecare rol, sa se afiseze id-ul jucatorului ce joaca acel rol
    -- si are numarul maxim de kill-uri facute de acesta intr-un singur meci. Afisati si numarul de killuri.
    PROCEDURE ex6(p_tournament_name IN tournaments.tournament_name%TYPE) AS
        TYPE t_role_kills IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
        TYPE t_role_players IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
        TYPE t_result IS TABLE OF VARCHAR2(100);
        v_result        t_result := t_result();
        v_role_kills    t_role_kills;
        v_role_players  t_role_players;
        v_max_kills     NUMBER;
        v_player_id     players.id%TYPE;
        v_role_id       roles.id%TYPE;
        v_tournament_id tournaments.id%TYPE;
    BEGIN
        SELECT id INTO v_tournament_id FROM tournaments WHERE tournament_name = p_tournament_name;

        FOR r IN (SELECT id FROM roles)
            LOOP
                v_role_id := r.id;
                SELECT ps.player_id, MAX(ps.kills)
                INTO v_player_id, v_max_kills
                FROM player_statistics ps
                         JOIN matches m ON m.id = ps.match_id
                         JOIN players p ON p.id = ps.player_id
                WHERE m.tournament_id = v_tournament_id
                  AND p.role_id = v_role_id
                GROUP BY ps.player_id
                ORDER BY MAX(ps.kills) DESC
                    FETCH FIRST ROW ONLY;

                IF v_role_kills.EXISTS(v_role_id) THEN
                    IF v_max_kills > v_role_kills(v_role_id) THEN
                        v_role_kills(v_role_id) := v_max_kills;
                        v_role_players(v_role_id) := v_player_id;
                    END IF;
                ELSE
                    v_role_kills(v_role_id) := v_max_kills;
                    v_role_players(v_role_id) := v_player_id;
                END IF;
            END LOOP;

        v_role_id := v_role_kills.first;
        WHILE v_role_id IS NOT NULL
            LOOP
                v_result.extend;
                v_result(v_result.count) :=
                            'Player with id ' || v_role_players(v_role_id) || ' in role ' || v_role_id ||
                            ' had the maximum kills: ' || v_role_kills(v_role_id);
                v_role_id := v_role_kills.next(v_role_id);
            END LOOP;

        FOR i IN 1 .. v_result.count
            LOOP
                dbms_output.put_line(v_result(i));
            END LOOP;
    END ex6;

    -- Afișați numele echipelor și numărul de meciuri câștigate de acestea intr-un turneu dat.
    PROCEDURE ex7(p_tournament_name IN tournaments.tournament_name%TYPE)
        IS
        CURSOR c_teams
            IS
            SELECT id, team_name
            FROM teams;
        TYPE ref_cur_type IS REF CURSOR;
        v_team_wins     ref_cur_type;
        v_team_id       teams.id%TYPE;
        v_team_name     teams.team_name%TYPE;
        v_wins          NUMBER;
        v_tournament_id tournaments.id%TYPE;
    BEGIN
        SELECT id INTO v_tournament_id FROM tournaments WHERE tournament_name = p_tournament_name;

        OPEN c_teams;
        LOOP
            FETCH c_teams INTO v_team_id, v_team_name;
            EXIT WHEN c_teams%NOTFOUND;

            OPEN v_team_wins FOR
                SELECT COUNT(*) AS wins
                FROM match_results mr
                         JOIN matches m ON m.id = mr.match_id
                WHERE m.tournament_id = v_tournament_id
                  AND mr.winning_team_id = v_team_id;

            FETCH v_team_wins INTO v_wins;
            CLOSE v_team_wins;

            dbms_output.put_line('Team: ' || v_team_name || ' - Wins: ' || v_wins);
        END LOOP;
        CLOSE c_teams;
    END ex7;

    -- Afisati numele jucatorilor care au un KDA mai mare decat media KDA-urilor tuturor jucatorilor dintr-un turneu dat.
    -- KDA = (kills + assists) / deaths, in cazul in care deaths = 0, KDA = kills + assists
    FUNCTION ex8(p_tournament_name IN tournaments.tournament_name%TYPE)
        RETURN players_table_package IS
        v_kda_avg           NUMBER;
        v_player_name       VARCHAR2(100);
        v_player_kda        NUMBER;
        v_tournament_exists NUMBER;
        e_tournament_not_found EXCEPTION;
        e_no_statistics_found EXCEPTION;
        e_multiple_tournaments_found EXCEPTION;
        v_players_above_avg players_table_package := players_table_package();
        CURSOR c_kda_cursor IS
            SELECT p.summoner_name,
                   (SUM(ps.kills) + SUM(ps.assists)) / (NULLIF(SUM(ps.deaths), 0)) AS player_kda
            FROM players p
                     JOIN player_statistics ps ON ps.player_id = p.id
                     JOIN matches m ON m.id = ps.match_id
                     JOIN tournaments t ON t.id = m.tournament_id
            WHERE t.tournament_name = p_tournament_name
            GROUP BY p.summoner_name;
    BEGIN
        SELECT COUNT(*)
        INTO v_tournament_exists
        FROM tournaments
        WHERE tournament_name = p_tournament_name;

        IF v_tournament_exists = 0 THEN
            RAISE e_tournament_not_found;
        ELSIF v_tournament_exists > 1 THEN
            RAISE e_multiple_tournaments_found;
        END IF;

        SELECT AVG((ps.kills + ps.assists) / NULLIF(ps.deaths, 0))
        INTO v_kda_avg
        FROM players p
                 JOIN player_statistics ps ON ps.player_id = p.id
                 JOIN matches m ON m.id = ps.match_id
                 JOIN tournaments t ON t.id = m.tournament_id
        WHERE t.tournament_name = p_tournament_name;

        IF v_kda_avg IS NULL THEN
            RAISE e_no_statistics_found;
        END IF;

        OPEN c_kda_cursor;
        LOOP
            FETCH c_kda_cursor INTO v_player_name, v_player_kda;
            EXIT WHEN c_kda_cursor%NOTFOUND;
            IF v_player_kda > v_kda_avg THEN
                v_players_above_avg.extend;
                v_players_above_avg(v_players_above_avg.count) := v_player_name;
            END IF;
        END LOOP;
        CLOSE c_kda_cursor;

        RETURN v_players_above_avg;

    EXCEPTION
        WHEN e_no_statistics_found THEN
            RAISE_APPLICATION_ERROR(-20001, 'No statistics found for tournament ' || p_tournament_name || '.');
            RETURN NULL;
        WHEN e_multiple_tournaments_found THEN
            RAISE_APPLICATION_ERROR(-20002,
                                    'Multiple tournaments found with name ' || p_tournament_name || '.');
            RETURN NULL;
        WHEN e_tournament_not_found THEN
            RAISE_APPLICATION_ERROR(-20003, 'Tournament with name ' || p_tournament_name || ' does not exist.');
            RETURN NULL;
    END ex8;

    -- Afisati numele campionilor si media de cs ce sunt in top 5 in functie de media de cs pe meci
    -- pentru un anumit turneu.
    PROCEDURE ex9(p_tournament_name IN tournaments.tournament_name%TYPE)
        IS
        TYPE r_cs_champions_type IS RECORD
                                    (
                                        champion_name champions.champion_name%TYPE,
                                        average_cs    NUMBER
                                    );
        TYPE t_cs_champions_table IS TABLE OF r_cs_champions_type;
        v_cs_champions      t_cs_champions_table;
        v_tournament_exists NUMBER;
        CURSOR c_top5_avg IS
            SELECT c.champion_name, AVG(ps.cs) AS average_cs
            FROM champions c
                     JOIN champion_picks cp ON c.id = cp.champion_id
                     JOIN player_statistics ps ON cp.player_id = ps.player_id AND cp.match_id = ps.match_id
                     JOIN matches m ON cp.match_id = m.id
                     JOIN tournaments t ON m.tournament_id = t.id
            WHERE t.tournament_name = p_tournament_name
            GROUP BY c.champion_name
            HAVING AVG(ps.cs) > 250
            ORDER BY AVG(ps.cs) DESC;
    BEGIN
        SELECT id INTO v_tournament_exists FROM tournaments WHERE tournament_name = p_tournament_name;

        OPEN c_top5_avg;
        FETCH c_top5_avg BULK COLLECT INTO v_cs_champions;
        CLOSE c_top5_avg;

        FOR i IN 1..LEAST(v_cs_champions.count, 5)
            LOOP
                dbms_output.put_line('Champion ' || v_cs_champions(i).champion_name || ' has an average CS of ' ||
                                     ROUND(v_cs_champions(i).average_cs, 0));
            END LOOP;
    EXCEPTION
        WHEN no_data_found THEN
            RAISE_APPLICATION_ERROR(-20001, 'Tournament with name ' || p_tournament_name || ' does not exist.');
        WHEN too_many_rows THEN
            RAISE_APPLICATION_ERROR(-20002, 'Multiple tournaments with name ' || p_tournament_name || ' exist.');
    END ex9;

END package_ex13;
/

DECLARE
    players package_ex13.players_table_package;
BEGIN
    package_ex13.ex6('Worlds 2022');
    package_ex13.ex7('Worlds 2022');
    players := package_ex13.ex8('Worlds 2022');
    FOR i IN 1..players.count
        LOOP
            dbms_output.put_line(players(i));
        END LOOP;
    package_ex13.ex9('Worlds 2022');
END;
/

------------------------------------------------------------------------------------------------------------------------

-- EX14
-- Definiți un pachet care să includă tipuri de date complexe și obiecte necesare unui flux de acțiuni integrate,
-- specifice bazei de date definite (minim 2 tipuri de date, minim 2 funcții, minim 2 proceduri).

-- Vrem sa aflam care este cel mai bun campion din meta intr-un turneu dat.
-- Pentru a afla asta vom lua in considerare urmatoarele:
-- 1. Numarul de banuri pe care il are campionul
-- 2. Performanta campionului (KDA)
-- Vom folosi urmatoarele formule:
-- 1. Pentru numarul de banuri: bans_count * 100 / total_bans
-- 2. Pentru performanta: (kills + assists) / deaths
-- 3. Pentru scorul campionului: bans_score * 10 + performance * 5

CREATE OR REPLACE PACKAGE package_ex14 AS

    TYPE t_champion IS RECORD
                       (
                           id            champions.id%TYPE,
                           champion_name champions.champion_name%TYPE,
                           role_id       champions.role_id%TYPE,
                           bans_count    NUMBER,
                           bans_score    NUMBER,
                           performance   NUMBER
                       );

    PROCEDURE parse_champion(p_champion_id IN NUMBER, p_tournament_id IN NUMBER, t_champion OUT t_champion);

    PROCEDURE calculate_champion_performance(p_champion IN OUT t_champion);

    FUNCTION calculate_meta_score(p_champion IN t_champion) RETURN NUMBER;

    FUNCTION get_meta_champion(p_tournament_id IN NUMBER) RETURN t_champion;

END package_ex14;
/

CREATE OR REPLACE PACKAGE BODY package_ex14 AS

    PROCEDURE parse_champion(p_champion_id IN NUMBER, p_tournament_id IN NUMBER, t_champion OUT t_champion) IS
        v_total_bans NUMBER;
        v_bans_count NUMBER;
    BEGIN
        SELECT COUNT(*)
        INTO v_total_bans
        FROM bans b
                 INNER JOIN matches m ON b.match_id = m.id
        WHERE m.tournament_id = p_tournament_id;

        SELECT COUNT(*)
        INTO v_bans_count
        FROM bans b
                 INNER JOIN matches m ON b.match_id = m.id
        WHERE m.tournament_id = p_tournament_id
          AND champion_id = p_champion_id;
        t_champion.id := p_champion_id;

        SELECT champion_name, role_id
        INTO t_champion.champion_name, t_champion.role_id
        FROM champions
        WHERE id = p_champion_id;

        t_champion.bans_score := (v_bans_count * 100) / v_total_bans;
        calculate_champion_performance(t_champion);
    END parse_champion;

    PROCEDURE calculate_champion_performance(p_champion IN OUT t_champion) IS
    BEGIN
        SELECT ROUND(AVG((ps.kills + ps.assists) / NULLIF(ps.deaths, 0)), 3)
        INTO p_champion.performance
        FROM player_statistics ps
                 INNER JOIN champion_picks cp ON ps.match_id = cp.match_id AND ps.player_id = cp.player_id
        WHERE cp.champion_id = p_champion.id;
    END calculate_champion_performance;

    FUNCTION calculate_meta_score(p_champion IN t_champion) RETURN NUMBER IS
    BEGIN
        RETURN p_champion.bans_score * 10 + p_champion.performance * 5;
    END calculate_meta_score;

    FUNCTION get_meta_champion(p_tournament_id IN NUMBER) RETURN t_champion IS
        v_best_champion    t_champion;
        v_current_champion t_champion;
        v_best_score       NUMBER := 0;
        v_current_score    NUMBER;
        e_no_champion_data_found EXCEPTION;
        CURSOR c_champions_with_data IS
            SELECT id
            FROM champions
            WHERE 0 < (SELECT COUNT(*)
                       FROM champion_picks
                       WHERE champion_id = champions.id
                         AND match_id IN (SELECT id FROM matches WHERE tournament_id = p_tournament_id))
               OR 0 < (SELECT COUNT(*)
                       FROM bans
                       WHERE champion_id = champions.id
                         AND match_id IN (SELECT id FROM matches WHERE tournament_id = p_tournament_id));
    BEGIN
        FOR r IN c_champions_with_data
            LOOP
                parse_champion(r.id, p_tournament_id, v_current_champion);
                v_current_score := calculate_meta_score(v_current_champion);
                IF v_current_score > v_best_score THEN
                    v_best_score := v_current_score;
                    v_best_champion := v_current_champion;
                END IF;
            END LOOP;
        IF v_best_champion.id is NULL THEN
            RAISE e_no_champion_data_found;
        END IF;
        RETURN v_best_champion;
    EXCEPTION
        WHEN e_no_champion_data_found THEN
            RAISE_APPLICATION_ERROR(-20001, 'No champion data found for tournament with id ' || p_tournament_id);
    END get_meta_champion;

END package_ex14;
/

DECLARE
    v_meta_champion package_ex14.t_champion;
BEGIN
    v_meta_champion := package_ex14.get_meta_champion(1);
    dbms_output.put_line('Meta champion is ' || v_meta_champion.champion_name || ' with a score of ' ||
                         v_meta_champion.performance);
END;
/

-- EXPECTED:
-- Meta champion is Yasuo with a score of 14

DECLARE
    v_meta_champion package_ex14.t_champion;
BEGIN
    v_meta_champion := package_ex14.get_meta_champion(3);
    dbms_output.put_line('Meta champion is ' || v_meta_champion.champion_name || ' with a score of ' ||
                         v_meta_champion.performance);
END;
/

-- EXPECTED:
-- ORA-20001: No champion data found for tournament with id 3
