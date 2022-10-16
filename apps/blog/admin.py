from django.contrib import admin
from .models import Author, ChiefEditor,Publication,Article,articleimg
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","family","email","register_date","age","is_active")
    list_filter = ("name","is_active","family")
    search_fields = ("name","family")
    ordering=["family"]
    prepopulated_fields ={'slug':('name','family')}
    


@admin.register(ChiefEditor)
class ChiefEditorAdmin(admin.ModelAdmin):
    list_display = ("name","family","publication")


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title","chiefeditor")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("article_title","published_at","is_active","status","author")

# admin.site.register(Author,BlogAdmin)



@admin.register(articleimg)
class articleimgAdmin(admin.ModelAdmin):
    list_display = ("title","text","is_active","main_img")