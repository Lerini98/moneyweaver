from django.shortcuts import render
import pandas as pd
import json
from moneyweaver.models import db_connect
def index(request):
    return render(request, "chart/chart-index.html")

def kt_detail_view(request):
    df_company, df_day_tb, df_historical_tb = db_connect()

    # 날짜 데이터를 문자열로 변환하고, 잘못된 날짜 값 처리
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
  
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == '030200'].sort_values(by='stck_bsop_date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['stck_bsop_date'].tolist()
    avg_prices = filtered_df['stck_avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': 'KT',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/kt.html', context)



def lg_detail_view(request):
    # CSV 파일 로드
    df_company, df_day_tb, df_historical_tb = db_connect()
    
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')
    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '003550'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': companyname_list[1],
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/lg.html', context)


def ssSDS_detail_view(request):
    # CSV 파일 로드
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')
    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '018260'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': companyname_list[2],
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/ssSDS.html', context)

def hd_detail_view(request):
    # CSV 파일 로드
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '005380'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '현대자동차',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/hyundai.html', context)

def kakao_detail_view(request):
    # CSV 파일 로드
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '035720'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '카카오',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/kakao.html', context)

def ssg_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '035510'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '신세계 InC',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/ssgInC.html', context)

def lotteino_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '286940'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '롯데 이노베이트',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/lotteino.html', context)

def naver_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '035420'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '네이버',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }
    print(filtered_df.head())
    return render(request, 'chart/naver.html', context)

def posco_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '005490'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '포스코',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/posco.html', context)

def poscodx_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '022100'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '포스코',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/poscodx.html', context)

def hyundaiauto_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '307950'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '현대 오토에버',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/hyundaiauto.html', context)

def ssSDI_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '006400'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '삼성 SDI',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/ssSDI.html', context)

def ssElec_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '005930'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '삼성 전자',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/ssElec.html', context)

def skhynix_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '000660'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': 'SK 하이닉스',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/skhynix.html', context)

def hyundaidp_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '069960'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '현대백화점',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/hyundaidp.html', context)

def hanhwasys_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '272210'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': '한화 시스템',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/hanhwasys.html', context)

def skinc_detail_view(request):
    
    df_company, df_day_tb, df_historical_tb = db_connect()
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

    # 필요한 컬럼 계산 및 변환
    df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
    df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d')
    df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df_historical_tb.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = '034730'  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df_historical_tb[df_historical_tb['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': 'SK inc',
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/skinc.html', context)
