FROM python:3.12 AS python-build
RUN pip install mysqlclient

FROM python:3.12-slim
COPY --from=python-build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
RUN apt-get update && apt-get install -y libmariadb3 nginx

# 파이썬 모듈 설치 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Django server
RUN mkdir /app
COPY . /app
WORKDIR /app

# 환경변수 적용 
# config/settings.py 안에 SECRET_KEY 확인하고 삽입
ENV SECRET_KEY 'django-insecure-ur9y8)5!pe#5d-+i!vxj$bm(&xy#0bv#&=2^$p+()izoh0$tdn'

COPY run.sh .
RUN chmod +x run.sh
CMD ["./run.sh"]