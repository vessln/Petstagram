from django.contrib import admin
from django.contrib.auth import admin as auth_admin


class UserAdmin(auth_admin.UserAdmin):
    pass
