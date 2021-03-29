from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',) # User선택 필드 빼고
        # exclude = ('title',)
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # fields = '__all__' => 게시글은 빠져야함
        exclude = ('article',) # 얘 하나만 제외하면 되니까 편하게 ~