from django import forms
from .models import Board

class BoardForm(forms.Form):
    writer = forms.CharField(
        max_length=50,  # 작성자 이름 최대 길이 설정
        required=False,  # 필수 입력 아님
        label='작성자 이름',  # 레이블 설정
        initial='익명'  # 기본값으로 '익명' 설정
    )
    title = forms.CharField(error_messages={
        'required' : '제목을 입력해 주세요.'
    }, max_length = 128, label="제목")
    contents = forms.CharField(error_messages={
        'required' : '내용을 입력해 주세요'
    }, widget=forms.Textarea,label='내용')
    