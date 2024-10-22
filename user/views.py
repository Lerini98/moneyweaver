from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardForm

def index(request):
    return render(request, 'user/user.html')



def board_list(request):
    boards = Board.objects.all().order_by('-created_at') 
    paginator = Paginator(boards, 10)  # 한 페이지에 10개씩 보여줌
    page_number = request.GET.get('page')  # 요청한 페이지 번호
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 객체를 가져옴

    # 'boards' 대신 'page_obj'를 전달하여 페이지네이션을 사용할 수 있게 함
    return render(request, 'user/user.html', {'page_obj': page_obj})
    #return render(request, 'user/user.html', {'boards': boards})


def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 로그인 여부 확인
            if request.user.is_authenticated:
                writer = request.user
            else:
                writer = form.cleaned_data['writer']
            Board.objects.create(
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                writer=writer
            )
            return redirect('/user/')
        else:
            # 폼이 유효하지 않은 경우, 작성 페이지를 다시 보여줌.
            return render(request, 'user/writing.html', {'form': form})
    else:
        form = BoardForm()
    return render(request, 'user/writing.html', {'form': form})

# 게시글을 부르는 함수
def board_detail(request, pk):
    # 게시글 중 pk를 이용해 하나의 게시글을 검색
    board = Board.objects.get(pk=pk)
    return render(request, 'user/board_detail.html', {'board': board})

# 게시글 삭제
def delete(request, pk):
  post = Board.objects.get(pk=pk)
  post.delete()
  return redirect('board_list')

