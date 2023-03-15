# baekjoon_result_crawler

## 백준문제 채점 확인기 version 1

- Python Version: 3.10
- requirement: pandas, selenium
- 작동 환경에 맞는 chrome driver 설정필요(my_code)

### 작동방식

- my_code.py: 교육생이름,백준id를 dictionary 형태로 저장, 웹크롤러 작동
- main.py: 백준문제 번호를 입력하여 get_submissions 함수실행

- output:
   - Dataframe 형태의 id, 이름, correct 유무
 
 ![SE-db63e5e7-c0e4-454e-8021-c20664965655](https://user-images.githubusercontent.com/39439424/225235407-3f916b74-5b4b-4823-ba17-62bbed1c991d.png)

### 업데이트 가능한 것

1. 문제 맞은사람 or 틀린사람의 막대그래프
2. 정답 공개 전에 맞은 사람, 틀린사람 결과 조회
