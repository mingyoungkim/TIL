from django.contrib import admin
from .models import Article
# 현재 dicrectory에 models의 Article 클래스 가져옴

# Register your models here.

# admin사이트를 custom하기 위한 기능들을 제공하는 class를 만들어보자
class ArticleAdmin(admin.ModelAdmin):
    # ModelAdmin에 정해진 변수명임
    # tuple, list로 작성하면 됨
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    # 만들어주고 다시 밑에 admin에 저장 

# admin site에 register 하겠다. => 뭐를? Article class를    
admin.site.register(Article, ArticleAdmin)