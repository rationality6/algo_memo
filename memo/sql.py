# 문제 설명
#
# VIDEOS 테이블은 OO 비디오 대여점이 갖고 있는 영화 정보를 담고 있는 테이블입니다. VIDEOS 테이블 구조는 다음과 같으며, TITLE, RATE, NUM_VIEW, RELEASE_DATE, MPAA_RATE는 각각 제목, 평점, 관객 수, 개봉일, 영화 등급을 의미합니다.
#
# NAME	TYPE	NULLABLE
# ID	INT	FALSE
# TITLE	VARCHAR(N)	FALSE
# RATE	NUMERIC(N,M)	FALSE
# NUM_VIEW	INT	FALSE
# RELEASE_DATE	DATE	FALSE
# MPAA_RATE	VARCHAR(N)	FALSE
# OO 비디오 대여점이 보유한 영화의 평균 평점을 구하는 SQL문을 작성해주세요. 단, 평균 평점은 반올림하여 소숫점 2번째 자리까지만 나타냅니다.
#
# 예를 들어 VIDEOS 테이블이 다음과 같다면
#
# ID	TITLE	RATE	NUM_VIEW	RELEASE_DATE	MPAA_RATE
# 2057	ALADIN	8.0	269634	Wed Mar 09 2011 00:00:00 GMT+0000 (UTC)	G
# 3209	ADAM	7.2	29981	Wed Mar 09 2011 00:00:00 GMT+0000 (UTC)	PG-13
# 6206	Chicken Run	7.0	143897	Wed Mar 09 2011 00:00:00 GMT+0000 (UTC)	G
# 평균 평점은 ( 8.0 + 7.2 + 7.0 ) / 3 = 7.399999999 입니다.
# 이를 반올림하여 소숫점 2번째 자리까지만 나타내면 8.40 입니다. 따라서 SQL 문을 실행하면 다음과 같이 출력되어야 합니다.
#
# average
# 8.40

SELECT ROUND(AVG(RATE),2) FROM VIDEOS;
