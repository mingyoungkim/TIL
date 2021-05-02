from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',) # User선택 필드 빼고
        # exclude = ('user',)
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # fields = '__all__' => 게시글은 빠져야함
        exclude = ('article', 'user', ) # 게시글과 user선택사항도 빠져야함