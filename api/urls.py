from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (BlacklistTokenView,LoggedInUserView,RegisterView,MedicineViewSet,UserDetailViewSet,DoctorViewSet,
                    MedicinePurchaseViewSet,BookAppointmentViewSet)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('medicines',MedicineViewSet,basename='medicines')
router.register('user-detail',UserDetailViewSet,basename='user-detail')
router.register('doctors',DoctorViewSet,basename='doctors')
router.register('purchase-medicine',MedicinePurchaseViewSet,basename='purchase-medicine')
router.register('book-appointment',BookAppointmentViewSet,basename='book-appointment')


urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]