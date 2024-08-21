from django.shortcuts import render
import pandas as pd
import json

def kt_detail_view(request):
    # CSV 파일 로드
    df = pd.read_csv('C:/dev/github/moneyweaver/moneyweaver/merged_output_dailysource.csv')

    # 필요한 컬럼 계산 및 변환
    df['stck_avg'] = (df['stck_hgpr'] + df['stck_lwpr']) / 2
    df['stck_bsop_date'] = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
    df['stck_bsop_date'] = df['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = 30200  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df[df['company_id'] == company_id].sort_values(by='Date', ascending=True)

    # 필요한 데이터를 추출
    dates = filtered_df['Date'].tolist()
    avg_prices = filtered_df['avg'].tolist()

    # 데이터를 템플릿에 전달
    context = {
        'company_id': companyname_list[0],
        'dates': json.dumps(dates),
        'avg_prices': json.dumps(avg_prices)
    }

    return render(request, 'chart/kt.html', context)

def lg_detail_view(request):
    # CSV 파일 로드
    df = pd.read_csv('C:/dev/github/moneyweaver/moneyweaver/merged_output_dailysource.csv')

    # 필요한 컬럼 계산 및 변환
    df['stck_avg'] = (df['stck_hgpr'] + df['stck_lwpr']) / 2
    df['stck_bsop_date'] = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
    df['stck_bsop_date'] = df['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = 3550  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df[df['company_id'] == company_id].sort_values(by='Date', ascending=True)

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
    df = pd.read_csv('C:/dev/github/moneyweaver/moneyweaver/merged_output_dailysource.csv')

    # 필요한 컬럼 계산 및 변환
    df['stck_avg'] = (df['stck_hgpr'] + df['stck_lwpr']) / 2
    df['stck_bsop_date'] = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
    df['stck_bsop_date'] = df['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
    df.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    company_id = 18260  # 예시로 30200번 회사 ID 사용
    companyname_list = ['KT', 'LG', '삼성SDS', '현대자동차', '카카오', '신세계 I&C', '롯데이노베이트', '네이버', '포스코', '포스코 DX',
                        '현대오토에버', '삼성 SDI', '삼성전자', 'SK 하이닉스', '현대백화점', '한화시스템', 'SK inc.']

    # 특정 회사 ID에 대한 데이터 필터링
    filtered_df = df[df['company_id'] == company_id].sort_values(by='Date', ascending=True)

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
