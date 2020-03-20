from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dolphins/', views.dolphins_index, name='index'),
    path('dolphins/<int:dolphin_id>/', views.dolphins_detail, name='detail'),
    path('dolphins/create/', views.DolphinCreate.as_view(), name='dolphins_create'),
    path('dolphins/<int:pk>/update/', views.DolphinUpdate.as_view(), name='dolphins_update'),
    path('dolphins/<int:pk>/delete/', views.DolphinDelete.as_view(), name='dolphins_delete'),
    path('dolphins/<int:dolphin_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dolphins/<int:dolphin_id>/assoc_ocean/<int:ocean_id>/', views.assoc_ocean, name='assoc_ocean'),
]