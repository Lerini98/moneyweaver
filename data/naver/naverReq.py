import requests
from bs4 import BeautifulSoup as bs
import time
import os
import pandas as pd
import re




def crawling(ticker, date):
    for j in range(1,51):
        try:
            # 사이트 접속
            custom_header = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "referer": "https://finance.naver.com/"
            }
            url = "https://finance.naver.com/item/sise_time.naver?code={ticker}&thistime={date}&page={j}".format(ticker = ticker, date = date, j=j)
            response = requests.get(url, headers=custom_header)
            response.raise_for_status()
            # time.sleep(0.2)
        except:
            return makeDf(lst, soup, ticker, date)
        # 텍스트 추출
        response.text

        # html로 파싱//
        soup = bs(response.text, "html.parser")

        # 마지막 페이지 찾기
        find_page = soup.findAll("a") 
        href = []
        for link in find_page:
            href = link.attrs['href']
        last_page = href[-2:]

        # 반복문 빠져나가기
        if int(last_page) < j :
            return makeDf(lst, soup, ticker, date)

        # if not column:
        #    th_list = soup.find_all("th")
        #    for i in range(7):
        #        column.append(th_list[i].get_text())
        #    lst.append(column)

        td_list = soup.find_all("td") # 통괄
        # span_list = soup.find_all("span", class_="tah p10 gray03") #채결 시각
        # span1_list = soup.find_all("span", class_="tah p11") # 채결가, 매도, 매수, 거래량, 변동량
        # span2_list = soup.find_all("span", class_="tah p11 nv01") # 전일비


        for i in range(5):
            try:
                contents = []
                contents.append(td_list[7*i+1].text) # 채결 시각
                contents.append(td_list[7*i+2].text) #채결가
                contents.append(re.findall(r'\d?,?\d+', td_list[7*i+3].text)[0]) # 전일비
                contents.append(td_list[7*i+4].text) # 매도호가
                contents.append(td_list[7*i+5].text) # 매수호가
                contents.append(td_list[7*i+6].text) # 거래량
                contents.append(td_list[7*i+7].text) # 변동량
                lst.append(contents)
            except:
                return makeDf(lst, soup, ticker, date)
            
        for i in range(5):
            try:
                contents = []
                contents.append(td_list[7*i+39].text) # 채결 시각
                contents.append(td_list[7*i+40].text) #채결가
                contents.append(re.findall(r'\d?,?\d+', td_list[7*i+41].text)[0]) # 전일비
                contents.append(td_list[7*i+42].text) # 매도호가
                contents.append(td_list[7*i+43].text) # 매수호가
                contents.append(td_list[7*i+44].text) # 거래량
                contents.append(td_list[7*i+45].text) # 변동량
                lst.append(contents)
            except:
                return makeDf(lst, soup, ticker, date)
            
def makeDf(lst, soup, ticker, date):
    df = pd.DataFrame(lst)
    try:
        th_list = soup.find_all("th")
        column = []
        for i in range(len(th_list)):
            column.append(th_list[i].text)
        df.columns=column
        return saveDf(df, ticker, date)
    except :
        return saveDf(df, ticker, date)


# 추출 데이터 csv 저장
def saveDf(df, ticker, date):
    try:
        df.to_csv('./csvsource/{ticker}/{date}.csv'.format(ticker=ticker, date=date), index=False, encoding='utf-8-sig')
    except:
        try:
            os.mkdir('csvsource')
            os.mkdir('csvsource/{ticker}'.format(ticker = ticker))
            df.to_csv('./csvsource/{ticker}/{date}.csv'.format(ticker=ticker, date=date), index=False, encoding='utf-8-sig')
        except:
            os.mkdir('csvsource/{ticker}'.format(ticker = ticker))
            df.to_csv('./csvsource/{ticker}/{date}.csv'.format(ticker=ticker, date=date), index=False, encoding='utf-8-sig')


# 기존 하드웨어를 가지고 SI, AI에 투자하는 기업 (다소 SI에 편향되어 있는 기업도 있음)
    # 006400 삼성 SDI
    # 018260 삼성 SDS <- 미라콤아이앤씨의 모회사
    # 022100 포스코 DX
    # 003550 LG <- LG CNS로 하고 싶었으나 독점 운영하다가 징계 먹고 최근에 분할되서 상장되려면 2020.4에 사모펀드로 강제 매각됨 국내 정식 상장은 2025년 예상
    # 307950 현대오토에버
    # 034730 SK inc. <- sk 텔레콤, sk C&C 지주회사
    # 286940 롯데이노베이트
    # 272210 한화시스템
    # 035510 신세계 I&C
    # 069960 현대백화점 <- 현대 it&e가 현대백화점의 IT 전문 기업

# 대규모 정보를 기반으로 AI에 투자하는 기업
    # 005930 삼성전자 
    # 035420 네이버
    # 003550 LG <- LG CNS로 하고 싶었으나 독점 운영하다가 징계 먹고 최근에 분할되서 상장되려면 2020.4에 사모펀드로 강제 매각됨 국내 정식 상장은 2025년 예상
    # 034730 SK inc. <- sk 텔레콤, sk C&C 지주회사
    # 035720 카카오
    # 000660 SK 하이닉스
    # 030200 KT
    # 005380 현대자동차
    # 005490 포스코

code = ['006400', '018260', '022100', '307950', '286940', '272210', '035510', '069960', '005930', '035420', '003550', '034730', '035720', '000660', '030200', '005380', '005490'] # 종목코드
dates = ['202409051800', '202409061800', '202409091800'] # 날짜 

for date in dates:
    for ticker in code:
        # 데이터 저장할 리스트
        lst = []
        df = crawling(ticker, date)