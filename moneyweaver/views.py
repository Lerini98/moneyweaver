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
