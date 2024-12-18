# 📒 3rd Agile 소개
## 📍3rd Agile 배경과 목표
### 📌 3rd Agile 진행 개요
이번 3차 애자일은 웹 페이지의 개선 사항과 주식 예측 모델 성능 향상을 목표로 진행되었습니다.
<br>
### 📌 주요 개선 사항
#### 웹 페이지 개선
1. **게시판 로그인 기능 제거** : 사용자의 편의성을 고려하여 불필요한 로그인 기능을 제거하고, 더 간편한 접근 방식을 도입하였습니다.
2. **주식 예측 모델 최적화** : 주식 예측 모델을 적용한 후 데이터 로딩 시간이 지나치게 길어지는 문제를 해결하기 위해, 모델 결과값을 저장하고 추가되는 데이터만을 순차적으로 로드하는 방식으로 성능을 최적화했습니다. 

#### DevOps 및 CI/CD 구축
- GitHub에 커밋할 때마다 자동으로 수정 사항이 적용되는 CI/CD 파이프라인을 구축하여 개발과 배포 과정을 자동화하였습니다.

#### 모델 성능 향상
1. **뉴스 감정분석** : 3차 애자일에서는 네이버 뉴스 API를 활용해 실시간 뉴스 데이터를 수집하고, BERT 모델로 감정 분석을 진행했습니다. 이를 통해 주식 시장 관련 뉴스의 감성 분석을 바탕으로 주식 상승/하락 예측 모델의 정확성을 높였으며, 투자자에게 실시간으로 신뢰성 있는 예측 정보를 제공할 수 있었습니다. BERT 모델을 활용해 뉴스 제목과 본문에서 긍정적, 부정적, 중립적 감정을 구분하고 이를 투자 전략에 반영했습니다.
   
3. **LSTM 개선 및 BERT모델과 병합** : LSTM 모델을 개선하기 위해 주가의 변동 패턴을 더 정교하게 분석할 수 있도록 window size를 조정하여 모델이 더 넓은 범위의 데이터를 학습하도록 했습니다. 또한, 주가에 영향을 미칠 수 있는 다양한 외부 지표들, 예를 들어 거래량, 경제 지표, 관련 산업 동향 등의 데이터를 추가 컬럼으로 포함시켜 모델의 예측력을 강화하였습니다. 이와 함께, 개선된 LSTM 모델과 BERT 모델을 결합하여 두 모델의 강점을 최대화하고, 주식 예측의 정확성을 더욱 높였습니다.

## 📍3rd 요구사항

<img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD.png?raw=true" alt="요구사항" width="600">

## 📍Architecture
<details>
   <summary>
      <h3 style="display: inline;">📌 AI </h3>
   </summary>
   <h4>LSTM Model Architecture</h4>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/final_toy_LSTM_model.png?raw=true" alt="요구사항" width="600">
   <h4>Combined Model Architecture</h4>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/combined.png?raw=true" alt="요구사항" width="600">
</details>
<details>
   <summary>
      <h3 style="display: inline;">📌 AWS : CICD </h3>
   </summary>
   <h4>LSTM Model Architecture</h4>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/cicd.png?raw=true" alt="요구사항" width="600">
  
</details>
<details>
   <summary>
      <h3 style="display: inline;">📌 전체 </h3>
   </summary>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%A0%84%EC%B2%B4%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png?raw=true" alt="요구사항" width="600">
  
  
  
</details>

## 📍사이트 맵
<img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%82%AC%EC%9D%B4%ED%8A%B8%EB%A7%B5.png?raw=true" alt="요구사항" width="600">

