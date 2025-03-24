from django.urls import path
from . import views

app_name = 'dlog'

urlpatterns = [
    path('new_user/', views.new_user_view, name="new_user"),
    path('login/', views.login_view, name='login_view'),
    path('migraines_log/', views.migraines_log_view, name='migraines_log'),  
]
