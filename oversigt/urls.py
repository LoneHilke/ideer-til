from django.urls import path
from . import views
from .views import Forside,Info

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('info', Info.as_view(), name='info'),
  
] 