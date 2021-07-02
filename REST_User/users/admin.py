from django.contrib import admin

# Register your models here.
from REST_User.users.models import Profile

admin.site.register(Profile)
