from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Board
from .forms import BoardForm

def index(request):
    return render(request, 'user/user.html')

def board_list(request):
    boards = Board.objects.all() #.order_by('-id') 
    return render(request, 'user/user.html', {'boards': boards})

# def board_write(request):
#     if request.method == "POST":
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             user_id = request.session.get('user')
#             user = User.objects.get(pk=user_id)
#             board = Board()
#             board.title = form.cleaned_data['title']
#             board.contents = form.cleaned_data['contents']  
#             board.writer = user
#             board.save()
#             return redirect('board_list') # '/user/'
#     else:
#         form = BoardForm()
#     return render(request, 'user/writing.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import BoardForm  # 폼 임포트

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 로그인 여부 확인
            if request.user.is_authenticated:
                writer = request.user
            else:
                writer = None
            Board.objects.create(
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                writer=writer
            )
            return redirect('/user/')
        else:
            # 폼이 유효하지 않은 경우, 작성 페이지를 다시 보여줌
            return render(request, 'user/writing.html', {'form': form})
    else:
        form = BoardForm()
    return render(request, 'user/writing.html', {'form': form})




# 게시글을 부르는 함수
def board_detail(request, pk):
    # 게시글 중 pk를 이용해 하나의 게시글을 검색
    board = Board.objects.get(pk=pk)
    return render(request, 'user/board_detail.html', {'board': board})


def delete(request, pk):
  post = Board.objects.get(pk=pk)
  post.delete()
  return redirect('board_list')

