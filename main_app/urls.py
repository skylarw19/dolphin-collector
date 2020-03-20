from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dolphins/', views.dolphins_index, name='index'),
    path('dolphins/<int:dolphin_id>/', views.dolphins_detail, name='detail'),
    path('dolphins/create/', views.DolphinCreate.as_view(), name='dolphins_create'),
]