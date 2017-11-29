# 문제 설명
#
# FRIENDS 테이블은 게임 내 친구 관계 정보를 담고 있습니다. FRIENDS 테이블 구조는 다음과 같으며 ID1, ID2 쌍은 ID1과 ID2가 서로 친구라는 뜻입니다. 이 테이블에서, 친구 관계는 양방향이며, 친구 관계가 중복으로 등록되는 경우는 없습니다. (id1가 id2의 친구이면 id2는 id1의 친구이고, 레코드 id1, id2가 등록되어 있을 때, 레코드 id2, id1가 등록되는 경우는 없습니다)
#
# NAME	TYPE	NULLABLE
# ID1	VARCHAR(N)	FALSE
# ID2	VARCHAR(N)	FALSE
# FRIENDS 테이블로, solidwillow917 계정의 친구를 찾아내는 SQL문을 작성해주세요.
# 친구 목록은 닉네임을 사전순으로 나열해주세요.
#
# 예를 들어
#
# 예를 들어 FRIENDS 테이블이 다음과 같다면
#
# ID1	ID2
# naneekgunpowder1886	treesbeta791
# chongqingricochet889	naneekgunpowder1886
# adorableblue1813	treesbeta791
# solidwillow917	treesbeta791
# daysglossy1776	treesbeta791
# chongqingricochet889	solidwillow917
# solidwillow917 의 친구는 treesbeta791와 chongqingricochet889 이므로 SQL을 실행하면 다음과 같이 출력되어야 합니다.
#
# ID
# chongqingricochet889
# treesbeta791


barracudafried1489
cronzbloviate1050
rhapsodydusky1531
triumphfox488

SELECT ID2 AS ID
FROM FRIENDS
WHERE ID1 LIKE 'solidwillow917'
UNION
SELECT ID1
FROM FRIENDS
WHERE ID2 LIKE 'solidwillow917'




barracudafried1489
cronzbloviate1050
rhapsodydusky1531
triumphfox488



SELECT ID1
FROM FRIENDS
WHERE ID2 LIKE 'solidwillow917'


SELECT ID2
FROM FRIENDS
WHERE ID1 LIKE 'solidwillow917'



SELECT *
FROM
    (SELECT *
    FROM FRIENDS
    WHERE ID2 LIKE 'solidwillow917' OR ID1 LIKE 'solidwillow917') AS T1
WHERE ID1 LIKE 'solidwillow917'
