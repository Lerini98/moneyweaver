# django dockerfile
FROM python:3.12 AS python-build
RUN pip install mysqlclient

FROM python:3.12-slim
COPY --from=python-build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
RUN apt-get update && apt-get install -y libmariadb3 nginx

# 파이썬 모듈 설치 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Nginx 설정 복사
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# AWS CLI와 Boto3 설치 (AWS Parameter Store에 접근하기 위해)
RUN pip install awscli boto3

# Django 서버 설정
RUN mkdir /app
COPY . /app
WORKDIR /app

# 환경 변수 설정 - SECRET_KEY
# AWS SSM에서 SECRET_KEY를 가져오기 위해 run.sh에서 가져오는 설정을 수행
ENV AWS_REGION="ap-northeast-2"
ENV SECRET_KEY_PARAM="/mw-db-info/SECRET_KEY"

# config/settings.py 안에 SECRET_KEY 확인하고 삽입
COPY ./run.sh .
RUN chmod +x run.sh
CMD ["./run.sh"]
