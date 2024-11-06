from django.shortcuts import render
import pandas as pd
import json
from moneyweaver.models import db_connect
from model.model_sk import predict_stock_sk
from model.model_skhynix import predict_stock_skhynix
# y_pred, y_test, days_2022 = predict_stock()
# print(y_pred.tolist())
# days_2022=days_2022.tolist()
# days_2022 = [date.strftime('%Y-%m-%d') for date in days_2022]

# print(days_2022)


def chartindex(request):
    return render(request, "chart/index.html")

# def data_load(input:str):
#     df_company, df_day_tb, df_historical_tb = db_connect()

#      # 날짜 데이터를 문자열로 변환하고, 잘못된 날짜 값 처리
#     df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].astype(str)
#     df_historical_tb['stck_bsop_date'] = pd.to_datetime(df_historical_tb['stck_bsop_date'], format='%Y%m%d', errors='coerce')

#     # # 2021년 1월 1일 이후의 데이터만 필터링
#     df_historical_tb = df_historical_tb[df_historical_tb['stck_bsop_date'] >= '2022-01-01']
#     # 필요한 컬럼 계산 및 변환
#     df_historical_tb['stck_avg'] = (df_historical_tb['stck_hgpr'] + df_historical_tb['stck_lwpr']) / 2
#     df_historical_tb['stck_bsop_date'] = df_historical_tb['stck_bsop_date'].dt.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환

#     # 특정 회사 ID에 대한 데이터 필터링
#     filtered_df = df_historical_tb[df_historical_tb['company_id'] == input].sort_values(by='stck_bsop_date', ascending=True)
#     # 필요한 데이터를 추출
#     dates = filtered_df['stck_bsop_date'].tolist()
#     avg_prices = filtered_df['stck_avg'].tolist()

#     return dates, avg_prices


def skhynix_detail_view(request):
    y_pred, y_test, days_2022, trend = predict_stock_skhynix()
    days_2022=days_2022.tolist()
    days_2022 = [date.strftime('%Y-%m-%d') for date in days_2022]
    

    # 고유 회사 ID 리스트
    company_id = '000660'  # 예시로 30200번 회사 ID 사용
   
    # skhynix_date, skhynix_date = data_load(company_id)
    # 오늘의 종가 (예시로 y_test의 마지막 값을 사용)
    today_close_price = y_test[-1]  # y_test에서 오늘의 종가 가져오기
    predicted_price_tomorrow = y_pred[-1]  # y_pred에서 내일의 예측 가격 가져오기

    # 내일 주가 예측 여부 판단
    if predicted_price_tomorrow > today_close_price:
        prediction_message = "내일 오를 것 같습니다."
    else:
        prediction_message = "내일 내릴 것 같습니다."

    # 데이터를 템플릿에 전달
    context = {
        'company_id': 'SK inc',
        'y_pred': json.dumps(y_pred.tolist()),  # 템플릿에 넘기기 위해 리스트 변환
        'y_test': json.dumps(y_test.tolist()),
        'days_2022': json.dumps(days_2022),
        'trend': json.dumps(trend),  # trend 리스트 추가
        'prediction_message': prediction_message,  # 예측 메시지 추가
        'today_close_price': today_close_price,  # 오늘의 종가 추가
        'predicted_price_tomorrow': predicted_price_tomorrow  # 내일 예측 가격 추가
    }


    return render(request, 'chart/skhynix.html', context)


def skinc_detail_view(request):
    y_pred, y_test, days_2022, trend = predict_stock_sk()
    days_2022 = days_2022.tolist()
    days_2022 = [date.strftime('%Y-%m-%d') for date in days_2022]
    
    # 고유 회사 ID 리스트
    company_id = '034730'  # 예시로 30200번 회사 ID 사용

    # 오늘의 종가 (예시로 y_test의 마지막 값을 사용)
    today_close_price = y_test[-1]  # y_test에서 오늘의 종가 가져오기
    predicted_price_tomorrow = y_pred[-1]  # y_pred에서 내일의 예측 가격 가져오기

    # 내일 주가 예측 여부 판단
    if predicted_price_tomorrow > today_close_price:
        prediction_message = "내일 오를 것 같습니다."
    else:
        prediction_message = "내일 내릴 것 같습니다."

    # 데이터를 템플릿에 전달
    context = {
        'company_id': 'SK inc',
        'y_pred': json.dumps(y_pred.tolist()),  # 템플릿에 넘기기 위해 리스트 변환
        'y_test': json.dumps(y_test.tolist()),
        'days_2022': json.dumps(days_2022),
        'trend': json.dumps(trend),  # trend 리스트 추가
        'prediction_message': prediction_message,  # 예측 메시지 추가
        'today_close_price': today_close_price,  # 오늘의 종가 추가
        'predicted_price_tomorrow': predicted_price_tomorrow  # 내일 예측 가격 추가
    }

    return render(request, 'chart/skinc.html', context)
