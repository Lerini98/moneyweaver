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
- 주식 사이트에서 흔히 볼 수 있는 사용자들 간의 소통 공간을 마련했습니다. 사용자는 회원가입 및 로그인을 통해 글을 작성하고 삭제할 수 있으며, 각 글의 상세 내용을 확인할 수 있습니다.
#### aws 배포부분
직접작성



## 📍 3. 개발 상세

### 설계 개요

#### LSTM Model

- **모델 선택 이유**: LSTM이 순환신경망 중에서도 장기 의존성(Long-Term Dependencies)을 잘 학습하기 때문에 선택
- **입력 변수 선정**: 시가, 고가, 저가, 종가, 변동량과 같은 주요 특징을 포함하여 데이터의 풍부한 정보를 활용
- **목표**: 다음 날의 종가를 예측하여 투자 전략 수립에 활용

</br>

### 데이터 탐색 및 전처리

- **데이터 수집**: Finance Data Reader를 통해 일별 주식 데이터를 수집.
- **데이터 탐색**:
  - 결측치 및 이상치 확인.
  - 데이터의 분포와 트렌드 분석.
- **전처리 방법**:
  - 결측치는 이전 값으로 대체(Fill Forward).
  - Standard 스케일링으로 정규화하여 학습 속도 향상.
  - window size 개념을 도입하여 학습 feature 갯수 증대.

### 모델의 구조
- **입력층**: 시계열 길이 8~20일, 특성 수 5개.
- **LSTM 층**:
  - 첫 번째 LSTM 층: 64 유닛, Dropout 0.4 ~ 0.6 적용.
- **Linear 층**:
  - 첫 번째 Linear 층: 64 유닛, Dropout 0.4 ~ 0.6 적용
- **Dense 층**:
  - 출력층: 1개의 뉴런, 활성화 함수 없음
