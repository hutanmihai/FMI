CREATE TABLE emp_HMA AS
SELECT *
FROM employees;

DECLARE
    TYPE vector IS varray(5) OF emp_hma.employee_id%type;
    v     vector;
    sal_initial INTEGER;
    sal_nou INTEGER;
BEGIN
    SELECT employee_id BULK COLLECT
    INTO v
    FROM (SELECT employee_id FROM emp_hma WHERE commission_pct IS NULL ORDER BY salary ASC)
    WHERE rownum <= 5;

    FOR i IN 1..5
        LOOP
            SELECT salary INTO sal_initial FROM emp_hma WHERE employee_id = v(i);
            UPDATE emp_hma SET salary = 1.05 * salary WHERE employee_id = v(i);
            SELECT salary INTO sal_nou FROM emp_hma WHERE employee_id = v(i);
            dbms_output.put_line('Salariul initial: ' || sal_initial || '; Salariul nou: ' || sal_nou);
        END LOOP;
    ROLLBACK;
END;
