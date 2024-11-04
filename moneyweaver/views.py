from django.shortcuts import render

# Create your views here.
# urls.py(Controller) -> 처리하는 함수
# -> 화면(Template) & 데이터/Database(Model)
def index(request):
    return render(request, "moneyweaver/moneyweaver.html")

def intro(request):
    return render(request, "moneyweaver/intro.html")

def popup(request):
    return render(request, "moneyweaver/popup.html")

# moneyweaver/views.py

import requests

def get_stock_prediction_model1(features):
    url = "http://fastapi-container:8000/predict_model_sk"  # 모델 1을 위한 FastAPI URL
    response = requests.post(url, json={"features": features})
    if response.status_code == 200:
        return response.json().get("prediction")
    else:
        return None

def get_stock_prediction_model2(features):
    url = "http://fastapi-container:8000/predict_model_skhynix"  # 모델 2를 위한 FastAPI URL
    response = requests.post(url, json={"features": features})
    if response.status_code == 200:
        return response.json().get("prediction")
    else:
        return None

