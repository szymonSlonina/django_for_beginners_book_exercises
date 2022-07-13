from django.contrib import admin

from .models import Article, Comment

# There is also TabularInline, that shows related in form of table.
class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)