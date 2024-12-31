from django.urls import path
from . import views

urlpatterns = [
    path('user/qrcode/<str:qrcode_id>/', views.UserByQRCodeView.as_view(), name='user_by_qrcode'),
]