## 📍Last Agile 까지 개발로그
<details>
    <summary><h3 style="display: inline;">Front / Back</h3>
    </summary>
    <h4>🔗 Web Framework : Django</h4>
    <p><span>Django 프레임워크 사용이유 </span> : 우리 프로젝트의 웹 서비스는 Django라는 풀스택 웹 프레임워크를 이용하여 개발되었습니다. Django를 이용한 이유는 팀원모두 웹 개발 경험이 아직 부족했기 때문에 다른 라이브러리를 사용하기 보다는 수업시간에 배운 Django를 이용하는 것이 개발 과정에서 효율적이고 빠르게 작업을 진행할 수 있을 것이라고 판단하였기 때문입니다.</p>
    <h4>🔗 각 Django 앱의 기능</h4>
    <li><strong>moneyweaver </strong>앱 : 메인화면과 소개페이지를 제공하는 기능이 있습니다. 따로 데이터베이스와 ai기능이 들어간 것은 아니지만 우리 프로젝트의 주요 서비스를 소개하는 등 moneyweaver의 정체성을 파악할 수 있는 기능을 합니다.</li>
    <br>
    <li><strong>Chart </strong>앱 : 우리 프로젝트의 데이터베이스와 또 우리 데이터를 이용하여 Ai 모델을 연동하여 사용자에게 우리가 개발한 ai모델이 예측한 주가와 실제 주가를 동시에 제공하여 사용자에게 제공하여 사용자가 보다 주식을 투자하는데 더 나은 결정을 하도록 돕습니다.</li>
    <br>
    <li><strong>user </strong>앱 : 우리 웹서비스를 이용하는 사용자들이 자유롭게 주식에 관한 정보를 서로 공유하고 이야기를 할 수 있도록 게시판 서비스를 제공하는 앱입니다. 사용자들이 작성한 글들은 우리 moneyweaver의 데이터베이스에 저장되고 이를 연동하여 화면에 띄움으로서 우리 서비스를 이용하는 모든 사용자들이 게시판에 작성된 모든 글의 목록을 조회할 수 있습니다.</li>
    <h4>🔗 template 부분 : Chart.js이용</h4>
    <p>Django의 views 파일에서 데이터베이스에서 필요한 데이터를 가져와 JSON 형태로 변환한 뒤, render 함수를 통해 HTML 템플릿에 전달하고, HTML에서는 Chart.js 라이브러리를 script로 불러와 JSON 데이터를 x축과 y축에 지정하여 그래프를 생성합니다.</p>
    <h4>🔗 Database 부분 : aws rds이용</h4>
    <p>프로젝트의 데이터베이스는 AWS RDS(Amazon Relational Database Service)를 사용해 구축했습니다. RDS는 관리형 데이터베이스 서비스로, MySQL, PostgreSQL 등 다양한 엔진을 지원하며 자동 백업, 보안 업데이트, 장애 복구 기능을 제공해 안정성이 뛰어납니다. 이를 통해 데이터베이스 운영과 유지보수에 소요되는 시간을 절약하고, 확장성과 성능을 확보할 수 있었습니다.</p>
   

   
</details>
<br>
<details>
    <summary><h3 style="display: inline;">DevOps</h3></summary>
    <h4>🔗 Cloud Service : AWS</h4>
    <p>프로젝트 배포는 AWS의 CI/CD 서비스를 이용해 자동화했습니다. 코드가 GitHub에 푸시되면 AWS CodePipeline이 변경 사항을 감지하고, CodeBuild를 통해 빌드 및 테스트를 수행한 후, CodeDeploy로 배포하는 방식입니다. 이를 통해 코드 변경이 있을 때마다 자동으로 애플리케이션이 배포되며, AWS CloudWatch를 통해 배포 후 성능과 오류를 모니터링해 안정성을 유지했습니다.</p>
    
</details>
<br>
<details>
    <summary><h3 style="display: inline;">Data</h3>
    </summary>
    <h4>🔗 주식 데이터 : Finance DataReader</h4>
    <p>주식, 채권, 환율, 경제 지표 등 다양한 금융 데이터를 손쉽게 수집할 수 있는 Python 라이브러리입니다. 주식 데이터를 분석하는 데 유용한 도구로, 다양한 금융 기관에서 제공하는 데이터를 간편하게 받아올 수 있습니다. 또한, 이 라이브러리는 매일매일 업데이트되는 주식 데이터를 제공하기 때문에, 실시간으로 주가 변동을 추적하고 차트를 동기화하는 작업이 용이합니다. 이 덕분에 주식 차트를 동적으로 업데이트하거나 주식 분석을 실시간으로 반영하는 데 매우 효율적으로 활용할 수 있습니다.</p>
    <h4>🔗 여러 기술적 지표 : pandas_ta </h4>
    <p>주가 데이터를 분석하기 위해 여러 기술적 지표를 pandas_ta 라이브러리를 사용하여 추가하였습니다. 적용된 지표로는 단순 이동 평균(SMA), 상대 강도 지수(RSI), 지수 이동 평균(EMA), 볼린저 밴드, ADX, MACD, 스토캐스틱 오실레이터, ATR, CCI 등이 있으며, 이를 통해 주가의 추세, 변동성, 과매수/과매도 여부 등을 분석하였습니다. 또한, 금, 유가, 환율 등의 경제 지표도 모델의 입력 데이터로 활용되었습니다. </p>
    <h4>🔗 네이버 뉴스 api </h4>
    <p>네이버 뉴스 api는 특정 키워드나 주제에 대한 최신 뉴스 기사들을 쉽게 불러올 수 있어, 주식 관련 뉴스나 경제 뉴스를 실시간으로 추적하는 데 유용합니다. 수집된 뉴스 데이터는 감정 분석 모델을 통해 긍/부정/중립 으로 분류되어 주가에 미칠 영향을 평가하는 데 이용하였습니다. </p>

    
