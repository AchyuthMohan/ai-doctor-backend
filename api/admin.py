from django.contrib import admin
from .models import (UserDetail,Medicine,Doctor,User)
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(User)
