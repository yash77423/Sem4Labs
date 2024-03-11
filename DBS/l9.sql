--Q6.

DECLARE
    v_dept_name VARCHAR2(255);
    v_course_title VARCHAR2(255);
BEGIN
    FOR dept_rec IN (SELECT DISTINCT dept_name FROM Course)
    LOOP
        v_dept_name := dept_rec.dept_name;
        v_course_title := course_popular(v_dept_name);
        DBMS_OUTPUT.PUT_LINE('Most popular course in department ' || v_dept_name || ': ' || v_course_title);
    END LOOP;
END;
/

CREATE OR REPLACE FUNCTION course_popular (p_dept_name VARCHAR2) RETURN VARCHAR2
IS
    v_course_title VARCHAR2(255);
    v_max_students NUMBER := 0;
    v_temp_course_title VARCHAR2(255);
BEGIN
    FOR course_rec IN (SELECT title, COUNT(*) AS num_students
                        FROM Takes
                        JOIN Course ON Takes.course_id = Course.course_id
                        WHERE Course.dept_name = p_dept_name
                        GROUP BY title)
    LOOP
        IF course_rec.num_students > v_max_students THEN
            v_max_students := course_rec.num_students;
            v_temp_course_title := course_rec.title;
        END IF;
    END LOOP;
    
    v_course_title := v_temp_course_title;
    
    RETURN v_course_title;
END;
/




--Q7.

-- Package Specification
CREATE OR REPLACE PACKAGE Instructor_Info AS
    -- Procedure to list instructor names of a given department
    PROCEDURE list_instructors(p_dept_name VARCHAR2);
    
    -- Function to return the max salary for a given department
    FUNCTION max_salary(p_dept_name VARCHAR2) RETURN NUMBER;
END Instructor_Info;
/

-- Package Body
CREATE OR REPLACE PACKAGE BODY Instructor_Info AS
    -- Procedure to list instructor names of a given department
    PROCEDURE list_instructors(p_dept_name VARCHAR2) IS
    BEGIN
        FOR instructor_rec IN (SELECT name FROM Instructor WHERE dept_name = p_dept_name)
        LOOP
            DBMS_OUTPUT.PUT_LINE('Instructor Name: ' || instructor_rec.name);
        END LOOP;
    END list_instructors;
    
    -- Function to return the max salary for a given department
    FUNCTION max_salary(p_dept_name VARCHAR2) RETURN NUMBER IS
        v_max_salary NUMBER;
    BEGIN
        SELECT MAX(salary)
        INTO v_max_salary
        FROM Instructor
        WHERE dept_name = p_dept_name;
        
        RETURN v_max_salary;
    END max_salary;
END Instructor_Info;
/

-- PL/SQL block to demonstrate usage
DECLARE
    v_dept_name VARCHAR2(255) := 'Computer Science'; -- Specify the department name
    v_max_salary NUMBER;
BEGIN
    -- Call the procedure to list instructors
    DBMS_OUTPUT.PUT_LINE('Instructors in ' || v_dept_name || ':');
    Instructor_Info.list_instructors(v_dept_name);
    
    -- Call the function to get the max salary
    v_max_salary := Instructor_Info.max_salary(v_dept_name);
    DBMS_OUTPUT.PUT_LINE('Max Salary in ' || v_dept_name || ': ' || v_max_salary);
END;
/



--Q8. 

CREATE OR REPLACE PROCEDURE calculate_interest (
    p_principle IN NUMBER,
    p_rate IN NUMBER,
    p_years IN NUMBER,
    p_simple_interest OUT NUMBER,
    p_compound_interest OUT NUMBER,
    p_total_sum IN OUT NUMBER
)
IS
BEGIN
    -- Calculate simple interest
    p_simple_interest := (p_principle * p_rate * p_years) / 100;
    
    -- Calculate compound interest
    p_compound_interest := p_principle * POWER((1 + p_rate/100), p_years) - p_principle;
    
    -- Update total sum
    p_total_sum := p_principle + p_simple_interest;
END;
/

-- Anonymous block to call the procedure
DECLARE
    v_principle NUMBER := 1000;
    v_rate NUMBER := 5;
    v_years NUMBER := 3;
    v_simple_interest NUMBER;
    v_compound_interest NUMBER;
    v_total_sum NUMBER := 0; -- Initialize total sum to 0
    
BEGIN
    calculate_interest(v_principle, v_rate, v_years, v_simple_interest, v_compound_interest, v_total_sum);
    
    DBMS_OUTPUT.PUT_LINE('Simple Interest: ' || v_simple_interest);
    DBMS_OUTPUT.PUT_LINE('Compound Interest: ' || v_compound_interest);
    DBMS_OUTPUT.PUT_LINE('Total Sum: ' || v_total_sum);
END;
/
