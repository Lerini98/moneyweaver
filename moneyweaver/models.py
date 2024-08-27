from django.db import models

# Create your models here.
from dotenv import load_dotenv
import pymysql
import pandas as pd
import os

# .env 파일 로드
load_dotenv()

def db_connect():
    # 데이터베이스 연결 설정
    con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT', '3306')),  # 기본값 3306
        charset='utf8'
    )
    # DictCursor를 사용하여 커서 생성
    cur = con.cursor(pymysql.cursors.DictCursor)
    
    try:
        # 데이터 조회
        company = "SELECT * FROM company"
        cur.execute(company)
        rows_company = cur.fetchall()
        df_company = pd.DataFrame(rows_company)

        day_tb = "SELECT * FROM stock_day_chart"
        cur.execute(day_tb)
        rows_day_tb = cur.fetchall()
        df_day_tb = pd.DataFrame(rows_day_tb)

        historical_tb = "SELECT * FROM historical_stock_data"
        cur.execute(historical_tb)
        rows_historical_tb = cur.fetchall()
        df_historical_tb = pd.DataFrame(rows_historical_tb)

        return df_company,df_day_tb,df_historical_tb
        
    finally:
        # 커서와 연결을 종료
        cur.close()
        con.close()

df_company, df_day_tb, df_historical_tb = db_connect()
print(db_connect())
print(type(df_historical_tb['stck_hgpr'][1]))
print('date:',type(df_historical_tb['stck_bsop_date'][1]))
print('회사',type(df_historical_tb['company_id'][1]))


