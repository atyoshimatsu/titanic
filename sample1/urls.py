from django.urls import path
from . import views

app_name = 'sample1'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('age/', views.age_view, name='age') ,
    path('ticket_class/', views.ticket_class_view, name='ticket_class'),
]