from django.contrib import admin
from .models import Services, Ctu, About


# admin.site.register('blog_title', 'blog_desc')
admin.site.register(Ctu)
class ServicAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_desc',)

admin.site.register(Services, ServicAdmin)


admin.site.register(About)
