from django.contrib import admin
from django.urls import path
from prueba.views import AdminPersonaView, AdminPersonaViewDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'persona/', AdminPersonaView.as_view()),
    path(r'persona/<int:pk>', AdminPersonaViewDetail.as_view())
]
