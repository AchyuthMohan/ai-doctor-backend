from django.contrib import admin
from .models import (UserDetail,Medicine,Doctor,User,MedicinePurchase,Book_appointment)
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(MedicinePurchase)
admin.site.register(Book_appointment)