</details>
<br>
<details>
    <summary><h3 style="display: inline;">AI</h3>
    </summary>
    <h4>🔗 LSTM </h4>
    <li><strong>시계열 데이터셋</strong> : 우리 프로젝트에서는 주가 예측을 위해 시계열 데이터셋을 생성하는데 window_size를 적용하는 방법을 사용하였습니다. 주어진 window_size 동안의 과거 데이터를 <strong>특징(feature)</strong>으로 사용하고, 이후의 데이터를 <strong>타겟(target)</strong>으로 설정하여 훈련 및 테스트 데이터셋을 구성하였습니다. 이를 위해 Sliding Window 방식을 적용하여 window_size에 맞게 일정 기간의 데이터를 슬라이딩하면서 추출하고, 이를 LSTM 모델의 입력 데이터로 변환하여 과거 주가 패턴을 학습하게 했습니다.</li>
    <br>
    <li><strong>성능 향상 방법 </strong>: Dropout 기법을 사용하여 LSTM 레이어와 Fully Connected 레이어 사이에 Dropout 레이어를 추가, 과적합을 방지하고 모델의 일반화 능력을 향상시켰습니다. 또한, ReLU 활성화 함수를 사용하여 비선형성을 추가하고 모델이 더 복잡한 패턴을 학습할 수 있도록 하였습니다.  </li>
    <h4>🔗 BERT : 뉴스 감정 분석</h4>
    <p>우리는 <strong>BERT</strong>모델을 활용하여 뉴스 데이터를 입력으로 받아 감성 분석을 수행하고, 그 결과를 주가 예측 모델에 반영하였습니다. 구체적으로 이미 사전 학습된 klue/bert-base 모델을 활용하여 한국어 뉴스 텍스트를 분석하고 분석 결과로 나온 긍부정 결과를 주가예측 지표로 활용하였습니다.</p>
    <h4>🔗 Combined Model : LSTM + BERT</h4>
    <p>우리는 LSTM과 BERT 모델을 결합하여 LSTM모델 결과에 뉴스 긍부정결과 까지 추가하였습니다. 이 두 모델의 출력값을 결합 한 후, <strong>fully connected layer</strong>를 통해 최종 예측값을 도출하였습니다. FC 레이어는 두 정보를 통합하여 주가 예측에 필요한 최종 결정을 내리는 역할을 합니다. 따라서 모델을 결합함으로서 과거 주가 패턴과 최신 뉴스 감성을 모두 고려하여 보다 정확한 예측을 가능하게 하였습니다.</p>
    
</details>

## 📍각 Agile 별 결과
<details>
    <summary>
        <h3 style="display: inline;">🔗 1st Agile</h3>   
    </summary>
    <p><b>📌 메인화면</b></p> 
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/image-1.png?raw=true" alt="요구사항" width="600">
    <br><br>
    <p><b>📌 인덱스 페이지 : Show Chart!를 누르면 각 회사의 주가를 확인할 수 있는 페이지로 연결되도록 </b></p> 
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/image-3.png?raw=true" alt="요구사항" width="600">
    <br><br>
    <p><b>📌 차트 페이지 : 회사별 주가를 확인할 수 있음 </b></p> 
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/image-4.png?raw=true" alt="요구사항" width="600">
    
</details>
<details>
    <summary>
        <h3 style="display: inline;">🔗 2nd Agile</h3>
    </summary>
    <p><b>📌 인덱스 페이지 수정 :</b> 1차 애자일에서 만든 인덱스 페이지가 각 페이지 별로 이동하기 불편한 단점이 있었고 조금 더 편리하게 이동할 수 있도록 사이드 네비바 추가, 또한 우리 인공지능 모델의 성능 지표와 회사별 정보 제공도 추가</p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/2%EC%B0%A8%20%EC%9D%B8%EB%8D%B1%EC%8A%A4%20%ED%8E%98%EC%9D%B4%EC%A7%80.png?raw=true" alt="요구사항" width="600">
   <br>
   <p><b>📌 차트 페이지 css적용 :</b> 예측 모델까지 연동하여 예상 주가도 사용자 화면에 구현하였음</p>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/2%EC%B0%A8%20%EC%B0%A8%ED%8A%B8%20%ED%8E%98%EC%9D%B4%EC%A7%80.png?raw=true" alt="요구사항" width="600">

   <br>
   <p><b>📌 게시판 서비스 생성 </b></p>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/2%EC%B0%A8%20%EA%B2%8C%EC%8B%9C%ED%8C%90.png?raw=true" alt="요구사항" width="600">
   <br>
   <p><b>📌 모델 성능 지표 </b></p>
   <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/2%EC%B0%A8%20%EB%AA%A8%EB%8D%B8%20%EC%84%B1%EB%8A%A5.png?raw=true" alt="요구사항" width="600">
   <br>
