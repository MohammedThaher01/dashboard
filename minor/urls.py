from django.urls import path
from .views import dashboard, record_event, get_stats

urlpatterns = [
    path('', dashboard),
    path('event', record_event),
    path('stats', get_stats),
]
