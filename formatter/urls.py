from django.urls import path
from .views import dashboard
from .views import load_history, delete_all_history, delete_history, history_page, filter_history, instructions

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('load_history/<int:pk>/', load_history, name='load_history'),
]

urlpatterns += [
    path('instructions/', instructions, name='instructions'),
    path('delete_history/<int:pk>/', delete_history, name='delete_history'),
    path('delete_all_history/', delete_all_history, name='delete_all_history'),
    path('history_page/', history_page, name='history_page'),
    path('filter_history/', filter_history, name='filter_history'),
]