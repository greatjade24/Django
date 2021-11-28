from django.contrib import admin
from board.models import justCount

# Register your models here.
class countView(admin.ModelAdmin):
    list_display = ['id', '좋아요']

admin.site.register(justCount ,countView)