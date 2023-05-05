from rest_framework import generics,mixins,viewsets,status
from .models import (User,Medicine,UserDetail,Doctor,MedicinePurchase,Book_appointment)
from .serializers import (UserSerializer,RegisterSerializer,MedicineSerializer,UserDetailSerializer,DoctorSerializer,
                          MedicinePurchaseSerializer,BookAppointmentSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
# Create your views here.
class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class MedicineViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=MedicineSerializer
    queryset=Medicine.objects.all()

class UserDetailViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                        mixins.ListModelMixin, mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class=UserDetailSerializer
    queryset=UserDetail.objects.all()
    lookup_field = 'user_foreign'

    def get_queryset(self):
        queryset = super().get_queryset()
        user_foreign = self.kwargs.get('user_foreign', None)
        if user_foreign is not None:
            queryset = queryset.filter(user_foreign=user_foreign)
        return queryset

class UserDetailAPIView(RetrieveAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'user_foreign'

class DoctorViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=DoctorSerializer
    queryset=Doctor.objects.all()

class MedicinePurchaseViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=MedicinePurchaseSerializer
    queryset=MedicinePurchase.objects.all()

class BookAppointmentViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=BookAppointmentSerializer
    queryset=Book_appointment.objects.all()
    

    

