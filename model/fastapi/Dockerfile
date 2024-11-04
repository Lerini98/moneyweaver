# Python 이미지
FROM python:3.12-slim

# 작업 디렉터리 설정
WORKDIR /model/fastapi

# 필요한 패키지 설치
COPY requirements.txt .  
RUN pip install -r requirements.txt

COPY sk_preprocessed_data_fin.pkl .
COPY skhynix_preprocessed_data.pkl .

# 애플리케이션 파일 복사
COPY . .  

# FastAPI 서버 실행
CMD ["uvicorn", "fastapi_main:app", "--host", "0.0.0.0", "--port", "8000"]
