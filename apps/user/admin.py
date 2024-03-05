from django.contrib import admin
from django.contrib.auth.hashers import make_password

from apps.user.models import User, Profile


class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.save()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
