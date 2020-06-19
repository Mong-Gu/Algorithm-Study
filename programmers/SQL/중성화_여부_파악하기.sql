SELECT ANIMAL_ID, NAME,
        REPLACE(REPLACE(REPLACE(REPLACE(SEX_UPON_INTAKE, 'Spayed Female', 'O'),'Neutered Male', 'O'), 'Intact Male', 'X'),'Intact Female', 'X') AS 중성화
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID

--- 다른 분 코드 ---
SELECT ANIMAL_ID,NAME, IF(SEX_UPON_INTAKE LIKE 'Intact %', 'X', 'O') as '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