</details>
<details>
    <summary>
        <h3 style="display: inline;">🔗 3rd Agile </h3>
    </summary>
    <p><b>📌 홈 화면 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%EB%A9%94%EC%9D%B8.png?raw=true" alt="메인" width="600">
    <p><b>📌 소개 페이지 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%EC%86%8C%EA%B0%9C.png?raw=true" alt="소개" width="600">
    <p><b>📌 팝업창! </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%ED%8C%9D%EC%97%85.png?raw=true" alt="팝업" width="600">
    <p><b>📌 차트 인덱스 페이지 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%EC%B0%A8%ED%8A%B8%20%EC%9D%B8%EB%8D%B1%EC%8A%A4.png?raw=true" alt="팝업" width="600">
    <p><b>📌 예측 주식 차트와 내일 주가 상승 하락 예측 정보 제공 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%EA%B7%B8%EB%9E%98%ED%94%84.png?raw=true" alt="차트" width="600">
    <p><b>📌 익명 게시판 </b>: 로그인 기능을 삭제함으로서 누구든지 와서 글을 작성하고 수정할 수 있다</p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/3%EC%B0%A8%20%EA%B2%8C%EC%8B%9C%ED%8C%90.png?raw=true" alt="게시판" width="600">
    <p><b>📌 ai - 단순주기 강화모델 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EB%8B%A8%EC%88%9C%EC%A3%BC%EA%B8%B0%EA%B0%95%ED%99%94%EB%AA%A8%EB%8D%B8.png?raw=true" alt="ai" width="600">
    <p><b>📌 ai - 성능지표자료1 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%84%B1%EB%8A%A5%EC%A7%80%ED%91%9C%EC%9E%90%EB%A3%8C1.png?raw=true" alt="ai" width="600">
    <p><b>📌 ai - 실제와 예측 그래프, 주기강화모델 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%8B%A4%EC%A0%9C%EC%99%80%EC%98%88%EC%B8%A1%EA%B7%B8%EB%9E%98%ED%94%84-%EC%A3%BC%EA%B8%B0%EA%B0%95%ED%99%94%EB%AA%A8%EB%8D%B8.png?raw=true" alt="ai" width="600">
    <p><b>📌 ai - 실제와 예측 그래프비교 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%8B%A4%EC%A0%9C%EC%99%80%EC%98%88%EC%B8%A1%EA%B7%B8%EB%9E%98%ED%94%84%EB%B9%84%EA%B5%90.png?raw=true" alt="ai" width="600">
    <p><b>📌 ai - 이동평균선 기준정확도 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%9D%B4%EB%8F%99%ED%8F%89%EA%B7%A0%EC%84%A0%EA%B8%B0%EC%A4%80%EC%A0%95%ED%99%95%EB%8F%84.png?raw=true" alt="ai" width="600">
    <p><b>📌 ai - 주기강화모델 </b></p>
    <img src="https://github.com/Lerini98/moneyweaver/blob/main/img/%EC%A3%BC%EA%B8%B0%EA%B0%95%ED%99%94%EB%AA%A8%EB%8D%B8.png?raw=true" alt="ai" width="600">



</details>

## 📍 이번 프로젝트를 통해 느낀점
<details>
   <summary>
      <h3 style="display: inline;">👑혜린</h3>
   </summary>
   <p>여기에 내용을 작성해주세요</p>
</details>
<details>
   <summary>
      <h3 style="display: inline;">성은</h3>
   </summary>
   <p>여기에 내용을 작성해주세요</p>
</details>
<details>
   <summary>
      <h3 style="display: inline;">나연</h3>
   </summary>
   <p>여기에 내용을 작성해주세요</p>
</details>
<details>
   <summary>
      <h3 style="display: inline;">명신</h3>
   </summary>
   <p>여기에 내용을 작성해주세요</p>
</details>

## ➕ 추가
### <a href="https://github.com/Lerini98/moneyweaver/blob/main/readme/ai_result_by.seongeun.md">❗AI 상세❗</a>
주가 예측에 사용되는 여러 경제 지표와 기술적 지표에 관한 설명, 그리고 이러한 지표들이 주가 예측에 미치는 영향과 AI 학습에 어떻게 적용되는지에 대한 내용이 담겨 있습니다. 또한, 교육에서 배운 AI 학습 과정과 이를 활용한 주식 예측 모델링 과정이 상세히 설명되어 있어, 이를 읽으시면 주가 예측과 관련된 깊은 이해와 함께 많은 공부가 될 것입니다.

