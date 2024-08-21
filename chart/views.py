from django.shortcuts import render
import pandas as pd

def company_detail_view(request):
    # CSV 파일 로드
    df = pd.read_csv('C:/dev/MoneyWeaver/moneyweaver/merged_output_dailysource.csv')

    # 필요한 컬럼 계산 및 변환
    df['stck_avg'] = (df['stck_hgpr'] + df['stck_lwpr']) / 2
    df['stck_bsop_date'] = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
    df.rename(columns={
        'stck_bsop_date': 'Date',
        'stck_hgpr': 'High',
        'stck_lwpr': 'Low',
        'stck_avg': 'avg'
    }, inplace=True)

    # 고유 회사 ID 리스트
    companyid_list = df['company_id'].unique().tolist()
    companyname_list=['KT','LG','삼성SDS','현대자동차','카카오','신세계 I&C','롯데이노베이트','네이버','포스코','포스코 DX'
                  ,'현대오토에버','삼성 SDI','삼성전자','SK 하이닉스','현대백화점','한화시스템','SK inc.']
    # 특정 회사 ID에 대한 데이터 필터링
    company_id = 30200  # 예시로 30200번 회사 ID 사용
    filtered_df = df[df['company_id'] == company_id]

    # 데이터를 템플릿에 전달
    kt = {
        'company_id': companyid_list[0],
        'company_data': filtered_df.to_dict(orient="records")
    }
    return render(request, 'chart/kt.html', kt)