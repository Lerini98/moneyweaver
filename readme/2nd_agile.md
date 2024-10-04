



# 📒 2nd Agile 소개
## 📍 1. 2nd Agile 배경과 목표
### 2nd Agile 진행 배경
1st Agile 이후 머신러닝 모델로 주식 예측을 시도했지만 만족스러운 결과를 얻지 못했습니다. 시계열 데이터에 강점이 있는 LSTM 모델을 적용하여 예측 성능을 향상시키고자 합니다.
<br><br><br>


### 2nd Agile 목표 : 머신러닝과 딥러닝을 이용하여 미래 주식 종가 예측모델 만들기
LSTM을 활용한 주식 가격 예측 모델 개발과 웹페이지 업데이트를 2차 에자일 목표로 삼았습니다. 시계열 데이터를 효과적으로 학습하여 주가 예측의 정확도를 0.5보다 높이는 것을 목표로 합니다.
<br><br><br>


### 팀원별 역할 소개
| 유혜린👑 | 김성은님 | 구나연님 | 송명신님 | 
|:----------:|:----------:|:----------:|:----------:|
|데이터베이스 관리, AWS 기반 인프라 구축 및 관리, 배포 및 모니터링|데이터 수집, 전처리, 통합, 데이터베이스 관리, 전체 아키텍처 설정|사용자 인터페이스 개발, 주식 데이터 시각화 구현, readme작성|프로젝트 도메인 조사|
<br><br><br>


## 📍 3. 기술 영역
| Data Modeling | DB | Front-End |   Back-End   | Deployment | AI
|------------|--------|-------------|------------|----------|----------|
| ![BeautifulSoup](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![OpenApi](https://img.shields.io/badge/Docs-OpenAPI%203.0-success?style=flat-square) ![requests](https://img.shields.io/badge/requests-3776AB?style=for-the-badge&logo=python&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white) | ![html](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white) ![css](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white) ![JavaScript](https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=black) | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)|![aws](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)|![aws](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

<br><br><br>
## 📍 2. 개발 개요
#### 데이터 탐색 및 전처리
- **데이터 수집**: Finance Data Reader를 통해 일별 주식 데이터를 수집.
- **데이터 탐색**:
  - 결측치 및 이상치 확인.
  - 데이터의 분포와 트렌드 분석.
- **전처리 방법**:
  - 결측치는 이전 값으로 대체(Fill Forward).
  - Standard 스케일링으로 정규화하여 학습 속도 향상.
  - window size 개념을 도입하여 학습 feature 갯수 증대.

#### AI 모델부분
- **모델 선택 이유**: LSTM이 순환신경망 중에서도 장기 의존성(Long-Term Dependencies)을 잘 학습하기 때문에 선택
- **입력 변수 선정**: 시가, 고가, 저가, 종가, 변동량과 같은 주요 특징을 포함하여 데이터의 풍부한 정보를 활용
- **목표**: 다음 날의 종가를 예측하여 투자 전략 수립에 활용

</br>

#### 사용자화면과 모델연동
- **chart-index page (서브페이지)** : 1차 애자일에서 구현했던 차트 인덱스 페이지가 가독성이 떨어진다는 아쉬움이 느껴져서 UI를 수정하였습니다. 또한 저희가 주식데이터에 적용한 LSTM의 성능을 나타내고 주요회사정보를 나타내었습니다.
- **주식 예측 화면** : 저희가 주식데이터에 적용한 LSTM 모델을 저장하고 해당 회사페이지마다 각각 적용하여 예측차트까지 구현하였습니다.

#### 게시판 화면
직접작성
#### aws 배포부분
직접작성



## 📍 3. 개발 상세 및 오류로그






## 📍 4. Architecture
모델의 구조를 상세히 설명하고 각 구성 요소의 역할을 명확히 합니다.

- **입력층**: 시계열 길이 8~20일, 특성 수 5개.
- **LSTM 층**:
  - 첫 번째 LSTM 층: 64 유닛, Dropout 0.4 ~ 0.6 적용.
- **Linear 층**:
  - 첫 번째 Linear 층: 64 유닛, Dropout 0.4 ~ 0.6 적용
- **Dense 층**:
  - 출력층: 1개의 뉴런, 활성화 함수 없음
- **모델 시각화**:
  
  ![모델 아키텍처](./pictures/09-ToyProject_fifth_model.png)
  ![모델 아키텍처](./pictures/LSTM_model_architecture.png)
<br><br><br>




## 📍 7. 프로젝트 결과 
#### 메인화면
![alt text](image-1.png)

#### 차트 화면
![alt text](image-5.png)

#### 게시판 
![alt text](image-4.png)






<br><br><br>


## 📍느낀점
- **혜린** : 
직접작성

- **성은**

- **나연**

- **명신**

## 📍9. 3rd Agile 주요계획


