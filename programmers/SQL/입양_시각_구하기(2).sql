SELECT HOUR(DATETIME), COUNT(HOUR(DATETIME))
FROM ANIMAL_OUTS 
GROUP BY HOUR(DATETIME);

/*
테이블에 없는 시간을 만들어내야 하는데 해결 방법은 크게 두 가지로 나뉘는 것 같다.
1) SQL문 내에서 변수를 직접 만들기 : https://murra.tistory.com/152, https://codingmoonkwa.tistory.com/26
2) UNION이라는 연산과 LEFT JOIN을 사용하기 : https://mentha2.tistory.com/97, https://codedrive.tistory.com/272
이건 ㄹㅇ 모르겠는데? 쌩판 첨보는거다. 이럴거야...?
*/