- **모델 아키텍처**:
> ![09-ToyProject_fifth_model](https://github.com/user-attachments/assets/c89ccf87-8182-48b2-9fab-04cd978f88a6)
> ![LSTM_model_architecture](https://github.com/user-attachments/assets/d180d29c-8ff4-4cc2-9534-4ed999121c4a)

### 구현 세부사항

- **사용된 라이브러리**: Pytorch
- **하이퍼파라미터 설정**:
  - 학습률:
    - optimizer : 0.1
    - scheduler : 0.5/10 steps
  - 배치 크기: 32, 64
  - 에포크 수: 150
- **손실 함수 및 옵티마이저**:
  - 손실 함수: Mean Squared Error(MSE), L1 정규화
  - 옵티마이저: Adam
- **코드 주요 부분**:
  ```python
  class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.dropout1 = nn.Dropout(0.4)
        self.fc1 = nn.Linear(hidden_size, 64)
        self.relu = nn.ReLU()
        self.dropout2 = nn.Dropout(0.4)
        self.fc2 = nn.Linear(64, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.dropout1(out[:, -1, :])
        out = self.fc1(out)
        out = self.relu(out)
        out = self.dropout2(out)
        out = self.fc2(out)
        return out
  ```

## 📍 4. 오류로그

### 문제점과 해결 과정

- **문제점 1**: 머신러닝의 학습 한계
  - **해결**: 패턴 분석에 적합한 딥러닝 모델 채택
    
- **문제점 2**: Feature data의 절대량 부족
  - **해결**: 윈도우 크기를 조정하여 데이터 샘플 수 증가
    
- **문제점 3**: 긴 학습 시간
  - **해결**: GPU 가속 사용 및 배치 크기, model layer 조정
    
- **문제점 4**: 과적합 현상 발생
  - **해결**: Dropout 층 추가 및 Early Stopping 적용
    
- **문제점 5**: 모델 정확성 불충분
  - **해결**: model layer, dropout, batch size, window size 조정
    
- **문제점 6**: 모델 학습 속도 저하
  - **해결**: 기존 LSTM의 활성함수인 tanh 대신 ReLU를 사용
    
- **문제점 7**: LSTM의 연산 결과 데이터 값의 부적절성
  - **해결**: LSTM 연산 이후 Linear 과정으로 넘길 때, outputs내의 데이터 선택 오류 수정
    
- **문제점 8**: LSTM 모델의 특성 과적합 발생
  - **해결**: LSTM의 layer 수를 줄이고 dropout을 0.4미만으로 내리지 않음
    
- **문제점 9**: 단순 데이터 셋으로 인해 제한적인 성능
  - **향후 방향**: 뉴스 키워드 인식 및 원본 데이터에서 제한한 데이터 column 추가할 예정

- **문제점 10**: 게시글을 참조하거나 삭제할 때 해당 게시글의 주소로 이동하지 않는 오류
  - **해결**: URL 패턴에서 게시글의 고유 식별자인 `pk` 값을 `int:pk`로 매핑한 후, 뷰 함수에서 이 `pk`를 사용하여 데이터베이스에서 해당 게시글을 검색하도록 설정


</br>


## 📍 5. AI 결과


### 모델 학습 과정

- **데이터 분할**: 훈련 70%, 검증 15%, 테스트 15%
- **학습 과정**:
  - Early Stopping 적용으로 과적합 방지
  - 모델 체크포인트 저장으로 최적 모델 보관

### 모델 결과
- **예측 곡선**:
> ![first_model_graph](https://github.com/user-attachments/assets/a150d161-2539-4260-91b3-ba73c0f1c71d)

- **Confusion Matrics**
> ![model_performance](https://github.com/user-attachments/assets/a0252b17-40e8-45e8-999d-21a8519abd3c)

- **평가지표**:
  - Accuracy: 0.5193
  - Precision: 0.5166
  - Recall: 0.5120
  - F1-score: 0.5143

- **분석**:
  - LSTM 모델이 단기 추세를 효과적으로 예측, Linear 모델이 장기 추세를 효과적으로 예측함.
  - 주식 데이터 자체의 변동성이 큰 구간에서 모델의 오차 증가.
  - 팬데믹, 금융이슈 등 사회적인 부문의 급격한 변화를 예측하기 어려움.
  - LSTM model의 과적합 = 그래프 추적 민감도 상승 but, 예측 정확도 하락
  - Linear model의 과적합 = 예측 정확도 적정량 상승 but, 상승/하락 예측 편향적 분석 결과 발생


## 📍 6. 프로젝트 결과 
#### 메인화면
> ![image](https://github.com/user-attachments/assets/dbfd1a66-f4b0-4d43-8e03-145719402821)


#### 차트 화면
1. 인덱스 페이지 : 모델 결과, 점수 그리고 조사한 기업의 정보를 사용자에게 제공
> ![image](https://github.com/user-attachments/assets/c2f59b29-dfdd-4e48-9a23-39a26764f214)
2. 주가 예측 페이지 : 2022년 1월 3일부터 실제 주가와 예측 주가를 사용자에게 제공
- 과거 주식 차트
> ![image](https://github.com/user-attachments/assets/4051f712-bf42-4547-bf92-f0d8ff796db3)
- 실제 주가와 예측 주가 비교
> ![image](https://github.com/user-attachments/assets/78ded884-a888-4fb8-8cbd-4486a9043f5d)


#### 게시판 
1. 게시판 메인 화면 : 게시글 목록을 볼 수 있음
> ![image](https://github.com/user-attachments/assets/62679c97-c8c4-4534-990a-022cb7935759)
2. 글쓰기
> ![image](https://github.com/user-attachments/assets/413546bb-8381-4154-b126-d39b4c7d4fec)
3. 게시글 등록
> ![image](https://github.com/user-attachments/assets/bf8eb384-c029-4568-8116-e72e96a77b1d)








<br><br><br>


## 📍느낀점
- **혜린** : 
직접작성

- **성은** : LSTM 모델 그대로 가져와서 대입해보는 과정에서 성과지표 0.5를 달성하는 것도 상당히 어려웠습니다. 이후 다른 column 적용할 때, 비슷한 현상이 발생할 것으로 생각이 들어서 모델의 최적 파라미터를 찾기위해 ray tune을 적용해서 최적값을 찾는 방법을 진행해보거나, GRU 모델을 적용해서 연산 시간을 최적화 하거나, 내부 RNN 계산 알고리즘을 수정해서 맞춰보는 방식 등 다양한 방법을 고려하고 있습니다. 다음 에자일에선 개선된 모델이 완성될 수 있도록 노력해보겠습니다.

- **나연**

- **명신** : 게시판 기능을 구현하는 과정에서 사소한 부분까지 신경 써야 한다는 점을 깨달았습니다. 여러 블로그를 참고하며 django-allauth라는 응용 프로그램을 통해 로그인, 로그아웃, 회원가입 등의 통합 기능을 간편하게 제공받을 수 있다는 사실을 알게 되었습니다. 또한, 게시글마다 고유 번호를 할당하는 과정에서 주소 관리와 관련된 여러 오류를 경험하면서 이제는 주소 설정 문제를 보다 수월하게 처리할 수 있게 되었습니다.


## 📍 참고 문헌

- [S. Hochreiter and J. Schmidhuber, "Long Short-Term Memory," Neural Computation, 1997.](https://www.bioinf.jku.at/publications/older/2604.pdf)
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) - Christopher Olah
- [Pytorch - LSTM 공식 문서](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)
- [pseudo-lab - Tutorial book](https://pseudo-lab.github.io/Tutorial-Book/chapters/time-series/Ch5-CNN-LSTM.html)
- [LSTM State, Gate 설명](https://blog.naver.com/winddori2002/221992543837)


## 📍3rd Agile 주요계획


