from django.contrib.auth.models import User
from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.CharField(max_length=50, null=True, blank=True, verbose_name='작성자 이름')  # CharField로 수정
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    
    # 게시글의 제목(title)이 Board object 대신하기
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'moneyweaver_board'
        verbose_name = '머니위버 게시글'
        verbose_name_plural = '머니위버 게시글'