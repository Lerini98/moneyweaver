# 🪙Moneyweaver

## 👥 팀 소개
### 팀원 소개
<table align="center">
  <tbody>
    <tr>
      <td align="center">
        <div>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeZKGzFP52YC9g4upvuMU9ZGkQiRdLe2rfXQ&s"width="100px;"height="100px;" alt=""/>
           <a href="https://github.com/Lerini98"><div align=center>팀장 유혜린</div></a>
        </div>
      </td>
      <td align="center">
        <div>
          <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA2MjhfODIg%2FMDAxNzE5NTYxNDczNTQ2.MDvMxsF7wnMCFYkxnStanI7xnfyvVOBJnyAhs0xslFkg.DvNfxx0e0i93olqlacSDzzBPCvBubCCTV7XnoWHRc1sg.JPEG%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5_%25282%2529.jpg&type=a340"width="100px;"height="100px;" alt=""/>
          <a href="https://github.com/jeehun98"><div align=center>김성은</div></a>
        </div>
      </td>
      <td align="center">
        <div>
          <img src="https://i.pinimg.com/736x/b4/76/c0/b476c001bb7d3b263fff8b6096f7a1a4.jpg"width="100px;"height="100px;" alt=""/>
          <a href="https://github.com/5-lee"><div align=center>구나연</div></a>
        </div>
      </td>
      <td align="center">
        <div>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY0XvhV7-uFsKFuBcBMeOGP8ytfDyEZkJnGw&s"width="100px;height="100px;" alt=""/>
            <a href="https://github.com/{깃헙주소}"><div align=center>송명신</div></a>
        </div>
      </td>
    </tr>
  </tbody>
</table>

<br><br>
### 팀원별 역할 소개
| 유혜린👑 | 김성은님 | 구나연님 | 송명신님 |
|:----------:|:----------:|:----------:|:----------:|
|데이터베이스 관리, AWS 기반 인프라 구축 및 관리, 배포 및 모니터링|데이터 수집, 전처리, 통합, 데이터베이스 관리, 전체 아키텍처 설정|사용자 인터페이스 개발, 주식 데이터 시각화 구현, readme작성|사용자 인터페이스 개발, 게시판 서비스 구현| 
<br><br>
## 📍프로젝트 소개
### 프로젝트 명 
<b>💰Stock Trading Program💰</b>
### 프로젝트 소개 
본 프로젝트는 실시간 주식 데이터를 분석하고, 실시간 뉴스 기사를 기반해 주식 거래를 자동화하는 주식 트레이딩 프로그램입니다. 
우리가 개발할 트레이딩 프로그램은 단순히 주식 데이터를 수집하고 분석하는 것을 넘어, 실시간으로 변화하는 시장 상황에 맞춰 자동으로 거래를 실행하는 것을 목표로 합니다.
### 프로젝트 내용 
#### 프로젝트 도메인
저희 프로젝트의 최종 목표는 RSI(Relative Strength Index)를 활용하여 주식 자동매매 프로그램을 개발하는 것입니다. 이를 위해 다음과 같은 기본 도메인 개념을 설명하겠습니다.<br>
- **RSI** : 식의 과매수 또는 과매도 상태를 판단하기 위한 기술적 지표로, 특정 기간 동안의 평균 상승과 하락 폭을 비교하여 주식의 가격 추세를 분석합니다.
    - RSI 70이상 : 과매수 상태로 가격이 지나치게 상승했음
    - RSI 30이하 : 과매도 상태로 가격이 지나치게 하락
- **RSI 다이버전스** : RSI 다이버전스는 RSI 보조 지표와 주가가 서로 반대 방향으로 움직이는 현상
    - ex: 주가가 상승하는데 보조 지표는 하락하거나 주가가 하락하는데 보조 지표는 상승하는 현상

