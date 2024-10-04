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
### LSTM모델과 django연동
- **모델학습코드 모듈화** : 모델학습을 진행하는 코드가 ipynb로 저장되어 있었는데 이를 데이터 로드함수, 모델 클래스, 예측 함수 세부분으로 구현하여 `model_회사이름.py`형태로 저장하였습니다.
- **view와 연동** : 예측함수에서 실제 주가, 예측 주가, 날짜를 리턴하여 chart앱의 view파일에서 불러왔습니다.
- **html과의 연동** : model에서 불러온 데이터의 타입이 tensor형태라 이를 리스트로 형변환을 해주고 chart.js와 연동을 위해 view에서 json.dumps형태로 리턴해주었습니다.
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
    
- **문제점 5**: 모델 정확성 불ㅇ


## 📍 5. 느낀점

- **혜린** : LSTM 성과지표 결과가 잘 나오지않아 아쉬웠고, AWS는 용량 문제 계속 생겨서 인스턴스 4번 삭제했습니다. URL 관련 문제가 있는데 이건 추후 업데이트 하겠습니다.
  
- **성은** : LSTM 모델 그대로 가져와서 대입해보는 과정에서 성과지표 0.5를 달성하는 것도 상당히 어려웠습니다. 이후 다른 column 적용할 때, 비슷한 현상이 발생할 것으로 생각이 들어서 모델의 최적 파라미터를 찾기위해 ray tune을 적용해서 최적값을 찾는 방법을 진행해보거나, GRU 모델을 적용해서 연산 시간을 최적화 하거나, 내부 RNN 계산 알고리즘을 수정해서 맞춰보는 방식 등 다양한 방법을 고려하고 있습니다. 다음 에자일에선 개선된 모델이 완성될 수 있도록 노력해보겠습니다.

- **나연** : 화면 개발 도중 잘 진행되다가 마지막에 배포과정중 url에 문제가 생겨서 많이 당황했습니다...

- **명신** : 게시판 기능을 구현하는 과정에서 사소한 부분까지 신경 써야 한다는 점을 깨달았습니다. 여러 블로그를 참고하며 django-allauth라는 응용 프로그램을 통해 로그인, 로그아웃, 회원가입 등의 통합 기능을 간편하게 제공받을 수 있다는 사실을 알게 되었습니다. 또한, 게시글마다 고유 번호를 할당하는 과정에서 주소 관리와 관련된 여러 오류를 경험하면서 이제는 주소 설정 문제를 보다 수월하게 처리할 수 있게 되었습니다.


## 📍 참고 문헌

- [S. Hochreiter and J. Schmidhuber, "Long Short-Term Memory," Neural Computation, 1997.](https://www.bioinf.jku.at/publications/older/2604.pdf)
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) - Christopher Olah
- [Pytorch - LSTM 공식 문서](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)
- [pseudo-lab - Tutorial book](https://pseudo-lab.github.io/Tutorial-Book/chapters/time-series/Ch5-CNN-LSTM.html)
- [LSTM State, Gate 설명](https://blog.naver.com/winddori2002/221992543837)


## 📍3rd Agile 주요계획


