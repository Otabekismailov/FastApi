from django.contrib import admin

from blogs.models import Post, Tag, Category, Comment


# class PostStacked(admin.StackedInline):
#     model =
#     extra = 1
#
#
# @admin.register(Tag)
# class ProductStacked(admin.ModelAdmin):
#     inlines = [PostStacked]

class Postadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'category', 'pub_year']


admin.site.register(Post, Postadmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
