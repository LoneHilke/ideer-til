from django.urls import path
from . import views
from .views import Forside,Info,Fane, Side, Knap, Ikon, Tekst, Tab, Rul

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('info', Info.as_view(), name='info'),
  path('fane', Fane.as_view(), name='fane'),
  path('side', Side.as_view(), name='side'),
  path('knap', Knap.as_view(), name='knap'),
  path('ikon', Ikon.as_view(), name='ikon'),
  path('tekst', Tekst.as_view(), name='tekst'),
  path('tab', Tab.as_view(), name='tab'),
  path('rul', Rul.as_view(), name='rul'),
  
] 