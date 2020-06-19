SELECT DISTINCT(A.CART_ID)

FROM CART_PRODUCTS AS A,
    (SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = '우유') AS B
    
WHERE (A.CART_ID = B.CART_ID) AND (A.NAME = '요거트')

ORDER BY A.CART_ID

/*
FROM에서 테이블을 저렇게 만들어낼 수 있다는 것을 처음 알았다.
https://sewonkimm.github.io/sql/2019/12/02/wintercoding2019.html
를 보고 참고함.
*/