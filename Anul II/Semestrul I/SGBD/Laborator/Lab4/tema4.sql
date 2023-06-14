--EX2
--a)
SELECT data_calendaristica,
       (SELECT COUNT(*)
        FROM rental
        WHERE EXTRACT(DAY FROM book_date) = EXTRACT(DAY FROM data_calendaristica)
          AND EXTRACT(MONTH FROM book_date) = EXTRACT(MONTH FROM data_calendaristica)) AS imprumuturi
FROM (SELECT TRUNC(LAST_DAY(SYSDATE - 30) - rownum) data_calendaristica
      FROM dual
      CONNECT BY rownum < EXTRACT(DAY FROM LAST_DAY(SYSDATE - 30)))
ORDER BY data_calendaristica;


--EX5
CREATE TABLE member_hma AS
SELECT *
FROM member;
DESC member;
DESC member_hma;
ALTER TABLE member_hma
    ADD CONSTRAINT pk_member_hma PRIMARY KEY (member_id);

SELECT *
FROM member_hma;

ALTER TABLE member_hma
    ADD discount NUMBER(6, 2);

DECLARE
    membru      member_hma.member_id%TYPE := &id;
    numar_filme NUMBER(6);
    numar_total NUMBER(6);
BEGIN
    SELECT COUNT(DISTINCT r.title_id)
    INTO numar_filme
    FROM rental r
             JOIN member_hma m ON m.member_id = r.member_id
    WHERE m.member_id = membru;


    SELECT COUNT(title_id)
    INTO numar_total
    FROM title;

    UPDATE member_hma
    SET discount =
            CASE
                WHEN numar_filme >= 0.75 * numar_total
                    THEN 0.1
                WHEN numar_filme BETWEEN 0.5 * numar_total AND 0.75 * numar_total
                    THEN 0.05
                WHEN numar_filme BETWEEN 0.25 * numar_total AND 0.5 * numar_total
                    THEN 0.03
                ELSE 0
                END
    WHERE member_id = membru;

    dbms_output.put_line('Success!');

END;
/