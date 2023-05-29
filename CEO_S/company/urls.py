from django.urls import path
from . import views

urlpatterns = [
    path('ceo/', views.ceo_view, name='ceo'),
    path('company/', views.company_view, name='company'),
    path('company_show/', views.company_show_view, name='show'),
    path('info_update/<int:pk>/', views.info_update_view, name='info_update'),
    path('company_update/<int:pk>/', views.company_update_view, name='company_update'),
    path('ceo_delete/<int:pk>/', views.delete_ceo_view, name='ceo_delete'),
    path('company_delete/<int:pk>/', views.delete_company_view, name='company_delete'),
]