- **매수 및 매도 매커니즘** <br>
  1. 📈상승을 암시하는 다이버전스
      - **첫 번째 꼭짓점 설정** : RSI가 충분히 낮아진 지점을 첫 번째 꼭짓점으로 설정
      - **두 번째 꼭짓점 설정** : 첫 번째 꼭짓점보다 주가가 낮아졌으나 RSI는 높아지면서 반등 기미를 보이는 지점을 두 번째 꼭짓점으로 설정
      - **매수 시점** : 두 번째 꼭짓점이 형성된 후 즉시 매수

  2. 📉하락을 암시하는 다이버전스
      - **첫 번째 꼭짓점 설정** : RSI가 충분히 높아진 지점을 첫 번째 꼭짓점으로 설정
      - **두 번째 꼭짓점 설정** : 첫 번째 꼭짓점보다 주가가 높아졌으나 RSI는 낮아지면서 하락 기미를 보이는 지점을 두 번째 꼭짓점으로 설정
      - **매도 시점** : 두 번째 꼭짓점이 형성된 후 즉시 매도

#### 1st Agile과 도메인
1. **historical_stock_data** 테이블 설명
테이블 이름: **historical_stock_data**
  * **stck_bsop_date**: 거래 일자. 주식 거래가 발생한 날짜를 의미합니다.
  * **company_id**: 회사 ID. 특정 회사를 식별하는 고유 식별자입니다.
  * **stck_clpr**: 종가(Close Price). 하루 거래가 종료될 때의 주가입니다.
  * **stck_oprc**: 시가(Open Price). 거래가 시작될 때의 주가입니다.
  * **stck_hgpr**: 최고가(High Price). 하루 중 가장 높았던 주가입니다.
  * **stck_lwpr**: 최저가(Low Price). 하루 중 가장 낮았던 주가입니다.
  * **acml_vol**: 누적 거래량(Accumulated Volume). 하루 동안 거래된 총 주식 수를 나타냅니다.
  * **acml_tr_pbmn**: 누적 거래 대금(Accumulated Trading Value). 하루 동안 거래된 총 금액입니다.

2. 도메인 연결 및 RSI 매커니즘에서의 역할
RSI 계산에 필요한 데이터

* **stck_clpr (종가)**: RSI 계산의 기본이 되는 데이터입니다. 일정 기간 동안의 종가 변동을 바탕으로 RSI가 계산됩니다. 종가를 이용해 주가의 상승/하락의 강도를 계산한 뒤, 이를 평균으로 계산하여 RSI를 도출합니다.
    - **모델 학습**
    위에서 수집한 일간 주가와 계산한 RSI를 사용하여 모델을 학습시킵니다. 이 모델은 다음 날의 주가와 RSI를 예측하는 데 사용됩니다.

    - **다이버전스 포착**
    예측한 주가와 RSI 사이의 다이버전스를 분석합니다. 예를 들어, 주가가 하락할 것으로 예측되지만 RSI가 상승할 것으로 예측된다면, 이는 매수 신호로 해석합니다.

    - **매매 실행**
    다음 날 아침 9시 장이 열리는 시점에 매매가 이루어집니다. 자동매매 프로그램은 키움증권의 API와 연동되어 있어 신호에 따라 자동으로 매매를 실행합니다.


#### 프로젝트 목표 
- **실시간 주식 데이터 분석 및 자동화된 거래 시스템 구축** : 실시간으로 변동하는 주식 데이터를 수집하고 분석하여, 사용자가 설정한 트레이딩 전략에 따라 자동으로 매수, 매도를 실행할 수 있는 시스템을 개발합니다.
- **뉴스 기반 시장 예측 및 대응** : 실시간 뉴스 기사를 분석하여 시장에 영향을 미칠 수 있는 중요한 이벤트를 감지하고, 이를 기반으로 주식 거래 전략을 자동으로 조정하여 시장 변화에 빠르게 대응 시스템 개발합니다.

## 📍Agile Readme 


<details>
  <summary><h3 style="display: inline;">1nd Agile</h3></summary>
  <a href="https://www.google.com">🔗🔗</a>

</details>








<br><br><br>
