from django.urls import path
from . import views

app_name = 'pages'  # Здесь был перенос строки
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
