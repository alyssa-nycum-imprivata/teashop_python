from django.urls import path
from django.conf.urls import include
from .views import *
from .models import *

app_name = "teaapp"

urlpatterns = [
    path('', tea_list, name='tea_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tea/form', tea_form, name='tea_form'),
    path('teas/<int:tea_id>/', tea_details, name='tea'),
]
